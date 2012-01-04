from com.eviware.soapui.tools import (SoapUITestCaseRunner)

class SoapUILibrary:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LIBRARY_VERSION = '0.1'

    def run_project(self, prj):
        runner = SoapUITestCaseRunner()
        runner.setProjectFile(prj)
        if not runner.run():
            raise AssertionError('FAIL: failed to run')

        if runner.getFailedTests().size() != 0:
            raise AssertionError('FAIL: ' + str(n) + ' tests failed')
