from sys import stdin, stdout


def stan_wins(n):
    stan_turn = True
    p = 1
    while (p < n):
        if stan_turn:
            p *= 9
        else:
            p *= 2
        stan_turn = not stan_turn
    return not stan_turn


def main():
    numbers = [int(x) for x in stdin.readlines()]
    for number in numbers:
        if stan_wins(number) == True:
            stdout.write("Stan wins.\n")
        else:
            stdout.write("Ollie wins.\n")


if __name__ == '__main__':
    main()
