def fool():
    try:
        a = int(input("Enter number 1 = "))
        b = int(input("Enter number 2 = "))
        c = int(input("Enter number 3 = "))
        print(a + b + c)
    except ValueError:
        print("Value is not interger, print a integer value")
    except:
        print("Some other error occured")
    finally:
        print("thanks for calculating the sum")


# def fool():
#     try:
#         print(1)
#     finally:
#         print(2)

fool()
