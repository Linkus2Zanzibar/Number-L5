largest=int(input(" Enter a larger number "))
smallest=int(input(" Enter a smaller number "))
while smallest:
    number=smallest
    smallest=largest%smallest
    largest=number
print(largest)