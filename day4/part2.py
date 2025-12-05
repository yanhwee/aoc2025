from sys import stdin

def parse(s: str) -> list[list[str]]:
    return list(map(list, s.splitlines()))

def solve(grid: list[list[str]]):
    DIRS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]
    n = len(grid)
    m = len(grid[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.': continue
            stack = [(i, j)]
            while stack:
                p, q = stack.pop()
                if grid[p][q] == '.': continue
                c = 0
                for (a, b) in DIRS:
                    if not (0 <= p + a < n): continue
                    if not (0 <= q + b < m): continue
                    if grid[p + a][q + b] == '.': continue
                    c += 1
                if c >= 4: continue
                grid[p][q] = '.'
                count += 1
                for (a, b) in DIRS:
                    if not (0 <= p + a < n): continue
                    if not (0 <= q + b < m): continue
                    if grid[p + a][q + b] == '.': continue
                    stack.append((p + a, q + b))
    return count

if __name__ == '__main__':
    print(solve(parse(stdin.read())))