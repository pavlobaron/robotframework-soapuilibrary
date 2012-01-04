from com.eviware.soapui.tools import (SoapUITestCaseRunner)

class SoapUILibrary:

    ROBOT_LIBRARY_SCOPE = 'TEST CASE'
    ROBOT_LIBRARY_VERSION = '0.2'

    def soapui_project(self, prj):
        self.__runner = SoapUITestCaseRunner()
        self.__runner.setProjectFile(prj)

    def soapui_suite(self, s):
        self.__runner.setTestSuite(s)

    def soapui_case(self, c):
        self.__runner.setTestCase(c)

    def soapui_run(self):
        if not __runner.run():
            raise AssertionError('FAIL: failed to run')

        n = self.__runner.getFailedTests().size()
        if n != 0:
            raise AssertionError('FAIL: ' + str(n) + ' tests failed')
