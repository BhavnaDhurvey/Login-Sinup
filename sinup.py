import json,os
user_input=input("enter a for sign-up and b for log-in:-")
if user_input=="a":
    username=input("Enter your name:-")
    def my():
        password1=input("Enter your password:-")
        password2=input("Confirm  password:-")
        up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lo="abcdefghijklmnopqrstuvwxyz"
        dig="0123456789"
        spc="!@#$%^&*()"
        u,l,d,s=0,0,0,0
        i=0
        while i<len(password1):  
            if password1[i] in up:
                u+=1 
            if password1[i]in lo: 
                l+=1			 
            if password1[i]in dig:
                d+=1
            if password1[i]in spc:		
                s+=1	
            i=i+1
        
        if (u>=1 and l>=1 and d>=1 and s>=1 and u+l+d+s==len(password1)):
                if password1==password2:
                    if len(password1)>=6 and len(password1)<=10:
                        if(os.path.isfile('login.json')):
                            file_name=open("login.json","r+")
                            a=json.load(file_name)
                            for i in a["User"]:
                                if i["Username"]==username:
                                    print("This user already exist")
                                    break
                            else:
                                dic={}
                                d={}
                                dic["Username"]=username
                                dic["Password"]=password1
                                d["Description"]=input("Enter Your Description:-")
                                d["D.O.B"]=input("Enter your D.O.B:-")
                                d["Gender"]=input("Enter your Gender:-")
                                d["Hobbies"]=input("Enter your Hobbies:-")
                                dic["Profile"]=d
                                v=a["User"]
                                v.append(dic)
                                f=open("login.json","w+")
                                json.dump(a,f,indent=4)  
                                f.close()
                                print("Signup Successful")
                                   
                        else:
                            
                            dic={}
                            l=[]
                            d={}
                            d1={}
                            dic["Username"]=username
                            dic["Password"]=password1
                            d["Description"]=input("Enter your Description:-")
                            d["D.O.B"]=input("Enter your D.O.B:-")
                            d["Gender"]=input("Enter your Gender:-")
                            d["Hobbies"]=input("Enter your Hobbies:-")
                            dic["Profile"]=d
                            l.append(dic)
                            d1["User"]=l
                            f=open("login.json","w+")
                            json.dump(d1,f ,indent=4)
                            f.close()
                            print("Signup Successful")

                    else:
                        print("password length must be between 6 and 10")
                else:
                    print("Password not match")
        else:
            print("must have atleast a digit,specail character,lowercase and an uppercase")
    my()
elif user_input=="b":
    a=open("login.json","r")
    f=json.load(a)
    d=input("Enter your user name:-")
    v=input("Enter your password:-")
    for i in f["User"]:
        if i["Username"]==d:
            if v == i["Password"]:
                print("login successful")
                print(i)
                break
            else:
                print("wrong password")
    else:
        print("wrong username")
else:
    print("Your enter wrong input")