import customtkinter
import tkinter as tk
from PIL import Image


### INCLUDES  #### estos van en Ventana, asi que se incluyen en todas las vistas #######
class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.image = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\header2.png"),
                                  dark_image=Image.open(r"C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\header2.png"),
                                  size=(1900,170))
        self.image_label = customtkinter.CTkLabel(self, image=self.image, text="",)
        self.image_label.pack(fill=tk.X, expand=True, padx=0, pady=0)
        
class FooterImageFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.image = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\footer.png"),
                                  dark_image=Image.open(r"C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\footer.png"),
                                  size=(1900, 24))
        self.image_label = customtkinter.CTkLabel(self, image=self.image, text="")
        self.image_label.pack(fill=tk.X, expand=True, padx=0, pady=0)
           
############################# VISTAS  #########
# CALCULADORA INVERSIONES  
class InversionesFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1,2,3,4,5,6), weight=1)
        self.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        
        #### INPUT
        self.columna1 = customtkinter.CTkFrame(self)
        self.columna1.grid(row=1, column=1)
        
        self.entrada_monto = customtkinter.CTkEntry(self.columna1, placeholder_text="MONTO DE LA INVERSIÓN",font=("Purisa",24), width=350, height=80, corner_radius=55)
        self.entrada_monto.grid(row=1, column=0, padx=10, pady=10)


        self.entrada_n_cuotas = customtkinter.CTkEntry(self.columna1, placeholder_text="MESES",font=("Purisa",24), width=350, height=80, corner_radius=55)
        self.entrada_n_cuotas.grid(row=4, column=0, padx=10, pady=10)

        self.entrada_valor_cuota = customtkinter.CTkEntry(self.columna1, placeholder_text="RETRNO ANUAL",font=("Purisa",24), width=350, height=80, corner_radius=55)
        self.entrada_valor_cuota.grid(row=7, column=0, padx=10, pady=10)
        
        
        
        
        self.columna2 = customtkinter.CTkFrame(self)
        self.columna2.grid(row=1, column=3)
        
        ### output
        
        self.texto = customtkinter.CTkEntry(self.columna2, placeholder_text="Préstamos y Cuotificación",font=("Purisa",24), width=350, height=80, corner_radius=55, state="disabled")
        self.texto.grid(row=1, column=0, padx=10, pady=10)
        
        self.salida_1 = customtkinter.CTkEntry(self.columna2, placeholder_text="",font=("Purisa",24), width=350, height=80, corner_radius=55, state="disabled")
        self.salida_1.grid(row=3, column=0, padx=10, pady=10)
        
        self.salida_2 = customtkinter.CTkEntry(self.columna2, placeholder_text="",font=("Purisa",24), width=350, height=80, corner_radius=55, state="disabled")
        self.salida_2.grid(row=5, column=0, padx=10, pady=10)

       

        ### botonera
         
        self.columna3 = customtkinter.CTkFrame(self)
        self.columna3.grid(row=1, column=5)
        self.button_prestamos = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Calcular intereses", font=("Purisa", 36), command=self.calcular_interes)
        self.button_prestamos.grid(row=4, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  

        self.button_ayuda = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Ayuda", font=("Purisa", 36))
        self.button_ayuda.grid(row=6, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  
        
        self.button_volver = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Volver", font=("Purisa", 36), command=self.volver)
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
        self.pack_forget()
        index = IndexFrame(master)
        index.pack(fill=tk.X, expand=True)
 
# CALCULADORA PRESTAMOS  
class PrestamosFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1,2,3,4,5,6), weight=1)
        self.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        
        #### INPUT
        self.columna1 = customtkinter.CTkFrame(self, fg_color="white", corner_radius=55)
        self.columna1.grid(row=1, column=1, pady=20)
        self.columna1.grid_columnconfigure(1, weight=1)
        self.columna1.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        self.label_monto = customtkinter.CTkLabel(self.columna1, text="Precio final",font=("Purisa",24), text_color="grey72")
        self.label_monto.grid(row=0, column=0, padx=0,pady=(70,10))
        self.entrada_monto = customtkinter.CTkEntry(self.columna1, fg_color="white",placeholder_text_color="aquamarine",placeholder_text="$ ____________________________________________________________________________",font=("Purisa",44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_monto.grid(row=1, column=0, padx=0, pady=10)

        self.label_n_cuotas = customtkinter.CTkLabel(self.columna1, text="N° cuotas",font=("Purisa",24), text_color="grey72")
        self.label_n_cuotas.grid(row=3, column=0, padx=0, pady=10)
        self.entrada_n_cuotas = customtkinter.CTkEntry(self.columna1,placeholder_text_color="aquamarine", fg_color="white", placeholder_text="____________________________________________________________________________",font=("Purisa",44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_n_cuotas.grid(row=4, column=0, padx=0, pady=10)
        
        self.label_valor_cuota = customtkinter.CTkLabel(self.columna1, text="Valor de la cuota",font=("Purisa",24), text_color="grey72")
        self.label_valor_cuota.grid(row=6, column=0, padx=0, pady=10)
        self.entrada_valor_cuota = customtkinter.CTkEntry(self.columna1, fg_color="white", placeholder_text="$ ____________________________________________________________________________", placeholder_text_color="aquamarine",font=("Purisa",44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_valor_cuota.grid(row=7, column=0, padx=10, pady=(10,70))
        
        
        
        
        self.columna2 = customtkinter.CTkFrame(self, fg_color="snow", corner_radius=55)
        self.columna2.grid(row=1, column=3)
        self.columna2.grid_columnconfigure(1, weight=1)
        self.columna2.grid_rowconfigure((0,1 ,2), weight=1)
        
        ### output
        self.label_salida1 = customtkinter.CTkLabel(self.columna2, text="Diferencia total",font=("Purisa",24), text_color="grey72")
        self.label_salida1.grid(row=1, column=0, padx=0,pady=(70,10))
                
        self.salida_1 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1", placeholder_text="$ ____________________________________________________________________________",font=("Purisa",44),border_width=0,width=350, height=20, corner_radius=55)
        self.salida_1.grid(row=3, column=0, padx=20, pady=10)
        
        
        self.label_salida2 = customtkinter.CTkLabel(self.columna2, text="Pérdida mensual",font=("Purisa",24), text_color="grey72")
        self.label_salida2.grid(row=4, column=0, padx=0,pady=(70,10))
        
        self.salida_2 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1",placeholder_text="$ ____________________________________________________________________________",font=("Purisa",44),border_width=0, width=350, height=20, corner_radius=55)
        self.salida_2.grid(row=5, column=0, padx=20, pady=10)

        
        
        self.label_salida3 = customtkinter.CTkLabel(self.columna2, text="Porcentaje intereses",font=("Purisa",24), text_color="grey72")
        self.label_salida3.grid(row=6, column=0, padx=0,pady=(70,10))
        
        self.salida_3 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1", placeholder_text="% ____________________________________________________________________________",font=("Purisa",44),border_width=0, width=350, height=20, corner_radius=55)
        self.salida_3.grid(row=7, column=0, padx=20, pady=(10,70))
       # TODO:AÑADIR PORCENTJEDEINERESEES

        ### botonera
         
        self.columna3 = customtkinter.CTkFrame(self, fg_color="transparent", corner_radius=55)
        self.columna3.grid(row=1, column=5, pady=40)
        
        self.label_texto = customtkinter.CTkLabel(self.columna3, text="Préstamos \n y \n Cuotificación",font=("Purisa",44), text_color="white")
        self.label_texto.grid(row=3, column=1, padx=10,pady=(0,10))
        
        
        self.button_prestamos = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Calcular intereses", font=("Purisa", 36), command=self.calcular_interes)
        self.button_prestamos.grid(row=4, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  

        self.button_ayuda = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Ayuda", font=("Purisa", 36))
        self.button_ayuda.grid(row=6, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  
        
        self.button_volver = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Volver", font=("Purisa", 36), command=self.volver)
        self.button_volver.grid(row=8, column=1, padx=10, pady=(10,0), sticky="ew",  columnspan=1)
        
    def calcular_interes(self):
        try:
            monto = float(self.entrada_monto.get())
            n_cuotas = int(self.entrada_n_cuotas.get())
            valor_cuota = float(self.entrada_valor_cuota.get())

            interes_total = (n_cuotas * valor_cuota) - monto
            interes_mensual =  interes_total / n_cuotas

            self.salida_1.configure(state="normal",placeholder_text=f"$ {interes_total:.2f}")
            self.salida_2.configure(state="normal",placeholder_text=f"$ {interes_mensual:.2f}")
            self.label_texto.configure(text="Préstamos \n y \n Cuotificación", text_color="DodgerBlue2")

        except ValueError:
            self.label_texto.configure(text="Ingresa valores válidos", text_color="red")

    def volver(self):
        master = self.master
        self.pack_forget()
        index = IndexFrame(master)
        index.pack(fill=tk.X, expand=True)

           
## INICIO   
class IndexFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1 ,2), weight=1)
        
        self.texto_frame = customtkinter.CTkFrame(self, fg_color="azure", corner_radius=55)
        self.texto_frame.grid(row=0, column=0, padx=10, pady=80)
        self.texto_frame.grid_columnconfigure((0, 1,2,3), weight=1)
        self.texto_frame.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        self.titulo_label = customtkinter.CTkLabel(self.texto_frame, text="Bienvenido", text_color="grey72", font=("Purisa", 36))
        self.titulo_label.grid(row=0, column=1, padx=170, pady=(70,10), sticky="ew",  columnspan=2)  
        
        self.text_label = customtkinter.CTkLabel(self.texto_frame, text_color="grey72", text="¿Qué deseas calcular ahora?", font=("Purisa", 26))
        self.text_label.grid(row=1, column=1, padx=70, pady=(10,60), sticky="ew",  columnspan=2)  
        
        self.button_prestamos = customtkinter.CTkButton(self.texto_frame, corner_radius=45,width=95,  height=95, text="Préstamos", font=("Purisa", 36), command=self.open_prestamos)
        self.button_prestamos.grid(row=4, column=1, padx=70, pady=0, sticky="ew",  columnspan=1)  
        
        self.button_inversiones = customtkinter.CTkButton(self.texto_frame, corner_radius=45, width=95,  height=95, text="Inversiones", font=("Purisa", 36), command=self.open_inversiones)
        self.button_inversiones.grid(row=4, column=2, padx=70, pady=0, sticky="ew",  columnspan=1)    
        
        self.button_ayuda = customtkinter.CTkButton(self.texto_frame, corner_radius=45, width=95,  height=95, text="Salir", font=("Purisa", 36), command=self.salir)
        self.button_ayuda.grid(row=5, column=1, padx=70, pady=(10,70), sticky="ew",  columnspan=1) 
        
        self.button_about = customtkinter.CTkButton(self.texto_frame, corner_radius=45, width=95,  height=95, text="Acerca de", font=("Purisa", 36), command=self.open_acercade)
        self.button_about.grid(row=5, column=2, padx=70, pady=(10,70), sticky="ew",   columnspan=1)
        self.toplevel_window = None
        
    def salir(self):
        master = self.master
        self.pack_forget() 
        master.master.destroy()
        
    def open_acercade(self):
        master = self.master
        self.pack_forget()
        acerca_de_frame = AcercaDeFrame(master)
        acerca_de_frame.pack(fill=tk.BOTH, expand=True, padx=120)
        
    def open_prestamos(self):
        master = self.master
        self.pack_forget()
        prestamos_frame = PrestamosFrame(master)
        prestamos_frame.pack(fill=tk.BOTH, expand=True)
        
    def open_inversiones(self):
        master = self.master
        self.pack_forget()

        inversiones_frame = InversionesFrame(master)
        inversiones_frame.pack(fill=tk.BOTH, expand=True)


## ABOUT
class AcercaDeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1,2), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        
        self.columna1 = customtkinter.CTkFrame(self, fg_color="azure", corner_radius=25)
        self.columna1.grid(row=0, column=0, pady=10, padx=5)
        
        self.columna2 = customtkinter.CTkFrame(self, fg_color="snow", corner_radius=25)
        self.columna2.grid(row=0, column=1, pady=10, padx=5)
        
        self.columna3 = customtkinter.CTkFrame(self, fg_color="azure", corner_radius=25)
        self.columna3.grid(row=0, column=2, pady=10, padx=5)
        
        
        
        self.label_texto = customtkinter.CTkLabel(self.columna1, text="Calculadoras Financieras",font=("Purisa",24), text_color="turquoise1")
        self.label_texto.grid(row=0, column=0, padx=10, pady=10)
        
        self.texto_largo = customtkinter.CTkLabel(self.columna1, fg_color="transparent", text="Bienvenido a la Aplicación Financiera, \n tu compañero confiable en el mundo de las finanzas personales.\n Nuestra aplicación está diseñada para brindarte herramientas poderosas que \n te ayudarán a tomar decisiones financieras informadas y maximizar tus recursos.", text_color="grey72", font=("Purisa", 15))
        self.texto_largo.grid(row=1, column=0, padx=10, pady=10)  
        
               
        
        
        self.subtitulo_label0 = customtkinter.CTkLabel(self.columna2,fg_color="transparent",  text="Calculadora de Cuotas y Pérdida en Intereses", text_color="turquoise1", font=("Purisa", 16))
        self.subtitulo_label0.grid(row=0, column=0, padx=10, pady=10)  
        
        self.texto_largo2 = customtkinter.CTkLabel(self.columna2, fg_color="transparent", text="Diseñada para aquellos que buscan administrar préstamos o financiamientos. \n Con esta herramienta, puedes calcular cuotas mensuales, plazos y,\n lo más importante, el valor de pérdida en intereses a lo largo del tiempo.\n Visualiza claramente cómo tus decisiones financieras afectarán \ntu presupuesto a largo plazo y toma decisiones inteligentes.", text_color="grey72", font=("Purisa", 16))
        self.texto_largo2.grid(row=1, column=0, padx=10, pady=10)  
        
        
        
        
        self.subtitulo_label = customtkinter.CTkLabel(self.columna3,fg_color="transparent",  text="Calculadora de Inversiones y Valor de Retorno", text_color="aquamarine", font=("Purisa", 10))
        self.subtitulo_label.grid(row=0, column=0, padx=10, pady=10)  
        
        
        self.texto_largo3 = customtkinter.CTkLabel(self.columna3, fg_color="transparent", text="Pensada para quienes desean invertir y hacer crecer su dinero.\n Con esta herramienta, podrás calcular el valor de retorno de tus inversiones, lo que te permitirá planificar tu futuro financiero con confianza. \n Comprende cómo tus inversiones pueden crecer con el tiempo y toma decisiones estratégicas para alcanzar tus metas financieras.", text_color="grey72", font=("Purisa", 10))
        self.texto_largo3.grid(row=1, column=0, padx=10,  pady=10) 
        
        
        
        ### botonera       
        
        self.button_volver = customtkinter.CTkButton(self, corner_radius=45, width=95,  height=95, text="Volver", font=("Purisa", 16), command=self.volver)
        self.button_volver.grid(row=2, column=1)
        
    def volver(self):
        master = self.master
        self.pack_forget()
        index = IndexFrame(master)
        index.pack(fill=tk.BOTH, expand=True)
         

################## CLASE PRINCIPAL . APLICACIÓN ###############

## Ventana
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth() -400
        screen_height = self.winfo_screenheight() -200

        self.geometry(f"{screen_width}x{screen_height}")
        self.title("Calculadoras")
        self.iconbitmap(r'C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\redondo.ico')
        self.wm_iconbitmap(r'C:\Users\merce\OneDrive\Documentos\code\projects\calcul\tkinter\calc\redondo.ico')

        self.create_widgets()
        
    def create_widgets(self):
        container = customtkinter.CTkFrame(self, fg_color="azure")
        container.pack(fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
            
        self.header = HeaderFrame(container)
        self.header.pack(fill=tk.X, expand=True)

        self.index = IndexFrame(container)
        self.index.pack(fill=tk.BOTH, expand=True)
        
        
        
        self.footerline = FooterImageFrame(container)
        self.footerline.pack(fill=tk.X, expand=True, side="bottom")
        
        

### se crea una instancia de la clase App:
app = App()
# le damos play:
app.mainloop()

# TODO PROBAR EN ABOUT COLOCARLOS LABELS EN SUPROPIO FRAME