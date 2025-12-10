from functools import reduce
from itertools import starmap
from sys import stdin
from operator import or_

def parse(s: str) -> list[tuple[list[bool], list[list[int]]]]:
    def parse_line(s: str) -> tuple[list[bool], list[list[int]]]:
        a, *b, _ = s.split(' ')
        a = [c == '#' for c in a[1:-1]]
        b = [list(map(int, c[1:-1].split(','))) for c in b]
        return a, b
    return list(map(parse_line, s.strip().splitlines()))

def solve(pattern: list[bool], buttons: list[list[int]]) -> int:
    n = len(pattern)
    pattern = reduce(
        lambda a, b: a << 1 | int(b), pattern, 0)
    buttons = [
        reduce(or_, (1 << (n - a - 1) for a in button))
        for button in buttons]
    if pattern == 0:
        return 0
    front = [(0, 0)]
    for i in range(1, n + 1):
        front_ = []
        for pat, j in front:
            for k in range(j, len(buttons)):
                pat_ = pat ^ buttons[k]
                if pat_ == pattern:
                    return i
                front_.append((pat_, k + 1))
        front = front_
        front_ = []
    raise Exception

def solve_(lines):
    # return list(starmap(solve, lines))
    return sum(starmap(solve, lines))

if __name__ == '__main__':
    print(solve_(parse(stdin.read())))