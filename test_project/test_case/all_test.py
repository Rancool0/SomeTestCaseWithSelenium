import unittest,HTMLTestRunner
def createsuite():
    suite = unittest.TestSuite()
    file_dir = '/home/chenyueming/test_project/test_case'
    discover = unittest.defaultTestLoader.discover(
        file_dir,
        pattern = 'test*.py',
        top_level_dir = None
    )
    for test_file in discover:
        for test_case in test_file:
            suite.addTest(test_case)
    return suite

if __name__ == '__main__':
    file_obj = open('/home/chenyueming/Desktop/test.html','wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file_obj,
        title='Test Report',
        description = 'The detail of the test',
    )
    runner.run(createsuite())