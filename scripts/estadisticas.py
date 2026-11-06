"""Genera las tarjetas de actividad del perfil (estadisticas/*.svg) con la API de GitHub.

Sin dependencias: solo la biblioteca estándar. Lo lanza .github/workflows/estadisticas.yml.
Variables: GITHUB_TOKEN (obligatoria) y USUARIO (por omisión, Dathinel).
"""
import json
import os
import pathlib
import urllib.request
from xml.sax.saxutils import escape

USUARIO = os.environ.get("USUARIO", "Dathinel")
SALIDA = pathlib.Path(__file__).resolve().parent.parent / "estadisticas"

FONDO, BORDE, ACENTO, TEXTO, SUAVE = "#1D1D1D", "#3A3A3A", "#E8833A", "#ECECEC", "#B0B0B0"
FUENTE = "Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif"

CONSULTA = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    createdAt
    contributionsCollection { totalCommitContributions restrictedContributionsCount }
    repositories(first: 100, after: $cursor, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        releases { totalCount }
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""


def graphql(variables):
    peticion = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": CONSULTA, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "User-Agent": "perfil-Dathinel"},
    )
    with urllib.request.urlopen(peticion, timeout=30) as respuesta:
        datos = json.load(respuesta)
    if "errors" in datos:
        raise SystemExit(f"Error de la API: {datos['errors']}")
    return datos["data"]["user"]


def recoger():
    repos, cursor = [], None
    while True:
        usuario = graphql({"login": USUARIO, "cursor": cursor})
        pagina = usuario["repositories"]
        repos += pagina["nodes"]
        if not pagina["pageInfo"]["hasNextPage"]:
            break
        cursor = pagina["pageInfo"]["endCursor"]
    lenguajes = {}
    for repo in repos:
        for borde in repo["languages"]["edges"]:
            nombre = borde["node"]["name"]
            total, color = lenguajes.get(nombre, (0, borde["node"]["color"]))
            lenguajes[nombre] = (total + borde["size"], color or SUAVE)
    aportes = usuario["contributionsCollection"]
    return {
        "repos": len(repos),
        "estrellas": sum(r["stargazerCount"] for r in repos),
        "releases": sum(r["releases"]["totalCount"] for r in repos),
        "commits": aportes["totalCommitContributions"] + aportes["restrictedContributionsCount"],
        "lenguajes": sorted(lenguajes.items(), key=lambda par: -par[1][0]),
    }


def tarjeta(titulo, cuerpo, alto):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="420" height="{alto}" viewBox="0 0 420 {alto}" '
        f'role="img" aria-label="{escape(titulo)}">\n'
        f'  <rect x="1" y="1" width="418" height="{alto - 2}" rx="10" fill="{FONDO}" stroke="{BORDE}" stroke-width="2"/>\n'
        f'  <rect x="1" y="1" width="6" height="{alto - 2}" rx="3" fill="{ACENTO}"/>\n'
        f'  <g font-family="{FUENTE}">\n'
        f'    <text x="28" y="38" font-size="18" font-weight="600" fill="{ACENTO}">{escape(titulo)}</text>\n'
        f"{cuerpo}"
        "  </g>\n</svg>\n"
    )


def tarjeta_resumen(datos):
    filas = [
        ("Repositorios públicos", datos["repos"]),
        ("Releases publicadas", datos["releases"]),
        ("Commits en el último año", datos["commits"]),
        ("Estrellas recibidas", datos["estrellas"]),
    ]
    cuerpo = "".join(
        f'    <text x="28" y="{78 + i * 28}" font-size="15" fill="{SUAVE}">{escape(nombre)}</text>\n'
        f'    <text x="392" y="{78 + i * 28}" font-size="15" font-weight="700" fill="{TEXTO}" text-anchor="end">{valor}</text>\n'
        for i, (nombre, valor) in enumerate(filas)
    )
    return tarjeta("Actividad en GitHub", cuerpo, 180)


def tarjeta_lenguajes(datos, maximo=6):
    lenguajes = datos["lenguajes"][:maximo]
    total = sum(tam for _, (tam, _) in lenguajes) or 1
    x, barra = 28.0, ""
    for _, (tam, color) in lenguajes:
        ancho = 364 * tam / total
        barra += f'    <rect x="{x:.1f}" y="56" width="{ancho:.1f}" height="10" fill="{color}"/>\n'
        x += ancho
    leyenda = ""
    for i, (nombre, (tam, color)) in enumerate(lenguajes):
        cx, cy = 28 + (i % 2) * 190, 96 + (i // 2) * 26
        leyenda += (
            f'    <circle cx="{cx + 5}" cy="{cy - 5}" r="5" fill="{color}"/>\n'
            f'    <text x="{cx + 16}" y="{cy}" font-size="14" fill="{TEXTO}">{escape(nombre)} '
            f'<tspan fill="{SUAVE}">{100 * tam / total:.1f} %</tspan></text>\n'
        )
    return tarjeta("Lenguajes más usados", barra + leyenda, 180)


def main():
    datos = recoger()
    SALIDA.mkdir(exist_ok=True)
    (SALIDA / "resumen.svg").write_text(tarjeta_resumen(datos), encoding="utf-8")
    (SALIDA / "lenguajes.svg").write_text(tarjeta_lenguajes(datos), encoding="utf-8")
    print(f"{datos['repos']} repos, {datos['releases']} releases, {datos['commits']} commits")


if __name__ == "__main__":
    main()
