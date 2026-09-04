class TimeMap:

    def __init__(self):
        self.keyValue = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyValue[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        pairs = self.keyValue.get(key, [])
        
        l = 0
        r = len(pairs) - 1
        
        while l <= r:
            m = (l + r) // 2
            if pairs[m][1] <= timestamp:
                res = pairs[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
