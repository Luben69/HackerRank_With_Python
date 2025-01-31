def everything_to_do(*args):
    total_negative = 0
    total_positive = 0
    for i in args:
        if int(i) > 0:
            total_positive += int(i)
        else:
            total_negative += int(i)

    print(total_negative)
    print(total_positive)

    if abs(total_negative) > total_positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


our_input = input().split()
everything_to_do(*our_input)
