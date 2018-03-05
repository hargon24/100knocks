import re
from knock20 import getUKdata

re_level = re.compile('(?P<indent>=+)\s*(?P<name>[^=]+)=+')
for line in getUKdata().split('\n'):
    result = re_level.search(line)
    if result:
        level = int(len(result.group('indent')) - 1)
        word = result.group('name')
        print('{0}: level{1}'.format(word, level))
