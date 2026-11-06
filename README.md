<p align="center">
  <img src="banner.svg" alt="Dathinel: estudiante que aprende a crear software con IA" width="100%">
</p>

<p align="center">
  <a href="#rodaje">Rodaje</a> ·
  <a href="#herramientas-de-ia">Herramientas de IA</a> ·
  <a href="#complementos">Complementos</a> ·
  <a href="#lo-próximo">Lo próximo</a> ·
  <a href="#universidad">Universidad</a>
</p>

Soy estudiante y estoy aprendiendo a crear software con ayuda de la IA (Claude Code y otros agentes). Aquí publico en código abierto programas para cosas que me gustan y uso, cada uno en su propio repositorio. De otros programas solo tomo ideas, nunca su código ni sus recursos.

Todo es **nativo para Windows**, funciona **sin conexión** y la IA corre **en tu PC**.

## Rodaje

<table>
  <tr>
    <td width="150" align="center" valign="top">
      <a href="https://github.com/Dathinel/rodaje"><img src="https://raw.githubusercontent.com/Dathinel/rodaje/main/assets/marca/rodaje.svg" alt="Logotipo de Rodaje" width="120"></a>
    </td>
    <td valign="top">
      <b>Editor de video nativo para Windows.</b> Edición por capas al cuadro exacto, imagen en la GPU (Direct3D 11), títulos y subtítulos, audio con mezcla a LUFS, exportación por GPU e IA local por módulos. Escrito en C# con .NET 10 y WinUI 3; compilado con Native AOT, no necesita .NET instalado.
      <br><br>
      <a href="https://github.com/Dathinel/rodaje/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje?style=flat-square&labelColor=1D1D1D&color=E8833A&label=versi%C3%B3n" alt="Última versión publicada"></a>
      <a href="https://github.com/Dathinel/rodaje/commits/main"><img src="https://img.shields.io/github/commits-since/Dathinel/rodaje/latest?style=flat-square&labelColor=1D1D1D&color=E8833A&label=cambios%20sin%20publicar" alt="Cambios desde la última versión"></a>
      <a href="https://github.com/Dathinel/rodaje/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Dathinel/rodaje/ci.yml?branch=main&style=flat-square&labelColor=1D1D1D&label=CI" alt="Estado de la CI"></a>
      <a href="https://github.com/Dathinel/rodaje/blob/main/LICENSE"><img src="https://img.shields.io/badge/licencia-GPLv3-E8833A?style=flat-square&labelColor=1D1D1D" alt="Licencia GPLv3"></a>
      <img src="https://img.shields.io/badge/Windows-x64-E8833A?style=flat-square&labelColor=1D1D1D" alt="Windows x64">
      <br><br>
      <a href="https://github.com/Dathinel/rodaje/releases/latest"><b>Descargar</b></a> ·
      <a href="https://github.com/Dathinel/rodaje">Repositorio</a> ·
      <a href="https://github.com/Dathinel/rodaje/blob/main/docs/README.md">Documentación</a>
    </td>
  </tr>
</table>

## Herramientas de IA

Las funciones de IA de Rodaje como programas aparte, cada uno con su propia interfaz y su propia descarga. Usan los mismos módulos que Rodaje y los comparten entre sí: lo que bajas para uno sirve para los demás.

| Herramienta | Qué hace | Versión |
|---|---|---|
| [**Subtitular**](https://github.com/Dathinel/subtitular) | Subtítulos automáticos (SRT y VTT), traducción conservando los tiempos y texto a voz | <a href="https://github.com/Dathinel/subtitular/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/subtitular?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de Subtitular"></a> |
| [**Rastrear**](https://github.com/Dathinel/rastrear) | Seguimiento de puntos, quitar fondo, rostros y personas, reencuadre y estabilización | <a href="https://github.com/Dathinel/rastrear/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rastrear?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de Rastrear"></a> |
| [**Lanzador**](https://github.com/Dathinel/lanzador) | Lista, descarga e instala las herramientas, con firma y huellas comprobadas | <a href="https://github.com/Dathinel/lanzador/releases"><img src="https://img.shields.io/github/v/release/Dathinel/lanzador?include_prereleases&style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de Lanzador"></a> |

Las tres son GPLv3, con interfaz en WinUI 3 y una CLI para guiones.

## Complementos

Rodaje viene completo como editor y exportador; lo demás se instala desde la app (Complementos), que baja cada `.paquete` del [catálogo firmado](https://github.com/Dathinel/rodaje-catalogo) <a href="https://github.com/Dathinel/rodaje-catalogo/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-catalogo?style=flat-square&labelColor=1D1D1D&color=E8833A&label=%C3%ADndice" alt="Última versión del índice"></a> y comprueba su firma. Cómo se hace: [guía de complementos](https://github.com/Dathinel/rodaje/blob/main/docs/guia/complementos.md).

<details>
<summary><b>10 paquetes de contenido</b>: transiciones, looks, fuentes, títulos, sonidos, preajustes y más</summary>
<br>

| Complemento | Qué trae | Versión | Licencia |
|---|---|---|---|
| [rodaje-transiciones](https://github.com/Dathinel/rodaje-transiciones) | 45 transiciones: curvas de movimiento y mezclas de calidad en la GPU | <a href="https://github.com/Dathinel/rodaje-transiciones/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-transiciones?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-transiciones"></a> | CC0 |
| [rodaje-filtros](https://github.com/Dathinel/rodaje-filtros) | 13 looks de color con LUT 3D | <a href="https://github.com/Dathinel/rodaje-filtros/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-filtros?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-filtros"></a> | CC0 |
| [rodaje-fuentes](https://github.com/Dathinel/rodaje-fuentes) | 10 familias tipográficas libres | <a href="https://github.com/Dathinel/rodaje-fuentes/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-fuentes?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-fuentes"></a> | OFL |
| [rodaje-titulos](https://github.com/Dathinel/rodaje-titulos) | 15 estilos de texto, subtítulos y karaoke | <a href="https://github.com/Dathinel/rodaje-titulos/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-titulos?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-titulos"></a> | CC0 |
| [rodaje-zonas](https://github.com/Dathinel/rodaje-zonas) | 12 guías de encuadre para el visor | <a href="https://github.com/Dathinel/rodaje-zonas/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-zonas?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-zonas"></a> | CC0 |
| [rodaje-camaras](https://github.com/Dathinel/rodaje-camaras) | 9 LUT de log de cámara a Rec. 709 | <a href="https://github.com/Dathinel/rodaje-camaras/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-camaras?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-camaras"></a> | CC0 |
| [rodaje-sonidos](https://github.com/Dathinel/rodaje-sonidos) | 50 efectos de sonido sintetizados | <a href="https://github.com/Dathinel/rodaje-sonidos/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-sonidos?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-sonidos"></a> | CC0 |
| [rodaje-preajustes-pro](https://github.com/Dathinel/rodaje-preajustes-pro) | 15 preajustes de exportación: ProRes, DNxHR, emisión, cine | <a href="https://github.com/Dathinel/rodaje-preajustes-pro/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-preajustes-pro?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-preajustes-pro"></a> | CC0 |
| [rodaje-360](https://github.com/Dathinel/rodaje-360) | Video 360: reencuadre, pequeño planeta y exportación esférica | <a href="https://github.com/Dathinel/rodaje-360/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-360?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-360"></a> | CC0 |
| [rodaje-codificadores-gpl](https://github.com/Dathinel/rodaje-codificadores-gpl) | x264 y x265 con un ffmpeg.exe GPL propio | <a href="https://github.com/Dathinel/rodaje-codificadores-gpl/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-codificadores-gpl?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de rodaje-codificadores-gpl"></a> | GPLv3 |

</details>

<details>
<summary><b>6 módulos de IA local</b>: subtítulos, traducción, voz, audio, visión y RAW</summary>
<br>

| Módulo | Qué hace | Versión | Licencia |
|---|---|---|---|
| [modulo-subtitulos](https://github.com/Dathinel/modulo-subtitulos) | Subtítulos automáticos con Whisper | <a href="https://github.com/Dathinel/modulo-subtitulos/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-subtitulos?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-subtitulos"></a> | GPLv3 |
| [modulo-traducir](https://github.com/Dathinel/modulo-traducir) | Traducción de subtítulos con Qwen3-4B | <a href="https://github.com/Dathinel/modulo-traducir/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-traducir?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-traducir"></a> | GPLv3 |
| [modulo-voz](https://github.com/Dathinel/modulo-voz) | Texto a voz con Kokoro-82M | <a href="https://github.com/Dathinel/modulo-voz/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-voz?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-voz"></a> | GPLv3 |
| [modulo-audio-ia](https://github.com/Dathinel/modulo-audio-ia) | Reducción de ruido y detección de voz | <a href="https://github.com/Dathinel/modulo-audio-ia/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-audio-ia?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-audio-ia"></a> | GPLv3 |
| [modulo-vision](https://github.com/Dathinel/modulo-vision) | Quitar fondo, rostros y reencuadre automático | <a href="https://github.com/Dathinel/modulo-vision/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-vision?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-vision"></a> | GPLv3 |
| [modulo-raw](https://github.com/Dathinel/modulo-raw) | Revelado de CinemaDNG con LibRaw | <a href="https://github.com/Dathinel/modulo-raw/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-raw?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-raw"></a> | GPLv3 |

</details>

## Lo próximo

Lo que ya está en el código y saldrá en la siguiente versión de cada herramienta:

- **Subtitular 1.1**: cola de varios archivos (o una carpeta entera), atajos de teclado, guardar sin revisar y aviso de versión nueva.
- **Rastrear 1.1**: cola de videos, vista previa «Después» con los parámetros actuales, carpeta de salida propia, atajos y aviso de versión nueva.
- **Lanzador 1.0 estable**: modo sin conexión, descargas reanudables con velocidad y tiempo restante, y actualizaciones de las herramientas desde la propia ventana.
- **Código compartido**: sacar lo común de las tres herramientas a un paquete propio en vez de copiarlo entre repositorios.

## Universidad

[**Sensores-Teoria**](https://github.com/Dathinel/Sensores-Teoria): prácticas y teoría de sensores y microcontroladores. ESP32 con MicroPython y C++, detección de objetos con OpenCV, control por gestos, brazo robótico simulado, enjambres y laboratorios Docker con MQTT.

## Tecnologías

<p align="center">
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=cs,dotnet,windows,powershell,git,github,githubactions,py,cpp,docker,arduino,opencv,pytorch,tensorflow,js,html,css&theme=dark&perline=9" alt="C#, .NET, Windows, PowerShell, Git, GitHub, GitHub Actions, Python, C++, Docker, Arduino, OpenCV, PyTorch, TensorFlow, JavaScript, HTML, CSS"></a>
</p>

- **Escritorio Windows:** C#, .NET 10, WinUI 3, Native AOT, Direct3D 11 con shaders HLSL, FFmpeg (LGPL) por P/Invoke, ONNX y DirectML para la IA, Inno Setup para los instaladores, PowerShell para construir y distribuir, GitHub Actions como CI.
- **Sensores y microcontroladores:** ESP32 con MicroPython y C++, Python con OpenCV, PyTorch, TensorFlow y Streamlit, laboratorios Docker con MQTT.

## Actividad

<p align="center">
  <img src="estadisticas/resumen.svg" alt="Actividad de Dathinel en GitHub" width="49%">
  <img src="estadisticas/lenguajes.svg" alt="Lenguajes más usados por Dathinel" width="49%">
</p>

<sub>Las tarjetas las genera cada día [un workflow](.github/workflows/estadisticas.yml) de este repositorio. Textos e imágenes de este perfil: [CC BY 4.0](LICENSE). El nombre y el logotipo de Rodaje no se incluyen (ver su [TRADEMARK.md](https://github.com/Dathinel/rodaje/blob/main/TRADEMARK.md)).</sub>
