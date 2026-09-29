import io

import pytest

from montycasino.accounts import CasinoAccount
from montycasino.utils import IOConsole


@pytest.fixture
def make_console():
    """Build a console fed by ``lines``; returns ``(console, output_buffer)``."""

    def factory(*lines: str) -> tuple[IOConsole, io.StringIO]:
        out = io.StringIO()
        stdin = io.StringIO("".join(f"{line}\n" for line in lines))
        return IOConsole(stdin=stdin, stdout=out), out

    return factory


@pytest.fixture
def account() -> CasinoAccount:
    return CasinoAccount()
