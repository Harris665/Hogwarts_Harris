# conftest是共享公共的fixture的，自动import的方法

# @pytest.fixture(autouse=True,scope='function')
# #autous为True时，自动应用到每个方法里面,默认为False；scope默认就是function级别的，还有class/module/package/session

# 如果项目有多个conftest文件，调用的是最近的那个

import pytest

from calualate import Calculator


@pytest.fixture(scope='module')
def get_calc():
    calc = Calculator()
    print("开始计算")
    yield calc
    print("计算结束")
