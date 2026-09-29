"""The casino: the dashboard where users create accounts and pick games."""

from montycasino.accounts import CasinoAccountManager
from montycasino.errors import AccountNotFoundError, InvalidGameSelectionError
from montycasino.game import Game
from montycasino.games import GAMES
from montycasino.player import Player
from montycasino.utils import AnsiColor, IOConsole


class Casino:
    def __init__(
        self,
        console: IOConsole | None = None,
        account_manager: CasinoAccountManager | None = None,
    ) -> None:
        self.console = console or IOConsole(AnsiColor.BLUE)
        self.account_manager = account_manager or CasinoAccountManager()

    def run(self) -> None:
        """Show the arcade dashboard until the user logs out."""
        while (choice := self._dashboard_input()) != "logout":
            if choice == "select-game":
                self._select_game()
            elif choice == "create-account":
                self._create_account()

    def _select_game(self) -> None:
        name = self.console.get_string_input("Enter your account name:")
        password = self.console.get_string_input("Enter your account password:")
        account = self.account_manager.get_account(name, password)
        if account is None:
            # TODO - implement better exception handling
            raise AccountNotFoundError(
                f"No account found with name of [ {name} ] and password of [ {password} ]"
            )
        selection = self._game_selection_input().upper()
        if selection not in GAMES:
            # TODO - implement better exception handling
            raise InvalidGameSelectionError(f"[ {selection} ] is an invalid game selection")
        game_class, player_class = GAMES[selection]
        self._play(game_class(), player_class(account))

    def _create_account(self) -> None:
        self.console.println("Welcome to the account-creation screen.")
        name = self.console.get_string_input("Enter your account name:")
        password = self.console.get_string_input("Enter your account password:")
        account = self.account_manager.create_account(name, password)
        self.account_manager.register_account(account)

    def _dashboard_input(self) -> str:
        return self.console.get_string_input(
            "Welcome to the Arcade Dashboard!"
            "\nFrom here, you can select any of the following options:"
            "\n\t[ create-account ], [ select-game ], [ logout ]"
        )

    def _game_selection_input(self) -> str:
        options = ", ".join(f"[ {name} ]" for name in GAMES)
        return self.console.get_string_input(
            "Welcome to the Game Selection Dashboard!"
            "\nFrom here, you can select any of the following options:"
            f"\n\t{options}"
        )

    @staticmethod
    def _play(game: Game, player: Player) -> None:
        game.add(player)
        game.run()
