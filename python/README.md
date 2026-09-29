# MontyCasino (Python)

The casino starter project. It is a scaffold: the dashboard, console and class structure work, and the parts
students implement are stubs that raise `NotImplementedError`.

```bash
cd python
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
montycasino                      # or: python -m montycasino
pytest --cov=montycasino         # fails under 80% coverage, as the assignment requires
```

Requires Python 3.11+.

## Layout

```
python/
├── pyproject.toml
├── src/montycasino/
│   ├── casino.py            # Casino: the dashboard loop
│   ├── accounts.py          # CasinoAccount, CasinoAccountManager (stubs)
│   ├── game.py              # Game: abstract base class for games
│   ├── player.py            # Player: abstract base class for players
│   ├── errors.py            # AccountNotFoundError, InvalidGameSelectionError
│   ├── utils/               # IOConsole, AnsiColor
│   └── games/
│       ├── __init__.py      # GAMES registry: menu name -> (game, player)
│       ├── slots/           # SlotsGame, SlotsPlayer (stubs)
│       └── numberguess/     # NumberGuessGame, NumberGuessPlayer (stubs)
└── tests/
```

## What you implement

1. `CasinoAccountManager.get_account`, `create_account`, `register_account`, and give `CasinoAccount` a balance.
2. `SlotsGame` / `SlotsPlayer` and `NumberGuessGame` / `NumberGuessPlayer`.
3. Four more games (see the root README for the requirements).

To add a game, write a `Game` and `Player` subclass and add one line to `GAMES`; the menu updates itself.

The tests marked `xfail` describe behaviour you still owe. They are *strict*: once you implement something, its test reports as failing until you delete the marker.

## Design notes

- `Game` and `Player` are abstract base classes. All players must have a reference to the `CasinoAccount` used to log in, and are capable of `play`ing a game. `Game` implements `add` / `remove` with a list, so multi-player games work out of the box; each subclass defines how the game will `run`.
- `CasinoAccount` is registered for each user and is used to log in and select a game. It outlives any single game, so it is the natural owner of the player's balance.
- `CasinoAccountManager` stores, manages and retrieves accounts. It is advised that every operation in it is logged.
- `IOConsole` prompts the user and reads input. Its message templates use `str.format` placeholders (`"{}"`), and its streams are injectable so tests need no mocking. `AnsiColor` supplies output colours.
- `Casino` chooses a game through the `GAMES` dictionary, so the menu updates itself when one is added.
- The `TODO`s in `Casino` mark where better error handling is expected: a failed login raises `AccountNotFoundError` and a bad selection raises `InvalidGameSelectionError`.
