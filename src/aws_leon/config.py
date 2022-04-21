from rich.console import Console
from rich.table import Table


class Config:
    def __init__(self, region: str, keep_previous: int, min_days: int) -> None:
        self._region = region
        self._keep_previous = keep_previous
        self._min_days = min_days

    def display(self) -> None:
        table = Table(title="Configuration values")
        table.add_column("Setting", justify="left", style="cyan")
        table.add_column("Value", justify="right", style="green")
        table.add_row("region", f"{self._region}")
        table.add_row("keep_previous", f"{self._keep_previous}")
        table.add_row("min_days", f"{self._min_days}")
        console = Console()
        console.print()
        console.print(table)
        console.print()

    @property
    def region(self) -> str:
        return self._region

    @property
    def keep_previous(self) -> int:
        return self._keep_previous

    @property
    def min_days(self) -> int:
        return self._min_days
