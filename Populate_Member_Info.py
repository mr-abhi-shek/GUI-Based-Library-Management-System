
import customtkinter
from tkinter import StringVar
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk


fields={}
# Populate form with book data
def populate_member_form(member_id,member_data, update_main_frame):
    primary_color = "#9bb2e5"
    label_font = ("Montserrat", 14, "bold")
    entry_font = ("Consola", 14)
        
    update_main_frame.configure( border_width=1, corner_radius=50, fg_color="white", border_color="white")

    print(member_data)
        
    # Create labels and entries for other fields and pre-populate them with fetched data
    fields.update({
        "Member_ID": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[0]),  font=entry_font, state="disable"),
        "Password": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[1]),  font=entry_font,  state="disable"),
        "Role": customtkinter.CTkEntry(update_main_frame, textvariable=StringVar(value=member_data[2]),font=entry_font,  state="disable"),
        "Name": customtkinter.CTkEntry(update_main_frame, textvariable=StringVar(value=member_data[3]), font=entry_font,  state="disable"),
        "Contact_Number": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[4]), font=entry_font,  state="disable"),
        "Email": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[5]), font=entry_font, state="disable"),
        "DOB": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[6]), font=entry_font, state="disable"),
        "Communication_Address": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[7]), font=entry_font,  state="disable"),
        "Registartion_Date": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[8]), font=entry_font, state="disable"),
        "Gender": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[10]), font=entry_font,  state="disable"),
        "Occupation": customtkinter.CTkEntry(update_main_frame,textvariable=StringVar(value=member_data[11]), font=entry_font, state="disable"),
    })

    y = 0.075
    for label_text, entry in fields.items():
        label = customtkinter.CTkLabel(update_main_frame, text=label_text, font=label_font, text_color="#34495e")
        label.place(relx=0.35, rely=y, anchor="e", relwidth=0.25)
        entry.place(relx=0.4, rely=y, anchor="w", relwidth=0.25)
        y += 0.065

    # Label for the image
    image_label = customtkinter.CTkLabel(update_main_frame, text="Profile\nImage", fg_color=primary_color, compound="top", text_color="black")
    image_label.place(relx=0.7, rely=0.25, relwidth=0.25, relheight=0.4, anchor="w")

    profile_image=member_data[9]
        
    # Preload cover image if available
        
    if profile_image:
        try:
            img = Image.open(profile_image)
            img = img.resize((150, 150))
            img = ImageTk.PhotoImage(img)
            image_label.configure(image=img, fg_color="transparent")
            image_label.image = img
        except Exception as e:
                messagebox.showerror("Loading Image ...... ", e)
