from sys import stdin
from typing import List

def parse(s: str) -> List[str]:
    return s.splitlines()

def solve(banks: List[str]) -> int:
    total = 0
    for bank in banks:
        bank = map(int, bank)
        a, b, *bank = bank
        for c in bank:
            if a < b:
                a, b = b, c
            elif b < c:
                b = c
        total += a * 10 + b
    return total

if __name__ == '__main__':
    print(solve(parse(stdin.read())))