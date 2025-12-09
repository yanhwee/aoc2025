from itertools import combinations, starmap
from sys import stdin

def parse(s: str) -> list[tuple[int, int]]:
    return [
        tuple(map(int, l.split(',')))
        for l in s.strip().splitlines()]

def area(a: tuple[int, int], b: tuple[int, int]) -> int:
    x1, y1 = a
    x2, y2 = b
    w = abs(x2 - x1) + 1
    h = abs(y2 - y1) + 1
    return w * h

def solve(coords: list[tuple[int, int]]) -> int:
    return max(starmap(area, combinations(coords, 2)))

if __name__ == '__main__':
    print(solve(parse(stdin.read())))