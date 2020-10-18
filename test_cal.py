import pytest

from calualate import Calculator


class TestCal:

    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # 测试加法
    @pytest.mark.parametrize('a,b,expect', [
        [1, 2, 3], [112233, 332211, 444444], [1.23, 2.23, 3.46], [-1, -2, -3]

    ], ids=['int_class', 'big_calss', 'float_class', 'negative_calss'])
    def test_add1(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    # 测试减法
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 0], [2.2, 1.2, 1], [-1, -2, 1]
    ], ids=['integer', 'decimals', 'minus'])
    def test_minus(self, a, b, expect):
        result = round(self.calc.minus(a, b))
        assert result == expect

    # 测试乘法
    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [2.2, 2.2, 5], [-1, -2, 2]
    ], ids=['int_case', 'big_case', 'minus_case'])
    def test_multiply(self, a, b, expect):
        result = round(self.calc.multiply(a, b))
        assert result == expect

    # 测试除法
    @pytest.mark.parametrize('a,b,expect', [
        [54, 6, 9], [120000, 500, 240], [340, 3.4, 100], [15, -1, -10], [1, 0, 1]
    ], ids=['int_case', 'big_case', 'fload_case', 'minus_case', 'zero_case'])
    def test_div(self, a, b, expect):
        result = round(self.calc.divide(a, b))
        assert result == expect


if __name__ == '__main__':
    pytest.main()
