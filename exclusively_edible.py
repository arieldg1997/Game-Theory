from sys import stdin, stdout


def solve(n, m, r, c):
    left = c
    below = n-r-1
    right = m-c-1
    above = r
    nim_number = left ^ below ^ right ^ above
    return nim_number == 0


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n, m, r, c = [int(x) for x in stdin.readline().strip().split()]
        if solve(n, m, r, c):
            stdout.write("Hansel\n")
        else:
            stdout.write("Gretel\n")


if __name__ == '__main__':
    main()
