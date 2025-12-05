from sys import stdin

def parse(s: str) -> tuple[list[tuple[int, int]], list[int]]:
    a, _ = s.strip().split('\n\n')
    a = [tuple(map(int, l.split('-'))) for l in a.split('\n')]
    return a

def solve(ranges: list[tuple[int, int]]):
    ranges.sort()
    count = 0
    a, b = ranges[0]
    for c, d in ranges[1:]:
        if b < c:
            count += b - a + 1
            a = c
        b = max(b, d)
    count += b - a + 1
    return count

if __name__ == '__main__':
    ranges = parse(stdin.read())
    ret = solve(ranges)
    print(ret)