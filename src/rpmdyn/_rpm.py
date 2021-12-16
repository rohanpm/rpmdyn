from ._ffi import rpmverNew, rpmverFree, rpmverCmp, NULL, cstr, gc
from ._transaction import TransactionSet
from ._const import *

# This is what we need:

#     ts = rpm.TransactionSet()
#     # no rpm.keyring on rhel5
#     if hasattr(rpm, "keyring"):
#         # Set an empty keyring to prevent accessing rpmdb,
#         # which may cause race-conditions when running in threads.
#         # NOTE: RPM is *not* tread-safe, but this *usually* works in threads.
#         ts.setKeyring(rpm.keyring())
#     ts.setVSFlags(rpm._RPMVSF_NOSIGNATURES|rpm._RPMVSF_NODIGESTS)
#
# hdr = ts.hdrFromFdno(fo.fileno())
#
#
# return rpm.labelCompare((str(nvr1["epoch"]), str(nvr1["version"]), str(nvr1["release"])), (str(nvr2["epoch"]), str(nvr2["version"]), str(nvr2["release"])))


def labelCompare(a, b):
    (e1, v1, r1) = a
    (e2, v2, r2) = b

    rpmver1 = gc(rpmverNew(cstr(e1, True), cstr(v1), cstr(r1, True)), rpmverFree)
    rpmver2 = gc(rpmverNew(cstr(e2, True), cstr(v2), cstr(r2, True)), rpmverFree)

    return rpmverCmp(rpmver1, rpmver2)
