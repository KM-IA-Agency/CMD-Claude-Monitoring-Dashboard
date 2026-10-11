from cmdash import __version__
from cmdash.cli import main


def test_version_is_set() -> None:
    assert __version__ == "0.0.0"


def test_main_returns_zero(capsys) -> None:
    assert main([]) == 0
    assert "cmdash" in capsys.readouterr().out
