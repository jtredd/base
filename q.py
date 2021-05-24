"""Attemp to use heap"""

BUFFER = b'47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
task = {}
priority = []
priorities = ()

wchar: dict = {i.to_bytes(1, 'big'): i for i in range(0, 255)}
uintlong: dict = {i: b for b, i in wchar.items() if i > 128}
uintshort: dict = {i: b for b, i in wchar.items() if i < 32}
uint: dict = {i: b for b, i in wchar.items() if not uintlong.get(i) and i > 32}
# might want to exclude b'\x7f', b'\x80', b'!', b'"' to name a few from `uint`


#class ImageSequence:
#  def __init__(self, im):
#    self.im = im
#
#  def __getitem__(self, ix):
#    try:
#      if ix:
#        self.im.seek(ix)
#      return self.im
#    except EOFError:
#      raise IndexError   # end of sequence
#

# my_hexlify() module
#BUFFER = b'47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
"""
In [2]: hexlify(BUFFER)
7 @[0] 7 @[1] 7 @[2] 6 @[3] 6 @[4] 7 @[5] 1 @[6] 0 @[7] 1 @[8] 0 @[9] 8 @[10] 0 @[11] 0 @[12] 0 @[13] 0 @[14] 0 @[15] 8 @[16] 8 @[17] 8 @[18] 6 @[19] 8 @[20] 3 @[21] 1 @[22] 0 @[23] 0 @[24] 0 @[25] 0 @[26] 6 @[27] 0 @[28] 0 @[29] 0 @[30] 0 @[31] 1 @[32] 0 @[33] 1 @[34] 0 @[35] 0 @[36] 2 @[37] 1 @[38] 7 @[39] 0 @[40] 6 @[41]
Out[2]: b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'
"""
# to_bytes(_chunk_bs(BUFFER)) ==> hexlify()
# hexlify(BUFFER) ==> bytestring


def _chunk_bs(bs, step=2):
    """chunk by step count"""
    stop = len(bs)
    start = 0
    bs_to_list = []
    for bstep in range(0, stop, step):
        bs_to_list.insert(bstep, bs[start:bstep+step])
        start = start + step
    return bs_to_list

def _from_list(self: list):
    """bytelist to ints"""
    return [int(str(b, 'utf8'), 16) for b in self if b.decode('utf8', errors='ignore').isalpha]
   
def _bit_length(self: int):
    s = bin(self)
    s = s.lstrip('-0b')
    return len(s)

def to_bytes(self: list):
    """intlist to bytes"""
    return [b.to_bytes(1, byteorder='big') for b in _from_list(self)]


def to_bin(self: str):
    for b in _from_list(_chunk_bs(self)):
        return bin(b)

def hexlify(self: str, verbose=False):
    """str/int repr to hex"""
    nbytes = len(_chunk_bs(self))
    buf = b''
    strlen = ''
    for b in to_bytes(_chunk_bs(self)):
        buf+=b
#    for s in _from_list(_chunk_bs(self)):
#        strlen+=f'{ _bit_length(s): 02d}'
    if verbose:
        for n in range(nbytes):
            strlen += f'{_bit_length(_from_list(_chunk_bs(self))[n])} @[{n}] '
        print(strlen)
    return buf



class Mapping:
    """sub classed object for transitive updates"""
    def __init__(self, iterable):
        self.entries = []
        self.__update(iterable)

    def update(self, iterable):
        """instance class object"""
        for entry in iterable:
            self.entries.append(entry)

    __update = update


class MappingSubclass(Mapping):
    """Instance class override"""
    def update(self, keys, values):
      # provides new signature for update()
      # but does not break __init__()
        for entry in zip(keys, values):
            self.entires.append(entry)


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.count = self.count + 1
        self.index = self.index - 1
        return self.data[self.index]



def heappush(heap, item):
    """Push the item onto the heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def heapify(x):
    """ O(len(x)) linear time """
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)



def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos -1) >> 1
        parent = heap[parentpos]
        if newitem < heap[pos]:
            heap[pos] = parent
            pos = parentpos
            continue
        break

    heap[pos] = newitem

def _siftup(heap, pos):
    endpos = len(heap)
    # assuming length is counting literal
    # types?
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1
    while childpos < endpos:
        # Set childpos to index of previous index
        rightpos = childpos + 1
        # avoid IndexError
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
       # increment index
        heap[pos] = heap[childpos]
        pos = childpos
       # Blow another Bubble
        childpos = 2*pos + 1
    # The leaf at pos is empty now.
    # Sift the parents down.
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


#if __name__ == "__main__":
#    from heapq import heappush, heappop
#    heapq = []
#    data = [1, 3, 5, 7, 11, 13, 1, 7, 2, 0]
#    for item in data:
#        heappush(heapq, item)
#    sort = []
#    while heapq:
#        sort.append(heappop(heapq))
#    print(sort)
