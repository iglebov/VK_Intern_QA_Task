import pytest


class TestSet:
    """Тесты для типа данных set."""

    @pytest.mark.parametrize("value, result", [({1, 2}, {1, 2}), ({1, 1}, {1})])
    def test_set(self, value, result):
        assert value, result

    def test_set_error(self):
        with pytest.raises(TypeError):
            assert {1} + {2}

    def test_set_with_fixture(self, data_for_set: tuple):
        assert set(data_for_set).pop() == 1


class TestFloat:
    """Тесты для типа данных float."""

    @pytest.mark.parametrize(
        "value, result",
        [("-2.5", -2.5), ("0", 0.0), ("2.5", 2.5)],
    )
    def test_float(self, value, result):
        assert float(value) == result

    def test_float_error(self):
        with pytest.raises(ZeroDivisionError):
            assert 2.1 % 0

    def test_float_with_fixture(self, data_for_float: str):
        assert float(data_for_float) == 100.0
