from importlib.metadata import entry_points

display_eps = entry_points(group="timmins.display")
try:
    display = display_eps[0].load()
except IndexError:

    def display(text: str) -> None:
        print(text)


def hello_world() -> None:
    display("Hello world")
