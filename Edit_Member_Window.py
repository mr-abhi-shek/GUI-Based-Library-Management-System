import customtkinter
from tkinter import StringVar
import tkinter.messagebox as messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import useable_module

def edit_member_form(content_frame):

    # Colors and Fonts
    primary_color = "#E6E6FA"  
    button_bg = "#FF8C00"  # Dark Orange
    frame_bg = "#F0F0F0"  # Light Gray
    label_font = ("Montserrat", 13, "bold")
    entry_font = ("Montserrat", 13)

    # Create main frame with border, shadow, and 3D effect
    main_frame = customtkinter.CTkFrame(content_frame, fg_color="#E6E6FA", corner_radius=20)
    main_frame.place(relx=0.5,rely=0.5,relwidth=1, relheight=1, anchor="center")

    # Create main frame with border, shadow, and 3D effect
    update_main_frame = customtkinter.CTkFrame(main_frame, fg_color="#E6E6FA", corner_radius=20)
    update_main_frame.place(relx=0.5, rely=0.55, relwidth=0.9,relheight=0.725,anchor="center")#relx=0.5,rely=0.5,relwidth=0.98, relheight=0.98, anchor="center"
    

    # Add heading label with an icon
    heading_Label = customtkinter.CTkLabel(main_frame, text="📚 Update Member Information", font=("Georgia", 22, "bold"), text_color="#010B13")
    heading_Label.place(relx=0.5, rely=0.055, anchor="center")

    # Section to enter the unique Book ID
    member_id_label = customtkinter.CTkLabel(main_frame, text="Enter Unique Member ID", font=label_font, text_color="#34495e")
    member_id_label.place(relx=0.35, rely=0.125, anchor="e", relwidth=0.2)
    
    member_id_entry = customtkinter.CTkEntry(main_frame, font=entry_font)
    member_id_entry.place(relx=0.4, rely=0.125, anchor="w", relwidth=0.25)

    # Variables to hold book information fields (initialized empty until book is fetched)
    fields = {}
    
    # Function to fetch existing book data
    def fetch_member_data(member_id):
        try:
            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
            cursor = connector.cursor()
            sql = "SELECT * FROM PROFILES WHERE member_id = %s"
            cursor.execute(sql, (member_id,))
            member_data = cursor.fetchone()
            cursor.close()
            if member_data:
                #book_id_entry.configure(state="disable")
                populate_member_form(member_id,member_data)  # Call function to populate form with book data
            else:
                for widget in update_main_frame.winfo_children():
                    widget.destroy()
                update_main_frame.configure( border_width=0, corner_radius=0, fg_color=primary_color)
                messagebox.showerror("Error", f"No Such Member found with given Member_ID={member_id}!")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching Member Informations: {e}")

    # Populate form with book data
    def populate_member_form(member_id,member_data):
        update_main_frame.configure( border_width=1, corner_radius=50, fg_color="white", border_color="white")
        (Member_ID, Password, Role, Name, Contact_Number, Email, DOB, Communication_Address, Registartion_Date, profile_image, gender, Occupation) = member_data

        # Create Dropdown Menus (CTkOptionMenu) for Genre, Language, Edition fields
        role_options = ["MEMBER"]
        gender_options = ["Male","Female", "Other"]
        occupation_options = ["Student", "Teacher", "Housewife", "Corporate Worker", "Self-Employed", "Unemployed", "Other", "Prefer not to say"]

        # Create labels and entries for other fields and pre-populate them with fetched data
        fields.update({
            "Member_ID": customtkinter.CTkEntry(update_main_frame, font=entry_font),
            "Password": customtkinter.CTkEntry(update_main_frame, font=entry_font),
            "Role": customtkinter.CTkOptionMenu(update_main_frame, font=entry_font, values=role_options),
            "Name": customtkinter.CTkEntry(update_main_frame, font=entry_font),
            "Contact_Number": customtkinter.CTkEntry(update_main_frame, font=entry_font),
            "Email": customtkinter.CTkEntry(update_main_frame, font=entry_font),
            "DOB": customtkinter.CTkEntry(update_main_frame, font=entry_font),
            "Communication_Address": customtkinter.CTkEntry(update_main_frame, font=entry_font),
            "Registartion_Date": customtkinter.CTkEntry(update_main_frame, font=entry_font),
            "Gender": customtkinter.CTkOptionMenu(update_main_frame, font=entry_font, values=gender_options),
            "Occupation": customtkinter.CTkOptionMenu(update_main_frame, font=entry_font, values=occupation_options),
        })

        # Pre-fill form fields with fetched data
        fields["Member_ID"].insert(0, Member_ID)
        fields["Member_ID"].configure(state="disable")
        fields["Password"].insert(0, Password)
        fields["Role"].set(Role)
        fields["Name"].insert(0, Name)
        fields["Contact_Number"].insert(0, Contact_Number)
        fields["Email"].insert(0, Email)
        fields["DOB"].insert(0, DOB)
        fields["Communication_Address"].insert(0, Communication_Address)
        fields["Registartion_Date"].insert(0, Registartion_Date)
        fields["Registartion_Date"].configure(state="disable")
        fields["Gender"].set(gender)
        fields["Occupation"].set(Occupation)

        y = 0.075
        for label_text, entry in fields.items():
            label = customtkinter.CTkLabel(update_main_frame, text=label_text, font=label_font, text_color="#34495e")
            label.place(relx=0.35, rely=y, anchor="e", relwidth=0.25)
            entry.place(relx=0.4, rely=y, anchor="w", relwidth=0.25)
            y += 0.0725

        # Label for the image
        image_label = customtkinter.CTkLabel(update_main_frame, text="Cover Image", fg_color=primary_color, compound="top", text_color="black")
        image_label.place(relx=0.7, rely=0.3, relwidth=0.25, relheight=0.4, anchor="w")

        # Preload cover image if available
        if profile_image:
            img = Image.open(profile_image)
            img = img.resize((190, 220))
            img = ImageTk.PhotoImage(img)
            image_label.configure(image=img, text="", fg_color="transparent")
            image_label.image = img


        # Image upload section
        def upload_profile_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                img = Image.open(file_path)
                img = img.resize((190, 220))
                img = ImageTk.PhotoImage(img)
                image_label.configure(image=img, text="", fg_color="transparent")
                image_label.image = img
                return file_path
            return profile_image  # Return existing cover image path if no new image is selected


        # Save updated book function with confirmation pop-up
        def update_info(member_id):
            updated_member_data = {field: entry.get() for field, entry in fields.items()}
            print("MEMBER DATA : ", updated_member_data)
            updated_profile_image = upload_profile_image()
            print("Profile_Image",updated_profile_image)
            if updated_member_data["Password"].isalnum():
                if updated_member_data["Role"] in ["ADMIN", "MEMBER"]:
                    if useable_module.is_valid_string(updated_member_data["Name"]):
                        if useable_module.verify_mobile_number(updated_member_data["Contact_Number"]):
                            if useable_module.verify_email(updated_member_data["Email"]):
                                if useable_module.verify_date(updated_member_data["DOB"]):
                                    if useable_module.verify_address(updated_member_data["Communication_Address"]):
                                        
                                        try:
                                            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                                            cursor = connector.cursor()
                                            sql = """
                                                                UPDATE Profiles
                                                                SET Member_ID=%s, Password=%s, Role=%s, Name=%s,
                                                                Contact_Number=%s, Email=%s, DOB=%s,
                                                                Communication_Address=%s, Registartion_Date=%s, gender=%s, Occupation=%s,
                                                                profile_image=%s
                                                                WHERE member_id=%s
                                                """
                                            response=messagebox.askyesno("Update Member Request Confirmation", "Do you want to update Member information?")
                                            if response:
                                                print("\n\n*updated_member_data.values() : ", updated_member_data.values(),"\n\nupdated_profile_image : ", updated_profile_image, "\n\nmember_id : ", member_id)
                                                cursor.execute(sql, (*updated_member_data.values(), updated_profile_image, member_id))
                                                connector.commit()
                                                cursor.close()

                                                messagebox.showinfo("Member info updated", f"Information upadted for '{updated_member_data['Name']}' successfully!")
                                                main_frame.destroy()
                                        except Exception as e:
                                            messagebox.showerror("Error", f"Error updating: {e}")
                                    else:
                                        messagebox.showerror("Error","Enter valid ADDRESS of minimum 10 characters.")
                                else:
                                    messagebox.showerror("Error","Enter valid DOB in YYYY-MM-DD formate")
                            else:
                                messagebox.showerror("Error","Enter valid EMAIL Address")
                        else:
                            messagebox.showerror("Error","Enter valid 10 Digit MOBILE NUMBER")
                    else:
                        messagebox.showerror("Error","Enter valid NAME in Alphabets")
                else:
                    messagebox.showerror("Error","Select Role from Option Menu")
            else:
                messagebox.showerror("Error","Create Password That Contain Numbers and Alphabets Only")

            

        # Add hover effects on buttons
        save_button = customtkinter.CTkButton(update_main_frame, text="💾 Update", fg_color=button_bg, command=lambda : update_info(member_id), hover_color="#FF4500")
        save_button.place(relx=0.3, rely=0.925, anchor="e", relwidth=0.15)

        cancel_button = customtkinter.CTkButton(update_main_frame, text="❌ Cancel", command=main_frame.destroy, hover_color="#FF4500")
        cancel_button.place(relx=0.75, rely=0.925, anchor="w", relwidth=0.15)

        messagebox.showinfo("Information", "You can change and save information.")

    # Button to fetch the book data based on entered Book ID
    fetch_button = customtkinter.CTkButton(main_frame, text="🔍 Fetch Info", fg_color=button_bg, hover_color="#FF4500", command=lambda: fetch_member_data(member_id_entry.get()))
    fetch_button.place(relx=0.7275, rely=0.125, anchor="w", relwidth=0.15)

    # Footer Section
    footer_label = customtkinter.CTkLabel(main_frame, text="Library Management System v1.0 | Need Help? Contact support@library.com", 
                                      font=("Arial", 12), text_color="#010B13")
    footer_label.place(relx=0.5, rely=0.95, anchor="center")

if __name__ == "__main__":
    edit_member_form(content_frame)
