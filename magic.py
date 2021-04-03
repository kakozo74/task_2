print('Введите сторону матрицы')
def print_spiral_matrix(number):
    dx, dy = 1, 0
    x, y = 0, 0
    a = [[None] * number for _ in range(number)]
    for i in range(1, number ** 2 + 1):
        a[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < number and 0 <= ny < number and not a[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    for x in list(zip(*a)):
        print(*x)


n = input()

try:
    n = int(n)
except ValueError:
    print('Введено не число')

if n < 4 or n > 1000:
    print('Число должно быть в диапазоне от 4 до 1000')
else:
    print_spiral_matrix(n)