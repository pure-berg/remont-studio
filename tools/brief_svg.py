"""Схемы для brief/index.html: угловая ловушка и облако. Печатает SVG в stdout по имени: trap | cloud.
Цвета фиксированные (страница светлая, печатается в PDF)."""
import sys

EDGE, ACCENT, TINT, INK, QUIET, GRID = '#8a8a8a', '#2563eb', '#ececec', '#1a1a1a', '#666', '#d4d4d4'
F = 'font-family="system-ui,sans-serif"'


def t(x, y, s, size=13, anchor='start', fill=INK, weight=None, rot=None):
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    w = f' font-weight="{weight}"' if weight else ''
    r = f' transform="rotate({rot[0]} {rot[1]:.1f} {rot[2]:.1f})"' if rot else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}"{a}{w}{r} fill="{fill}">{s}</text>'


def trap():
    s, ox, oy = 7, 150, 150
    P = lambda x, y: f'{ox + x * s:.1f},{oy + y * s:.1f}'
    bx1, fx1, fy1 = ox + 42 * s, ox + 49.07 * s, oy + 7.07 * s
    fx2, fy2 = ox + 7.07 * s, oy + 49.07 * s
    mid, face = ox + 24.5 * s, ox + 30.5 * s
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 560" {F} role="img" aria-label="Угловая ловушка, вид сверху">',
         t(24, 30, 'Ловушка в углу: плита поперёк угла, за ней пустой воздух', 15, weight=600),
         t(24, 50, 'Вид сверху на один угол, в масштабе', 11.5, fill=QUIET),
         f'<rect x="{ox-16}" y="{oy-16}" width="470" height="16" fill="{TINT}" stroke="{EDGE}"/>',
         f'<rect x="{ox-16}" y="{oy}" width="16" height="390" fill="{TINT}" stroke="{EDGE}"/>',
         t(ox + 452, oy - 24, 'стена', 11.5, 'end', QUIET), t(ox - 24, oy + 386, 'стена', 11.5, 'end', QUIET),
         f'<polygon points="{P(0,0)} {P(42,0)} {P(0,42)}" fill="{TINT}"/>',
         t(ox + 40, oy + 90, 'воздух,'), t(ox + 40, oy + 108, 'не заполнять'),
         f'<polygon points="{P(42,0)} {P(49.07,7.07)} {P(7.07,49.07)} {P(0,42)}" fill="{ACCENT}" fill-opacity="0.12" stroke="{ACCENT}" stroke-width="2"/>',
         t(mid, mid + 5, 'Rockwool 100 мм в спанбонде, ширина 60 см', 13, 'middle', weight=600, rot=(-45, mid, mid)),
         t(face, face + 4, 'лицо: мешковина', 11.5, 'middle', QUIET, rot=(-45, face, face)),
         f'<g fill="none" stroke="{EDGE}">'
         f'<path d="M{ox} 110H{bx1}M{ox} 104V116M{bx1} 104V116"/>'
         f'<path d="M{ox} 82H{fx1:.1f}M{ox} 76V88M{fx1:.1f} 76V88"/>'
         f'<path d="M{bx1} 116V{oy-16}M{fx1:.1f} 88V{fy1:.1f}" stroke-dasharray="3 3"/>'
         f'<path d="M{ox} {fy2+18:.1f}H{fx2:.1f}M{ox} {fy2+12:.1f}V{fy2+24:.1f}M{fx2:.1f} {fy2+12:.1f}V{fy2+24:.1f}"/>'
         f'<path d="M{fx2:.1f} {fy2:.1f}V{fy2+12:.1f}" stroke-dasharray="3 3"/></g>',
         t((ox + bx1) / 2, 103, '42 см: тут плита касается стены', 11.5, 'middle'),
         t((ox + fx1) / 2, 75, '49 см: дальше ловушка не заходит', 11.5, 'middle'),
         t((ox + fx2) / 2, fy2 + 40, '7 см', 11.5, 'middle')]
    for y, line in [(236, 'Плита под 45° к обеим стенам.'), (262, 'Так во всех четырёх углах,'),
                    (278, 'по высоте — до потолка.'), (304, 'Крепление: уголки к обеим'),
                    (320, 'стенам сверху и снизу.'), (346, 'За плитой ничего не ставить'), (362, 'и не зашивать.')]:
        o.append(t(548, y, line, 11.5))
    o.append('</svg>')
    return '\n'.join(o)


def cloud():
    s, ox, oy = 2, 75, 90
    X = lambda c: ox + c * s
    Y = lambda c: oy + c * s
    pt = lambda x, y, m: f'{X(305 - x if m else x):.1f},{Y(y):.1f}'

    def trp(m):
        return (f'<polygon points="{pt(0,0,m)} {pt(42,0,m)} {pt(0,42,m)}" fill="{TINT}"/>'
                f'<polygon points="{pt(42,0,m)} {pt(49.07,7.07,m)} {pt(7.07,49.07,m)} {pt(0,42,m)}" fill="none" stroke="{EDGE}" stroke-width="1.5"/>')

    def hang(x, y):
        return (f'<circle cx="{X(x)}" cy="{Y(y)}" r="6" fill="none" stroke="{INK}" stroke-width="1.5"/>'
                f'<circle cx="{X(x)}" cy="{Y(y)}" r="2" fill="{INK}"/>')

    sy0 = 562
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 640" {F} role="img" aria-label="Облако: план потолка и разрез">',
         t(24, 30, 'Облако: 13,5 см от боковых стен, 50 см от окна, низ ≈10 см под потолком', 15, weight=600),
         t(24, 50, 'План потолка у окна в масштабе, ниже разрез', 11.5, fill=QUIET),
         f'<rect x="{ox-12}" y="{oy-12}" width="634" height="12" fill="{TINT}" stroke="{EDGE}"/>',
         f'<rect x="{ox-12}" y="{oy}" width="12" height="370" fill="{TINT}" stroke="{EDGE}"/>',
         f'<rect x="{X(305)}" y="{oy}" width="12" height="370" fill="{TINT}" stroke="{EDGE}"/>',
         f'<rect x="{X(138)}" y="{oy-12}" width="240" height="12" fill="{GRID}" stroke="{EDGE}" stroke-dasharray="4 3"/>',
         t(X(198), oy - 20, 'окно', 11.5, 'middle', QUIET), t(ox, oy - 20, 'оконная стена', 11.5, fill=QUIET),
         trp(False), t(X(5), Y(15), 'Л1', 11.5, weight=600),
         trp(True), t(X(300), Y(15), 'Л2', 11.5, 'end', weight=600),
         f'<rect x="{X(13.5)}" y="{Y(50)}" width="{278*s}" height="{120*s}" fill="{ACCENT}" fill-opacity="0.12" stroke="{ACCENT}" stroke-width="2"/>']
    for i in range(29):
        y = Y(54 + 4 * i)
        o.append(f'<line x1="{X(13.5)}" x2="{X(291.5)}" y1="{y}" y2="{y}" stroke="{ACCENT}" stroke-opacity="0.35" stroke-width="0.75"/>')
    o += [hang(33, 60), hang(272, 60), hang(33, 160), hang(272, 160),
          f'<g fill="none" stroke="{EDGE}">'
          f'<path d="M{ox} {Y(110)}H{X(13.5)}"/>'
          f'<path d="M{X(152.5)} {oy}V{Y(50)}M{X(152.5)-6} {Y(50)}H{X(152.5)+6}"/>'
          f'<path d="M{X(298.5)} {Y(50)}V{Y(170)}M{X(298.5)-5} {Y(50)}H{X(298.5)+5}M{X(298.5)-5} {Y(170)}H{X(298.5)+5}"/>'
          f'<path d="M{X(13.5)} {Y(181)}H{X(291.5)}M{X(13.5)} {Y(181)-6}V{Y(181)+6}M{X(291.5)} {Y(181)-6}V{Y(181)+6}"/></g>',
          t(X(6.75), Y(110) - 6, '13,5', 11.5, 'middle'), t(X(152.5) + 8, Y(28), '50', 11.5),
          t(X(305) + 18, Y(112), '120', 11.5), t(X(152.5), Y(181) + 18, '278', 11.5, 'middle'),
          t(X(20), Y(44), '≈5 см до ловушки', 11.5),
          t(X(13.5), 490, '○ — 4 подвеса: 33 см от боковых стен, 60 и 160 см от окна', 11.5),
          t(24, 522, 'Разрез поперёк облака (по высоте крупнее)', 13, weight=600),
          f'<rect x="80" y="{sy0-12}" width="400" height="12" fill="{TINT}" stroke="{EDGE}"/>',
          f'<path d="M130 {sy0}V{sy0+16}M430 {sy0}V{sy0+16}" stroke="{INK}" stroke-width="1.25"/>',
          f'<rect x="106" y="{sy0+16}" width="348" height="20" fill="{TINT}" stroke="{EDGE}"/>',
          f'<rect x="100" y="{sy0+20}" width="6" height="16" fill="none" stroke="{INK}" stroke-width="1.25"/>',
          f'<rect x="454" y="{sy0+20}" width="6" height="16" fill="none" stroke="{INK}" stroke-width="1.25"/>']
    for i in range(30):
        o.append(f'<rect x="{100 + 3 * (0.7 + 4 * i):.1f}" y="{sy0+36}" width="7.8" height="4" fill="{ACCENT}"/>')
    o += [f'<path d="M90 {sy0}V{sy0+40}M84 {sy0}H96M84 {sy0+40}H96" fill="none" stroke="{EDGE}"/>',
          t(280, sy0 - 18, 'потолок, анкеры', 11.5, 'middle', QUIET),
          t(280, sy0 + 12, 'трос с регулировкой', 11.5, 'middle'),
          t(280, sy0 + 30, 'вата 50 мм в спанбонде', 11.5, 'middle'),
          t(100, sy0 + 58, 'PLASTWOOD 9 мм, рейками вниз', 11.5),
          t(460, sy0 + 58, 'рама из рейки 20 × 40', 11.5, 'end'),
          t(80, sy0 + 24, '≈10 см', 11.5, 'end'), '</svg>']
    return '\n'.join(o)


if __name__ == '__main__':
    print({'trap': trap, 'cloud': cloud}[sys.argv[1]]())
