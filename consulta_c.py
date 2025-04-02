import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT,
        endereco TEXT
    )
""")

conn.close()

root = Tk()
root.title("XYZ COMÉRCIO CLIENTES")
root.geometry("800x600")

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

tree = ttk.Treeview(root, columns=("id", "nome", "email", "telefone", "endereco"), show="headings")
tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

tree.column("id", minwidth=50, width=50)
tree.column("nome", minwidth=100, width=150)
tree.column("email", minwidth=100, width=150)
tree.column("telefone", minwidth=100, width=150)
tree.column("endereco", minwidth=100, width=150)

tree.heading("id", text="ID")
tree.heading("nome", text="Nome")
tree.heading("email", text="E-mail")
tree.heading("telefone", text="Telefone")
tree.heading("endereco", text="Endereco")

Label(root, text="ID").grid(row=5, column=0, padx=10, pady=5)
id_entry = Entry(root)
id_entry.grid(row=5, column=1, padx=10, pady=5)

def atualizar_treeview():
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    for cliente in clientes:
        tree.insert("", "end", values=(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]))

def cadastrar_cliente():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)",
                   (nome_entry.get(), email_entry.get(), telefone_entry.get(), endereco_entry.get()))
    conn.commit()
    conn.close()
    nome_entry.delete(0, END)
    email_entry.delete(0, END)
    telefone_entry.delete(0, END)
    endereco_entry.delete(0, END)
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    atualizar_treeview()

def editar_cliente():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nome = ?, email = ?, telefone = ?, endereco = ? WHERE id = ?",
                   (nome_entry.get(), email_entry.get(), telefone_entry.get(), endereco_entry.get(), id_entry.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Cliente editado com sucesso!")
    atualizar_treeview()

def excluir_cliente():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_entry.get(),))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Cliente excluido com sucesso!")
    atualizar_treeview()

def selecionar_registro(event):
    registro = tree.selection()[0]
    id_entry.delete(0, END)
    nome_entry.delete(0, END)
    email_entry.delete(0, END)
    telefone_entry.delete(0, END)
    endereco_entry.delete(0, END)

    id_entry.insert(0, tree.item(registro, "values")[0])
    nome_entry.insert(0, tree.item(registro, "values")[1])
    email_entry.insert(0, tree.item(registro, "values")[2])
    telefone_entry.insert(0, tree.item(registro, "values")[3])
    endereco_entry.insert(0, tree.item(registro, "values")[4])

tree.bind("<<TreeviewSelect>>", selecionar_registro)

Button(root, text="Cadastrar", command=cadastrar_cliente).grid(row=6, column=0, padx=10, pady=10)
Button(root, text="Editar", command=editar_cliente).grid(row=6, column=1, padx=10, pady=10)
Button(root, text="Excluir", command=excluir_cliente).grid(row=6, column=2, padx=10, pady=10)

atualizar_treeview()
root.mainloop()
