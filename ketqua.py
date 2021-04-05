import requests
import sys
from bs4 import BeautifulSoup


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
    result = None
    if sys.argv[1] in li:
        result = int(sys.argv[1])
    else:
        result = '\n'.join(li6)
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
