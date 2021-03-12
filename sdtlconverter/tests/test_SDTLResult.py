import unittest
from sdtlconverter import SDTLResult
from unittest import mock


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_sdtl = test_sdtl={"var1": "111"}
        self.test_filename = "sdtl_test_output.json"
        self.res = SDTLResult.SDTLResult(self.test_sdtl, self.test_filename)
    def test_ctor(self):
        self.assertEqual(self.res.sdtl, self.test_sdtl)
        self.assertEqual(self.res.filename, self.test_filename)

    def test_save(self):
        with mock.patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            self.res.save()
        mocked_file.assert_called_once()


if __name__ == '__main__':
    unittest.main()
