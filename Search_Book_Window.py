import customtkinter as ctk
from tkinter import Scrollbar
from tkinter import StringVar, messagebox
import mysql.connector
from PIL import Image, ImageTk  # For image handling

def book_search_Form(center_frame):

    # Set color palette
    primary_color = "#6A5ACD"  # Slate blue
    secondary_color = "#7D7DD7"  # Lighter purple
    fg_color = "#E8EAF6"  # Light greyish-blue for background
    text_color = "#2E2E2E"  # Dark grey for text             fg_color = "#E8EAF6" text_color = "#6A5ACD"
    white_color = "#FFFFFF"  # White for labels and buttons
    button_hover_color = "#4040A1"  # Button hover color
    font_type = ("Georgia", 13, "bold")  # Stylish modern font for buttons
    label_font_type = ("Georgia", 12, "underline")  # Modern font for labels

    # Create the main form frame
    new_frame = ctk.CTkFrame(center_frame,
                             fg_color=fg_color,  # Light background color
                             corner_radius=15,border_width=2)
    new_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

    # Add title label (centered)
    title_label = ctk.CTkLabel(new_frame, text="🔍 Search Book Information",
                               font=("Georgia", 22, "bold"),
                               text_color="black")
    title_label.place(relx=0.5, rely=0.05, anchor="center")

    # Create a search form frame
    search_form_frame = ctk.CTkFrame(new_frame, 
                                     fg_color="white",  
                                     corner_radius=10)
    

    # Add section title label
    book_list_label = ctk.CTkLabel(search_form_frame, text="📂 Books List",
                                       font=("consolas", 22, "bold"),
                                       text_color="black",
                                        corner_radius=5)

    fields={}

    def show_book_details(book_id):
        print("BOOK_ID : ", book_id)
        label_font = ("Montserrat", 14, "bold")
        entry_font = ("Consola", 14)
        search_by_button.configure(state="disable")
        show_detail_frame = ctk.CTkFrame(new_frame, 
                                     fg_color="white",  
                                     corner_radius=20)
        show_detail_frame.place(relx=0.5, rely=0.575, relwidth=0.95, relheight=0.8, anchor="center")


        try:
            connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
            cursor = connector.cursor()
            sql = "Select * FROM BOOKS WHERE Book_ID = %s"
            cursor.execute(sql,(book_id,))
            book_data = cursor.fetchone()
            print(book_data)
            cursor.close()
        except Exception as e:
            messagebox.showerror("Error", e)

        # Add section title label
        title_label = ctk.CTkLabel(show_detail_frame, text=f"📂 ({book_data[0]}) Book Information",
                                       font=("Badoni", 18, "bold"),
                                       text_color="Black",
                                        corner_radius=5)
        title_label.place(relx=0.5, rely=0.05, anchor="center")
            

        fields.update({
            "Book_ID": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_id),  font=entry_font, state="disable"),
            "Title": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_data[0]),  font=entry_font,  state="disable"),
            "Author(s)": ctk.CTkEntry(show_detail_frame, textvariable=StringVar(value=book_data[1]),font=entry_font,  state="disable"),
            "Publisher": ctk.CTkEntry(show_detail_frame, textvariable=StringVar(value=book_data[2]), font=entry_font,  state="disable"),
            "Publication Date": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_data[3]), font=entry_font,  state="disable"),
            "Genre": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_data[4]), font=entry_font, state="disable"),
            "Language": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_data[5]), font=entry_font, state="disable"),
            "Number of Pages": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_data[6]), font=entry_font,  state="disable"),
            "Edition": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_data[7]), font=entry_font, state="disable"),
            "Number of Books": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_data[8]), font=entry_font,  state="disable"),
            "Price": ctk.CTkEntry(show_detail_frame,textvariable=StringVar(value=book_data[9]), font=entry_font, state="disable"),
        })

        y = 0.15
        for label_text, entry in fields.items():
            label = ctk.CTkLabel(show_detail_frame, text=label_text, font=label_font, text_color="#34495e")
            label.place(relx=0.35, rely=y, anchor="e", relwidth=0.25)
            entry.place(relx=0.4, rely=y, anchor="w", relwidth=0.25)
            y += 0.065

        # Label for the image
        image_label = ctk.CTkLabel(show_detail_frame, text=" \nCover\nImage", fg_color=primary_color, compound="top", text_color="black")
        image_label.place(relx=0.7, rely=0.4, relwidth=0.25, relheight=0.4, anchor="w")

        cover_image=book_data[11]
        
        # Preload cover image if available
        
        if cover_image:
            try:
                img = Image.open(cover_image)
                img = img.resize((150, 150))
                img = ImageTk.PhotoImage(img)
                image_label.configure(image=img, fg_color="transparent")
                image_label.image = img
            except Exception as e:
                messagebox.showerror("Loading Image ...... ", e)

        # Function to copy text from the disabled entry when the button is clicked
        def copy_text():
        
            # Copy the content of the entry box to the clipboard
            show_detail_frame.clipboard_clear()
            show_detail_frame.clipboard_append(book_id)
        
            # Show a message to inform the user
            messagebox.showinfo("Copied", "Text has been copied to clipboard!")

        # Create a button to copy text
        copy_button = ctk.CTkButton(show_detail_frame, text="Copy Book_ID", fg_color="orange", command=copy_text)
        copy_button.place(relx=0.7, rely=0.15, anchor="w",relwidth=0.25)


        def close():
            show_detail_frame.destroy()
            search_by_button.configure(state="normal")

        cancel_button = ctk.CTkButton(show_detail_frame, text="❌ Close", command=close, hover_color="Green")
        cancel_button.place(relx=0.5, rely=0.925, anchor="center", relwidth=0.15)

        messagebox.showinfo("Message", "You can copy Book_ID by CTRL-c")



    # Function to create scrollable frame
    def create_scrollable_frame(root, color, radius):
        # Create the main frame that will hold everything
        main_frame = ctk.CTkFrame(root, fg_color=color, corner_radius=radius)

        # Create a canvas within the frame
        canvas = ctk.CTkCanvas(main_frame,bg=color)
        canvas.grid(row=0, column=0, sticky="nsew")  # Use grid instead of pack for better layout control

        # Create horizontal and vertical scrollbars
        h_scrollbar = Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
        v_scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)

        # Position scrollbars correctly
        h_scrollbar.grid(row=1, column=0, sticky="ew")  # Horizontal scrollbar at the bottom
        v_scrollbar.grid(row=0, column=1, sticky="ns")  # Vertical scrollbar on the right

        # Configure the canvas to work with the scrollbars
        canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

        # Create a frame inside the canvas (this is where your content goes)
        scrollable_frame = ctk.CTkFrame(canvas,fg_color=color, corner_radius=radius)

        # The frame needs to be added as a window in the canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Configure the scroll region of the canvas based on the frame size
        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Bind configure event to update scroll region
        scrollable_frame.bind("<Configure>", configure_scroll_region)

        # Make the main_frame's grid expand with the window
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        return [scrollable_frame,main_frame]

    frame_list = create_scrollable_frame(search_form_frame,"#AFDBF5", 20)
    scrollable_frame = frame_list[0]
    main_frame = frame_list[1]

    # Search button functionality
    def Search_button():

        search_option = search_by_menu.get()
        detail = detail_EntryBox.get()
        if search_option != "Select by Detail":
            book_data = []
            try:
                connector = mysql.connector.connect(host="localhost", user="root", password="12345678", database="Library_Database")
                cursor = connector.cursor()
                sql = f'SELECT Book_ID,Title, Author,Publisher,Genre,Language FROM BOOKS WHERE {search_option} like "{detail}%"'
                cursor.execute(sql)
                book_data = cursor.fetchall()
                print(book_data)
                cursor.close()
            except Exception as e:
                messagebox.showerror("Error", e)

            if book_data:

                # Clear previous labels
                try:
                    print(search_form_frame.winfo_children())
                    for widget in search_form_frame.winfo_children():
                        widget.place_forget()
                except Exception as e:
                    messagebox.showerror("Error",e)
                        
                search_form_frame.place(relx=0.5, rely=0.575, relwidth=0.95, relheight=0.8, anchor="center")
                
                # Create the progress bar widget
                progress_bar = ctk.CTkProgressBar(search_form_frame, width=300, height=20, corner_radius=10)
                progress_bar.place(relx=0.5,rely=0.5,anchor="center",relwidth=0.5)

                # Set initial value of the progress bar to 0 (start point)
                progress_bar.set(0)
                
                x , y = 1 , 0

                try:
                    # Clear previous labels
                    for widget in scrollable_frame.winfo_children():
                        widget.destroy()
                except:
                    pass

                # Define headings with improved styling
                headings = ["Book_ID", "Title", "Author", "Publisher", "Genre", "Language"]
                for i, heading in enumerate(headings):
                    label = ctk.CTkLabel(scrollable_frame, text=heading,
                                         font=font_type, 
                                         text_color="Black", fg_color=white_color, corner_radius=8)
                    label.grid(row=0, column=i, padx=20, pady=15)

                # Add content inside the scrollable frame
                progress=len(book_data)
                for i, row in enumerate(book_data):
                    book_id_button = ctk.CTkButton(scrollable_frame, text=row[0],
                                                   font=("Consolas", 12, "bold","underline"), text_color="white",
                                                   fg_color="black", corner_radius=8, width=50,
                                                   command=lambda row_value=row[0]: show_book_details(row_value))
                    book_id_button.grid(row=x, column=0, padx=15, pady=10)

                    for column in range(1,6):
                        label = ctk.CTkLabel(scrollable_frame, text=row[column],
                                             font=label_font_type, text_color=text_color,
                                             fg_color=white_color, corner_radius=8)
                        label.grid(row=x, column=column, padx=15, pady=10)
                    x += 1
                    progress_bar.set((i/progress)*100)
                    search_form_frame.update()
                    
                    
                progress_bar.place_forget()
                book_list_label.place(relx=0.5, rely=0.045, anchor="center")
                main_frame.place(relx=0.5, rely=0.53, relwidth=0.95, relheight=0.875, anchor="center")
                messagebox.showinfo("Information", " You can view information of book by clicking on the Book_ID button.")
            else:
                search_form_frame.place_forget()
                messagebox.showinfo("Search", f"No Book Information found for given {detail}!")
                
                
        else:
            messagebox.showwarning("Warning", "Select an option for searching")

    # Search by options
    search_by_var = StringVar(value="Select by Detail")
    search_by_options = ["Book_ID","Title", "Author", "Publisher","Genre","Language"]

    # Search by dropdown
    search_by_menu = ctk.CTkOptionMenu(new_frame, values=search_by_options, variable=search_by_var, fg_color=primary_color)
    search_by_menu.place(relx=0.0975, rely=0.125, anchor="w", relwidth=0.225)

    # Entry box for entering detail
    detail_EntryBox = ctk.CTkEntry(new_frame, placeholder_text="Enter Number", font=font_type, text_color="Black")
    detail_EntryBox.place(relx=0.4, rely=0.125, anchor="w", relwidth=0.225)

    # Search button
    search_by_button = ctk.CTkButton(new_frame, text="Search", font=font_type, fg_color=primary_color, command=Search_button)
    search_by_button.place(relx=0.675, rely=0.125, anchor="w", relwidth=0.225)

if __name__ == "__main__":

    book_search_Form(center_frame)


