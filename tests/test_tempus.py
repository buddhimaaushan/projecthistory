import os
import tempfile
import unittest

from tempus import cli


class TempusTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False)
        self.tmp.close()
        cli.DATA_FILE = self.tmp.name
        cli.save({"entries": []})

    def tearDown(self):
        os.unlink(self.tmp.name)

    def test_start_and_stop(self):
        self.assertEqual(cli.start("reading"), 0)
        self.assertEqual(cli.stop(), 0)
        entries = cli.load()["entries"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["label"], "reading")
        self.assertIsNotNone(entries[0]["end"])

    def test_cannot_start_twice(self):
        cli.start("first")
        self.assertEqual(cli.start("second"), 1)


if __name__ == "__main__":
    unittest.main()
