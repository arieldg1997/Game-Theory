from sys import stdin, stdout


def solve(n):
    modules = [0, 0, 0]
    str_n = str(n)
    for char in str_n:
        modules[int(char) % 3] += 1
    if modules[n % 3] != 0:
        modules[n % 3] -= 1
        return modules[0] % 2 == 0
    else:
        return False


def main():
    t = int(stdin.readline().strip())
    for t in range(t):
        n = int(stdin.readline().strip())
        if solve(n):
            stdout.write("Case "+str(t+1)+": S\n")
        else:
            stdout.write("Case "+str(t+1)+": T\n")


if __name__ == '__main__':
    main()
