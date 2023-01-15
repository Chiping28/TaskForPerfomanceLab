import sys


if __name__ == "__main__":
    file = sys.argv[1]
    with open(file, "r") as f:
        nums = [int(i) for i in f]
        m = sorted(nums)[len(nums) // 2]
        print(sum(abs(i - m) for i in nums))
