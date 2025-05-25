import heapq

class Node:
    def __init__(self, sz, val=None, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        self.sz = sz
    def __lt__(self, other):
        return self.sz < other.sz
def get_huffman_tree(s):
    hist = [0 for i in range(256)]
    for i in s:
        hist[int(i)] += 1
    heap = [Node(hist[i], i) for i in range(256) if hist[i]]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        par = Node(a.sz+b.sz, None, a, b)
        heapq.heappush(heap, par)
    return heap[0]

def code_all(tree: Node, codes, cur=""):
    if tree is None:
        return
    if tree.val is not None:
        codes[tree.val] = cur
    else:
        code_all(tree.left, codes, cur+"0")
        code_all(tree.right, codes, cur+"1")
def zip_file(s: bytes) -> bytes:
    tree = get_huffman_tree(s)
    codes = ["" for i in range(256)]
    code_all(tree, codes)
    encoded = "".join([codes[int(i)] for i in s])
    end = ""
    for i in range(256):
        if not len(codes[i]):
            end += "0"
        else:
            la = bin(len(codes[i]))[2:]
            la = (8-len(la))*"0" + la
            end += "1" + la + codes[i]
    if len(end)%8:
        end += (8-len(end)%8)*"0"
    f = (len(encoded) + len(end)) % 8
    if f > 0:
        f = 8-f
    ignore = bin(f)[2:]
    ignore = (8 - len(ignore)) * "0" + ignore
    total = end + ignore + encoded
    c = [int(total[i:i + 8], 2) for i in range(0, len(total), 8)]
    return bytes(c)

def get(arr):
    ans = 0
    for i in arr:
        ans *= 2
        ans += i
    return ans
from bitarray import bitarray

def unzip_file(bytes_:bytes) -> bytes:
    ba = bitarray()
    ba.frombytes(bytes_)
    #bytes_ = ''.join(f'{b:08b}' for b in bytes_)
    ind = 0
    codes = dict()
    for i in range(256):
        if ba[ind] == 0:
            ind += 1
            continue
        ind += 1
        sz = get(ba[ind:ind+8])
        ind += 8
        c = ba[ind:ind+sz]
        codes["".join(str(i) for i in ba[ind:ind+sz])] = i
        ind += sz
    if ind%8 != 0:
        ind += 8-ind%8
    ans = bytes()
    cur = ""
    ignore = get(ba[ind:ind+8])
    ind += 8
    while ind < len(ba)-ignore:
        cur += str(ba[ind])
        a = codes.get(cur)
        if a is not None:
            ans += a.to_bytes(1, "big")
            cur = ""
        ind += 1
    return ans


if __name__ == "__main__":
    b = zip_file(b"urherhfureh ioghtzhgitrhiotehgjzrijgiore")
    print(unzip_file(b))
