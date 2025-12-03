from sys import stdin
from typing import List

def parse(s: str) -> List[str]:
    return s.splitlines()

def solve(banks: List[str]) -> int:
    total = 0
    for bank in banks:
        stack = []
        for i, c in enumerate(bank):
            while stack and stack[-1] < c:
                missing = 12 - len(stack)
                remaining = len(bank) - i
                if missing >= remaining:
                    break
                stack.pop()
            if len(stack) < 12:
                stack.append(c)
        n = int(''.join(stack))
        total += n
    return total

if __name__ == '__main__':
    print(solve(parse(stdin.read())))