import datetime
import unittest

from newsapi import utils


class StringifyDateParamTest(unittest.TestCase):
    """Test utils.stringify_date_param()."""

    def test_str_input(self):
        for inp in (
            "2019-01-01",
            "2019-01-01T00:00:00",
            "2019-12-30T00:00:00",
            "2019-12-30T04:05:06",
            "2019-09-06T16:17:48",
        ):
            if utils.PY3:
                with self.subTest(inp=inp):
                    self.assertEqual(inp, utils.stringify_date_param(inp))
            else:
                self.assertEqual(inp, utils.stringify_date_param(inp))

    def test_date_input(self):
        self.assertEqual("2019-01-01", utils.stringify_date_param(datetime.date(2019, 1, 1)))
        self.assertEqual("2019-12-30", utils.stringify_date_param(datetime.date(2019, 12, 30)))

    def test_datetime_input(self):
        self.assertEqual("2019-01-01T00:00:00", utils.stringify_date_param(datetime.datetime(2019, 1, 1)))
        self.assertEqual("2019-12-30T00:00:00", utils.stringify_date_param(datetime.datetime(2019, 12, 30)))
        self.assertEqual("2019-12-30T04:05:06", utils.stringify_date_param(datetime.datetime(2019, 12, 30, 4, 5, 6)))

    def test_unix_ts_input(self):
        self.assertEqual("2019-09-06T16:17:48", utils.stringify_date_param(1567786668.826787))
        self.assertEqual("2019-09-06T16:17:48", utils.stringify_date_param(1567786668))

    def test_malformed_str_input(self):
        for bad_input in ("20190101", "01-01-2019", "2019-01-01 00:00:00", "2019-01-01T00:00:00-04:00"):
            if utils.PY3:
                with self.subTest(bad_input=bad_input):
                    with self.assertRaises(ValueError):
                        utils.stringify_date_param(bad_input)
            else:
                with self.assertRaises(ValueError):
                    utils.stringify_date_param(bad_input)

    def test_incorrect_type_input(self):
        with self.assertRaises(TypeError):
            utils.stringify_date_param(None)
        with self.assertRaises(TypeError):
            utils.stringify_date_param([datetime.date(2019, 12, 30)])
