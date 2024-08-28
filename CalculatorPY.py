from tkinter import *
import customtkinter as ctk

def Calculator_Main(option):
    global text_input
    
    if option == "Enter":
        try:
            result = eval(text_input.get())
            text_input.set(str(result))
        except Exception as e:
            text_input.set("Error")
    elif option == "Erase":
        text_input.set("") 

def run_in_thread(option):
    current_text = text_input.get()
    
    if option not in ["Enter", "Erase"]:
        new_text = current_text + option
        text_input.set(new_text)
    else:
        Calculator_Main(option) 

def main():
    global app, text_input, display

    app = ctk.CTk() 
    app.title("Calculator")
    app.geometry("600x400")

    text_input = ctk.StringVar()
    
    display = ctk.CTkEntry(app, textvariable=text_input, font=("Arial", 18), justify='right')
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")

    button_7 = ctk.CTkButton(app, text="7", command=lambda: run_in_thread('7'))
    button_7.grid(row=1, column=0, padx=5, pady=5)

    button_8 = ctk.CTkButton(app, text="8", command=lambda: run_in_thread('8'))
    button_8.grid(row=1, column=1, padx=5, pady=5)

    button_9 = ctk.CTkButton(app, text="9", command=lambda: run_in_thread('9'))
    button_9.grid(row=1, column=2, padx=5, pady=5)

    button_Dividir = ctk.CTkButton(app, text="/", command=lambda: run_in_thread('/'))
    button_Dividir.grid(row=1, column=3, padx=5, pady=5)

    button_4 = ctk.CTkButton(app, text="4", command=lambda: run_in_thread('4'))
    button_4.grid(row=2, column=0, padx=5, pady=5)

    button_5 = ctk.CTkButton(app, text="5", command=lambda: run_in_thread('5'))
    button_5.grid(row=2, column=1, padx=5, pady=5)

    button_6 = ctk.CTkButton(app, text="6", command=lambda: run_in_thread('6'))
    button_6.grid(row=2, column=2, padx=5, pady=5)

    button_Multiplicar = ctk.CTkButton(app, text="*", command=lambda: run_in_thread('*'))
    button_Multiplicar.grid(row=2, column=3, padx=5, pady=5)

    button_1 = ctk.CTkButton(app, text="1", command=lambda: run_in_thread('1'))
    button_1.grid(row=3, column=0, padx=5, pady=5)

    button_2 = ctk.CTkButton(app, text="2", command=lambda: run_in_thread('2'))
    button_2.grid(row=3, column=1, padx=5, pady=5)

    button_3 = ctk.CTkButton(app, text="3", command=lambda: run_in_thread('3'))
    button_3.grid(row=3, column=2, padx=5, pady=5)

    button_Resta = ctk.CTkButton(app, text="-", command=lambda: run_in_thread('-'))
    button_Resta.grid(row=3, column=3, padx=5, pady=5)

    button_0 = ctk.CTkButton(app, text="0", command=lambda: run_in_thread('0'))
    button_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    button_Enter = ctk.CTkButton(app, text="Enter", command=lambda: run_in_thread('Enter'))
    button_Enter.grid(row=4, column=2, padx=5, pady=5)

    button_Mas = ctk.CTkButton(app, text="+", command=lambda: run_in_thread('+'))
    button_Mas.grid(row=4, column=3, padx=5, pady=5)

    button_Erase = ctk.CTkButton(app, text="Erase", command=lambda: run_in_thread('Erase'))
    button_Erase.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

    app.mainloop()

if __name__ == "__main__":
    main()
