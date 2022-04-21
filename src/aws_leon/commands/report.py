from ..config import Config
from ..resources import AMI
from rich.console import Console
from rich.table import Table


class Reporter:
    def __init__(self, region: str, keep_previous: int, min_days: int) -> None:
        self.region = region
        self.keep_previous = keep_previous
        self.min_days = min_days
        self.config = Config(region, keep_previous, min_days)

    def execute(self):
        self.config.display()
        console = Console()

        with console.status("Retrieving AMIs data..."):
            candidates = AMI().filter(self.config)

        table = Table(title="AMIs data")
        table.add_column("ImageId", justify="left", style="cyan")
        table.add_column("Name", justify="center", style="green")
        table.add_column("CreationDate", justify="center", style="magenta")
        for ami in candidates:
            table.add_row(
                ami, candidates[ami]["name"], candidates[ami]["creation_date"]
            )
        console = Console()
        console.print()
        console.print(table)
        console.print()
