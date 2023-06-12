import pytest
from Pytest.baseClass import baseClass

@pytest.mark.usefixtures('datalog')
class Test_userData:
    def test_userData(self, datalog):
        print(datalog)
        print(datalog[0])
        print(datalog[1])

@pytest.mark.usefixtures('datalog')
class Test_userData2(baseClass):
    def test_editProfile(self, datalog):
        print(datalog)
        log = self.getlogger()
        log.info(datalog[0])
        print(datalog[1])