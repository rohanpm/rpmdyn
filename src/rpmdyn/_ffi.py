from cffi import FFI

ffi = FFI()
ffi.cdef(
    """
    typedef void* Header;
    typedef void* rpmtd;
    typedef uint32_t rpm_count_t;
    typedef int32_t rpmTagVal;
    typedef int32_t rpmTagType;
    typedef int32_t rpmTagClass;
    typedef uint32_t rpmtdFlags;

    void* rpmverNew(const char *e, const char *v, const char *r);
    void* rpmverFree(void*);
    int rpmverCmp(void*, void*);

    void* fdDup(int);

    rpmtd rpmtdNew();
    rpmtd rpmtdFree(void*);
    rpm_count_t rpmtdCount(rpmtd);
    rpmTagVal rpmtdTag(rpmtd);
    rpmTagType rpmtdType(rpmtd);
    rpmTagClass rpmtdClass(rpmtd);
    rpmtdFlags rpmtdGetFlags(rpmtd);
    const char* rpmtdGetString(rpmtd);

    void* rpmtsCreate();
    void* rpmtsFree(void*);
    uint32_t rpmtsSetVSFlags(void*, uint32_t);

    int rpmReadPackageFile(void*, void*, const char*, Header*);

    Header headerNew();
    Header headerFree(void*);
    int headerGet(Header, int32_t, void*, uint32_t);
"""
)

rpm = ffi.dlopen("rpm")
rpmio = ffi.dlopen("rpmio")

# >>> arg = ffi.new("char[]", b"world")        # equivalent to C code: char arg[] = "world";
# >>> C.printf(b"hi there, %s.\n", arg)        # call printf
# hi there, world.
# 17                                           # this is the return value
# >>>

NULL = ffi.NULL
gc = ffi.gc


def cstr(value, nullable=False):
    if value is None and nullable:
        return NULL
    if value is None and not nullable:
        raise TypeError("expected str, got None")
    return value.encode("utf-8")


rpmverNew = rpmio.rpmverNew
rpmverFree = rpmio.rpmverFree
rpmverCmp = rpmio.rpmverCmp

fdDup = rpmio.fdDup

rpmtdNew = rpm.rpmtdNew
rpmtdFree = rpm.rpmtdFree
rpmtdCount = rpm.rpmtdCount
rpmtdTag = rpm.rpmtdTag
rpmtdType = rpm.rpmtdType
rpmtdClass = rpm.rpmtdClass
rpmtdGetFlags = rpm.rpmtdGetFlags
rpmtdGetString = rpm.rpmtdGetString

rpmtsCreate = rpm.rpmtsCreate
rpmtsFree = rpm.rpmtsFree
rpmtsSetVSFlags = rpm.rpmtsSetVSFlags

rpmReadPackageFile = rpm.rpmReadPackageFile

headerNew = rpm.headerNew
headerFree = rpm.headerFree
headerGet = rpm.headerGet
