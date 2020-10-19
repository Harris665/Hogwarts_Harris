import allure
import pytest
import yaml

from calualate import Calculator


# 获取测试数据
def get_datas():
    with open("./calc.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


@allure.feature("计算器")
class TestCal:

    # def setup_class(self):
    #     print("计算开始")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # 测试加法
    # @pytest.mark.parametrize('a,b,expect', [
    #     [1, 2, 3], [112233, 332211, 444444], [1.23, 2.23, 3.46], [-1, -2, -3]
    #
    # ], ids=['int_class', 'big_calss', 'float_class', 'negative_calss'])
    @allure.story("加法")
    @pytest.mark.parametrize("a,b,expect", get_datas()['add']['datas'], ids=get_datas()['add']['ids'])
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    # 测试减法
    # @pytest.mark.parametrize('a,b,expect', [
    #     [1, 1, 0], [2.2, 1.2, 1], [-1, -2, 1]
    # ], ids=['integer', 'decimals', 'minus'])
    @allure.story("减法")
    @pytest.mark.parametrize("a,b,expect", get_datas()['sub']['datas'], ids=get_datas()['sub']['ids'])
    @pytest.mark.run(order=2)
    def test_minus(self, get_calc, a, b, expect):
        # result = round(self.calc.minus(a, b))
        result = round(get_calc.minus(a, b), 10)
        assert result == expect

    # 测试乘法
    # @pytest.mark.parametrize('a,b,expect', [
    #     [1, 1, 1], [2.2, 2.2, 5], [-1, -2, 2]
    # ], ids=['int_case', 'big_case', 'minus_case'])
    @allure.story("乘法")
    @pytest.mark.parametrize("a,b,expect", get_datas()['mul']['datas'], ids=get_datas()['mul']['ids'])
    @pytest.mark.run(order=3)
    def test_multiply(self, get_calc, a, b, expect):
        # result = round(self.calc.multiply(a, b))
        result = round(get_calc.multiply(a, b), 10)
        assert result == expect

    # 测试除法
    # @pytest.mark.parametrize('a,b,expect', [
    #     [54, 6, 9], [120000, 500, 240], [340, 3.4, 100], [15, -1, -10], [1, 0, 1]
    # ], ids=['int_case', 'big_case', 'fload_case', 'minus_case', 'zero_case'])
    @allure.story("除法")
    @pytest.mark.parametrize("a,b,expect", get_datas()['div']['datas'], ids=get_datas()['div']['ids'])
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, a, b, expect):
        if b != 0:
            result = get_calc.divide(a, b)
            assert result == expect

        if b == 0:
            try:
                get_calc.divide(a, b)
            except ZeroDivisionError as e:
                print("divesion by zero")

#
# if __name__ == '__main__':
#     pytest.main()


# import allure
# import pytest
# import yaml
#
#
# # from pythoncode.caculator import Caculator
#
# # 获取测试数据
# def get_datas():
#     with open('./calc.yaml', encoding='utf-8') as f:
#         datas = yaml.safe_load(f)
#     return datas
#
#
# @allure.feature("计算器")
# class TestCaculator:
#
#     def setup_class(self):
#         print("setup_class...")
#
#     def teardown_class(self):
#         print("teardown_class...")
#
#     # def setup_method(self):
#     #     self.calc = Caculator()
#     #     print("【开始计算】")
#     #
#     # def teardown_method(self):
#     #     print("【计算结束】")
#
#     @pytest.mark.run(order=1)
#     @allure.story("加法")
#     # @pytest.mark.parametrize('a,b,expect', [(1, 2, 3), (1, 1.4, 2.4), (8.8, 0.2, 9), (20, -12, 8),
#     #                                         (9223372036854775807, 1, 9223372036854775808), (1, 1, 3)],
#     #                          ids=['int+int', 'int+float', 'float+float', 'integer+iegative', 'BigNumber', 'make a failure'])
#     @pytest.mark.parametrize("a,b,expect", get_datas()['add']['datas'], ids=get_datas()['add']['ids'])
#     def test_add(self, get_calc, a, b, expect):
#         # result = self.calc.add(a, b)
#         result = get_calc.add(a, b)
#         assert result == expect
#
#     @pytest.mark.run(order=2)
#     @allure.story("减法")
#     @pytest.mark.parametrize("a,b,expect", get_datas()['sub']['datas'], ids=get_datas()['sub']['ids'])
#     def test_sub(self, get_calc, a, b, expect):
#         # result = self.calc.sub(a, b)
#         result = round(get_calc.sub(a, b), 10)
#         assert result == expect
#
#     @pytest.mark.run(order=3)
#     @allure.story("乘法")
#     # @pytest.mark.parametrize('a,b,expect', [(0, 2, 0), (2, -4, -8), (10, 0.2, 2)])
#     @pytest.mark.parametrize("a,b,expect", get_datas()['mul']['datas'], ids=get_datas()['mul']['ids'])
#     def test_mul(self, get_calc, a, b, expect):
#         # result = self.calc.mul(a, b)
#         result = round(get_calc.mul(a, b), 10)
#         assert result == expect
#
#     @pytest.mark.run(order=4)
#     @allure.story("除法")
#     # @pytest.mark.parametrize('a,b,expect',
#     #                          [(1, 2, 0.5), (2, 0.5, 4), (8.8, 8.8, 1), (20, -2, -10), (1, 0, ZeroDivisionError)],
#     #                          ids=['int/int', 'int/float', 'float/float', 'integer/iegative', 'Zero Division'])
#     @pytest.mark.parametrize("a,b,expect", get_datas()['div']['datas'], ids=get_datas()['div']['ids'])
#     def test_div(self, get_calc, a, b, expect):
#         if b != 0:
#             # result = self.calc.div(a, b)
#             result = get_calc.divide(a, b)
#             assert result == expect
#         if b == 0:
#             try:
#                 get_calc.divide(a, b)
#             except ZeroDivisionError as e:
#                 print("Divesion by Zero")
