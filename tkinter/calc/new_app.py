import customtkinter
import tkinter as tk
from PIL import Image

## FONT VARIABLES
h1_font = "Franklin Gothic Medium"
h2_font = h1_font
boton_font = h1_font
main_text_font ="Verdana"

### TODO : anular siguiente o previo boton en navegaciones de ayuda en caso de que no exista prev

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
        self.columna1 = customtkinter.CTkFrame(self, fg_color="white", corner_radius=55)
        self.columna1.grid(row=1, column=1, pady=20)
        self.columna1.grid_columnconfigure(1, weight=1)
        self.columna1.grid_rowconfigure((0,1 ,2), weight=1)
        
        self.label_monto = customtkinter.CTkLabel(self.columna1, text="Monto a invertir",font=(main_text_font,24), text_color="grey72")
        self.label_monto.grid(row=0, column=0, padx=0,pady=(70,10))
        self.entrada_monto = customtkinter.CTkEntry(self.columna1, fg_color="white",placeholder_text_color="aquamarine",placeholder_text="$ ____________________________________________________________________________",font=(main_text_font,44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_monto.grid(row=1, column=0, padx=0, pady=10)


        self.label_n_cuotas = customtkinter.CTkLabel(self.columna1, text="N° meses",font=(main_text_font,24), text_color="grey72")
        self.label_n_cuotas.grid(row=3, column=0, padx=0, pady=10)
        self.entrada_n_cuotas = customtkinter.CTkEntry(self.columna1,placeholder_text_color="aquamarine", fg_color="white", placeholder_text="____________________________________________________________________________",font=(main_text_font,44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_n_cuotas.grid(row=4, column=0, padx=0, pady=10)

        self.label_valor_cuota = customtkinter.CTkLabel(self.columna1, text="Tasa de interés",font=(main_text_font,24), text_color="grey72")
        self.label_valor_cuota.grid(row=6, column=0, padx=0, pady=10)
        self.entrada_tasa = customtkinter.CTkEntry(self.columna1, fg_color="white", placeholder_text="% ____________________________________________________________________________", placeholder_text_color="aquamarine",font=(main_text_font,44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_tasa.grid(row=7, column=0, padx=10, pady=(10,70))
        
        
        
        ############ COLUMNA 2 - RESULTADOS
        self.columna2 = customtkinter.CTkFrame(self, fg_color="snow", corner_radius=55)
        self.columna2.grid(row=1, column=3)
        self.columna2.grid_columnconfigure(1, weight=1)
        self.columna2.grid_rowconfigure((0,1 ,2), weight=1)
        
        ### output
        
        self.label_salida1 = customtkinter.CTkLabel(self.columna2, text="Retorno anual",font=(main_text_font,24), text_color="grey72")
        self.label_salida1.grid(row=1, column=0, padx=0,pady=(70,10))
                
        self.salida_1 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1", placeholder_text="$ ____________________________________________________________________________",font=(main_text_font,44),border_width=0,width=350, height=20, corner_radius=55)
        self.salida_1.grid(row=3, column=0, padx=20, pady=10)
        
        
        self.label_salida2 = customtkinter.CTkLabel(self.columna2, text="Retorno del periodo",font=(main_text_font,24), text_color="grey72")
        self.label_salida2.grid(row=4, column=0, padx=0,pady=(70,10))
        
        self.salida_2 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1",placeholder_text="$ ____________________________________________________________________________",font=(main_text_font,44),border_width=0, width=350, height=20, corner_radius=55)
        self.salida_2.grid(row=5, column=0, padx=20, pady=10)

        
        
        self.label_salida3 = customtkinter.CTkLabel(self.columna2, text="ALGO",font=(main_text_font,24), text_color="grey72")
        self.label_salida3.grid(row=6, column=0, padx=0,pady=(70,10))
        
        self.salida_3 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1", placeholder_text="% ____________________________________________________________________________",font=(main_text_font,44),border_width=0, width=350, height=20, corner_radius=55)
        self.salida_3.grid(row=7, column=0, padx=20, pady=(10,70))
       # TODO:AÑADIR ALGO

       

        ### botonera
         
        self.columna3 = customtkinter.CTkFrame(self, fg_color="transparent", corner_radius=55)
        self.columna3.grid(row=1, column=5, pady=40)
        
        self.label_texto = customtkinter.CTkLabel(self.columna3, text="Inversiones",font=(h1_font,44), text_color="white")
        self.label_texto.grid(row=3, column=1, padx=10,pady=10)
        
        
        self.button_prestamos = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Calcular ganancias", font=(boton_font, 36), command=self.calcular_ganancia)
        self.button_prestamos.grid(row=4, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  

        self.button_ayuda = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Ayuda", font=(boton_font, 36), command=self.ayuda)
        self.button_ayuda.grid(row=6, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  
        
        self.button_volver = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Volver", font=(boton_font, 36), command=self.volver)
        self.button_volver.grid(row=8, column=1, padx=10, pady=(10,0), sticky="ew",  columnspan=1)
        
    def ayuda(self):
        self.pack_forget()
        new_content = [
        {
            "titulo": "FAQs Calculadora Inversiones",
            "texto": "Aquí encontrarás una serie de arespuestas a las preguntas frecuentes. \n Navega con los botones 'anterior' y 'siguiente' para leer los textos."
        },
        {
            "titulo": "Custom Title 2",
            "texto": "Custom Text 2"
        },
        ]
        
        ayuda = AyudaBaseFrame(self.master, custom_content=new_content, previous_frame=self)
        ayuda.pack(fill=tk.X, expand=True)
        
            
    def calcular_ganancia(self):
        try:
            monto_inicial = float(self.entrada_monto.get())
            tasa_interes = float(self.entrada_tasa.get())
            periodo_meses = float(self.entrada_n_cuotas.get())

            tasa_decimal = tasa_interes / 100
            retorno_anual = tasa_decimal * monto_inicial
            retorno_periodo = (periodo_meses * retorno_anual) / 12

            self.salida_1.configure(placeholder_text=f"$ {retorno_anual:.2f}")
            self.salida_2.configure(placeholder_text=f"$ {retorno_periodo:.2f}")

        except ValueError:
            self.label_texto.configure(text="Error: Ingresa valores válidos", text_color="red")    
   
                   
        
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
        
        
        self.label_monto = customtkinter.CTkLabel(self.columna1, text="Precio final",font=(main_text_font,24), text_color="grey72")
        self.label_monto.grid(row=0, column=0, padx=0,pady=(70,10))
        self.entrada_monto = customtkinter.CTkEntry(self.columna1, fg_color="white",placeholder_text_color="aquamarine",placeholder_text="$ ____________________________________________________________________________",font=(main_text_font,44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_monto.grid(row=1, column=0, padx=0, pady=10)

        self.label_n_cuotas = customtkinter.CTkLabel(self.columna1, text="N° cuotas",font=(main_text_font,24), text_color="grey72")
        self.label_n_cuotas.grid(row=3, column=0, padx=0, pady=10)
        self.entrada_n_cuotas = customtkinter.CTkEntry(self.columna1,placeholder_text_color="aquamarine", fg_color="white", placeholder_text="____________________________________________________________________________",font=(main_text_font,44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_n_cuotas.grid(row=4, column=0, padx=0, pady=10)
        
        self.label_valor_cuota = customtkinter.CTkLabel(self.columna1, text="Valor de la cuota",font=(main_text_font,24), text_color="grey72")
        self.label_valor_cuota.grid(row=6, column=0, padx=0, pady=10)
        self.entrada_valor_cuota = customtkinter.CTkEntry(self.columna1, fg_color="white", placeholder_text="$ ____________________________________________________________________________", placeholder_text_color="aquamarine",font=(main_text_font,44), border_width=0, width=450, height=100, corner_radius=55, text_color="aquamarine")
        self.entrada_valor_cuota.grid(row=7, column=0, padx=10, pady=(10,70))
        
        
        
                ############ COLUMNA 2 - RESULTADOS

        self.columna2 = customtkinter.CTkFrame(self, fg_color="snow", corner_radius=55)
        self.columna2.grid(row=1, column=3)
        self.columna2.grid_columnconfigure(1, weight=1)
        self.columna2.grid_rowconfigure((0,1 ,2), weight=1)
        
        ### output
        self.label_salida1 = customtkinter.CTkLabel(self.columna2, text="Diferencia total",font=(main_text_font,24), text_color="grey72")
        self.label_salida1.grid(row=1, column=0, padx=0,pady=(70,10))
                
        self.salida_1 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1", placeholder_text="$ ____________________________________________________________________________",font=(main_text_font,44),border_width=0,width=350, height=20, corner_radius=55)
        self.salida_1.grid(row=3, column=0, padx=20, pady=10)
        
        
        self.label_salida2 = customtkinter.CTkLabel(self.columna2, text="Pérdida mensual",font=(main_text_font,24), text_color="grey72")
        self.label_salida2.grid(row=4, column=0, padx=0,pady=(70,10))
        
        self.salida_2 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1",placeholder_text="$ ____________________________________________________________________________",font=(main_text_font,44),border_width=0, width=350, height=20, corner_radius=55)
        self.salida_2.grid(row=5, column=0, padx=20, pady=10)

        
        
        self.label_salida3 = customtkinter.CTkLabel(self.columna2, text="Porcentaje intereses",font=(main_text_font,24), text_color="grey72")
        self.label_salida3.grid(row=6, column=0, padx=0,pady=(70,10))
        
        self.salida_3 = customtkinter.CTkEntry(self.columna2, fg_color="snow",placeholder_text_color="turquoise1", placeholder_text="% ____________________________________________________________________________",font=(main_text_font,44),border_width=0, width=350, height=20, corner_radius=55)
        self.salida_3.grid(row=7, column=0, padx=20, pady=(10,70))
       # TODO:AÑADIR PORCENTJEDEINERESEES

        ### botonera
         
        self.columna3 = customtkinter.CTkFrame(self, fg_color="transparent", corner_radius=55)
        self.columna3.grid(row=1, column=5, pady=40)
        
        self.label_texto = customtkinter.CTkLabel(self.columna3, text="Préstamos \n y \n Cuotificación",font=(h1_font,44), text_color="white")
        self.label_texto.grid(row=3, column=1, padx=10,pady=(0,10))
        
        
        self.button_prestamos = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Calcular intereses", font=(boton_font, 36), command=self.calcular_interes)
        self.button_prestamos.grid(row=4, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  

        self.button_ayuda = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Ayuda", font=(boton_font, 36), command=self.ayuda)
        self.button_ayuda.grid(row=6, column=1, padx=10, pady=10, sticky="ew",  columnspan=1)  
        
        self.button_volver = customtkinter.CTkButton(self.columna3, corner_radius=45, width=95,  height=95, text="Volver", font=(boton_font, 36), command=self.volver)
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
        
    def ayuda(self):
        self.pack_forget()
        new_content = [
        {
            "titulo": "FAQs Calculadora préstamos",
            "texto": "Aquí encontrarás una serie de arespuestas a las preguntas frecuentes. \n Navega con los botones 'anterior' y 'siguiente' para leer los textos."
        },
        {
            "titulo": "Custom Title 2",
            "texto": "Custom Text 2"
        },
        ]
        
        ayuda = AyudaBaseFrame(self.master, custom_content=new_content, previous_frame=self)
        ayuda.pack(fill=tk.X, expand=True)
           
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
        
        
        self.titulo_label = customtkinter.CTkLabel(self.texto_frame, text="Bienvenido", text_color="grey72", font=(h1_font, 36))
        self.titulo_label.grid(row=0, column=1, padx=170, pady=(70,10), sticky="ew",  columnspan=2)  
        
        self.text_label = customtkinter.CTkLabel(self.texto_frame, text_color="grey72", text="¿Qué deseas calcular ahora?", font=(h2_font, 26))
        self.text_label.grid(row=1, column=1, padx=70, pady=(10,60), sticky="ew",  columnspan=2)  
        
        self.button_prestamos = customtkinter.CTkButton(self.texto_frame, corner_radius=45,width=125,  height=75, text="Préstamos", font=(boton_font, 36), command=self.open_prestamos)
        self.button_prestamos.grid(row=4, column=1, padx=70, pady=0, sticky="ew",  columnspan=1)  
        
        self.button_inversiones = customtkinter.CTkButton(self.texto_frame, corner_radius=45, width=125,  height=75, text="Inversiones", font=(boton_font, 36), command=self.open_inversiones)
        self.button_inversiones.grid(row=4, column=2, padx=70, pady=0, sticky="ew",  columnspan=1)    
        
        self.button_ayuda = customtkinter.CTkButton(self.texto_frame, corner_radius=45, width=125,  height=75, text="Salir", font=(boton_font, 36), command=self.salir)
        self.button_ayuda.grid(row=5, column=1, padx=70, pady=(10,70), sticky="ew",  columnspan=1) 
        
        self.button_about = customtkinter.CTkButton(self.texto_frame, corner_radius=45, width=125,  height=75, text="Acerca de", font=(boton_font, 36), command=self.open_acercade)
        self.button_about.grid(row=5, column=2, padx=70, pady=(10,70), sticky="ew",   columnspan=1)
        
    def salir(self):
        master = self.master
        self.pack_forget() 
        master.master.destroy()
        
    def open_acercade(self):
        master = self.master
        self.pack_forget()
        acerca_de_frame = AcercaDeFrame(master)
        acerca_de_frame.pack(fill=tk.BOTH, expand=True)
        
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
        self.grid_columnconfigure((0,1 ,2), weight=1)
        self.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        ### contenedor de los textos
        self.texto_frame = customtkinter.CTkFrame(self, fg_color="azure", corner_radius=45)
        self.texto_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        self.texto_frame.grid_columnconfigure((0, 1,2,3), weight=1)
        self.texto_frame.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        
        ### textos dinámicos
        self.titulo_label = customtkinter.CTkLabel(self.texto_frame, text="Calculadoras Financieras Python App", text_color="grey72", font=(h2_font, 36))
        self.titulo_label.grid(row=0, column=1, padx=170, pady=(70,10), sticky="ew",  columnspan=2)  
        
        self.text_label = customtkinter.CTkLabel(self.texto_frame, text_color="grey72", text="Aquí encontrarás información sobre el proyecto. \n Navega entre los diferentes textos con los botones 'anterior' y 'siguiente'.", font=(main_text_font, 26))
        self.text_label.grid(row=1, column=1, padx=70, pady=(10,60), sticky="ew",  columnspan=2)  
        ###
        
        
        
        # naveegacion entre los textos

        self.current_content_index = 0

        
        self.botonera = customtkinter.CTkFrame(self, fg_color="transparent")
        self.botonera.grid(row=1, column=0, padx=5, pady=0, columnspan=3)
        self.botonera.grid_columnconfigure((0, 1,2,3), weight=1)
        self.botonera.grid_rowconfigure((0,1 ,2), weight=1)
        
        
        self.button_prev = customtkinter.CTkButton(self.botonera, corner_radius=75,width=75,  height=70, text="Anterior <", font=(boton_font, 26), command=self.prev_text)
        self.button_prev.grid(row=0, column=0, padx=70, pady=10, sticky="ew",  columnspan=1)  
        
        self.button_next = customtkinter.CTkButton(self.botonera, corner_radius=75, width=75,  height=70, text="> Siguiente", font=(boton_font, 26), command=self.next_text)
        self.button_next.grid(row=0, column=3, padx=70, pady=10, sticky="ew",  columnspan=1)    
        
        
        self.button_volver = customtkinter.CTkButton(self, corner_radius=45, width=95,  height=95, text="Volver", font=(boton_font, 36), command=self.volver)
        self.button_volver.grid(row=4, column=0, columnspan=3, pady=(0,20))
        
        
        #### anadir las páginas que sean necesarias
        self.content = [
            {   # pagina 1
                "titulo": "Calculadoras Financieras Python App",
                "texto": "Aquí encontrarás información sobre el proyecto.\n Navega entre los diferentes textos con los botones 'anterior' y 'siguiente'."
            },
            {   # pagina 2
                "titulo": "Next Title",
                "texto": "This is the next content to display."
            },"""
            ,
            { # pagina 3
                "titulo": "Next Title",
                "texto": "This is the next content to display."
            },
            { # pagina 2
                "titulo": "Next Title",
                "texto": "This is the next content to display."
            },
            { # pagina 2
                "titulo": "Next Title",
                "texto": "This is the next content to display."
            },
            
            { # pagina 2
                "titulo": "Next Title",
                "texto": "This is the next content to display."
            },
            { # pagina 2
                "titulo": "Next Title",
                "texto": "This is the next content to display."
            },
            
            """
        ]

        self.update_content()

    def update_content(self):
        content_data = self.content[self.current_content_index]
        self.titulo_label.configure(text=content_data["titulo"])
        self.text_label.configure(text=content_data["texto"])

    def prev_text(self):
        if self.current_content_index > 0:
            self.current_content_index -= 1
            self.update_content()

    def next_text(self):
        if self.current_content_index < len(self.content) - 1:
            self.current_content_index += 1
            self.update_content()
    
    def volver(self):
        master = self.master
        self.pack_forget()
        index = IndexFrame(master)
        index.pack(fill=tk.X, expand=True)
        
## como las otras ventanas también tienen su propia sección de ayuda, vamos a usarla de modelo, creamos una clase base heredando de la ventana de acercade general, y le pasamos las variables necesarias para el correcto funcionamiento de cada caso específico        
class AyudaBaseFrame(AcercaDeFrame):
    def __init__(self, master, custom_content, previous_frame):
        super().__init__(master)

        self.content = custom_content

        self.current_content_index = 0
        
        self.update_content()
        
        self.previous_frame = previous_frame

    def volver(self):
        if self.previous_frame:
            self.pack_forget()
            self.previous_frame.pack(fill=tk.X, expand=True)
     

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
        
        # CABECERA  -fijo
        self.header = HeaderFrame(container)
        self.header.pack(fill=tk.X, expand=True)

        ### BODY - dinámico
        #  esta es la parte que vamos a poblar dinámicamente
        # desempaquetando (ver el método pack en la manifestación de la instancia de la clase)
        self.index = IndexFrame(container)
        self.index.pack(fill=tk.BOTH, expand=True)
        ###
        
        # FOOTER -fijo
        self.footerline = FooterImageFrame(container)
        self.footerline.pack(fill=tk.X, expand=True, side="bottom")
    
### se crea una instancia de la clase App:
app = App()
# le damos play:
app.mainloop()

