import tkinter as tk
import time

# admin = ''
try:
    fileRead = open('./passwords.txt')
    for line in fileRead.readlines():
        admin = line
except:
    admin = ''
    
    

def set_password():
    global entry1
    global new_window
    new_window = tk.Toplevel(root)
    new_window.geometry("400x400")
    
    label = tk.Label(new_window, text="Set the password:")
    label.pack()
    
    entry1 = tk.Entry(new_window, show="*")
    entry1.pack()
    
    button = tk.Button(new_window, text="Submit", command=setNewPass)
    button.pack()
  

def showNotif(x):
    new_window10 = tk.Toplevel(root)
    new_window10.geometry("600x50")
    
    label = tk.Label(new_window10, text=x)
    label.pack()  

def setNewPass():
    global admin
    global entry1
    global new_window
    if admin == '':
        admin = entry1.get()
        myFile = open('./passwords.txt', 'w')
        myFile.write(admin)
        myFile.close()
        entry1.delete(0, 'end')
        showNotif('Password is set!')
    else:
        showNotif('Password has been set! In order to change the password choose correct option!')
    
    new_window.destroy()
    
   
def changePass():
    global admin
    global entry2
    global entry3
    global new_window2
    global new_window3
     
    oldpass = entry2.get()
    if oldpass == admin:
        
        new_window3 = tk.Toplevel(root)
        new_window3.geometry("300x100")
        
        label = tk.Label(new_window3, text="Enter new password:")
        label.pack()
        
        entry3 = tk.Entry(new_window3, show="*")
        entry3.pack()
        
        button = tk.Button(new_window3, text="Submit", command=ChangeNewpass)
        button.pack()
               
    else:
        showNotif('Wrong password!')
    new_window2.destroy()
    
def ChangeNewpass():
    global new_window3
    global entry3
    global admin
    admin = entry3.get()
    myFile = open('./passwords.txt', 'w')
    myFile.write(admin)
    myFile.close()
    showNotif('Password has been changed!') 
    new_window3.destroy()       

def change_password():
    global admin
    global entry2
    global new_window2
    new_window2 = tk.Toplevel(root)
    new_window2.geometry("300x100")
    new_window2.title('Change password')
    
    label = tk.Label(new_window2, text="Enter your password:")
    label.pack()
    
    entry2 = tk.Entry(new_window2, show="*")
    entry2.pack()
    
    button = tk.Button(new_window2, text="Submit", command=changePass)
    button.pack()
    
    
def open_page():
    global admin
    global entry4
    global new_window4
    new_window4 = tk.Toplevel(root)
    new_window4.geometry("300x100")
    new_window4.title('Login')
    
    label = tk.Label(new_window4, text="Enter your password:")
    label.pack()
    
    entry4 = tk.Entry(new_window4, show="*")
    entry4.pack()
    
    button = tk.Button(new_window4, text="Submit", command=login)
    button.pack()
   
def login():
    global admin
    global entry4
    global new_window4
    guess = entry4.get()
    if guess == admin:
        showNotif('Access Granted!') 
    else:
        showNotif('Wrong password!') 
    new_window4.destroy()
     

# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.title("Password Protected Application")

set_password_button = tk.Button(root, text="Set Password", command=set_password)
set_password_button.pack()

change_password_button = tk.Button(root, text="Change Password", command=change_password)
change_password_button.pack()

open_page_button = tk.Button(root, text="Open Page", command=open_page)
open_page_button.pack()

# Run the main loop
root.mainloop()





# def f(x):
#     y = 2*x+1
#     return y
    
# y = f(3)

# print(y)