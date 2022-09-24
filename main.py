def display():
        bal=20000
        password=1234
        i=1
        while i<=9999:
            print("------------WELCOME TO SBI BANK-----------")
            print("1.Check balance\n2.Withraw cash\n3.Change pin\n4.Deposit Money\n5.Exit")
            p=int(input("Enter your password:"))
            if p==password:
                n=int(input("ENTER YOUR CHOICE:"))
                if n==1:
                    print("YOUR BALANCE IS:",bal,"Rupees")
                elif n==2:
                    withraw=int(input("Enter the amount to withraw:"))
                    if withraw>bal:
                        print("INSUFFICIENT BALANCE")
                    else:
                        print("TRANSACTION SUCCESSFUL\nTHANK YOU")
                        bal=bal-withraw
                elif n==3:
                    oldpin=int(input("Enter old password:"))
                    if oldpin==password:
                        newpin=int(input("Enter new password:"))
                        password=newpin
                        print("PASSWORD CHANGED SUCCESSFULLY")
                    else:
                        print("INCORRECT PASSWORD,TRY AGAIN")
                elif n==4:
                    deposit=int(input("Enter the amount to Deposit:"))
                    print("DEPOSITED SUCCESSFULLY")
                    bal=bal+deposit
                elif n==5:
                    print("EXIT")
                    break;
                elif n>5:
                    print("INVALID CHOICE")
            else:
                print("INCORRECT PASSWORD,TRY AGAIN")
        i+=1
display()
    

    














