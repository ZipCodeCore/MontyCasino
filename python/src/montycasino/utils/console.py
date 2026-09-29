"""Prompting the user and reading their answers."""

import sys
from typing import TextIO

from montycasino.utils.ansi_color import RESET, AnsiColor


class IOConsole:
    """Writes coloured output and reads input from text streams.

    Message templates use :meth:`str.format` placeholders, filled in only
    when arguments are given::

        console.println("Hello, {}!", name)
    """

    def __init__(
        self,
        color: AnsiColor = AnsiColor.AUTO,
        stdin: TextIO | None = None,
        stdout: TextIO | None = None,
    ) -> None:
        self.color = color
        self._stdin = stdin or sys.stdin
        self._stdout = stdout or sys.stdout

    def print(self, message: str, *args: object) -> None:
        text = message.format(*args) if args else message
        self._stdout.write(f"{self.color.code}{text}{RESET}")
        self._stdout.flush()

    def println(self, message: str, *args: object) -> None:
        self.print(message + "\n", *args)

    def get_string_input(self, prompt: str, *args: object) -> str:
        self.println(prompt, *args)
        line = self._stdin.readline()
        if not line:
            raise EOFError("input stream closed")
        return line.rstrip("\r\n")

    def get_float_input(self, prompt: str, *args: object) -> float:
        while True:
            answer = self.get_string_input(prompt, *args)
            try:
                return float(answer)
            except ValueError:
                self.println("[ {} ] is an invalid user input!", answer)
                self.println("Try inputting a numeric value!")

    def get_int_input(self, prompt: str, *args: object) -> int:
        while True:
            answer = self.get_string_input(prompt, *args)
            try:
                return int(answer)
            except ValueError:
                self.println("[ {} ] is an invalid user input!", answer)
                self.println("Try inputting an integer value!")
