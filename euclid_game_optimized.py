from sys import stdin, stdout


def stan_wins(n, m):
    stan_turn = True
    while(n != 0 and m != 0):
        if (m > n):
            n, m = m, n
        if (n//m > 1 or n % m == 0):
            break
        else:
            n %= m
            stan_turn = not stan_turn
    return stan_turn


def main():
    numbers = [int(x) for x in stdin.readline().strip().split()]
    while numbers[0] != 0 and numbers[1] != 0:
        if stan_wins(numbers[0], numbers[1]) == True:
            stdout.write("Stan wins\n")
        else:
            stdout.write("Ollie wins\n")
        numbers = [int(x) for x in stdin.readline().strip().split()]


if __name__ == '__main__':
    main()
