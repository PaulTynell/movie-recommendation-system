import tkinter
import customtkinter
import main

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Setup
root = customtkinter.CTk()
root.title("Movie recommendations")

#Size
root.geometry("500x400")

#Widgets
def myClick():
    clickLabel = customtkinter.CTkLabel(master=root, text="These are your movie recommendations:", font=("Arial", 14))
    clickLabel.pack(pady=10)
    output = main.main()
    text = tkinter.Text(master=root, height=13, width=61, font=("Arial", 10))
    text.insert(tkinter.END, str(output))
    text.pack(pady=10)
    scrollbar = tkinter.Scrollbar(master=root, command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

label1 = customtkinter.CTkLabel(master=root, text="Movie recommendations", font=("Arial", 15))
button1 = customtkinter.CTkButton(master=root, text="Get my recommendation!", command=myClick, font=("Arial", 14))
quit_button = customtkinter.CTkButton(master=root, text="Exit", font=("Arial", 10), command=root.quit)

#Inserts
label1.pack(pady=20)
button1.pack(pady=10)
quit_button.pack(pady=20)

root.mainloop()


