import unittest

from execute_by_path import execute_by_path


class MyTestCase(unittest.TestCase):
    path = "/some/path"

    def test_prepare_by_path(self):
        execute_by_path(self.path)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
