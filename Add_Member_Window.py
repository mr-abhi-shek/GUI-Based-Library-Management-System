import customtkinter
from tkinter import StringVar
import tkinter.messagebox as messagebox
import random
import string
from datetime import datetime
import useable_module
import mysql.connector
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import datetime

def add_member_form(content_frame):
    # Colors and Fonts
    primary_color = "#6A5ACD"  # Slate Blue
    button_bg = "#FF8C00"  # Dark Orange
    frame_bg = "#AFDBF5"  # Light Gray
    label_font = ("Montserrat", 14, "bold")
    entry_font = ("Consola", 13)

    # Create main frame with border, shadow, and 3D effect
    main_frame = customtkinter.CTkFrame(content_frame, fg_color="#8C92AC", corner_radius=20)
    main_frame.place(relx=0.5,rely=0.5,relwidth=1, relheight=1, anchor="center")

    # Add heading label with an icon
    heading_Label = customtkinter.CTkLabel(main_frame, text="👤 Account Registration", font=("Georgia", 22, "bold"), text_color="#010B13")
    heading_Label.place(relx=0.5, rely=0.05, anchor="center")

    new_frame= customtkinter.CTkFrame(main_frame, fg_color="white", corner_radius=20)
    new_frame.place(relx=0.5,rely=0.5,relwidth=0.8, relheight=0.8, anchor="center")

    # Create Dropdown Menus (CTkOptionMenu) for Genre, Language, Edition fields
    role_options = ["ADMIN","MEMBER"]
    gender_options = ["Male","Female","Other"]
    occupation_options = ["Student", "Teacher", "Housewife", "Corporate Worker", "Self-Employed", "Unemployed", "Other", "Prefer not to say"]

    # Create labels and entries for other fields
    fields = {
        "Account Type": customtkinter.CTkOptionMenu(new_frame, values=role_options, font=entry_font),
        "Full Name": customtkinter.CTkEntry(new_frame, font=entry_font),
        "Contact Number": customtkinter.CTkEntry(new_frame, font=entry_font),
        "E-Mail": customtkinter.CTkEntry(new_frame, font=entry_font),
        "DOB (YYYY-MM-DD)": customtkinter.CTkEntry(new_frame, font=entry_font),
        "Communication_Address" : customtkinter.CTkEntry(new_frame, font=entry_font),
        "Gender": customtkinter.CTkOptionMenu(new_frame, values=gender_options, font=entry_font),
        "Occupation" : customtkinter.CTkOptionMenu(new_frame, values=occupation_options, font=entry_font),
    }

    y = 0.1
    for label_text, entry in fields.items():
        label = customtkinter.CTkLabel(new_frame, text=label_text, font=label_font, text_color="#2A3439", corner_radius=20)
        label.place(relx=0.45, rely=y, anchor="e", relwidth=0.35)
        entry.place(relx=0.5, rely=y, anchor="w", relwidth=0.35)
        y += 0.06

    # Image upload section
    file_path = ""

    def upload_cover_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            img = Image.open(file_path)
            img = img.resize((150, 150))
            img = ImageTk.PhotoImage(img)
            image_label.configure(image=img, text="", fg_color="transparent")
            image_label.image = img
            return file_path
        else:
            messagebox.showerror("Error","Upload PROFILE IMAGE")
            upload_cover_image()
    

    # Label for the image with hover tooltip
    image_label = customtkinter.CTkLabel(new_frame, text="🖼Image",font=label_font, text_color="#2A3439", corner_radius=20)
    image_label.place(relx=0.45, rely=0.675, relwidth=0.35, anchor="e")
    
    image_label = customtkinter.CTkLabel(new_frame, fg_color="#8C92AC", text="Profile\nImage", font=("Consola", 14, "bold"), compound="top", text_color="black")
    image_label.place(relx=0.595, rely=0.675, relwidth=0.15, relheight=0.2, anchor="w")

    # Generate unique code function
    def generate_id_password():
        letters = string.ascii_uppercase
        digits = string.digits
        random_letters = random.choices(letters, k=5)
        random_digits = random.choices(digits, k=6)
        combined = random_letters + random_digits
        unique_code = ''.join(combined)
        return unique_code

    # Save book function with confirmation pop-up
    def save_book():
        member_data = {field: entry.get() for field, entry in fields.items()}
        if useable_module.is_valid_string(member_data["Account Type"]):
            if useable_module.is_valid_string(member_data["Full Name"]):
                if useable_module.verify_mobile_number(member_data["Contact Number"]):
                    if useable_module.verify_email(member_data["E-Mail"]):
                        if useable_module.verify_date(member_data["DOB (YYYY-MM-DD)"]):
                            if useable_module.verify_address(member_data["Communication_Address"]):
                                if member_data["Gender"]:
                                    if member_data["Occupation"]:
                                        
                                        entry_data=list(member_data.values())
                                        entry_data.pop()
                                        entry_data.pop()
                                        print(entry_data)
                                        
                                        entry_data.append(datetime.today().strftime('%Y-%m-%d'))
                                        
                                        print(entry_data)
                                        
                                        file_path=upload_cover_image()
                                        entry_data.append(file_path)
                                        entry_data.append(member_data["Gender"])
                                        entry_data.append(member_data["Occupation"])
                                        
                                        print(entry_data)

                                        
                                        member_id=generate_id_password()
                                        member_password=generate_id_password()
                                        entry_data.insert(0,member_id)
                                        entry_data.insert(1,member_password)
            
                                        print(entry_data)
                                        
                                        try:
                                            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                                            cursor = connector.cursor()
                                            sql = "INSERT INTO PROFILES VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            response=messagebox.askyesno("Memebr Registration", "Do you want to create Member Profile?")
                                            if response:
                                                
                                                cursor.execute(sql, tuple(entry_data))
                                                connector.commit()
                                                cursor.close()

                                                member_name=member_data["Full Name"]
                                                messagebox.showinfo("Book Registered", f"""Member Account created for ({member_name})!\n\n
                                                                                                Member_ID : {member_id}\n
                                                                                                Member_Password : {member_password}\n\n
                                                                                                Member can login now.""")
                                                main_frame.destroy()
                                    
                                                        
                                        except Exception as e:
                                            messagebox.showerror("Error",e)
                                    else:
                                        messagebox.showerror("Error","Select OCCUPATION from option menu")
                                else:
                                    messagebox.showerror("Error","Select GENDER from option menu")
                            else:
                                messagebox.showerror("Error","Enter valid COMMUNICATION ADDRESS with minimum 10 characters")
                        else:
                            messagebox.showerror("Error","Enter DATE OF BIRTH in YYYY_MM_DD formate")
                    else:
                        messagebox.showerror("Error","Enter valid E-MAIL ID")
                else:
                    messagebox.showerror("Error","Enter valid MOBILE NUMBER with only 10 digits")
            else:
                messagebox.showerror("Error","Enter valid NAME in alphabets")
        else:
            messagebox.showerror("Error","Select Account Type From Option Menu")

    # Add hover effects on buttons
    save_button = customtkinter.CTkButton(new_frame, text="💾 Save", fg_color=button_bg, command=save_book, hover_color="#FF4500")
    save_button.place(relx=0.35, rely=0.9, anchor="e", relwidth=0.15)

    cancel_button = customtkinter.CTkButton(new_frame, text="❌ Cancel", command=main_frame.destroy, hover_color="#FF4500")
    cancel_button.place(relx=0.595, rely=0.9, anchor="w", relwidth=0.15)

    # Footer Section
    footer_label = customtkinter.CTkLabel(main_frame, text="Library Management System v1.0 | Need Help? Contact support@library.com", 
                                      font=("Arial", 12), text_color="#010B13")
    footer_label.place(relx=0.5, rely=0.95, anchor="center")


if __name__ == "__main__":
    add_member_form(content_frame)
