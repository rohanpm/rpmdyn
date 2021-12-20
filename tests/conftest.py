import rpm as native
import pytest

from rpmdyn import _rpm as dyn


@pytest.fixture(params=[native, dyn], ids=["native", "dyn"])
def rpm(request):
    yield request.param


@pytest.fixture()
def rpm_native():
    yield native


@pytest.fixture()
def rpm_dyn():
    yield dyn
