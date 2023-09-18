class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        record = []
        for ch in s:
            record.append([ch] if ch.isdigit() else [ch.lower(), ch.upper()])
        print(record)
        return [''.join(v) for v in product(*record)]
        