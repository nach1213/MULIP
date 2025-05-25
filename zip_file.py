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

def BWT(bytestr: bytes):
    bytestr = b'^' + bytestr +b'$'
    n = len(bytestr)
    bwt = [''] * n
    i = 0
    for sa_i in SA(bytestr):
        print(sa_i)
        if sa_i == 0:
            bwt[i] = bytestr[n - 1].to_bytes()
        else:
            bwt[i] = bytestr[sa_i - 1].to_bytes()
        i += 1
    return b''.join(bwt)

def SA(bytestr: bytes):
    n = len(bytestr)
    suffixes = [(bytestr[-i:]+bytestr[:-i], i) for i in range(n)]
    suffixes.sort(key=lambda pair: pair[0])
    return [index for (_, index) in suffixes]


def unzip_file(bytes_:bytes):
    bytes_ = ''.join(f'{b:08b}' for b in bytes_)
    i=0
    ind = 0
    while i<256:
        if bytes_[ind] == 0:
            ind+=1
            i += 1
            continue







if __name__ == "__main__":
    print((rle(b"A" * 2)))
    print(rle(BWT(b"BANANA")))

