all_the_numbers_we_getting = input().split(", ")
positive_numbers = [x for x in all_the_numbers_we_getting if int(x) >= 0]
negative_numbers = [x for x in all_the_numbers_we_getting if "-" in x]
even_numbers = [x for x in all_the_numbers_we_getting if int(x) % 2 == 0]
odd_numbers = [x for x in all_the_numbers_we_getting if int(x) % 2 == 1]
print("Positive:", ', '.join(n for n in positive_numbers))
print("Negative:", ', '.join(n for n in negative_numbers))
print("Even:", ', '.join(n for n in even_numbers))
print("Odd:", ', '.join(n for n in odd_numbers))
