from tkinter import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/kelson/GITHUB/Tkinter_estudo/Projetos/Formulario_GSPREAD/api.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("database").sheet1

window = Tk()
window.geometry("600x700")
window.resizable(0,0)
window.title("Formulário Embaixadores do Reino")
window.config(bg="#34495e")

check = IntVar()
var_check = ""

def clear():
    name.delete(0, 'end')
    celular.delete(0, 'end')
    email.delete(0, 'end')
    idade.delete(0, 'end')
    qual.delete(0, 'end')

def checked ():
    if check.get():
        return "Sim"
    else:
        return "Não"

def file_func(info_get, list_info):
    file = open("form.csv", "a")
    file.write(info_get)
    file.close()
    wks.append_row(list_info)

def func_submit():
    v = ","

    var_check = checked()
    info_get = name.get() + v + celular.get() + v + email.get() + v + idade.get() + " anos" + v + var_check + v + qual.get() + "\n"
    list_info = [name.get(), celular.get(), email.get(), idade.get()+" anos", var_check, qual.get()]
    print (info_get)
    file_func(info_get, list_info)
    clear()

app_label = Label(window, text="Formulário de Incrição", bg="#34495e", font=("Arial", 26), fg="#ecf0f1")
app_label.grid(row=0, column=2, ipady=20)

info = ["Nome: ", "Celular: ", "E-mail: ", "Idade: ", "Membro de alguma igreja: ", "Qual: "]

x = 1
for i in info:
    a = Label(window, text=i, bg="#34495e", fg="#ecf0f1", pady=20)
    a.grid(row=x, column=1, sticky=W)
    x+=1

name = Entry(window)
celular = Entry(window)
email = Entry(window)
idade = Entry(window)
sim = Checkbutton(window, text="SIM", bg="#34495e", variable=check)
qual = Entry(window)

entrys = [name, celular, email, idade, sim, qual]

x = 1
for ent in entrys:
    ent.grid(row=x, column=2, ipady=1, ipadx=100)
    x+=1


submit = Button(window, text="SUBMIT", command=func_submit)
submit.grid(row=7, column=2, pady=50, sticky=W)


window.mainloop()