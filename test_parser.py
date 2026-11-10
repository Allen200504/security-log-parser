import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from parser import count_failed_logins


class TestLoginParser(unittest.TestCase):
    def parse_csv(self, contents):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "log.csv"
            path.write_text(contents, encoding="utf-8")
            return dict(count_failed_logins(path))

    def test_counts_failed_logins(self):
        sample = Path(__file__).with_name("sample_logs.csv")
        self.assertEqual(dict(count_failed_logins(sample)), {"alice": 2, "bob": 1})

    def test_success_only(self):
        self.assertEqual(self.parse_csv("username,result\nalice,success\n"), {})

    def test_header_only(self):
        self.assertEqual(self.parse_csv("username,result\n"), {})

    def test_missing_result_column(self):
        with self.assertRaisesRegex(ValueError, "username and result columns"):
            self.parse_csv("username\nalice\n")

    def test_invalid_result(self):
        with self.assertRaisesRegex(ValueError, "line 2"):
            self.parse_csv("username,result\nalice,unknown\n")