#これ実行したらpickleをサーバーに渡せるようにしたい
#cronで定期実行できる？

import json
import urllib.parse
import urllib.request


def main():
    with open("model.pickle"):
        reqbody = f.read()

    url = "http://jp-main/pickle"

    req = urllib.request.Request(
        url,
        reqbody,
        method="POST",
        headers={"Content-Type": "application/octet-stream"},
    )

    with urllib.request.urlopen(req):
        pass
    

if __name__ == "__main__":
    main()
