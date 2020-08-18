handle=open('data.txt','r+')
#basic home page
def login(handle):
    response=input("Do you have an account?")
    if response.lower()=="yes":
        yes(handle)
    elif response.lower()=='no':
        no(handle)
# if you have account
def yes(handle):
    f=0
    email=input("enter your email address:")
    for line in handle:
        line=line.rstrip()
        data=line.split()
        if len(data)==0:
            continue
        elif email==data[0]:
            password1(data)
            f+=1
    if f==0:
        print("email doen't exist")
        response2=input("Do you want to create an account?")
        if response2.lower()=='yes':
            handle=open('data.txt','r+')
            no(handle)
        else:
            handle=open('data.txt','r+')
            yes(handle)
    handle.close()
# if you don,t have a account
def no(handle):
    f=0
    email=input("enter a email:")
    for line in handle:
        line=line.rstrip()
        data=line.split()
        if len(data)==0:
            continue
        elif email==data[0]:
            f=f+1
    if f==0:
        username=input("your name:")
        password=input("enter your password")
        details="\n"+email+" "+password+" "+username
        handle.write(details)
        print("welcome!"+username)
        from functions import work
        work(username)
    elif f>0:
        print("you are already registered")
        response3=input("You want to login into your account?")
        if response3.lower()=='yes':
            handle=open('data.txt','r+')
            yes(handle)
        else:
            handle=open('data.txt','r+')
            no(handle)
        close(handle)
    handle.close()
# checking password
def password1(data):
    password=input("enter your password")
    if password==data[1]:
        print("hey!"+data[2])
        from functions import work
        work(data[2])
    else:
        print("password incorrect")
        password1(data)
login(handle)
        
            
    

            
            
            
            
                        
    
    
    

        
        
    
