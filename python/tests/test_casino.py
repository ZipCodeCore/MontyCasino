import pytest

from montycasino.accounts import CasinoAccount, CasinoAccountManager
from montycasino.casino import Casino
from montycasino.errors import AccountNotFoundError, CasinoError, InvalidGameSelectionError
from montycasino.game import Game
from montycasino.games import GAMES
from montycasino.player import Player


class FakeAccounts(CasinoAccountManager):
    """An in-memory manager so the dashboard can be tested independently."""

    def __init__(self):
        self.accounts: dict[tuple[str, str], CasinoAccount] = {}
        self.log: list[str] = []

    def get_account(self, name, password):
        return self.accounts.get((name, password))

    def create_account(self, name, password):
        self.log.append(f"create {name}")
        return CasinoAccount()

    def register_account(self, account):
        self.log.append("register")


class RecordingGame(Game):
    ran: list["RecordingGame"] = []

    def run(self):
        RecordingGame.ran.append(self)


class RecordingPlayer(Player):
    def play(self):
        return "played"


def test_logout_ends_the_loop(make_console):
    console, out = make_console("logout")
    Casino(console).run()
    assert "Welcome to the Arcade Dashboard!" in out.getvalue()


def test_unknown_dashboard_input_just_reprompts(make_console):
    console, out = make_console("bogus", "logout")
    Casino(console).run()
    assert out.getvalue().count("Welcome to the Arcade Dashboard!") == 2


def test_default_console_and_manager():
    casino = Casino()
    assert isinstance(casino.account_manager, CasinoAccountManager)


def test_create_account_flow(make_console):
    console, out = make_console("create-account", "leon", "secret", "logout")
    accounts = FakeAccounts()
    Casino(console, accounts).run()
    assert accounts.log == ["create leon", "register"]
    assert "account-creation screen" in out.getvalue()


def test_select_game_runs_the_chosen_game(make_console, monkeypatch):
    RecordingGame.ran.clear()
    monkeypatch.setitem(GAMES, "SLOTS", (RecordingGame, RecordingPlayer))
    console, out = make_console("select-game", "leon", "secret", "slots", "logout")
    accounts = FakeAccounts()
    account = accounts.accounts["leon", "secret"] = CasinoAccount()
    Casino(console, accounts).run()
    (game,) = RecordingGame.ran
    (player,) = game.players
    assert player.account is account
    assert "[ SLOTS ], [ NUMBERGUESS ]" in out.getvalue()


def test_bad_login_raises(make_console):
    console, _ = make_console("select-game", "leon", "wrong")
    with pytest.raises(AccountNotFoundError, match="name of \\[ leon \\] and password of \\[ wrong \\]"):
        Casino(console, FakeAccounts()).run()


def test_bad_game_selection_raises(make_console):
    console, _ = make_console("select-game", "leon", "secret", "poker")
    accounts = FakeAccounts()
    accounts.accounts["leon", "secret"] = CasinoAccount()
    with pytest.raises(InvalidGameSelectionError, match="POKER"):
        Casino(console, accounts).run()


def test_errors_share_a_base_class():
    assert issubclass(AccountNotFoundError, CasinoError)
    assert issubclass(InvalidGameSelectionError, CasinoError)


def test_stub_manager_surfaces_not_implemented(make_console):
    """With the starter manager, creating an account fails loudly (for now)."""
    console, _ = make_console("create-account", "a", "b")
    with pytest.raises(NotImplementedError):
        Casino(console).run()
