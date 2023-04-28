import unittest
import os

#from tests.main import *

# //////////////////////////////////////////////////////////////////////////////////////////

from tests.main import LogFile, defaultLogFile

class TestLogFile(unittest.TestCase):
    def setUp(self):
        self.filename = "testlog.txt"
        with open(self.filename, 'w') as file:
            file.write("test")

    def testFileCreated(self):
        os.remove(self.filename)
        self.assertEqual(LogFile(self.filename), "File created")
        self.assertTrue(os.path.exists(self.filename))

    def testFileExistsNotTruncated(self):
        self.assertEqual(LogFile(self.filename, ClearLogFile=False), "File exists not truncated")
        with open(self.filename, 'r') as file:
            self.assertEqual(file.read(), "test")

    def testFileExistsTruncated(self):
        self.assertEqual(LogFile(self.filename, ClearLogFile=True), "File exists truncated")
        with open(self.filename, 'r') as file:
            self.assertEqual(file.read(), "")

    def testGlobalDefaultLogFile(self):
        self.filename = "newtestLog.txt"
        print(defaultLogFile)
        LogFile(self.filename)
        print(defaultLogFile)
        self.assertEqual(defaultLogFile, self.filename)

# //////////////////////////////////////////////////////////////////////////////////////////

class TestLog(unittest.TestCase):
    def setUp(self):
        self.defaultLogFile = "log.txt"
        self.defaultLogMessageType = "INFO"
        self.logSettings = True

    def testLogSucceeded(self):
        pass

    def testLogFailed(self):
        pass

if __name__ == '__main__':
    unittest.main()

