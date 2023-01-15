import sys


if __name__ == "__main__":
    f1, f2 = sys.argv[1], sys.argv[2]
    with open(f1, "r") as file1:
        x, y = map(int, file1.readline().split())
        r = int(file1.readline())
    coord = []
    with open(f2, "r") as file2:
        for dots in file2:
            coord.append(list(map(int, dots.split())))
    for d in coord:
        if (d[0] - x) ** 2 + (d[1] - y) ** 2 == r ** 2:
            print(0)
        elif (d[0] - x) ** 2 + (d[1] - y) ** 2 < r ** 2:
            print(1)
        else:
            print(2)
