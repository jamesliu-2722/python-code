import re
def remove_last_zero(list):
    if list and list[-1] == '0':
        list.pop()

def remove_leading_zero(item) -> str:
    while True:
        if item[0] == '0' and len(item[0]) > 1:
            item = item[1:]
        else:
            break
    return item

def nonezero(item) -> bool:
    pattern = r'^0+$'
    for it in item:
        if not re.match(pattern, it):
            return True
    return False

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
            v1 = version1.split(".")
            v2 = version2.split(".")

            while True:
                temp = list(v1)
                remove_last_zero(v1)
                if temp == v1:
                    break
            while True:
                temp = list(v2)
                remove_last_zero(v2)
                if temp == v2:
                    break
            for i in range(min(len(v1), len(v2))):
                temp1 = int(remove_leading_zero(v1[i]))
                temp2 = int(remove_leading_zero(v2[i]))
                if temp1 > temp2:
                    return 1
                elif temp1 < temp2:
                    return -1

            if len(v1) > len(v2) and nonezero(v1[len(v2):]):
                return 1
            elif len(v1) < len(v2) and nonezero(v2[len(v1):]):
                return -1
            else:
                return 0

# version1 = "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000"
# version2 = "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000"
version1 ="1.01"
version2 ="1"
print(Solution().compareVersion(version1, version2))