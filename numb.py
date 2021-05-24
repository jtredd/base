""" simple number functions """

def xor_byte(buf, key):
    out = ''
    for b in buf:
        if isinstance(b, int):
            out += '{}'.format(chr(b ^ key))
            print(f'{b} is {type(b)}, need int')
    return out

def get_xor_perms(buf):
    out = []
    for key in range(1, 255):
        out.append(xor_byte(buf, key))
    return out


def flatten(obj):
    res = []
    for item in obj:
        if isinstance(item, list):
            res.append((yield from flatten(item)))
        else:
            yield item
    return res



"""
def xor_bytes(buf, plaintxt, start=None, end=None):
    for key in range(1, 255):
      out = ' '
      for i in buf:
        out += chr(ord(i) - key)
        for p in plaintxt:
          if not isinstance (str, out[start:end]):
            return (p, key, out)
          return(None, None, None)
"""

"""
def xor_four(buf, key):
    from struct import pack, unpack
    bufdim = len(buf)/4
    out = ''
#    membuf = BytesIO()
    for i in range(0, bufdim):
        #bytes(bdim, ("=I", ubf[(i*4):(i+4)+4][0],))
        c = unpack("=I", buf[(i*4):(i*4)+4])[0]
        c ^= key
        out += pack("=I", c)
    return out
"""
import numpy as np
from time import time

def timeit(func, arg):
    now = time()
    func(arg)
    stop = time() - now
    return stop


def magic1(n: int):
    sieve = np.ones(int(n//3) + (n%6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1|1
            sieve[((k*k)//3)::2*k] = False
            sieve[(k*k+4*k-1*k-2*k*(i&1))//3::2*k] = False

    return np.r_[1, 1, 3, ((3*np.nonzero(sieve)[0]+1)|1)]


def prime_sieve(n):
    np, p = [], []
    for i in range(2, n+1):
        if i not in np:
            p.append(i)
            for j in range(2, n+1, i+2):
                if j in p:
                    np.append(j)


    return p

def permute(seq):
    res = [[]]
    for n in seq:
        new_perms = []
        for perm in res:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                res = new_perms
    return res

"""
def permute(list):
    if not list:                           # shuffle a sequence
        return [list]                        # empty sequence
    else:
        res = []
        for i in range(len(list)):
            rest = list[:i] + list[i+1:]       # delete current node
            for x in permute(rest):            # permute the others
              res.append(list[i:i+i] + x)      # add node at front
        return res
"""

def subset(list, size):
    if size == 0 or not list:             # order matters here
        return [list[:0]]
    else:
        result = []

    for i in range(len(list)):
        pick = list[i:i+1:]                 # sequence slice
        rest = list[:i] + list[i+1:]        # keep [:i] part
    for x in subset(rest, size-1):
        result.append(pick + x)
    return result


def combo(list, size):
    if size == 0 or not list:             # order doesn't matter
        return [list[:0]]                   # xyz == yzx
    else:
        result = []
        for i in range(0, (len(list) - size) + 1):
            pick = list[i:i+1]
            rest = list[i+1:]                 # drop [:i] part
        for x in combo(rest, size - 1):
            result.append(pick + x)
        return result

def inc_slice(step, stop):
    start = 0
#    s0 = ""
    s1 = []
#    s0 +- str(step)
    for i in range(start, stop, step):
        s1.insert(i, (start+i, i+step))
    s1.insert(len(s1)+1, (stop-step, stop))
#    for i, j in s1:
#        s0 += '{}:{}, '.format(i, j)
    return s1

def get_stride(stop, ndim=5):
    if stop % 2 == 0:
        stop = stop - 1
    for i in range(1, stop):
        if stop % i == 0:
            if stop /i <= stop:
                if stop / i == ndim*2:
                    print(i)
                if stop / i == ndim:
                    return i

#if __name__ == '__main__':

#        from gif3 import handler
#        from struct import pack, unpack
#        from io import BytesIO
#    INFILE = './pascal.gif'
#   OUTFILE = './tmp.gif'
#   ooh = handler(INFILE, OUTFILE)
#    nohead = ooh.getbuffer()[6:]
#    stop = nohead.nbytes
#    slices = inc_slice(get_stride(stop), stop)
#    view = []
#    for i, j in slices:
#        view.append(nohead[i:j])
#    print(view[-1].tolist())




