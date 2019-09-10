import os
import tempfile
import unittest

import tempus


class TempusTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False)
        self.tmp.close()
        tempus.DATA_FILE = self.tmp.name
        tempus.save({"entries": []})

    def tearDown(self):
        os.unlink(self.tmp.name)

    def test_start_and_stop(self):
        self.assertEqual(tempus.start("reading"), 0)
        self.assertEqual(tempus.stop(), 0)
        entries = tempus.load()["entries"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["label"], "reading")
        self.assertIsNotNone(entries[0]["end"])

    def test_cannot_start_twice(self):
        tempus.start("first")
        self.assertEqual(tempus.start("second"), 1)


if __name__ == "__main__":
    unittest.main()
