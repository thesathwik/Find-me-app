from os import path
print('''How can I help you?
1.'ADD' new element
2.'FIND' the element
3.'EDIT' the element''')
def add(handle):
    f=0
    element=input("What do you want to add?")
    for line in handle:
        line=line.rstrip()
        details=line.split()
        if len(details)==0:
            continue
        elif details[0]==element:
            print("There is already "+" in the list")
            f+=1
            break
    if f==0:
        place=input("where did you place it?")
        handle.write('\n'+element+" "+place)
        handle.close()
        print("ADDED")
def find(handle):
    f=0
    element=input("What do you want to find?")
    for line in handle:
        line=line.rstrip()
        details=line.split()
        if len(details)==0:
            continue
        elif details[0]==element:
            f+=1
            print(details[1:])
            break
    if f==0:
        print("there is no "+element+" in the list")
def edit(handle):
    f=0
    element=input("Which element do you want to edit?")
    new=input("where did you place now?")
    for line in handle:
        line=line.rstrip()
        details=line.split()
        if len(details)==0:
            continue
        elif element==details[0]:
            del details[1:]
            details.append(new)
            f+=1
            print("EDITED")
            break
    if f==0:
        print("There is no "+element+" in the list")
def work(username):
    file=username+'.txt'
    if path.exists(file):
        handle=open(file,'r+')
        response=input("Choose the survice:")
        if response.upper()=='ADD':
            add(handle)
        if response.upper()=='FIND':
            find(handle)
        if response.upper()=='EDIT':
            edit(handle)
    else:
        print("please create your list")
        handle=open(file,'w+')
        add(handle)
        


            

        
        
    


