
# import sys

class FindString:

    def __init__(self):
        pass

    def testMe(s, i, j):
        for k in range(int(i/2)):
            if s[k] != s[len(s)-k-1]:
                return False

        print('target is ', s[j-1:i])
        exit(0)



    def walkMe(s):
        for i in range(len(s), 1, -1):
            for j in range(1, len(s)):
                if i + j <= len(s) + 1:
                    if not FindString.testMe(s, i, j):
                        pass

s = 'atesset'
FindString.walkMe(s)