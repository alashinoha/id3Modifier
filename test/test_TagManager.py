import unittest

from TagManager import TagManager
from TrackEntitiesLoader import TrackEntitiesLoader


class MyTestCase(unittest.TestCase):

    path = "/some/path"

    def test_read(self):
        tl = TrackEntitiesLoader(self.path).load_list_from_settings()
        for track in tl[:1]:
            tags = TagManager.read(track)
            print(tags)
        self.assertEqual(True, True)  # add assertion here

    def test_bulk_update(self):
        tl = TrackEntitiesLoader(self.path).load_list_from_settings()
        TagManager.bulk_update(tl)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
