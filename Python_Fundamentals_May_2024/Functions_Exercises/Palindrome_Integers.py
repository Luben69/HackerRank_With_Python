def the_function(n):
    for char in n:
        if char[::-1] == char:
            print('True')
        else:
            print('False')


positive_integers = input().split(", ")

the_function(positive_integers)
