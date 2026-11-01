# Código QR del taller

[![Código QR para abrir la página del taller](qr.png)](https://TU-USUARIO.github.io/taller-fish/)

**Escanea el código para abrir la página:** <https://TU-USUARIO.github.io/taller-fish/>

> ⚠️ **Antes de publicar:** esa URL es un ejemplo. Cuando subas el proyecto a GitHub Pages, actualiza la dirección real con
> `python3 tools/make_qr.py https://tu-usuario.github.io/tu-repo/` y reemplaza también el enlace de este README.

---

## Proyecto educativo

Este repositorio es un **trabajo académico** del Taller de Auditoría y Seguridad. La página reproduce el portal **Co-banking de AV Villas** con un único propósito: **mostrar cómo se ve un phishing real** y enseñar a reconocerlo.

- **No envía ni almacena datos.** El formulario no tiene backend, no envía peticiones y no guarda información. Simula la carga de sesión y la clave temporal; al final muestra lo escrito (con botón **Ver**, enmascarado) y vacía todos los campos.
- **No está afiliado** a AV Villas, Grupo Aval ni a ninguna entidad financiera. La marca y los recursos gráficos se usan únicamente con fines académicos.
- **No usa cookies** ni servicios externos: funciona sin conexión.
- El aviso del pie y la nota del formulario son parte del ejercicio. Si publicas la página, no los elimines.

> Esta página **no debe usarse para capturar datos reales** ni presentarse como el sitio oficial de una entidad financiera. Un clon de un login bancario, sin el aviso de simulación, es un kit de phishing.

Si encontraste esta página fuera del contexto del taller, no ingreses datos reales en ningún sitio al que llegues por un enlace o un QR.

## Recursos usados

| Archivo | Uso |
| --- | --- |
| `brand-primary.svg` | Logo de AV Villas en la tarjeta de login |
| `forgot-password.svg` | Ilustración del candado en la modal de clave temporal |
| `Banner-card_modal_lg.webp` | Promoción «Eleva tu Rentabilidad» |
| `Banner-card_2_new.webp` | Promoción de Bre-B |
| `Banner-card_3_new.webp` | Promoción de nómina |
| `Onest-*.ttf` | Tipografía Onest (Regular, Medium, SemiBold, Bold) |
| `favicon.png` | Icono de la pestaña |

Los banners se redimensionaron (900–1000 px de ancho, WebP) para que la página cargue rápido. Los archivos `styles.*.css`, `indigo-pink.css` y las imágenes `*_md` / `*_modal` que no se usan quedaron como material de referencia; puedes borrarlos.

## Actualizar el QR

```bash
python3 tools/make_qr.py https://tu-usuario.github.io/tu-repo/
```

Genera `img/qr.png` y `img/qr.svg` con la nueva dirección. Requiere [`segno`](https://pypi.org/project/segno/): `pip install segno`.
