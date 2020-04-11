import pytest

# Все методы класса должны использовать аргумент
@pytest.mark.parametrize("test_input", [1, 2, 3])
class TestClassParametrized:

    def test_one(self, test_input, param_test):
        pass

    def test_two(self, test_input):
        pass
