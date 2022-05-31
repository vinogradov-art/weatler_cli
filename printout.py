import datetime
from rich import box
from rich.console import Console
from rich.table import Table


def printout(data: dict) -> None:
    console = Console()
    console.rule(f"погода в городе {data['city']} на {datetime.datetime.now().strftime('%d-%m-%Y')}")
    table = Table(expand=True, show_lines=True, box=box.SQUARE, highlight=True, border_style="green")
    table.add_column("Наименование", justify="left", width=20)
    table.add_column("значение", justify="center")

    table.add_row(
        f"Температура",
        f"{data['temperature']} °C",
    )
    table.add_row(
        f"За окном",
        f"{data['weather'].capitalize()}",
    )
    table.add_row(
        f"Скорость ветра",
        f"{data['wind']} m/s",
    )
    table.add_row(
        f"Давление",
        f"{data['pressure']} hPa"
    )
    table.add_row(
        f"Влажность",
        f"{data['humidity']} %"
    )
    console.print(table)
