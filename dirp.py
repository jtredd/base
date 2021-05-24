""" handle bytes io """
from os.path import exists, pathsep, extsep, abspath, curdir, join
import re

def bio(fname, data):
    """ copy file without appending to the obj-like buffer"""
    buf = b''
    buf += data
#    if exists(fname):
#      ff = open(fname, 'rb+')
##      ff.write(b'abc')
#    print(ff.read(200))
    if exists(fname):
        print('exists')
        f = open(fname + 'out', 'wb', buffering=200)
    else:
        # file does not exist
        print('doesnt exist')
        f = open(fname, 'wb+', buffering=200)          # create handle
        f.write(data)
    with open(fname, 'rb+') as rio:
        print('rio', rio.seek(0), rio.read(200))
        rio.seek(0)
#        print(len(data), rio.seek(0), rio.read(20000)
        rio.flush()
        f.write(rio.read(200))
        rio.seek(0)
        return rio.read(200)
    f.close()

def repfile(infile, data):
    name, ext = infile.split(extsep)
    n = 0
    if exists(infile):
      name, ext = infile.split('.')
      newname = name + str(n) + extsep + ext
      n=n+1
      outfile = open(newname, 'wb')
      if isinstance(data, bytes):
          outfile.write(data)

## FIXME
## scrap this
def newname(filename, sep, limit=None):
    """alpha + _ + digit"""
    ret = []
    if limit is not None or not sep:
      name, ext = filename.split('.')
      if exists(abspath(join(curdir, filename))):
          print(f'{filename} appears to exist.')
          print(f'but sep: {sep} \n does not conform to pattern:')
          print('alpha + _ + digit')
          if sep in name:
            prefix, suffix = re.split(f'\{sep}', name)
            for n in range(int(suffix), limit):
              ret.append(n)
              if int(suffix) == n:
                ret.remove(n)
              else:
                continue
            for e in range(len(ret)):
                 ret[e] = (e, exists(str(prefix + sep + str((int(e))) + extsep + ext)))
          for item in ret:
            if True in item:
              continue
            elif False in item:
              return f'{prefix}{sep}{item[0]}.{ext}'
              break

                  #print(f'suffix: {suffix}\n is not an expected pattern, expecting: digit')
      return False
    return f"Usage: newname('alpha_1.gif', '_', 20)"


def newfile(filename,limit):
  filenames = ()
  for s in filename.split('.')[0]:
      if not s.isalnum():
        if s.isprintable():
          sep = s
  name, ext = filename.split('.')
  prefix, suffix = re.split(f'{sep}', name)
  for n in range(int(suffix), limit):
    if exists(f'{prefix}{sep}{n+1}.{ext}'):
      next
    elif not exists(f'{prefix}{sep}{n+1}.{ext}'):
      filenames +=(f'{prefix}{sep}{n+1}.{ext}',)
  return filenames
