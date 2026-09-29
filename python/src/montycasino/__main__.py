"""Entry point: ``python -m montycasino`` or the ``montycasino`` script."""

from montycasino.casino import Casino


def main() -> None:
    Casino().run()


if __name__ == "__main__":
    main()
