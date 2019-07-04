file1=open("phone_contacts.txt","a")
file=open("phone_contacts.txt","r")

def pgmf():
    prompt_user=input("do you want to add or view contact?  :\n")
    if prompt_user=="view":
        file=open("phone_contacts.txt","r")
        for contact in file:
            print(contact)
        con()
            
    elif prompt_user=="add":
        file1=open("phone_contacts.txt","a")
        contact_name=input("enter name")
        file1.write(contact_name+"  ")
        new_phone=input("enter phone number")
        file1.write(new_phone)
        file1.write("\n")
        file1.close()
        con()

    else:
        print("invalid option")
        con()
       
def con():        
    inputu=input("do you want to continue? y/n  ")
    if inputu=="n":
        file.close()
    elif inputu=="y":
        pgmf()
        
pgmf()

            
