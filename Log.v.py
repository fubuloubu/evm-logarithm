@constant
@public
def log(a: int128, b: int128) -> int128:
    assert a > 1
    assert b > 1
    assert a >= b
    c: int128 = a
    res: int128 = 0
    for _ in range(256):
        if (c == 1):
            break
        if (c % b > 0):
            break
        c /= b
        res += 1
    return res
