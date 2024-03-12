import os
import random
import string
import json , csv 


def password_generator(length,ch):


    charecters=''

    while(len(charecters)<length): 
        if ch==1:
            charecters+=random.choice(string.digits)
        #     charecters+=
        if ch==2:
            charecters+=random.choice(string.ascii_letters)

        if ch==3:
            charecters+=random.choice(string.ascii_letters+string.digits)
        if ch==4:
            charecters+=random.choice(string.ascii_letters+string.punctuation)
        if ch==5:
            charecters+=random.choice(string.digits+string.punctuation)
        if ch==6:
            charecters+=random.choice(string.ascii_letters+string.punctuation+string.digits)

    return charecters

def exp(filetype,name,password,opt=1):
    

        if opt==2:
            f=open(name,"a")
        else:
            f=open(name,"w")

        if filetype==1 or filetype==3:       
            print("password,",password, file=f)
            f.close()
        if filetype==2:
            data={"password":password}
            json.dump(data,f)
            f.close()
        print(f"output has been exported to {name}")




if __name__=="__main__":
    length=int(input("enter the number of charecters needed in your password. Choose a number between 8 and 30 \n"))

    if length <8 or length >30:
        print("password length specified is out of range")
    else:
        print('''select charecter set for password from below :
                        1 . only digits
                        2 . only charecters
                        3 . digits and charecters
                        4 . charecters and punctuations
                        5 . digits and punctuations
                        6 . charecters digits and punctuations \n ''')

        ch= int(input("select any number from above list \n"))
        if ch not in (1,2,3,4,5,6):
            print("choice selected is incorrect")
        else:
            password= password_generator(length , ch)
            # print("your passord is :" ,password)

    
            print('''select from the below in which file you want the output
                    1.csv file
                    2.json file
                    3.text file''')
            filetype=int(input("select any from above options \n"))

            if filetype not in (1,2,3):
                print("invalid file option selected")
            else:
                name=input("enter the file name you want \n")
                dir_path=os.path.join(os.getcwd(), name)
                if os.path.isfile(dir_path):
                    print('''filename already exist. please select which option you need from below
                          1. override the contents of file
                          2. append the output to existing file
                          3. provide new filename''')
                    opt=int(input("select one option from above  \n"))
                    if opt in (1,2):
                        exp(filetype,name,password,opt)
                    elif opt==3:
                        name=input("enter the new file name you want \n")
                        exp(filetype,name,password)
                else:
                    exp(filetype,name,password)
