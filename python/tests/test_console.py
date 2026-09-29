import pytest

from montycasino.utils import AnsiColor, IOConsole
from montycasino.utils.ansi_color import RESET


def test_println_colours_and_formats(make_console):
    console, out = make_console()
    console.color = AnsiColor.RED
    console.println("hi {} and {}", "a", 2)
    assert out.getvalue() == f"{AnsiColor.RED.code}hi a and 2\n{RESET}"


def test_braces_untouched_without_args(make_console):
    console, out = make_console()
    console.print("{not a placeholder}")
    assert "{not a placeholder}" in out.getvalue()


def test_string_input_prompts_and_returns_line(make_console):
    console, out = make_console("Kris")
    assert console.get_string_input("Name?") == "Kris"
    assert "Name?" in out.getvalue()


def test_input_raises_eof_when_closed(make_console):
    console, _ = make_console()
    with pytest.raises(EOFError):
        console.get_string_input("?")


def test_float_input_retries_until_valid(make_console):
    console, out = make_console("abc", "", "2.5")
    assert console.get_float_input("Amount?") == 2.5
    assert out.getvalue().count("invalid user input") == 2
    assert "numeric value" in out.getvalue()


def test_int_input_retries_until_valid(make_console):
    console, out = make_console("1.5", "x", "42")
    assert console.get_int_input("Number?") == 42
    assert out.getvalue().count("invalid user input") == 2
    assert "integer value" in out.getvalue()


def test_prompt_arguments_are_formatted(make_console):
    console, out = make_console("7")
    console.get_int_input("Pick 1-{}", 10)
    assert "Pick 1-10" in out.getvalue()


def test_defaults_to_standard_streams(capsys):
    IOConsole().println("hello")
    assert "hello" in capsys.readouterr().out


@pytest.mark.parametrize("color", list(AnsiColor))
def test_every_colour_is_an_escape_code(color):
    assert color.code.startswith("\x1b[") and color.code.endswith("m")
