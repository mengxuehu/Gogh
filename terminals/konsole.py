import os

variants = ['', 'Faint', 'Intense']


def format_color_scheme(basename, rgbs):
    """
    rgbs: [regular_rgb, faint_rgb, intense_rgb]
    """
    result = ''
    for rgb, suffix in zip(rgbs, variants):
        result += '[%s%s]\nColor=%d,%d,%d\n\n' % (basename, suffix, rgb[0], rgb[1], rgb[2])
    return result


def write_schemes(schemes, target_dir):
    for s in schemes:
        name = 'gogh-' + s['name']
        with open(os.path.join(target_dir, name + '.colorscheme'), 'w') as f:
            f.write(format_color_scheme('Background', [s['background_color']]))

            for i in range(0, 8):
                f.write(format_color_scheme('Color' + str(i),
                                            [s['colors'][i], s['colors'][i], s['colors'][i + 8]]))

            f.write(format_color_scheme('Foreground',
                                        [s['foreground_color'], s['foreground_color'],
                                         s['bold_foreground_color'] or s['colors'][-1]]))

            f.write('[General]\nDescription=%s' % name)
