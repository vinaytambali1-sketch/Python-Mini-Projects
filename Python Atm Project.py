Balance = 100000
atm_pin = 2226

pin = int(input("Enter Pin = "))

if pin != atm_pin:
    print("Incorrect Pin")

else:
    print("=== ATM menu ===")
    print("1. To check balance")
    print("2. Deposit amount")
    print("3. withdrawal amount")
    print("4. To change Pin")
    print("5. Exit")

    option = int(input("Enter Option = "))
    
    if option == 1:
        print("Your Balnce =",Balance)
    elif option == 2: 
        deposit_amount = int(input("Enter deposit amount = "))
        if deposit_amount > 0:
            Balance += deposit_amount
            print("Deposited has been successful")
            print("New balance = ",Balance)
        else:
            print("Invalid amount")
    elif option == 3:
        withdraw_amount = int(input("Enter withdrawal amount = "))
        if Balance < withdraw_amount:
            print("Insufficient amount")
        else:
            Balance -= withdraw_amount
            print("Withdrawal has been successful")
            print("Remaining Balance = ",Balance)
    elif option == 4:
        enter_pin = int(input("Enter pin = "))
        if enter_pin == atm_pin:
            new_pin = int(input("Enter new pin = "))
            atm_pin = new_pin
            print("Your Pin has been Successfully changed")
            print("Your new Pin = ",new_pin)
        else:
            print("Incorrect pin")
    elif option == 5:
        print("Thanks for visiting ")
        print("Visit again")
    else:
        print("Invalid Option")