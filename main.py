def largest_of_three(a, b, c):

    if (a>=b) and (a>=c):
        return(a)
    elif (b>=a) and (b>=c):
        return(b)
    elif(c>=a) and (c>=b):
        return(c)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(largest_of_three(a, b, c))


if __name__ == '__main__':
    main()
