#
# This file is part of SoapUI test library for the Robot Framework
#
# Copyright (c) 2012 by Pavlo Baron (pb[at]pbit[dot]org)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from com.eviware.soapui.tools import (SoapUITestCaseRunner)

class SoapUILibrary:
    """ The main class of the library """
    
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'
    ROBOT_LIBRARY_VERSION = '0.2'

    def __init__(self):
        self.__runner = None

    def soapui_project(self, prj):
        """ Initialize the runner and set the project string """
        self.__runner = SoapUITestCaseRunner()
        self.__runner.setProjectFile(prj)

    def soapui_suite(self, s):
        """ Set the suite string """
        self.__runner.setTestSuite(s)

    def soapui_case(self, c):
        """ Set the test case string """
        self.__runner.setTestCase(c)

    def soapui_run(self):
        """ Run the runner and report to Robot """
        if not self.__runner.run():
            raise AssertionError('FAIL: failed to run')

        n = self.__runner.getFailedTests().size()
        if n != 0:
            raise AssertionError('FAIL: ' + str(n) + ' tests failed')
