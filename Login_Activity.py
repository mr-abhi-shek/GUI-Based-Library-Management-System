# Importing Required Libraries
from Admin_Dashboard import *
import customtkinter
import mysql.connector
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
from tkinter import StringVar
from tkinter import ttk

# Setting the appearance mode to light
customtkinter.set_appearance_mode("light")

# Creating the window
login_window = customtkinter.CTk()

#fg_color = "#E8EAF6" text_color = "#6A5ACD"

# Setting the window Dimensions
width, height = login_window.winfo_screenwidth(), login_window.winfo_screenheight()
login_window.geometry(f"{int(width/1.2)}x{int(height/1.2)}")

# Setting the title of the window
login_window.title("Library Management System")

# Creating Parent Frame for login
parent_frame = customtkinter.CTkFrame(login_window, width=width, height=height, fg_color="#7A9E9F", corner_radius=15)
parent_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Creating a Child Frame for login
child_frame = customtkinter.CTkFrame(parent_frame, fg_color="#ffffff", corner_radius=10)
child_frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.7, anchor="center")

# Creating Label for Welcome Message
welcome_label = customtkinter.CTkLabel(login_window, text="Welcome to the Library Manager\nYour Gateway to Knowledge", 
                                       font=("Rockwell Extra Bold", 35), text_color="Black", fg_color="#7A9E9F")
welcome_label.place(relx=0.5, rely=0.1, anchor="center")

# Setting the login icon
login_icon = customtkinter.CTkImage(Image.open("icon/library-icon.jpg"), size=(60, 60))
login_icon_label = customtkinter.CTkLabel(child_frame, text="", image=login_icon)
login_icon_label.place(relx=0.5, rely=0.15, anchor="center")

# Creating Label for Library Login
login_label = customtkinter.CTkLabel(child_frame, text="Login", font=("Consolas", 25), text_color="#333333")
login_label.place(relx=0.5, rely=0.3, anchor="center")

# Creating Label and Entry for Login ID (Previously Username)
login_id_icon = ImageTk.PhotoImage(Image.open("icon/id-icon.png").resize((40, 40)))
login_id_label = customtkinter.CTkLabel(child_frame, text="Login ID", font=("Consolas", 18), image=login_id_icon, compound="left")
login_id_label.place(relx=0.2, rely=0.45, anchor="w")

login_id_var = StringVar(value="PDQPK178705")
login_id_entry = customtkinter.CTkEntry(child_frame, textvariable=login_id_var, placeholder_text="Enter Login ID", font=("Courier New", 14), width=180)
login_id_entry.place(relx=0.6, rely=0.45, anchor="w")

# Tooltip for Login ID
tooltip_login_id = ttk.Label(child_frame, text="Enter your Login ID")
tooltip_login_id.place(relx=0.6, rely=0.42, anchor="w")

# Creating Label and Entry for Password
password_icon = ImageTk.PhotoImage(Image.open("icon/password-icon.jpg").resize((40, 40)))
password_label = customtkinter.CTkLabel(child_frame, text="Password", font=("Consolas", 18), image=password_icon, compound="left")
password_label.place(relx=0.2, rely=0.55, anchor="w")

password_var = StringVar(value="KQRIQ291203")
password_entry = customtkinter.CTkEntry(child_frame, textvariable=password_var, placeholder_text="Enter Password", font=("Courier New", 14), width=180, show="*")
password_entry.place(relx=0.6, rely=0.55, anchor="w")

# Tooltip for Password
tooltip_password = ttk.Label(child_frame, text="Enter your Password")
tooltip_password.place(relx=0.6, rely=0.52, anchor="w")

# Show/Hide Password Functionality
show_password_var = StringVar(value="*")
toggle_button = customtkinter.CTkButton(child_frame, text="Show", width=50, command=lambda: toggle_password())
toggle_button.place(relx=0.8, rely=0.55, anchor="w")

# Creating Label and Option Menu for Role
role_icon = ImageTk.PhotoImage(Image.open("icon/password-icon.jpg").resize((40, 40)))
role_label = customtkinter.CTkLabel(child_frame, text="Role", font=("Consolas", 18), image=password_icon, compound="left")
role_label.place(relx=0.2, rely=0.65, anchor="w")


role_var=StringVar(value="Select Role")
role_option=["ADMIN","MEMBER"]

role_optionMenu=customtkinter.CTkOptionMenu(child_frame, values=role_option, variable=role_var,  font=("Courier New", 14), width=180)
role_optionMenu.place(relx=0.6, rely=0.65, anchor="w")

def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        toggle_button.configure(text="Hide")
    else:
        password_entry.configure(show="*")
        toggle_button.configure(text="Show")

# Login Function with User-Friendly Error Messages
def login():
    login_id, pwd, role = login_id_entry.get(), password_entry.get(), role_optionMenu.get()
    
    try:
        data_list=[]
        # Connecting to the MySQL Database
        my_sql = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")

        # Creating a Cursor for MySQL
        my_cursor = my_sql.cursor()

        my_cursor.execute("SELECT Member_ID, Password, Role, Name FROM PROFILES WHERE Member_ID = %s AND Password = %s AND Role = %s", (login_id, pwd, role))
        data_list=my_cursor.fetchall()
        print(data_list)
        my_cursor.close()
        if data_list !=[]:
            
            # Success message and open secondary window
            messagebox.showinfo("Login", f"{data_list[0][3]}, Successfully Logged In as {role}!")
            # Closing the Login Window after Successful Login
            login_window.destroy()

            if role=="ADMIN":
                Dashoard_Admin_Window(login_id, pwd)
            else:
                Dashoard_Member_Window(login_id, pwd)
                

        else:
            messagebox.showwarning("Login Failed", "Invalid Login ID or Password or Role. Please try again.")
                
    except mysql.connector.Error as e:
        messagebox.showwarning("Login Failed", f"An error occurred: {str(e)}")

# Creating Login Button
login_button = customtkinter.CTkButton(child_frame, text="Login", font=("Courier New", 15), command=login, fg_color="#4682b4")
login_button.place(relx=0.5, rely=0.8, anchor="center")

# Keyboard Shortcut (Enter Key) for Login
login_window.bind("<Return>", lambda event: login())

# Footer Section
footer_label = customtkinter.CTkLabel(login_window, text="Library Management System v1.0 | Need Help? Contact support@library.com", 
                                      font=("Arial", 12), text_color="#666666", fg_color="#7A9E9F")
footer_label.place(relx=0.5, rely=0.95, anchor="center")

# Running the window loop
login_window.mainloop()


#E6E6FA (Lavender Web)
