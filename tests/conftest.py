from pytest import fixture


@fixture
def data_for_set() -> tuple:
    return 1, 2, 3


@fixture
def data_for_float() -> str:
    return "1e+2"
