import os
import sys

os.system("mkdir ta-lib")
os.system("cd ta-lib && python -m venv env")
os.system("pip install requests")

import requests

python_version = sys.version.split(' ')[0]
detail_version = int(python_version.split('.')[1])

response = None
url = None

for _ in range(3):
    if detail_version == 8:
        url = "https://download.lfd.uci.edu/pythonlibs/archived/TA_Lib-0.4.24-pp38-pypy38_pp73-win_amd64.whl"
    elif detail_version == 9:
        url = "https://download.lfd.uci.edu/pythonlibs/archived/TA_Lib-0.4.24-cp39-cp39-win_amd64.whl"
    elif detail_version == 10:
        url = "https://download.lfd.uci.edu/pythonlibs/archived/TA_Lib-0.4.24-cp310-cp310-win_amd64.whl"

    response = requests.get(url)
    print(response.status_code)

    if response.status_code == 200:
        break

if response.status_code == 200:
    filename = url.split('/')[-1]
    with open(f"./ta-lib/{filename}", "wb") as f:
        f.write(response.content)

    os.system(f"ta-lib\\env\\Scripts\\activate && pip install ./ta-lib/{filename}")
    os.remove(f"./ta-lib/{filename}")
