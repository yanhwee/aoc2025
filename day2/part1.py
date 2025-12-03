from sys import stdin
from typing import List, Tuple

def is_invalid(num):
    s = str(num)
    if len(s) % 2 == 1:
        return False
    m = len(s) // 2
    return s[:m] == s[m:]

def solve(ranges: List[Tuple[int, int]]) -> int:
    total = 0
    for a, b in ranges:
        for i in range(a, b + 1):
            if is_invalid(i):
                total += i
    return total

def parse(s: str) -> List[Tuple[int, int]]:
    out = []
    for s1 in s.split(','):
        a, b = s1.split('-')
        a, b = int(a), int(b)
        out.append((a, b))
    return out

if __name__ == '__main__':
    print(solve(parse(stdin.read())))