class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        size = []
        for string in strs:
            size.append(len(string))
        result = []
        for sz in size:
            result.append(str(sz))
            result.append(',')
        result.append('#')
        result.extend(strs)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res = [], []
        pos = 0
        while s[pos] != '#':
            j = pos
            while s[j] != ",":
                j += 1
            sizes.append(int(s[pos:j]))
            pos = j + 1
        pos += 1
        for size in sizes:
            res.append(s[pos:pos + size])
            pos += size
        return res


