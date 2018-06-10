import json
import os

from terminals import konsole


def load_scheme(scheme_path):
    def create_bold_foreground_color(fore_color, back_color):
        bold = [fc + 48 * (1 if fc > bc else -1) for fc, bc in zip(fore_color, back_color)]
        bold = [max(min(x, 255), 0) for x in bold]
        return bold

    with open(scheme_path) as f:
        scheme = json.load(f)

    if 'bold_foreground_color' not in scheme:
        fore, back = scheme['foreground_color'], scheme['background_color']
        scheme['bold_foreground_color'] = create_bold_foreground_color(fore, back)
    return scheme


def load_schemes(scheme_dir):
    with os.scandir(scheme_dir) as it:
        schemes = [load_scheme(x.path) for x in it]
    return schemes


def get_current_terminal():
    return 'konsole'


def main():
    gogh_dir = os.path.dirname(os.path.abspath(__file__))
    scheme_dir = os.path.join(gogh_dir, 'schemes')
    terminal = get_current_terminal()
    if terminal == 'konsole':
        save_dir = os.path.join(os.getenv('HOME'), '.local/share/konsole')
        konsole.write_schemes(load_schemes(scheme_dir), save_dir)
    else:
        raise ValueError('Unknown terminal %s.' % terminal)


if __name__ == '__main__':
    main()
