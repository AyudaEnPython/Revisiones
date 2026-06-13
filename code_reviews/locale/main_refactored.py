import locale
from contextlib import contextmanager
from datetime import datetime
from decimal import Decimal
from platform import system
from typing import Final, Generator

_WIN_LOCALE: Final[str] = "es-ES"
_POSIX_LOCALE: Final[str] = "es_ES.UTF-8"


@contextmanager
def _scoped_locale(category: int) -> Generator[None, None, None]:
    # 'setlocale()' mutates global process state; restore it on exit.
    target = _WIN_LOCALE if system() == "Windows" else _POSIX_LOCALE
    saved = locale.setlocale(category)
    try:
        locale.setlocale(category, target)
        yield
    except locale.Error:
        yield
    finally:
        locale.setlocale(category, saved)


def format_currency(value: Decimal) -> str:
    with _scoped_locale(locale.LC_MONETARY):
        return locale.currency(value, grouping=True)


def format_date(dt: datetime) -> str:
    with _scoped_locale(locale.LC_TIME):
        return dt.strftime("%x")


if __name__ == "__main__":
    amount: Decimal = Decimal("1234567.89")
    today: datetime = datetime.now()
    print(f"Amount: {format_currency(amount)}")
    print(f"Date: {format_date(today)}")
