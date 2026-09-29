"""The account manager is a starter stub: these tests describe the contract.

Each ``xfail`` is strict, so once you implement a method its test will start
"unexpectedly passing" and fail, which is your cue to delete the marker.
"""

import pytest

from montycasino.accounts import CasinoAccount, CasinoAccountManager

todo = pytest.mark.xfail(raises=NotImplementedError, strict=True, reason="not yet implemented")


@todo
def test_created_and_registered_account_can_be_retrieved():
    manager = CasinoAccountManager()
    account = manager.create_account("leon", "secret")
    manager.register_account(account)
    assert manager.get_account("leon", "secret") is account


@todo
def test_unknown_account_returns_none():
    assert CasinoAccountManager().get_account("nobody", "nothing") is None


@todo
def test_wrong_password_returns_none():
    manager = CasinoAccountManager()
    manager.register_account(manager.create_account("leon", "secret"))
    assert manager.get_account("leon", "wrong") is None


def test_create_account_is_a_stub():
    with pytest.raises(NotImplementedError):
        CasinoAccountManager().create_account("a", "b")
    with pytest.raises(NotImplementedError):
        CasinoAccountManager().register_account(CasinoAccount())
    with pytest.raises(NotImplementedError):
        CasinoAccountManager().get_account("a", "b")
