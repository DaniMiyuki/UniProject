import tkinter as tk
from functools import partial

# Funcao que cria a janela de exibicao
def create_window():
    # Funcao interna (closures) para exibir 予定
    def show_schedule(schedule):
        def inner():
            text_schedule.config(text=schedule)
        return inner
    
    # Decorator para estilizar os botoes
    def estilizar_botao(func):
        def decorator(button):
            def wrapper():
                show_schedule(func())()
            button.config(command=wrapper, relief="raised", padx=10, pady=5)
        return decorator
    
    # Funcoes para obter 予定
    def get_schedule_Monday(monday):
        monday = {
            "5:00" : "alongamento",
            "5:30" : "Coffee and News",
            "19:00": "Dinner and Bath",
            "20:00": "Program Course",
            "21:00": "Classes"    
        }
        return monday
    def get_schedule_Tuesday(tuesday):
        tuesday = {
            "5:00" : "alongamento",
            "5:30" : "Coffee and News",
            "19:00": "Dinner and Bath",
            "20:00": "English Course",
            "21:00": "Classes"  
        }
        return tuesday
    def get_schedule_Wednesday(wednesday):
        wednesday = {
            "5:00" : "alongamento",
            "5:30" : "Coffee and News",
            "19:00": "Dinner and Bath",
            "20:00": "Program Course",
            "21:00": "Classes"
        }
        return wednesday
    def get_schedule_Thursday(thursday):
        thursday = {
            "5:00" : "alongamento",
            "5:30" : "Coffee and News",
            "19:00": "Dinner and Bath",
            "20:00": "Program Course",
            "21:00": "Classes" 
        }
        return thursday
    def get_schedule_Friday(friday):
        friday = {
            "5:00" : "alongamento",
            "5:30" : "Coffee and News",
            "19:00": "Dinner and Bath",
            "20:00": "Program Course",
            "21:00": "Classes"         
        }
        return friday
    def get_schedule_Saturday(saturday):
        saturday = {
            "5:00" : "alongamento",
            "5:30" : "Coffee and News",
            "6:30" : "Classes",
            "9:30" : "Break",
            "10:00": "Japanese Course",
            "11:00": "Lunch",
            "13:00": "Japanese Course",
            "15:00": "Classes",
            "18:00": "Dinner and Bath",
            "20:00": "Program Course",
            "21:00": "Classes"     
        }
        return saturday
    def get_schedule_Sunday(sunday):
        sunday = {
            "5:00" : "alongamento",
            "5:30" : "Coffee and News",
            "6:30" : "Classes",
            "9:30" : "Break",
            "10:00": "Japanese Course",
            "11:00": "Lunch",
            "13:00": "Japanese Course",
            "15:00": "Classes",
            "18:00": "Dinner and Bath",
            "20:00": "Program Course",
            "21:00": "Classes"   
        }
        return sunday
    

    # Criacao do window
    window = tk.Tk()
    window.title("Miyuu's Schedule")

    # Button Monday
    button_monday = tk.Button(window, text="Monday")
    button_monday.pack(pady=10)
    estilizar_botao(get_schedule_Monday)(button_monday)

    # Button Tuesday
    button_tuesday = tk.Button(window, text="Tuesday")
    button_tuesday.pack(pady=10)
    estilizar_botao(get_schedule_Tuesday)(button_tuesday)

    # Button Wednesday
    button_wednesday = tk.Button(window, text="Wednesday")
    button_wednesday.pack(pady=10)
    estilizar_botao(get_schedule_Wednesday)(button_wednesday)

    # Button Thursday
    button_thursday = tk.Button(window, text="Thursday")
    button_thursday.pack(pady=10)
    estilizar_botao(get_schedule_Thursday)(button_thursday)

    # Button Friday
    button_friday = tk.Button(window, text="Friday")
    button_friday.pack(pady=10)
    estilizar_botao(get_schedule_Friday)(button_friday)

    # Button Saturday
    button_saturday = tk.Button(window, text="Saturday")
    button_saturday.pack(pady=10)
    estilizar_botao(get_schedule_Saturday)(button_saturday)

    # Button Sunday
    button_sunday = tk.Button(window, text="Sunday")
    button_sunday.pack(pady=10)
    estilizar_botao(get_schedule_Sunday)(button_sunday)

    # Rotulo para exibir o schedule
    text_schedule =tk.Label(window, text="select a weekday!!!")
    text_schedule.pack(pady=20)


    # Execucao do Window
    window.mainloop()

# Chama a funcao para criar a janela
create_window()