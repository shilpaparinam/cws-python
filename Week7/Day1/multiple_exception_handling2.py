try:
    a = [54, 23, 34, 67, 89, 0]
    print(a[3])
    print(a[0] / a[1])
except ZeroDivisionError:
    print("Division cant be zero")
except IndexError:
    print("Out of Index")
except:
    print("Some other error occured")
finally:
    print("This is final statement")
