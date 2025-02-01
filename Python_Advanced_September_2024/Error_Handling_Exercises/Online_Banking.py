class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


user_input = input().split(", ")
user_pin = user_input[0]
balance = int(user_input[1])
age = int(user_input[2])
MINIMUM_AGE_TO_USE_BANKS_SERVICES = 18

while True:
    user_input = input().split("#")
    cmd = user_input[0]

    if cmd == 'End':
        break

    if cmd == 'Send Money':
        the_sending_money = int(user_input[1])
        our_pin = user_input[2]
        if balance < the_sending_money:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if user_pin != our_pin:
            raise PINCodeError("Invalid PIN code")

        if age < MINIMUM_AGE_TO_USE_BANKS_SERVICES:
            raise UnderageTransactionError("You must be 18 years "
                                           "or older to perform online transactions")

        balance -= the_sending_money

        print(f"\nSuccessfully sent {the_sending_money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif cmd == 'Receive':
        received_salary = int(user_input[1])
        if received_salary < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        for_investment = received_salary / 2
        left_salary = received_salary / 2
        balance += left_salary
        print(f"{left_salary:.2f} money went straight into the bank account")
