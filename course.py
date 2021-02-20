import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from math import *
#from ctypes  import windll
from tkinter import messagebox
from tkinter import filedialog

def window():
    root.resizable(False,False)
    #root.overrideredirect(1)
    #width  = int(windll.user32.GetSystemMetrics(0)*0.6)
    #height = int(windll.user32.GetSystemMetrics(1)*0.6)

    width = 1152
    height = 648
    
    root.geometry(str(width)+"x"+str(height))
    root["bg"] = "#A9A9A9"
    root.title("Прогнозирование трудоемкости производста 1 т цемента на основе трендовой модели")

    #Основные фреймы
    data_frame = tk.Frame(root,width = int(width * 0.7), height = height, bg = "#2F4F4F")
    analyze_frame = tk.Frame(root,width = int(width * 0.7), height = height, bg = "#2F4F4F")
    guide_frame_1 = tk.Frame(root,width = int(width * 0.7), height = height, bg = "#2F4F4F")
    guide_frame_2 = tk.Frame(root,width = int(width * 0.7), height = height, bg = "#2F4F4F")
    guide_frame_3 = tk.Frame(root,width = int(width * 0.7), height = height, bg = "#2F4F4F")
    main_frame = tk.Frame(root,width = int(width * 0.7), height = height,   bg = "#2F4F4F")

    #Список фреймов
    frames = [data_frame, analyze_frame, main_frame, guide_frame_1, guide_frame_2, guide_frame_3]

    #------------------------------------------------Меню кнопок-------------------------------------------------#
    button_menu = tk.Frame(root,width = int(width * 0.2), height = height, bg = "#2F4F4F").place(relx = 0, rely = 0) 
    
    button_names = ["Ввод данных", "Анализ", "Руководство", "О программе", "Выход"]

    #Кнопки
    button_data = tk.Button(button_menu, text = button_names[0], width = 15 , height = 2, bg = "#778899", font = "Times, 14",
                            command = lambda: ShowFrame(data_frame, frames)).place(relx = 0.02, rely = 0.025)
    
    button_analyze = tk.Button(button_menu, text = button_names[1], width = 15 , height = 2, bg = "#778899", font = "Times, 14",
                            command = lambda: analyze(data, analyze_frame, frames, flag, output_labels)).place(relx = 0.02, rely = 0.175)
    
    button_info = tk.Button(button_menu, text = button_names[2], width = 15 , height = 2, bg = "#778899", font = "Times, 14",
                            command = lambda: ShowFrame(guide_frame_1, frames)).place(relx = 0.02, rely = 0.33)
    
    button_guide = tk.Button(button_menu, text = button_names[3], width = 15 , height = 2, bg = "#778899", font = "Times, 14",
                            command = lambda: ShowFrame(main_frame, frames)).place(relx = 0.02, rely = 0.69)
    
    button_exit = tk.Button(button_menu, text = button_names[4], width = 15 , height = 2, bg = "#778899", font = "Times, 14",
                            command = lambda: root.destroy()).place(relx = 0.02, rely = 0.85)

    #------------------------------------------Фрейм ввода данных-----------------------------------------------#    

    data = list()               #Данные трудоемкости производства
    input_fields = list()       #Количество полей ввода
    labels = list()             #Количество надписей во фрейме ввода данных
    output_labels = list()
    flag = [0]

    frame_title = tk.Label(data_frame, text = "Трудоемкость производства 1 т цемента по месяцам",
                        bg = "#2F4F4F", fg = "white", font = "Times, 14").place(relx = 0.20, rely = 0.01)
    
    for i in range(6):
        label = tk.Label(data_frame, text = str(i+1)+" месяц", bg = "#2F4F4F", fg = "white", font = "Times, 14")
        field = tk.Entry(data_frame, bd = 2, width = 15, justify = "right")
        
        labels.append(label)
        input_fields.append(field)
        
        label.place(relx = 0.1, rely = 0.13*(i+1))
        field.place(relx = 0.25, rely = 0.13*(i+1))

    #Кнопки 
    button_add = tk.Button(data_frame, text = "Добавить поле", width = 13, height = 1, bg = "#778899", font = "Times, 14",
                           command = lambda: add_field(input_fields, labels, data_frame)).place(relx = 0.1, rely = 0.9)

    button_remove = tk.Button(data_frame, text = "Удалить поле", width = 13, height = 1, bg = "#778899", font = "Times, 14",
                           command = lambda: remove_field(input_fields,labels)).place(relx = 0.3, rely = 0.9)

    button_import = tk.Button(data_frame, text = "Импорт из файла", width = 13, height = 1, bg = "#778899", font = "Times, 14",
                           command = lambda: import_file(input_fields)).place(relx = 0.4, rely = 0.625)

    button_export = tk.Button(data_frame, text = "Экспорт в файл", width = 13, height = 1, bg = "#778899", font = "Times, 14",
                           command = lambda: export_file(input_fields)).place(relx = 0.4, rely = 0.755)

    button_save = tk.Button(data_frame, text = "Сохранить", width = 13, height = 1, bg = "#778899", font = "Times, 14",
                           command = lambda: save(input_fields,data, flag)).place(relx = 0.5, rely = 0.9)

    button_clear = tk.Button(data_frame, text = "Очистить", width = 13, height = 1, bg = "#778899", font = "Times, 14",
                           command = lambda: remove(input_fields)).place(relx = 0.7, rely = 0.9)

    #------------------------------------------------Руководство--------------------------------------------------#

    #Первая страница руководства
    tk.Label(guide_frame_1, text = "Кнопка 'Ввод данных'",
                        bg = "#2F4F4F", fg = "white", font = "Times, 14").place(relx = 0.37, rely = 0.05)

    tk.Label(guide_frame_1, text = "По нажатию данной кнопки осуществится переход на страницу, где пользователь может",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.15)

    tk.Label(guide_frame_1, text = "ввести данные, необходимые для прогнозирования.",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.20)

    tk.Label(guide_frame_1, text = "Список кнопок на странице ввода данных: ",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.3)

    tk.Label(guide_frame_1, text = "1) Добавить поле ",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.35)

    tk.Label(guide_frame_1, text = "По нажатию пользователь увеличивает количество полей ввода",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.35, rely = 0.35)

    tk.Label(guide_frame_1, text = "2) Удалить поле",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.45)

    tk.Label(guide_frame_1, text = "По нажатию пользователь уменьшает количество полей ввода",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.35, rely = 0.45)

    tk.Label(guide_frame_1, text = "3) Сохранить",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.55)

    tk.Label(guide_frame_1, text = "По нажатию сохраняет введенные данные в программе, которые",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.35, rely = 0.55)

    tk.Label(guide_frame_1, text = "затем будут использованы для прогнозирования",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.35, rely = 0.60)

    tk.Label(guide_frame_1, text = "4) Очистить",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.65)

    tk.Label(guide_frame_1, text = "По нажатию очищает все поля ввода",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.35, rely = 0.65)

    tk.Label(guide_frame_1, text = "5) Импорт с файла",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.75)

    tk.Label(guide_frame_1, text = "Заполняет данными из файла поля ввода построчно",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.35, rely = 0.75)

    tk.Label(guide_frame_1, text = "6) Экспорт в файл",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.85)

    tk.Label(guide_frame_1, text = "По нажатию сохраняет введенные данные в файл",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.35, rely = 0.85)

    tk.Button(guide_frame_1, text = "1", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_1, frames)).place(relx = 0.42, rely = 0.95)
    
    tk.Button(guide_frame_1, text = "2", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_2, frames)).place(relx = 0.47, rely = 0.95)
    
    tk.Button(guide_frame_1, text = "3", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_3, frames)).place(relx = 0.52, rely = 0.95)

    #Вторая страница руководства
    
    tk.Label(guide_frame_2, text = "Кнопка 'Анализ'",
                        bg = "#2F4F4F", fg = "white", font = "Times, 14").place(relx = 0.4, rely = 0.05)

    tk.Label(guide_frame_2, text = "По нажатию данной кнопки (если данные сохранены!!!) : ",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.15)
    
    tk.Label(guide_frame_2, text = "1) Осуществится переход на страницу, где пользователь может увидеть значение",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.2)

    tk.Label(guide_frame_2, text = "прогноза на месяц вперед и ошибку прогноза.",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.25)
    
    tk.Label(guide_frame_2, text = "2) Отстроится график, по которому пользователь может наглядно увидеть линию прогноза",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.35)

    tk.Label(guide_frame_2, text = "Кнопка 'Руководство'",
                        bg = "#2F4F4F", fg = "white", font = "Times, 14").place(relx = 0.38, rely = 0.45)

    tk.Label(guide_frame_2, text = "По нажатию данной кнопки осуществится переход на страницу с подробным руководством",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.55)

    tk.Label(guide_frame_2, text = "пользователя по программе.",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.6)

    tk.Button(guide_frame_2, text = "1", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_1, frames)).place(relx = 0.42, rely = 0.95)
    
    tk.Button(guide_frame_2, text = "2", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_2, frames)).place(relx = 0.47, rely = 0.95)
    
    tk.Button(guide_frame_2, text = "3", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_3, frames)).place(relx = 0.52, rely = 0.95)


    #Третья страница руководства

    tk.Label(guide_frame_3, text = "Кнопка 'О программе'",
                        bg = "#2F4F4F", fg = "white", font = "Times, 14").place(relx = 0.38, rely = 0.05)

    tk.Label(guide_frame_3, text = "По нажатию данной кнопки осуществится переход на страницу, где пользователь может",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.15)
    
    tk.Label(guide_frame_3, text = "увидеть автора программы и язык программирования, с помощью которого был написана",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.2)
    
    tk.Label(guide_frame_3, text = "программа.",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.25)
    
    tk.Label(guide_frame_3, text = "Кнопка 'Выход'",
                        bg = "#2F4F4F", fg = "white", font = "Times, 14").place(relx = 0.4, rely = 0.45)

    tk.Label(guide_frame_3, text = "По нажатию данной кнопки осуществится выход из программы",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.1, rely = 0.55)

    tk.Button(guide_frame_3, text = "1", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_1, frames)).place(relx = 0.42, rely = 0.95)
    
    tk.Button(guide_frame_3, text = "2", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_2, frames)).place(relx = 0.47, rely = 0.95)
    
    tk.Button(guide_frame_3, text = "3", width = 3 , height = 1, bg = "#778899", font = "Times, 10",
                            command = lambda: ShowFrame(guide_frame_3, frames)).place(relx = 0.52, rely = 0.95)
    
    #------------------------------------------------О Программе--------------------------------------------------#
    
    main_frame.place(relx = 0.3, rely = 0)

    tk.Label(main_frame, text = "Эта программа служит для прогнозирования трудоемкости производства 1 т",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.14, rely = 0.1)
    
    tk.Label(main_frame, text = "цемента на месяц вперед. Программа написана  студентом  группы  ИТП-21",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.12, rely = 0.15)
    
    tk.Label(main_frame, text = "Курако Кириллом на языке программирования Python v3.7.0 .",
                        bg = "#2F4F4F", fg = "white", font = "Times, 12").place(relx = 0.12, rely = 0.2)
    
    tk.Label(main_frame, text = "© 2018-2019 | Курако Кирилл | ИТП-21",
                        bg = "#2F4F4F", fg = "white", font = "Times, 10").place(relx = 0.35, rely = 0.95)

    photo = tk.PhotoImage(file = "logo.gif")
    artwork = tk.Button(main_frame, text = "", image = photo,  bg = "#2F4F4F" )
    artwork.image = photo
    artwork.place(relx = 0.08, rely = 0.3)

    
def ShowFrame(frame, frames):
    frame.place(relx = 0.3, rely = 0)
    n = len(frames)
    for i in range(n):
        if str(frames[i]) != str(frame):
            hideFrame(frames[i])

def hideFrame(frame):
    frame.place_forget()

def add_field(input_fields, labels, frame):
    i = len(labels)

    if i < 6:
        label = tk.Label(frame, text = str(i+1)+" месяц", bg = "#2F4F4F", fg = "white", font = "Times, 14")
        field = tk.Entry(frame, bd = 2, width = 15, justify = "right")
        
        labels.append(label)
        input_fields.append(field)
        
        label.place(relx = 0.1, rely = 0.13*(i+1))
        field.place(relx = 0.25, rely = 0.13*(i+1))

    elif i != 12:
        label = tk.Label(frame, text = str(i+1)+" месяц", bg = "#2F4F4F", fg = "white", font = "Times, 14")
        field = tk.Entry(frame, bd = 2, width = 15, justify = "right")
            
        labels.append(label)
        input_fields.append(field)
            
        label.place(relx = 0.6, rely = 0.13*(i-5))
        field.place(relx = 0.75, rely = 0.13*(i-5))

def remove_field(input_fields,labels):
    i = len(input_fields)
    if i != 2:
        labels[i-1].place_forget()
        input_fields[i-1].place_forget()
        labels.pop(i-1)
        input_fields.pop(i-1)

def import_file(input_fields):
    file_name = filedialog.askopenfilename()

    data = list()
    try:
        file = open(file_name, 'r')
    except IOError as e:
        messagebox.showinfo("Чтение данных", 'Не выбран файл')
        return
    else:
        with file:
            data = file.readlines()
            n = len(data)
            for i in range(n):
                data[i] = data[i].split()
            
    
            n = len(input_fields)
            remove(input_fields)
            for i in range(n):
                input_fields[i].insert(0, data[i])
            file.close()

def export_file(input_fields):
    file_name = filedialog.asksaveasfilename()
    
    try:
        file = open(file_name, 'w')
    except IOError as e:
        messagebox.showinfo("Сохранение данных", 'Не выбран файл')
        return
    else:
        with file:
            n = len(input_fields)
            for i in range(n):
                file.write(input_fields[i].get() + '\n')

            messagebox.showinfo("Сохранение данных", 'Данные сохранены в файле ' + file_name)
            file.close()

def save(input_fields, data, flag):
    n = len(input_fields)
    data.clear()
    if n != 0:
        for i in range(n):
            try:
                if float(input_fields[i].get()) <= 0:
                    messagebox.showerror("Ошибка","Введено не положительное значение!!!\n\nВведите данные в " +str(i+1)+" поле.")
                    break
                else:
                    data.append(float(input_fields[i].get()))
                    flag[0] = 0
            except ValueError :
                messagebox.showerror("Ошибка","Не все поля заполнены!!!\n\nВведите данные в " +str(i+1)+" поле.")
                flag[0] = 1
                break
            
def remove(input_fields):
    n = len(input_fields)
    if n != 0:
        for i in range(n):
            input_fields[i].delete(0, 'end')
    
def analyze(y,analyze_frame, frames, flag, output_labels):    
    n = len(y)
    if n > 1 and flag[0] != 1:
        for i in output_labels:
            i['text'] = ""
        output_labels.clear()


        #Анализ данных
        x = [i for i in range(1,n+2)]

        sum_1 = sum(x[i] / exp(1 / x[i]) for i in range(n))
        sum_2 = sum(y[i] for i in range(n))
        sum_3 = sum((x[i] ** 2) / exp(2 / x[i]) for i in range(n))
        sum_4 = sum(y[i] * x[i] / exp(1 / x[i]) for i in range(n))

        det_0 = np.linalg.det([[n,     sum_1],
                               [sum_1, sum_3]])

        det_1 = np.linalg.det([[sum_2, sum_1],
                               [sum_4, sum_3]])

        det_2 = np.linalg.det([[n,     sum_2],
                               [sum_1, sum_4]])

        a = det_1/det_0     #Коэффициент a
        b = det_2/det_0     #Коэффициент b
        
        f = [a + b*x[i]/exp(1/x[i]) for i in range(n+1)]     

        #Определение коэффициента детерминации
        avarage_y = sum(y[i] for i in range(n)) / n

        numerator = sum((y[i] - f[i]) ** 2 for i in range(n))

        denominator = sum((y[i] - avarage_y) ** 2 for i in range(n))

        determination = 1 - numerator / denominator

        #Определние средней ошибки аппроксимации
        error = sum(fabs((y[i] - f[i]) / y[i]) for i in range(n)) * 100 / n

        #Вывод значений
        label_t = tk.Label(analyze_frame, text = "Анализирование данных" , bg = "#2F4F4F",
                                                   fg = "white", font = "Times, 16").place(relx = 0.35, rely = 0)

        for i in range (n):
            output_labels.append(tk.Label(analyze_frame, text = str(i+1)+ " месяц: " +str(round(f[i], 3)), bg = "#2F4F4F", fg = "white",
                                                   font = "Times, 14"))
            output_labels[i].place(relx = 0.1, rely = 0.07*(i+1))    

        output_labels.append(tk.Label(analyze_frame, text = str(n+1)+ " месяц: " +str(round(f[n],3)), bg = "#2F4F4F", fg = "#FF5E00",
                                                   font = "Times, 14"))
        output_labels[-1].place(relx = 0.1, rely = 0.07*(n+1))

        label_d = tk.Label(analyze_frame, text = "Коэффициент детерминации : " +str(determination)[:6], bg = "#2F4F4F",
                                                   fg = "white", font = "Times, 14").place(relx = 0.5, rely = 0.07)

        label_error = tk.Label(analyze_frame, text = "Ошибка аппроксимации : " +str(error)[:6]+" %", bg = "#2F4F4F",
                                                   fg = "white", font = "Times, 14").place(relx = 0.5, rely = 0.14)

        #отрисовка фрейма с данными и графика
        ShowFrame(analyze_frame, frames)
        plt.clf()
        plt.title("Прогноз трудоемкости производства 1 т цемента на месяц вперед")
        plt.plot(x[:n], y[:n], "r", label="Экспериментальные данные", marker="o")
        plt.plot(x, f, "b", label="Линия тренда")
        plt.xlabel("Месяц")
        plt.ylabel("Трудоемкость производства")
        plt.legend()
        plt.grid()
        plt.show()
        
    else:
        messagebox.showerror("Ошибка","Данные отсутствуют или заполнены не все поля")


if __name__ == "__main__":
    root = tk.Tk()
    window()
    root.mainloop()
