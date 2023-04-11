def dna_string():
    user_input = int(input("How many bases in your string? "))
    lst = []
    comp_lst = []

    print("Enter your bases:")

    for i in range(0, user_input): # works through the user input of n lenght
        lst_ele = input().upper()
        lst.append(lst_ele)

    for j in range(len(lst)): # loops through the list and make a complimentary list of the other DNA base
        if lst[j] == "A":
            comp_lst.append("T")
        elif lst[j] == "T":
            comp_lst.append("A")
        elif lst[j] == "C":
            comp_lst.append("G")
        elif lst[j] == "G":
            comp_lst.append("C")

    print("- - - - -Your DNA string is:", lst) # prints both strings of the DNA
    print("The complimentary string is:", comp_lst)

dna_string()