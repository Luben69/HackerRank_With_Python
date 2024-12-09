def grade(n):
    if 2.00 <= n <= 2.99:
        print('Fail')
    elif 3.00 <= n <= 3.49:
        print('Poor')
    elif 3.50 <= n <= 4.49:
        print('Good')
    elif 4.50 <= n <= 5.49:
        print('Very Good')
    elif 5.50 <= n <= 6.00:
        print('Excellent')


rate = float(input())

grade(rate)
