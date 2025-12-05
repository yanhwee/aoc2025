from sys import stdin

def parse(s: str) -> tuple[list[tuple[int, int]], list[int]]:
    a, b = s.strip().split('\n\n')
    a = [tuple(map(int, l.split('-'))) for l in a.split('\n')]
    b = list(map(int, b.split('\n')))
    return a, b

def solve(ranges: list[tuple[int, int]], queries: list[int]):
    ranges.sort()
    queries.sort()
    count = 0
    i = 0
    for (a, b) in ranges:
        while queries[i] < a:
            if i >= len(queries):
                return count
            i += 1
        while queries[i] <= b:
            if i >= len(queries):
                return count
            count += 1
            i += 1
    return count

if __name__ == '__main__':
    ranges, queries = parse(stdin.read())
    ret = solve(ranges, queries)
    print(ret)