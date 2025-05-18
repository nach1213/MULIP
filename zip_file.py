def reverse_rle(bytestr: bytes):
    retbytes = b""
    for i in range(1, len(bytestr), 2):
        retbytes = retbytes + (bytestr[i]) * int.to_bytes(bytestr[i - 1], 1, "big")
    return retbytes


def rle(bytestr: bytes):
    retbytes = b""
    count = 1
    for i in range(1, len(bytestr)):
        if bytestr[i] == bytestr[i - 1] and count < 255:
            count += 1
        elif count > 1:
            retbytes += bytestr[i - 1 : i] + int.to_bytes(count, 1, "big")
            count = 1
        else:
            retbytes += bytestr[i - 1 : i]
    retbytes += bytestr[-1:] + int.to_bytes(count, 1, "big")
    return retbytes


if __name__ == "__main__":
    print(rle(b"A" * 260))
