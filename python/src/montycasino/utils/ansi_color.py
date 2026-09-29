"""Colours for :class:`~montycasino.utils.console.IOConsole` output."""

from enum import Enum


class AnsiColor(Enum):
    AUTO = "\x1b[0m"
    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    PURPLE = "\x1b[35m"
    CYAN = "\x1b[36m"
    WHITE = "\x1b[37m"

    @property
    def code(self) -> str:
        return self.value


RESET = AnsiColor.AUTO.code
