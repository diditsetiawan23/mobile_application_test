import asyncio
import unittest
import jpype as jp
from utils.drivers import driver
from wrappers import wrap
from tests import test_register
from tests import test_login

class MyTestSuite(unittest.TestCase):
    def test_Issue(self):
        mobile_test = unittest.TestSuite()
        mobile_test.addTests(
                [
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                    test_register.RegisterTestCase
                ),
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                    test_login.LoginTestCase
                ),
            ]
        )

        runner1 = unittest.TextTestRunner()
        runner1.run(mobile_test)

    def tearDown(self) -> None:
        # shutdown JVM
        jp.shutdownJVM()
        # close driver
        driver.quit()
        # sending report
        asyncio.run(wrap.send_result_to_telegram())

if __name__ == "__main__":
    unittest.main(exit=False)