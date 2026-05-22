class TimeMap:

    def __init__(self):
        self.result = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.result:
            self.result[key] = []
        self.result[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        Value = self.result.get(key, [])
        res = ''

        l, r = 0, len(Value)-1
        while l <= r:
            m = (l + r) // 2
            if Value[m][1] <= timestamp:
                res = Value[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

