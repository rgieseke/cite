import sys
from habanero import cn

for idx in sys.argvs[1:]:
    print(idx)

    # results = cn.content_negotiation(publication, format="text")
    # if type(results) is str:
    # results = [results]
    # for result in results:
    # out = []
    # for line in result.splitlines():
    # if "url = {https://doi.org/" in line:
    # continue
    # else:
    # out.append(line)
    # print("\n".join(out))
    # items.append("\n".join(out))

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
