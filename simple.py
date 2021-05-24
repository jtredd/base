import requests
import json

URL = 'https://download.dnscrypt.info/dnscrypt-resolvers/json/public-resolvers.json'
UA_STRING = 'Curl 7/59.1'
CERT = 'cert.pem'

def print_url(r, *args, **kwargs):
    print(r.url)

def record_hook(r, *args, **kwargs):
    r.hook_called = True
    return r

def get(url: str, ua_string=None):
    """
    function to get http response in text.
    :return response object
    """
    cert = CERT
    ua_string = UA_STRING
    headers = requests.utils.default_headers()
    headers['User-Agent'] = ua_string
    data=b'send exactly these bytes.'
    hooks={'response': [print_url, record_hook]}
    s = requests.Session()
    req = requests.Request('GET', url, data=data,json=hooks, headers=headers)
#    req.register_hook('request', hooks)
    prepped = s.prepare_request(req)
    resp = s.send(prepped,
                  stream=True,
                  verify=True,
                  proxies=None,
                  cert=cert,
                  timeout=(3, 20)
                 )
    return resp.content


def save_file(text: bytes):
    """ save bytes to file """
    with open(outfile, 'wb') as out:
        out.write(text)




if __name__ == '__main__':
    url = 'https://download.dnscrypt.info/dnscrypt-resolvers/json/public-resolvers.json'
    ua_string = 'Curl 7/59.1'
    cert = 'cert.pem'
    outfile = url.split('/')[-1]
    data = get(url)
    save_file(data)
