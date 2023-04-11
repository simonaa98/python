def binary_converter():
    to_list = [int(x) for x in input("Enter your binary number: ")] # takes input, catch the converted numbers
    binary_list = []
    carry = 0 # var to keep track of input numbers and for later input checks

    def convert(list):
        summen = 0
        for i in range(len(to_list)):  # reverse the order of the list, takes inputs out of original list
            binary_list.append(to_list.pop())
        for j in range(0, len(binary_list)): # does the math to translate binary to decimal numbers
            summen = summen + (binary_list[j]*2**j)
        return print("Your binary number in decimal form:", summen)

    for x in range(0,len(to_list)): # checks if input is binary
        if to_list[x] == 1 or to_list[x]== 0:
            carry = carry + 1

    if carry == len(to_list): # test if input is binary
        convert(to_list)
    else:
        print("That is not a binary number")

    repeat = input("Are there more numbers you want to convert? (y/n)").lower()
    if repeat == "y":
        binary_converter()
    else:
        exit() # loop makes sure you can repeat or exit the program

binary_converter() # original call of the function