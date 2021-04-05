### Intro
This is small project using python to help you check automatially Vietnamese lottery results everyday
I use macbook, so all of code here for Mac, not sure for other operating systems
### Library
Firstly, we need to install virtual environment:
```python
python3 -m venv venv1
```
Run it
```python
source venv1/bin/activate
```
Install libraries:
```python
python3 -m pip install requests bs4
```
Request: clawling data from website
bs4: turn `string` into `HTML tree`

### Code
We import all libraries we just install
```python
import requests
from bs4 import BeautifulSoup
import sys
```
We need to crawl all of result from first 7 winning lottery numbers and put on a list:
```python
def solve():
    r = requests.get('http://ketqua.net')
    tree = BeautifulSoup(markup=r.text)
    node = tree.find('table', attrs={'id': 'loto_mb'})
    li = [i.text for i in node.find_all('td')][1:28]
    node2 = tree.find('table', attrs={'id': 'result_tab_mb'})
    li2 = [a.text for a in node2.find_all(
        'div', attrs={'data-pattern': '[0-9]{5}'})]
    li3 = [b.text for b in node2.find_all(
        'div', attrs={'data-pattern': '[0-9]{4}'})]
    li4 = [c.text for c in node2.find_all(
        'div', attrs={'data-pattern': '[0-9]{3}'})]
    li5 = [d.text for d in node2.find_all(
        'div', attrs={'data-pattern': '[0-9]{2}'})]
    li6 = li2 + li3 + li4 + li5
```

We need to check if our number match to winning number or not:
```python
     result = None
    if sys.argv[1] in li:
        result = int(sys.argv[1])
    else:
        result = '\n'.join(li6)
    return result
```

Now run it in terminal:
`python ketqua.py [number1] [number2]`

