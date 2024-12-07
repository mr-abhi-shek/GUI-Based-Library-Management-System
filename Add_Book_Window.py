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

def add_book_form(content_frame):

    # Colors and Fonts
    primary_color = "#6A5ACD"  # Slate Blue
    button_bg = "#FF8C00"  # Dark Orange
    frame_bg = "#AFDBF5"  # Light Gray
    label_font = ("Montserrat", 14, "bold")
    entry_font = ("Consola", 13)

    # Create main frame with border, shadow, and 3D effect
    main_frame = customtkinter.CTkFrame(content_frame, fg_color="#CCCCFF", corner_radius=20) #8C92AC Gray most favourable
    main_frame.place(relx=0.5,rely=0.5,relwidth=1, relheight=1, anchor="center")

    # Add heading label with an icon
    heading_Label = customtkinter.CTkLabel(main_frame, text="📚 Library Book Registration", font=("Georgia", 22, "bold"), text_color="#010B13")
    heading_Label.place(relx=0.5, rely=0.05, anchor="center")

    new_frame= customtkinter.CTkFrame(main_frame, fg_color="white", corner_radius=20)
    new_frame.place(relx=0.5,rely=0.5,relwidth=0.8, relheight=0.8, anchor="center")

    # Create Dropdown Menus (CTkOptionMenu) for Genre, Language, Edition fields
    genre_options = ["Fiction", "Non-fiction", "Science Fiction", "Fantasy",
                     "Biography/Autobiography","Science & technology","Religion & spirituality",
                     "Philosophy","Humanities & social sciences","History"]
    language_options = ["Hindi","English", "Spanish", "French", "German", "Chinese"]
    edition_options = ["First", "Second", "Third", "Fourth", "Fifth", "Other", "Revised"]

    # Create labels and entries for other fields
    fields = {
        "Title": customtkinter.CTkEntry(new_frame, font=entry_font),
        "Author(s)": customtkinter.CTkEntry(new_frame, font=entry_font),
        "Publisher": customtkinter.CTkEntry(new_frame, font=entry_font),
        "Publication Date": customtkinter.CTkEntry(new_frame, font=entry_font),
        "Genre": customtkinter.CTkOptionMenu(new_frame, values=genre_options, font=entry_font),
        "Language" : customtkinter.CTkOptionMenu(new_frame, values=language_options, font=entry_font),
        "Number of Pages": customtkinter.CTkEntry(new_frame, font=entry_font),
        "Edition" : customtkinter.CTkOptionMenu(new_frame, values=edition_options, font=entry_font),
        "Number of Books": customtkinter.CTkEntry(new_frame, font=entry_font),
        "Price": customtkinter.CTkEntry(new_frame, font=entry_font),
    }

    y = 0.075
    for label_text, entry in fields.items():
        label = customtkinter.CTkLabel(new_frame, text=label_text, font=label_font, text_color="#2A3439", corner_radius=20)
        label.place(relx=0.45, rely=y, anchor="e", relwidth=0.35)
        entry.place(relx=0.5, rely=y, anchor="w", relwidth=0.35)
        y += 0.055

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
            upload_cover_image()

    # Label for the image with hover tooltip
    image_label = customtkinter.CTkLabel(new_frame, text="🖼Image",font=label_font, text_color="#2A3439", corner_radius=20)
    image_label.place(relx=0.45, rely=0.725, relwidth=0.35, anchor="e")
    
    image_label = customtkinter.CTkLabel(new_frame, fg_color="#CCCCFF", text="Cover\nPage", font=("Consola", 14), compound="top", text_color="black")
    image_label.place(relx=0.595, rely=0.725, relwidth=0.15, relheight=0.2, anchor="w")

    # Generate unique code function
    def generate_unique_code():
        letters = string.ascii_uppercase
        digits = string.digits
        random_letters = random.choices(letters, k=5)
        random_digits = random.choices(digits, k=6)
        combined = random_letters + random_digits
        random.shuffle(combined)
        unique_code = ''.join(combined)
        return unique_code

    # Save book function with confirmation pop-up
    def save_book():
        book_data = {field: entry.get() for field, entry in fields.items()}
        if useable_module.is_valid_string(book_data["Title"]):
            if useable_module.is_valid_string(book_data["Author(s)"]):
                if useable_module.is_valid_string(book_data["Publisher"]):
                    if useable_module.verify_date(book_data["Publication Date"]):
                        if book_data["Genre"]:
                            if book_data["Language"]:
                                if book_data["Number of Pages"].isdigit():
                                    if book_data["Edition"]:
                                        if book_data["Number of Books"].isdigit():
                                            if book_data["Price"].isdigit():
                                                file_path=upload_cover_image()
                                                if file_path!="":
                                                    entry_data=list(book_data.values())
                                                    unique_code=generate_unique_code()
                                                    entry_data.append(unique_code)
                                                    entry_data.append(file_path)
                                                    entry_data=tuple(entry_data)
                                                    try:
                                                        connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                                                        cursor = connector.cursor()
                                                        sql = "INSERT INTO BOOKS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        response=messagebox.askyesno("Book Registration", "Do you want to add book to the database?")
                                                        if response:
                                                            
                                                            cursor.execute(sql, entry_data)
                                                            connector.commit()
                                                            cursor.close()

                                                            book_title=book_data["Title"]
                                                            messagebox.showinfo("Book Registered", f"Book '{book_title}' Registered!\n\nUnique Code: {unique_code}")
                                                            main_frame.destroy()
                                    
                                                        
                                                    except Exception as e:
                                                        messagebox.showerror("Error",e)
                                                else:
                                                    messagebox.showerror("Error","Select an Image for Cover Page")
                                            else:
                                                messagebox.showerror("Error","Enter Valid Price in Numbers")
                                        else:
                                            messagebox.showerror("Error","Enter Quantity of Books in Number")
                                    else:
                                        messagebox.showerror("Error","Select Edition from Option Menu")
                                else:
                                    messagebox.showerror("Error","Enter Quantity of Pages in Number")
                            else:
                                messagebox.showerror("Error","Select Language from Option Menu")
                        else:
                            messagebox.showerror("Error","Select Genre from Option Menu")
                    else:
                        messagebox.showerror("Error","Enter Publication Date in YYYY-MM-DD Format")
                else:
                    messagebox.showerror("Error","Enter Valid Publisher in Alphabets")
            else:
                messagebox.showerror("Error","Enter Valid Author(s) in Alphabets")
        else:
            messagebox.showerror("Error","Enter Valid Title in Alphabets")

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
    add_book_form(content_frame)
