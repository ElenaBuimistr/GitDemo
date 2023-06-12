import pytest

# @pytest.fixture()
# def setup():
#     print('I will be executed first!')
#     yield  #all that is written after will be executed last after all the tests
#     print('I will be executed last!')

def test_demoFixture(setup):  #will go and execute first def setup
    print('I will go for setup')

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
