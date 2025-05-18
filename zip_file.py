def reverse_rle(bytestr: bytes):
    retbytes = b''
    for i in range(1, len(bytestr), 2):
        retbytes = retbytes + (bytestr[i])*int.to_bytes(bytestr[i-1], 1,"big")
    return retbytes

if __name__ == "__main__":
    print(reverse_rle(b'A\x04B\x02C\x01D\x02'))