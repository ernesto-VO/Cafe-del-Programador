from backend import *
import customtkinter as ctk

def main():
    cargar_todos_los_datos()
    ventana_main = ctk.CTk()
    
    ventana_main.iconify() 
    #ventana_main.iconbitmap("")
    ventana_main.title("hola")
    ventana_main.geometry("600x500")
    
    ventana_main.deiconify()
    ventana_main.mainloop()



if __name__ == "__main__":
    main()