class TimeMap:

    def __init__(self):
        self.h = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        value = self.h.get(key, [])
        res = ''

        l, r = 0, len(value)-1
        while l <= r:
            m = (l + r) // 2
            if value[m][1] <= timestamp:
                res = value[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
