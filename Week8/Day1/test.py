try:
    file_name = input("Enter file name = ")
    word = input("Enter the word = ").lower()  # is
    f = open(file_name, "r")
    lines = f.readlines()
    exists = False
    for i in range(0, len(lines)):
        if word in lines[i]:
            exists = True
            print(i + 1)
    if exists == False:
        print("Word does not exists")
    f.close()
except FileNotFoundError:
    print("File cannot be found")
except:
    print("Some error occurred")
