from cffi import FFI

ffi = FFI()
ffi.cdef("""
    void* rpmverNew(const char *e, const char *v, const char *r);
    void* rpmverFree(void*);
    int rpmverCmp(void*, void*);
""")

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
    return value.encode('utf-8')

rpmverNew = rpmio.rpmverNew
rpmverFree = rpmio.rpmverFree
rpmverCmp = rpmio.rpmverCmp
