import pytest

from montycasino.game import Game
from montycasino.games import GAMES, NumberGuessGame, NumberGuessPlayer, SlotsGame, SlotsPlayer
from montycasino.player import Player

todo = pytest.mark.xfail(raises=NotImplementedError, strict=True, reason="not yet implemented")


def test_game_and_player_are_abstract(account):
    with pytest.raises(TypeError):
        Game()
    with pytest.raises(TypeError):
        Player(account)


def test_registry_maps_names_to_classes():
    assert GAMES == {
        "SLOTS": (SlotsGame, SlotsPlayer),
        "NUMBERGUESS": (NumberGuessGame, NumberGuessPlayer),
    }


@pytest.mark.parametrize("game_class, player_class", GAMES.values())
class TestEveryGame:
    def test_is_wired_to_the_base_classes(self, game_class, player_class):
        assert issubclass(game_class, Game)
        assert issubclass(player_class, Player)

    def test_player_keeps_reference_to_account(self, game_class, player_class, account):
        assert player_class(account).account is account

    def test_supports_adding_and_removing_players(self, game_class, player_class, account):
        game, first, second = game_class(), player_class(account), player_class(account)
        game.add(first)
        game.add(second)
        assert game.players == [first, second]
        game.remove(first)
        assert game.players == [second]

    def test_games_do_not_share_player_lists(self, game_class, player_class, account):
        a, b = game_class(), game_class()
        a.add(player_class(account))
        assert b.players == []

    @todo
    def test_game_runs(self, game_class, player_class):
        game_class().run()

    @todo
    def test_player_plays(self, game_class, player_class, account):
        player_class(account).play()
