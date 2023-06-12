# Any pytest file should start with test_
# Any test method  should start with test_
# Any code should be wrapped in method
# 1 method == 1 testcase
import pytest

# creating the file with the name conftest and writing there permits to use of the code in this file in all the cases

# for running - configuration and select pytest configuration,after select the file for running
# - for run in terminal py.test -v -s - all cases py.test name -v -s  - specific cases


# @pytest.Mark.smoke  #for mark the test as smoke and then run only marked
# @pytest.Mark.skip  #for mark the test for skipping
# @pytest.Mark.xfile #for mark the test - it will run but not include in the report
# for generate the HTML report run pytest --html=report.html      https://pytest-html.readthedocs.io/en/latest/user_guide.html


def test_FirstTest():
    print('Hi')

def test_SecondTest():
    msg = 'Hi'
    assert msg == 'yyy'

@pytest.fixture()
def setup():
    print('I will be executing first!')

def test_demoFixture(setup):  #will go and execute first def setup
    print('I will go for setup')