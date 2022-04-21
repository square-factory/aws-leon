import logging

from rich.highlighter import ReprHighlighter
from rich.logging import RichHandler

from . import index


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(
            rich_tracebacks=True,
            markup=True,
            highlighter=ReprHighlighter()
        )]
    )
    logging.getLogger("rich")
    index.cli()
