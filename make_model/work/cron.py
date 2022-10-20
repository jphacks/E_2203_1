#これ実行したらpickleをサーバーに渡せるようにしたい
#cronで定期実行できる？

import json
import urllib.parse
import urllib.request

f = open("pickle_A", "rb")
reqbody = f.read()
f.close

url = "http://localhost:5000/pickle"

req = urllib.request.Request(
    url,
    reqbody,
    method="POST",
    headers={"Content-Type": "application/octet-stream"},
)

with urllib.request.urlopen(req) as res:
    print(json.loads(res.read()))
