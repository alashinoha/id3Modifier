import unittest

from TrackEntitiesLoader import TrackEntitiesLoader


class MyTestCase(unittest.TestCase):

    path = "/some/path"

    def test_generate_settings_success(self):
        TrackEntitiesLoader(self.path).generate_settings()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
