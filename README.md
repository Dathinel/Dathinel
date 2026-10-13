<p align="center">
  <img src="banner.svg" alt="Dathinel: software nativo para Windows, hecho desde cero" width="100%">
</p>

Programas propios para Windows, uno por repositorio: compilados de antemano con Native AOT, autocontenidos y sin instalador obligatorio. Todo el código es propio; de otros programas solo se toman ideas de producto.

## Rodaje

<table>
  <tr>
    <td width="150" align="center" valign="top">
      <a href="https://github.com/Dathinel/rodaje"><img src="https://raw.githubusercontent.com/Dathinel/rodaje/main/assets/marca/rodaje.svg" alt="Logotipo de Rodaje" width="120"></a>
    </td>
    <td valign="top">
      <b>Editor de video nativo para Windows.</b> Edición por capas al cuadro exacto, imagen en la GPU (Direct3D 11), títulos y subtítulos, audio con mezcla a LUFS, exportación por GPU e IA local por módulos. Escrito en C# con .NET 10 y WinUI 3; compilado con Native AOT, no necesita .NET instalado.
      <br><br>
      <a href="https://github.com/Dathinel/rodaje/blob/main/LICENSE"><img src="https://img.shields.io/badge/licencia-GPLv3-E8833A?style=flat-square&labelColor=1D1D1D" alt="Licencia GPLv3"></a>
      <a href="https://github.com/Dathinel/rodaje/releases"><img src="https://img.shields.io/badge/versi%C3%B3n-1.0.0-E8833A?style=flat-square&labelColor=1D1D1D" alt="Versión 1.0.0"></a>
      <img src="https://img.shields.io/badge/Windows-x64-E8833A?style=flat-square&labelColor=1D1D1D" alt="Windows x64">
      <img src="https://img.shields.io/badge/.NET-10-E8833A?style=flat-square&labelColor=1D1D1D&logo=dotnet&logoColor=white" alt=".NET 10">
      <a href="https://github.com/Dathinel/rodaje/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Dathinel/rodaje/ci.yml?branch=main&style=flat-square&labelColor=1D1D1D&label=CI" alt="Estado de la CI"></a>
      <br><br>
      <a href="https://github.com/Dathinel/rodaje">Repositorio</a> ·
      <a href="https://github.com/Dathinel/rodaje/releases">Descargas</a> ·
      <a href="https://github.com/Dathinel/rodaje/blob/main/docs/README.md">Documentación</a> ·
      <a href="#complementos">Complementos</a>
    </td>
  </tr>
</table>

### Complementos

Rodaje viene completo como editor y exportador; lo demás se instala desde la app (Complementos), que baja cada `.paquete` del [catálogo firmado](https://github.com/Dathinel/rodaje-catalogo) <a href="https://github.com/Dathinel/rodaje-catalogo/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/rodaje-catalogo?style=flat-square&labelColor=1D1D1D&color=E8833A&label=%C3%ADndice" alt="Última versión del índice"></a> y comprueba su firma. Cómo se hace: [guía de complementos](https://github.com/Dathinel/rodaje/blob/main/docs/guia/complementos.md).

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
| [modulo-subtitulos](https://github.com/Dathinel/modulo-subtitulos) | Subtítulos automáticos con Whisper | <a href="https://github.com/Dathinel/modulo-subtitulos/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-subtitulos?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-subtitulos"></a> | GPLv3 |
| [modulo-traducir](https://github.com/Dathinel/modulo-traducir) | Traducción de subtítulos con Qwen3-4B | <a href="https://github.com/Dathinel/modulo-traducir/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-traducir?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-traducir"></a> | GPLv3 |
| [modulo-voz](https://github.com/Dathinel/modulo-voz) | Texto a voz con Kokoro-82M | <a href="https://github.com/Dathinel/modulo-voz/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-voz?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-voz"></a> | GPLv3 |
| [modulo-audio-ia](https://github.com/Dathinel/modulo-audio-ia) | Reducción de ruido y detección de voz | <a href="https://github.com/Dathinel/modulo-audio-ia/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-audio-ia?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-audio-ia"></a> | GPLv3 |
| [modulo-vision](https://github.com/Dathinel/modulo-vision) | Quitar fondo, rostros y reencuadre automático | <a href="https://github.com/Dathinel/modulo-vision/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-vision?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-vision"></a> | GPLv3 |
| [modulo-raw](https://github.com/Dathinel/modulo-raw) | Revelado de CinemaDNG con LibRaw | <a href="https://github.com/Dathinel/modulo-raw/releases/latest"><img src="https://img.shields.io/github/v/release/Dathinel/modulo-raw?style=flat-square&labelColor=1D1D1D&color=E8833A&label=" alt="Última versión de modulo-raw"></a> | GPLv3 |

## Tecnologías

<p align="center">
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=cs,dotnet,windows,powershell,git,github,githubactions,py,cpp,docker,arduino,opencv,pytorch,tensorflow,js,html,css&theme=dark&perline=9" alt="C#, .NET, Windows, PowerShell, Git, GitHub, GitHub Actions, Python, C++, Docker, Arduino, OpenCV, PyTorch, TensorFlow, JavaScript, HTML, CSS"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/WinUI-3-E8833A?style=flat-square&labelColor=1D1D1D" alt="WinUI 3">
  <img src="https://img.shields.io/badge/Native-AOT-E8833A?style=flat-square&labelColor=1D1D1D" alt="Native AOT">
  <img src="https://img.shields.io/badge/Direct3D-11-E8833A?style=flat-square&labelColor=1D1D1D" alt="Direct3D 11">
  <img src="https://img.shields.io/badge/HLSL-shaders-E8833A?style=flat-square&labelColor=1D1D1D" alt="HLSL">
  <img src="https://img.shields.io/badge/FFmpeg-LGPL-E8833A?style=flat-square&labelColor=1D1D1D&logo=ffmpeg&logoColor=white" alt="FFmpeg">
  <img src="https://img.shields.io/badge/Inno_Setup-instalador-E8833A?style=flat-square&labelColor=1D1D1D" alt="Inno Setup">
  <img src="https://img.shields.io/badge/ESP32-MicroPython_y_C%2B%2B-E8833A?style=flat-square&labelColor=1D1D1D&logo=espressif&logoColor=white" alt="ESP32">
  <img src="https://img.shields.io/badge/MQTT-laboratorios-E8833A?style=flat-square&labelColor=1D1D1D&logo=mqtt&logoColor=white" alt="MQTT">
  <img src="https://img.shields.io/badge/Streamlit-paneles-E8833A?style=flat-square&labelColor=1D1D1D&logo=streamlit&logoColor=white" alt="Streamlit">
</p>

- **Escritorio Windows:** C#, .NET 10, WinUI 3, Native AOT, Direct3D 11 con shaders HLSL, FFmpeg (LGPL) por P/Invoke, PowerShell para construir y distribuir, GitHub Actions como CI en Windows y Linux.
- **Sensores y microcontroladores** ([Sensores-Teoria](https://github.com/Dathinel/Sensores-Teoria)): ESP32 con MicroPython y C++, Python con OpenCV, PyTorch, TensorFlow y Streamlit, laboratorios Docker con MQTT.

## Actividad

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Dathinel&show_icons=true&hide_border=true&bg_color=1D1D1D&title_color=E8833A&icon_color=E8833A&text_color=ECECEC&ring_color=E8833A&locale=es" alt="Estadísticas de GitHub de Dathinel" height="165">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Dathinel&layout=compact&hide_border=true&bg_color=1D1D1D&title_color=E8833A&text_color=ECECEC&locale=es" alt="Lenguajes más usados" height="165">
</p>

<sub>Textos e imágenes de este perfil: [CC BY 4.0](LICENSE). El nombre y el logotipo de Rodaje no se incluyen (ver su [TRADEMARK.md](https://github.com/Dathinel/rodaje/blob/main/TRADEMARK.md)).</sub>
