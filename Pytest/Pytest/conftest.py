# to share the fixture to all the files
import pytest

# if @pytest.fixture(scope ='class') the yield will be applied in the end of the class with tests'

@pytest.fixture()
def setup():
    print('I will be executed first!')
    yield  #all that is written after will be executed last after all the tests
    print('I will be executed last!')

@pytest.fixture()
def datalog():
    print('User data is created')
    return ['Ole', 'Buimistr', 'ole@gmail.com']

@pytest.fixture(params=['Chrome', 'FireFox', 'IE'])
def crossBrowser(request):
    return  request.param

# @pytest.fixture(params=[('Chrome', 'Ole'), 'FireFox', 'IE']) example - sent multiple values to the run