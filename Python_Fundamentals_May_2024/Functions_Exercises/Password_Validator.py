def password(y):
    valid_password = True

    if not 6 <= len(y) <= 10:
        print('Password must be between 6 and 10 characters')
        valid_password = False
    if not y.isalnum():
        print('Password must consist only of letters and digits')
        valid_password = False

    digit_count = sum(char.isdigit() for char in y)

    if digit_count < 2:
        print('Password must have at least 2 digits')
        valid_password = False

    if valid_password:
        print('Password is valid')


the_password = input()
password(the_password)
