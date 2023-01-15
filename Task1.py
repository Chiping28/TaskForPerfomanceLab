import sys


if __name__ == "__main__":
    n, m = int(sys.argv[1]), int(sys.argv[2])
    l = [i for i in range(1, n + 1)]
    t = l[:m]
    r = []
    b = True
    e = 0
    while b:
        r.append(t[0])
        if t[-1] == 1:
            b = False
        else:
            for i in range(m):
                t[i] = t[i] + (m - 1) if t[i] + (m - 1) <= n else t[i] - (n - m + 1)
        e += 1
    for i in r:
        print(i, end="")
