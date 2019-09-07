from __future__ import unicode_literals

import datetime
import re
import sys

__all__ = ("stringify_date_param",)


# Date in ISO-8601 format
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_LEN = len("YYYY-MM-DD")
DATE_FMT = "%Y-%m-%d"

# Datetime in ISO-8601 format
DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$")
DATETIME_LEN = len("YYYY-MM-DDTHH:MM:SS")
DATETIME_FMT = "%Y-%m-%dT%H:%M:%S"


def stringify_date_param(dt):
    if is_valid_string(dt):
        if len(dt) == DATE_LEN:
            validate_date_str(dt)
        elif len(dt) == DATETIME_LEN:
            validate_datetime_str(dt)
        else:
            raise ValueError("Date input should be in format of either YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS")
        return dt
    # Careful: datetime.datetime is subclass of datetime.date!
    elif isinstance(dt, datetime.datetime):
        # TODO: time zone
        return dt.strftime(DATETIME_FMT)
    elif isinstance(dt, datetime.date):
        return dt.strftime(DATE_FMT)
    elif is_valid_num(dt):
        return datetime.datetime.utcfromtimestamp(dt).strftime(DATETIME_FMT)
    else:
        raise TypeError("Date input must be one of: str, date, datetime, float, int, or None")


def validate_date_str(datestr):
    if not DATE_RE.match(datestr):
        raise ValueError("Date input should be in format of YYYY-MM-DD")


def validate_datetime_str(datetimestr):
    if not DATETIME_RE.match(datetimestr):
        raise ValueError("Datetime input should be in format of YYYY-MM-DDTHH:MM:SS")


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:

    def is_valid_string(var):
        return isinstance(var, str)

    def is_valid_num(var):
        return isinstance(var, (int, float))


elif PY2:

    def is_valid_string(var):
        return isinstance(var, basestring)  # noqa

    def is_valid_num(var):
        return isinstance(var, (int, float, long))  # noqa


else:

    def is_valid_string(var):
        raise SystemError("unsupported version of python detected (supported versions: 2, 3)")
