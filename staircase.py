def staircase(n):
    for i in range(n):
        stairs = i + 1
        spaces = n - stairs
        print(' ' * spaces + '#' * stairs)
staircase(6)