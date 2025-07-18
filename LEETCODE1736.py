class Solution(object):
    def maximumTime(self, time):
        res = list(time)
        if res[0] == '?':
            if res[1] != '?' and int(res[1]) > 3:
                res[0] = '1'
            else:
                n[0] = '2'
        if res[1] == '?':
            if res[0] == '2':
                res[1] = '3'
            else:
                res[1] = '9'
        if res[3] == '?':
            res[3] = '5'

        if res[4] == '?':
            res[4] = '9'

        return ''.join(res)