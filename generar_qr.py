from pathlib import Path
import json, qrcode
root=Path(__file__).parent
cfg=json.loads((root/'config.json').read_text(encoding='utf-8'))
base=cfg['base_url'].rstrip('/')+'/'
if 'TU-USUARIO' in base:
    raise SystemExit('Edita base_url en config.json antes de generar los QR.')
out=root/'qr'
out.mkdir(exist_ok=True)
for g in cfg['groups']:
    url=base+g['slug']+'.html'
    qrcode.make(url).save(out/f"QR_{g['slug']}.png")
    print(g['name'], url)
