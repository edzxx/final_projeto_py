import sqlite3
from tkinter import *
from tkinter import messagebox

def cadastrar_cliente_db(nome_entry, email_entry, telefone_entry, endereco_entry):
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)",
                   (nome_entry.get(), email_entry.get(), telefone_entry.get(), endereco_entry.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

root = Tk()
root.title("Cadastro de Clientes")
root.geometry("400x250")

Label(root, text="Nome").grid(row=0, column=0, padx=10, pady=5)
nome_entry = Entry(root)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="E-mail").grid(row=1, column=0, padx=10, pady=5)
email_entry = Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Telefone").grid(row=2, column=0, padx=10, pady=5)
telefone_entry = Entry(root)
telefone_entry.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Endereco").grid(row=3, column=0, padx=10, pady=5)
endereco_entry = Entry(root)
endereco_entry.grid(row=3, column=1, padx=10, pady=5)

Button(root, text="Cadastrar", command=lambda: cadastrar_cliente_db(nome_entry, email_entry, telefone_entry, endereco_entry)).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

