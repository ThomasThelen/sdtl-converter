import unittest
from unittest import mock
from pathlib import Path

from sdtlconverter import SDTLClient

json_response = {"data: SDTL_SAMPLE HERE"}

class TestClient(unittest.TestCase):

    def mocked_sdtl_post(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        return MockResponse(json_response, 200)

    def test_ctor(self):
        client_url = "test_url"
        test_path_path = Path("randomDirmyScrtipt.py")
        client = SDTLClient.SDTLClient(client_url, test_path_path, "python")
        self.assertEqual(len(client.input_files), 1)
        self.assertEqual(len(client.input_directories), 0)
        self.assertEqual(len(client.results), 0)

        #with mock.patch.object(Path, 'is_file') as path_mock:
        #    path_mock.return_value = True
        #    self.client = SDTLClient(self.client_url, Path("file1.txt"))

        #    self.assertTrue(len(self.client.input_files))


        # with mock.patch.object(Path, 'is_dir') as path_mock:
        #    path_mock.return_value = True
        #    self.client = SDTLClient(self.client_url, Path("dir1/"))
        #    self.assertTrue(len(self.client.input_directories))

    def test_add_result(self):
        filename = 'test'
        sdtl = {}
        client_url = "test_url"
        test_path_path = Path("randomDirmyScrtipt.py")
        client = SDTLClient.SDTLClient(client_url, test_path_path, "python")
        client.add_result(sdtl, filename)
        self.assertEqual(len(client.results), 1)
        res = client.results[0]
        self.assertEqual(res.filename, filename)
        self.assertEqual(res.sdtl, sdtl)

    def test_add_file(self):
        # Test with str
        client_url = "test_url"
        test_path_path = Path("randomDirmyScrtipt.py")
        client = SDTLClient.SDTLClient(client_url, test_path_path, "python")
        client.add_file(test_path_path)
        self.assertEqual(len(client.input_files), 2)
        self.assertEqual(client.input_files[1], test_path_path)

    #def test_add_directory(self):
    #    client.add_directory(test_directory_str)
    #    self.assertEqual(len(client.input_directories), 1)
    #    self.assertEqual(client.input_directories[0].as_posix(), test_directory_str)

        #client.add_directory(self.test_directory_path)
        #self.assertEqual(len(self.client.input_directories), 2)
        #self.assertEqual(client.input_directories[1].as_posix(), test_directory_path.as_posix())

    @mock.patch('requests.post', side_effect=mocked_sdtl_post)
    def test_get_sdtl(self, mock_get):
        with mock.patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            client_url = "test_url"
            test_path_path = Path("randomDirmyScrtipt.py")
            client = SDTLClient.SDTLClient(client_url, test_path_path, "python")
            test_file = Path('testFile.R')
            sdtl_result = client.get_sdtl(test_file)
            self.assertEqual(sdtl_result, json_response)

        mocked_file.assert_called_once()

    def test_save(self):
        filename = 'test'
        sdtl = {}
        client_url = "test_url"
        test_path_path = Path("randomDirmyScrtipt.py")
        client = SDTLClient.SDTLClient(client_url, test_path_path, "python")
        client.add_result(sdtl, filename)
        with mock.patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            client.save()
        mocked_file.assert_called_once()


if __name__ == '__main__':
    unittest.main()
