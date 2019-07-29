from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x700")
window.resizable(0,0)
window.title("Formulário Embaixadores do Reino")
window.config(bg="#34495e")

check = IntVar()
var_check = ""

def clear():
    name.delete(0, 'end')
    cellphone.delete(0, 'end')
    email.delete(0, 'end')
    age.delete(0, 'end')
    church.delete(0, 'end')

def checked ():
    if check.get():
        return "Sim"
    else:
        return "Não"

def file_func(info_get):
    file = open("/home/kelson/GITHUB/Tkinter_estudo/Projetos/Formulario/form.csv", "a")
    file.write(info_get)
    file.close()

def func_save():
    v = ","

    var_check = checked()
    info_get = name.get() + v + cellphone.get() + v + email.get() + v + age.get() + " anos" + v + var_check + v + church.get() + "\n"
    print (info_get)
    file_func(info_get)
    clear()

def func_submit():
    msg = messagebox.askquestion("Confirmação", "Salvar informações?")
    print (msg)
    if msg == "yes":
        func_save()
    else:
        None

app_label = Label(window, text="Formulário de Incrição", bg="#34495e", font=("Arial", 26), fg="#ecf0f1")
app_label.grid(row=0, column=2, ipady=20)

info = ["Nome: ", "Celular: ", "E-mail: ", "Idade: ", "Membro de alguma igreja: ", "Qual: "]

x = 1
for i in info:
    a = Label(window, text=i, bg="#34495e", fg="#ecf0f1", pady=20)
    a.grid(row=x, column=1, sticky=W)
    x+=1

name = Entry(window)
cellphone = Entry(window)
email = Entry(window)
age = Entry(window)
member = Checkbutton(window, text="SIM", bg="#34495e", variable=check)
church = Entry(window)

entrys = [name, cellphone, email, age, member, church]

x = 1
for ent in entrys:
    ent.grid(row=x, column=2, ipady=1, ipadx=100)
    x+=1


submit = Button(window, text="SUBMIT", command=func_submit)
submit.grid(row=7, column=2, pady=50, sticky=W)


window.mainloop()