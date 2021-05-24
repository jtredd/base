import json

FILENAME = 'config.toml'
FILEHANDLE = open(FILENAME, 'w+')

def open_file(name: str, filtered=True) -> list:
    """ opens bytes as file and returns list object. """
    filtered=list()
    flist = list()
    with open(name, 'r') as file:
        data = json.loads(file.read())
    return data


def filter_data(self: dict) -> str:
    """ filter json for dnscrypt, dnssec, 
    nolog, nofilter only """

    data = fix_missing(self)
    data_flt = []
    stop = len(data) - 1
    for i in range(stop):
        if data[i]['proto'] == 'DNSCrypt':
                if data[i]['nolog'] and data[i]['nofilter'] and data[i]['dnssec'] is True:
                    if data[i]['location']:
                        data_flt.append(data[i])

    return data_flt


def format_servers(self: list, filename=FILEHANDLE) -> str:
    server_list, static_list = list(), list()
    server_list += [f'{x["name"]}' for x in self]
    for e in self:
        static_list.append(f'[static.{e["name"]}]{_LF}country={e["country"]}{_LF}stamp={e["stamp"]}{_LF}')
    print(f"server_list = {server_list}", file=FILEHANDLE)
    print(f"[static]", file=FILEHANDLE)
    print(format(', '.join([x for x in static_list]).replace(",", "")), file=FILEHANDLE, end='')


def fix_missing(self: list):
    if isinstance(self, list):
        if isinstance(self[0], dict):
            for key in self[0].keys():
                for n in range(len(self) - 1):
                    try:
                        self[n][key]
                    except KeyError:
                        self[n].update({str(key): 'None'})
    return self



def format_list(self):
    L=set()
    for n in range(len(self)-1):
        for i in range(_count(self, self[n])):
            print(i, self[n])
            L.add((self[n][0] + i, self[n][1]))
    return L


def _count(self: list, s: str) -> int():
    count = 0
    for n in range(len(self) - 1):
        if s in self[n]:
            count = count + 1
    return count

if __name__ == '__main__':
    from sys import platform
    if platform != 'windows':
        _LF = '\n'
    _LF = '\r\n'

    data = open_file('public-resolvers.json')
    format_servers(filter_data(data))
