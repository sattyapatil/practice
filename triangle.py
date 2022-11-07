"""print triangle using python"""


def triangle(n):
    for i in range(n//2):
        print('')
        for j in range(n):
            if n // 2 == j + i or n // 2 == j - i or i == (n // 2)-1:
                print('*', end='')
            else:
                print(' ', end='')


triangle(50)
