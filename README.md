# Despedida interactiva v2

Esta versión usa `<details>` y `<summary>`, componentes nativos de HTML.
Por eso los bloques se abren y cierran sin JavaScript.

## Prueba
Abre `index.html` en Safari, Chrome o Firefox. Luego entra a cualquier clan y toca:
- Ingredientes del cóctel
- Colores del tartán
- Reto inicial
- Regla secreta

## Publicación
Puedes subir la carpeta a GitHub Pages o Netlify.

## QR permanentes
1. Publica el sitio.
2. Reemplaza `base_url` en `config.json`.
3. Instala `qrcode[pil]`.
4. Ejecuta `python generar_qr.py`.

Los QR no tienen que cambiar cuando actualices el contenido de las páginas.
