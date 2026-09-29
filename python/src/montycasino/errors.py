"""Exceptions raised by the casino."""


class CasinoError(Exception):
    """Base class for all casino errors."""


class AccountNotFoundError(CasinoError):
    """No account matches the given name and password."""


class InvalidGameSelectionError(CasinoError):
    """The requested game does not exist."""
