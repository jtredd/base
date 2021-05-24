""" define GIF standards interchange format """
from io import BytesIO

# constants from array2gif
BLOCK_TERMINATOR = b'\x00'
EXTENSION = b'\x21'
HEADER = b'GIF89a'
TRAILER = b'\x3b'
ZERO = b'\x00'


class LowerCaseDict(dict):
  def __getitem__(self, key):
    return dict.__getitem__(self, self.item(key.lower()))

class PlaceholderDict(dict):
  def __missing__(self, key):
    return '<{}>, missing.'.format(key)


# FIXME: Too few public methods
class ImageSequence:
    """ Boundaries for file object in memory """
    def __init__(self, im):
        self.im = im
    def __getitem__(self, ix):
        try:
            if ix:
                self.im.seek(ix)
                return self.im
        except EOFError:
            raise IndexError    # end of sequence


class SequenceIterator:
    """ Generator for Iterator class """
    def __init__(self, limit=None):
        self.start = 0
        self.step = 0
        self.end = limit

    def __iter__(self):
        return self

    def __next__(self):
        step = self.start
        self.start = self.step
        self.step = step + 1
        if self.limit is not None and \
            step < self.limit:
                return step
        raise StopIteration


# io.BytesIO().getbuffer() --> __sizeOf__
# io.BytesIO().getvalue()) --> __data___

#from io import BytesIO
# FIXME: need to pass buffer length and data
def handler(infile, outfile):
    """ generic method for file:obj interchange """
    with open(infile, 'rb+') as rio:
        buf = BytesIO(rio.read())
    out = open(outfile, 'wb+')
    if out.writable:
        out.write(buf.getvalue())
        view = buf.getbuffer()
    out.close()
#    im_size = buf.getbuffer().nbytes
#    im_data = buf.getvalue()
    return buf

if __name__ == '__handler__':
    # FIX: getbuffer().__slice__
    # FIXME: __func__
    # msg boundaries relation to chunk
    # frames
    # header size
    # header value
    # shared dimmension
    # palette information (0, range(254), 0)
    try:
        pass
    except SyntaxError:
        pass
