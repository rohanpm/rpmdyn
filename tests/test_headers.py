import os

import pytest

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
WALRUS_RPM = os.path.join(DATA_DIR, "walrus-5.21-1.noarch.rpm")
TEST_SRPM = os.path.join(DATA_DIR, "test-srpm01-1.0-1.src.rpm")


def get_header(rpm, filename):
    ts = rpm.TransactionSet()
    ts.setVSFlags(rpm._RPMVSF_NOSIGNATURES | rpm._RPMVSF_NODIGESTS)

    with open(filename, "rb") as f:
        hdr = ts.hdrFromFdno(f.fileno())

    return hdr


@pytest.fixture
def header_walrus(rpm):
    yield get_header(rpm, WALRUS_RPM)


@pytest.fixture
def header_test_srpm(rpm):
    yield get_header(rpm, TEST_SRPM)


@pytest.mark.parametrize("rpmname,key,value", [("walrus", "name", "walrus")])
def test_header_value(request, rpmname, key, value, rpm):
    hdr = request.getfixturevalue("header_" + rpmname)

    key = getattr(rpm, "RPMTAG_%s" % key.upper())

    actual_value = hdr[key]

    assert value == actual_value
    assert type(value) == type(actual_value)
