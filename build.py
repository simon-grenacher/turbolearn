"""Baut index.html (eigenständig, Bilder eingebettet) aus src/app.html und src/cars/.
Aufruf: python3 build.py"""
import base64, os
root = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(root, 'src', 'app.html'), encoding='utf-8').read()
for f in sorted(os.listdir(os.path.join(root, 'src', 'cars'))):
    b64 = base64.b64encode(open(os.path.join(root, 'src', 'cars', f), 'rb').read()).decode()
    s = s.replace("'cars/%s'" % f, "'data:image/jpeg;base64,%s'" % b64)
assert "'cars/" not in s, 'Bild fehlt in src/cars'
head = '''<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="TurboLearn">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#07090d">
<style>*{box-sizing:border-box}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head><body>
'''
open(os.path.join(root, 'index.html'), 'w', encoding='utf-8').write(head + s + '\n</body></html>')
print('index.html gebaut')
