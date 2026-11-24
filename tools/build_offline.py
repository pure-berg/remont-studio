import re, sys
src, dl, out = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
three = open(dl + '/three.min.js', encoding='utf-8').read()
orbit = open(dl + '/OrbitControls.js', encoding='utf-8').read()
for name, js in (('three', three), ('orbit', orbit)):
    assert '</script' not in js.lower(), name
# drop Google Fonts (fallback fonts are in the stacks)
s = re.sub(r'<link rel="preconnect"[^>]*>\n', '', s)
s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\n', '', s)
s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
s = s.replace('<script src="https://cdn.jsdelivr.net/npm/three@0.147.0/build/three.min.js"></script>', '<script>\n' + three + '\n</script>')
s = s.replace('<script src="https://cdn.jsdelivr.net/npm/three@0.147.0/examples/js/controls/OrbitControls.js"></script>', '<script>\n' + orbit + '\n</script>')
assert not re.search(r'(src=|<link[^>]*href=)"https?://', re.sub(r'<script>.*?</script>', '', s, flags=re.S)), 'external resource left'
head = '<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
s = s.replace('<style>\n', '<style>\nbody{margin:0}[hidden]{display:none!important}\n', 1)
i = s.index('</style>') + len('</style>')
s = head + s[:i] + '\n</head>\n<body>' + s[i:] + '\n</body>\n</html>\n'
open(out, 'w', encoding='utf-8').write(s)
print('ok', len(s))
