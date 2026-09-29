from unittest.mock import patch

from montycasino.__main__ import main


def test_main_runs_a_casino():
    with patch("montycasino.__main__.Casino") as casino_class:
        main()
    casino_class.return_value.run.assert_called_once_with()
