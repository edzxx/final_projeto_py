from tkinter import *
from tkinter import messagebox

def chama_cadastro():
    import cadastro
    cadastro.main()

def chama_consulta():
    import consulta_c
    consulta_c.main()

root = Tk()
root.title("Bem Vindo")
root.geometry("300x200")

Label(root, text="Bem Vindo").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

Button(root, text="Cadastrar", command=chama_cadastro).grid(row=1, column=0, padx=10, pady=10)
Button(root, text="Consultar", command=chama_consulta).grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
