from tkinter import *
from cryptography.fernet import Fernet

root=Tk()

mw=StringVar()



def execute():

    mastr_pwd=mw.get()

    with open("master_password.txt","r") as file:
        data=file.readline()
        #change=fer.decrypt(data.encode()).decode()
        change=data

    flag=True
    if mastr_pwd==change:


        def view():
            with open('passwords.txt', 'r') as f:
                for line in f.readlines():
                    data = line.rstrip()
                    user, passw = data.split("|")
                    a="User: "+user+ " Password: "+fer.decrypt(passw.encode()).decode()
                    Message(root, text=a).grid()
                
        Button(root, text="view",font="lucida 12 bold",padx=22,pady=5, command=view).grid()

        def add():

            name = StringVar()
            pwd = StringVar()
            Label(root, text="name" ).grid(row=4,column=5)
            Label(root, text="password").grid(row=5,column=5)
            Entry(root, textvariable=name).grid(row=4, column=6)
            Entry(root, textvariable=pwd).grid(row=5, column=6)

            def submit():
                Label(root, text="your password successfully saved").grid(row=8,column=6)
                with open('passwords.txt', 'a') as f:
                    f.write(name.get() + "|" + fer.encrypt(pwd.get().encode()).decode() + "\n")



       
     
            Button(root, text="submit", font="lucida 12 bold",padx=22,pady=5,command=submit).grid(row=7,column=6)
           

        def clear_all():
            Label(root, text="all users cleared").grid()
            with open("passwords.txt","w") as file:
                file.write("")

        
        Button(root, text="clear all users",font="lucida 12 bold",padx=22,pady=5, command=clear_all).grid()
        Button(root, text="add",font="lucida 12 bold",padx=22,pady=5, command=add).grid()
       

root.title("Password Manager")

root.geometry("800x800")

Label(root, text="enter master password").grid(row=0,column=1)
Entry(root, textvariable=mw).grid(row=0,column=2)
Button(root, text="execute",font="lucida 12 bold",padx=10,pady=5,command=execute).grid()
Button(root, text="stop",font="lucida 12 bold",padx=22,pady=5,command=root.destroy).grid()

'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as keyfile:
        keyfile.write(key)
write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)



root.mainloop()