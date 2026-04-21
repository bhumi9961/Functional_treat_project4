print("Welcome to the Data Analyzer and Transformer Program!!!")

data_list = []
while True:
    print("Main menu \n" \
    "1. Input Data \n"
    "2. Display Data Summary \n" \
    "3. Calculate Factorial \n" \
    "4. Filter Data by Threshold \n" \
    "5. Sort Data \n" \
    "6. Display Dataset Statistics \n" \
    "7. Exit program")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        data = int(input("enter the number of data: "))
        for i in range(data):
            value = int(input("Enter the value for data: "))
            data_list.append(value)
        print("Data entered successfully stored!!!")
        print(data_list)

    elif choice == 2:
        print("Data Summary: ")
        print(f"total elements: {range(data_list)}")
#        print(f"Minimum Value: {}")

    else:
        pass