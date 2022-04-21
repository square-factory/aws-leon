import click

from . import __version__
from .commands.clean import Cleaner
from .commands.report import Reporter
from .utils import get_default_region


@click.group()
def cli() -> None:
    pass


@cli.command()
def version() -> None:
    print(__version__)


def global_options(opt):
    opt = click.option('--region', required=False, default=get_default_region(), help='TODO')(opt)
    opt = click.option('--keep-previous', required=False, default=10, help='TODO')(opt)
    opt = click.option('--min-days', required=False, default=10, help='TODO')(opt)
    return opt


@cli.command(help='TODO')
@click.option('--param', default=1, help='TODO')
@click.argument('arg')
def clean(param, name):
    print(Cleaner().execute())


@cli.command(help='TODO')
@global_options
def report(region: str, keep_previous: int, min_days: int):
    return Reporter(region, keep_previous, min_days).execute()
