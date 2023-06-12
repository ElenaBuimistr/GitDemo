import pytest


@pytest.mark.usefixtures('setup')
class Test_userData():

    def test_FirstTest(self):
        print('Hi')

    def test_SecondTest(self):
        print('Hi')

    def test_First2Test(self):
        print('Hi')