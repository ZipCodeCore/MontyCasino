# MontyCasino (Python)

The Python edition of the casino starter project. Like the Java edition, it is
a scaffold: the dashboard, console and class structure work, and the parts
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
│   ├── casino.py            # Casino: the dashboard loop (was Casino.java)
│   ├── accounts.py          # CasinoAccount, CasinoAccountManager (stubs)
│   ├── game.py              # Game ABC        (was GameInterface)
│   ├── player.py            # Player ABC      (was PlayerInterface)
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

## Java to Python notes

- `GameInterface` / `PlayerInterface` became abstract base classes. `Game` already implements `add` / `remove` with a list, so multi-player games work out of the box.
- Players take their `CasinoAccount` in the constructor (the Java version's players had no way to get one).
- `IOConsole` uses `str.format` placeholders (`"{}"`), loops instead of recursing on bad numeric input, and resets colour after each write. Streams are injectable, so tests need no mocking.
- The `Casino` game `if/else` chain became the `GAMES` dictionary.
- Java's `Casino` swapped the name and password in its "No account found" message; that is fixed.
- The dashboard now lists `[ logout ]`, which the Java code accepted but never mentioned.
- The exception `TODO`s from the Java code are kept, but with specific exception types.
