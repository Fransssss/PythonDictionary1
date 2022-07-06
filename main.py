# nation and its constitutional form

nation_constitutional_form = {"Afghanistan": "Provisional", "Algeria":"Republic","Belgium":"Constitutional monarchy"
    ,"Brazil":"Republic","Canada":"Constitutional monarchy","Chile":"Republic","Dominica":"Republic","Egypt":"Republic"
    ,"Germany":"Republic","Russia":"Republic","Zambia":"Republic"}

print("\n== Nation and its Constitutional Form ==")
print("1. List of Nation and its Constitutional Form")
print("2. List of Nation")
print("3. List of Constitutional Form")
print("4. Add a Nation and its Constitutional Form")
print("5. Remove a Nation")
print("6. Clear the Dictionary")
print("E. Exit")
choice = input("choice: ")

while choice != 'E' and choice != 'e':
    if choice == '1':
        print("\n[List of Nation and its Constitutional Form]")
        print(nation_constitutional_form)
    elif choice == '2':
        print("\n[List of Nation]")
        print(nation_constitutional_form.keys())
    elif choice == '3':
        print("\n[List of Constitutional Form]")
        print(nation_constitutional_form.values())
    elif choice == '4':
        nat = input("\nname of a  nation: ")
        cont_form = input("name of the constitutional form: ")
        if len(nat) == 0 or len(cont_form) == 0:
            print("incomplete input")
        else:
            nation_constitutional_form.update({nat:cont_form})
            print("item added")
    elif choice == '5':
        nat = input("\nname of the nation: ")
        if len(nat) == 0:
            print("incomplete input")
        else:
            nation_constitutional_form.pop(nat)
            print("item removed")
    elif choice == '6':
        ar_u_sure = input("\nare you sure Y/N? ")
        if ar_u_sure == 'Y' or ar_u_sure == 'y':
            nation_constitutional_form.clear()
            print("list cleared")
        elif ar_u_sure == 'N' or ar_u_sure == 'n':
            print("command cancelled")
        else:
            print("the input should be Y/N")
    else:
        print("\n[Invalid input]")

    print("\n== Nation and its Constitutional Form ==")
    print("1. List of Nation and its Constitutional Form")
    print("2. List of Nation")
    print("3. List of Constitutional Form")
    print("4. Add a Nation and its Constitutional Form")
    print("5. Remove a Nation")
    print("6. Clear the Dictionary")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\nExit Program")