import os
from pathlib import Path

import click
from click_help_colors import HelpColorsGroup


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='magenta',
    help_options_custom_colors={
        'up': 'cyan',
        'push': 'cyan',
        'undo': 'red',
        'unstage': 'red',
        'revert': 'red',
        'diff': 'green',
        'branch': 'green',
        'add': 'blue',
        'commit': 'blue',
        'save': 'blue',
    }
)
def cli():
    """\b
          _____                .__
        _/ ____\ __ __   ____  |  |  ______
        \   __\ |  |  \ /    \ |  |  \____ \
         |  |   |  |  /|   |  \|  |__|  |_> >
         |__|   |____/ |___|  /|____/|   __/
                            \/       |__|
    """



@cli.command(help='Print version.')
def version():
    here = Path(__file__).parent.absolute()
    package_conf = {}
    with open(os.path.join(here, "__version__.py")) as f:
        exec(f.read(), package_conf)
    print(package_conf['__version__'])


def run():
    try:
        cli(prog_name='funlp')
    except Exception as e:
        pass


if __name__ == "__main__":
    run()
