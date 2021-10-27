#!/usr/bin/python3

import rpm

for sym in sorted(dir(rpm)):
    if sym.upper() != sym:
        continue

    value = getattr(rpm, sym)
    if not isinstance(value, (int, str)):
        continue

    print("%s = %s" % (sym, repr(value)))
