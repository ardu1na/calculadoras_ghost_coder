import customtkinter
import tkinter as tk
from PIL import Image

class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.image = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\header2.png"),
                                  dark_image=Image.open(r"C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\header2.png"),
                                  size=(1980, 200))
        self.image_label = customtkinter.CTkLabel(self, image=self.image, text="",)
        self.image_label.pack(fill=tk.X, expand=True, padx=0)


            
class InversionesFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1,2,3,4,5,6), weight=1)
        self.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        
        #### INPUT
        self.columna1 = customtkinter.CTkFrame(self)
        self.columna1.grid(row=1, column=1)
        
        self.entrada_monto = customtkinter.CTkEntry(self.columna1, placeholder_text="MONTO DE LA INVERSIÓN",font=("Verdana",24), width=350, height=80, corner_radius=55)
        self.entrada_monto.grid(row=1, column=0, padx=10, pady=10)


        self.entrada_n_cuotas = customtkinter.CTkEntry(self.columna1, placeholder_text="MESES",font=("Verdana",24), width=350, height=80, corner_radius=55)
        self.entrada_n_cuotas.grid(row=4, column=0, padx=10, pady=10)

        self.entrada_valor_cuota = customtkinter.CTkEntry(self.columna1, placeholder_text="RETRNO ANUAL",font=("Verdana",24), width=350, height=80, corner_radius=55)
        self.entrada_valor_cuota.grid(row=7, column=0, padx=10, pady=10)
        
        
        
        
        self.columna2 = customtkinter.CTkFrame(self)
        self.columna2.grid(row=1, column=3)
        
        ### output
        
        self.texto = customtkinter.CTkEntry(self.columna2, placeholder_text="Préstamos y Cuotificación",font=("Verdana",24), width=350, height=80, corner_radius=55, state="disabled")
        self.texto.grid(row=1, column=0, padx=10, pady=10)
        
        self.salida_1 = customtkinter.CTkEntry(self.columna2, placeholder_text="",font=("Verdana",24), width=350, height=80, corner_radius=55, state="disabled")
        self.salida_1.grid(row=3, column=0, padx=10, pady=10)
        
        self.salida_2 = customtkinter.CTkEntry(self.columna2, placeholder_text="",font=("Verdana",24), width=350, height=80, corner_radius=55, state="disabled")
        self.salida_2.grid(row=5, column=0, padx=10, pady=10)

       

        ### botonera
         
        self.columna3 = customtkinter.CTkFrame(self)
        self.columna3.grid(row=1, column=5)
        self.button_prestamos = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Calcular intereses", font=("Verdana", 36), command=self.calcular_interes)
        self.button_prestamos.grid(row=4, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  

        self.button_ayuda = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Ayuda", font=("Verdana", 36))
        self.button_ayuda.grid(row=6, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  
        
        self.button_volver = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Volver", font=("Verdana", 36), command=self.volver)
        self.button_volver.grid(row=8, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)
        
    def calcular_interes(self):
        try:
            monto = float(self.entrada_monto.get())
            n_cuotas = int(self.entrada_n_cuotas.get())
            valor_cuota = float(self.entrada_valor_cuota.get())

            interes_total = (n_cuotas * valor_cuota) - monto
            interes_mensual =  interes_total / n_cuotas

            self.salida_1.configure(placeholder_text=f"Diferencia total: \n${interes_total:.2f}")
            self.salida_2.configure(placeholder_text=f"Interés mensual: \n ${interes_mensual:.2f}")
        except ValueError:
            self.texto.configure(placeholder_text="Error: Ingresa valores válidos")
            
    
        
    def volver(self):
        master = self.master
        self.grid_forget()
        index = IndexFrame(master)
        index.grid(row=1, column=0, columnspan=7, ipady=130, ipadx=230)
        
                
            
class PrestamosFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1,2,3,4,5,6), weight=1)
        self.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        
        #### INPUT
        self.columna1 = customtkinter.CTkFrame(self, fg_color="grey")
        self.columna1.grid(row=1, column=1)
        self.columna1.grid_columnconfigure((0, 1,2,3), weight=1)
        self.columna1.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        self.label_monto = customtkinter.CTkLabel(self.columna1, text="Precio final",font=("Verdana",24), text_color="white")
        self.label_monto.grid(row=0, column=0, padx=0, pady=(40,10))
        self.entrada_monto = customtkinter.CTkEntry(self.columna1, fg_color="grey",placeholder_text_color="aquamarine",placeholder_text="____________________________________________________________________________",font=("Verdana",24), border_width=0, width=350, height=80, corner_radius=55, text_color="aquamarine")
        self.entrada_monto.grid(row=1, column=0, padx=10, pady=10)

        self.label_n_cuotas = customtkinter.CTkLabel(self.columna1, text="N° cuotas",font=("Verdana",24), text_color="white")
        self.label_n_cuotas.grid(row=3, column=0, padx=0, pady=10)
        self.entrada_n_cuotas = customtkinter.CTkEntry(self.columna1,placeholder_text_color="aquamarine", fg_color="grey", placeholder_text="____________________________________________________________________________",font=("Verdana",24),border_width=0, width=350, height=80, corner_radius=55,text_color="aquamarine")
        self.entrada_n_cuotas.grid(row=4, column=0, padx=10, pady=10)
        
        self.label_valor_cuota = customtkinter.CTkLabel(self.columna1, text="Valor de la cuota",font=("Verdana",24), text_color="white")
        self.label_valor_cuota.grid(row=6, column=0, padx=0, pady=10)
        self.entrada_valor_cuota = customtkinter.CTkEntry(self.columna1, fg_color="grey", placeholder_text="____________________________________________________________________________", placeholder_text_color="aquamarine",font=("Verdana",24), border_width=0,width=350, height=80, corner_radius=55, text_color="white")
        self.entrada_valor_cuota.grid(row=7, column=0, padx=10, pady=10)
        
        
        
        
        self.columna2 = customtkinter.CTkFrame(self)
        self.columna2.grid(row=1, column=3)
        
        ### output
        self.label_texto = customtkinter.CTkLabel(self.columna2, text="Préstamos y Cuotificación",font=("Verdana",24), text_color="grey")
        self.label_texto.grid(row=1, column=0, padx=10, pady=10)
        
        
        self.salida_1 = customtkinter.CTkEntry(self.columna2, placeholder_text="____________________________________________________________________________",font=("Verdana",24),border_width=0,width=350, height=80, corner_radius=55, state="disabled")
        self.salida_1.grid(row=3, column=0, padx=10, pady=10)
        
        self.salida_2 = customtkinter.CTkEntry(self.columna2, placeholder_text="____________________________________________________________________________",font=("Verdana",24),border_width=0, width=350, height=80, corner_radius=55, state="disabled")
        self.salida_2.grid(row=5, column=0, padx=10, pady=10)

        self.salida_3 = customtkinter.CTkEntry(self.columna2, placeholder_text="____________________________________________________________________________",font=("Verdana",24),border_width=0, width=350, height=80, corner_radius=55, state="disabled")
        self.salida_3.grid(row=7, column=0, padx=10, pady=10)
       # TODO:AÑADIR PORCENTJEDEINERESEES

        ### botonera
         
        self.columna3 = customtkinter.CTkFrame(self)
        self.columna3.grid(row=1, column=5)
        self.button_prestamos = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Calcular intereses", font=("Verdana", 36), command=self.calcular_interes)
        self.button_prestamos.grid(row=4, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  

        self.button_ayuda = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Ayuda", font=("Verdana", 36))
        self.button_ayuda.grid(row=6, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  
        
        self.button_volver = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Volver", font=("Verdana", 36), command=self.volver)
        self.button_volver.grid(row=8, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)
        
    def calcular_interes(self):
        try:
            monto = float(self.entrada_monto.get())
            n_cuotas = int(self.entrada_n_cuotas.get())
            valor_cuota = float(self.entrada_valor_cuota.get())

            interes_total = (n_cuotas * valor_cuota) - monto
            interes_mensual =  interes_total / n_cuotas

            self.salida_1.configure(state="normal",placeholder_text=f"Total: \n${interes_total:.2f}")
            self.salida_2.configure(state="normal",placeholder_text=f"Mensual: \n ${interes_mensual:.2f}")
            self.label_texto.configure(text="Dinero perdido en Intereses", text_color="grey")

        except ValueError:
            self.label_texto.configure(text="Error: Ingresa valores válidos", text_color="red")
            self.salida_1.configure(placeholder_text="")
            self.salida_2.configure(placeholder_text="")

    def volver(self):
        master = self.master
        self.grid_forget()
        index = IndexFrame(master)
        index.grid(row=1, column=0, columnspan=7, ipady=130, ipadx=230)
            
            
class IndexFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        
        super().__init__(master)
        self.grid_columnconfigure((0, 1,2,3), weight=1)
        self.grid_rowconfigure((0,1 ,2,3,4,5), weight=1)
        
        self.texto_frame = customtkinter.CTkFrame(self)
        self.texto_frame.grid(row=1, column=1,columnspan=2, padx=10, pady=(10, 0), sticky="nsew")
        self.titulo_label = customtkinter.CTkLabel(self.texto_frame, text="Bienvenido", text_color="grey", font=("Verdana", 36))
        self.titulo_label.pack(fill=tk.X, expand=True, padx=0)
        self.text_label = customtkinter.CTkLabel(self.texto_frame, text_color="grey", text="¿Qué deseas calcular ahora?", font=("Verdana", 36))
        self.text_label.pack(fill=tk.X, expand=True, padx=0)
        
        self.button_prestamos = customtkinter.CTkButton(self, corner_radius=45,width=95,  height=95, text="Préstamos", font=("Verdana", 36), command=self.open_prestamos)
        self.button_prestamos.grid(row=4, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  
        
        self.button_inversiones = customtkinter.CTkButton(self, corner_radius=45, width=95,  height=95, text="Inversiones", font=("Verdana", 36), command=self.open_inversiones)
        self.button_inversiones.grid(row=4, column=2, padx=10, pady=10, sticky="ew",  columnspan=1)    
        
        self.button_ayuda = customtkinter.CTkButton(self, corner_radius=45, width=95,  height=95, text="Ayuda", font=("Verdana", 36))
        self.button_ayuda.grid(row=5, column=1, padx=10, pady=10, sticky="ew",  columnspan=1) 
        
        self.button_about = customtkinter.CTkButton(self, corner_radius=45, width=95,  height=95, text="Acerca de", font=("Verdana", 36))
        self.button_about.grid(row=5, column=2, padx=10, pady=10, sticky="ew",   columnspan=1)    
           
        
        
    def open_prestamos(self):
        master = self.master
        self.grid_forget()

        prestamos_frame = PrestamosFrame(master)
        prestamos_frame.grid(row=1, column=0, columnspan=7, ipady=130, ipadx=230)
        
    def open_inversiones(self):
        master = self.master
        self.grid_forget()

        inversiones_frame = InversionesFrame(master)
        inversiones_frame.grid(row=1, column=0, columnspan=7, ipady=130, ipadx=230)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth() -400
        screen_height = self.winfo_screenheight() -200

        self.geometry(f"{screen_width}x{screen_height}")
        self.title("Calculadoras")

        self.create_widgets()
        
    def create_widgets(self):
        container = customtkinter.CTkFrame(self)
        container.pack(fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
            
        self.header = HeaderFrame(container)
        self.header.grid(row=0, column=0, columnspan=6)

        self.index = IndexFrame(container)
        self.index.grid(row=1, column=0, columnspan=6, ipady=130, ipadx=230)
        
      

app = App()
app.iconbitmap(r'C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\favicon.ico')

app.mainloop()

