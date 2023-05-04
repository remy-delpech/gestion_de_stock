import tkinter as tk
from tkinter import ttk
import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="Natalia280988!", database="boutique")

# Fonctions pour interagir avec la base de données
def get_products():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM produit")
    return cursor.fetchall()

def add_product(nom, description, prix, quantite, id_categorie):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)", (nom, description, prix, quantite, id_categorie))
    connection.commit()

def delete_product(product_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM produit WHERE id = %s", (product_id,))
    connection.commit()

def update_product(product_id, nom, description, prix, quantite, id_categorie):
    cursor = connection.cursor()
    cursor.execute("UPDATE produit SET nom = %s, description = %s, prix = %s, quantite = %s, id_categorie = %s WHERE id = %s", (nom, description, prix, quantite, id_categorie, product_id))
    connection.commit()


# Fonction pour mettre a jour l'affichage

def refresh_list():
    products_list.delete(0, tk.END)
    for product in get_products():
        products_list.insert(tk.END, product)

def on_add_product():
    nom = name_entry.get()
    description = description_entry.get()
    prix = int(price_entry.get())
    quantite = int(quantity_entry.get())
    id_categorie = int(category_id_entry.get())

    add_product(nom, description, prix, quantite, id_categorie)
    refresh_list()

def on_delete_product():
    selected_product = products_list.get(products_list.curselection())
    product_id = selected_product[0]

    delete_product(product_id)
    refresh_list()

def on_update_product():
    selected_product = products_list.get(products_list.curselection())
    product_id = selected_product[0]

    nom = name_entry.get()
    description = description_entry.get()
    prix = int(price_entry.get())
    quantite = int(quantity_entry.get())
    id_categorie = int(category_id_entry.get())

    update_product(product_id, nom, description, prix, quantite, id_categorie)
    refresh_list()

# Créez l'interface graphique avec des widgets TTK

root = tk.Tk()
root.title("Gestion de stock")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

name_label = ttk.Label(main_frame, text="Nom")
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(main_frame)
name_entry.grid(row=0, column=1)

description_label = ttk.Label(main_frame, text="Description")
description_label.grid(row=1, column=0, padx=(0, 10))
description_entry = ttk.Entry(main_frame)
description_entry.grid(row=1, column=1)

price_label = ttk.Label(main_frame, text="Prix")
price_label.grid(row=2, column=0, padx=(0, 10))
price_entry = ttk.Entry(main_frame)
price_entry.grid(row=2, column=1)

quantity_label = ttk.Label(main_frame, text="Quantité")
quantity_label.grid(row=3, column=0, padx=(0, 10))
quantity_entry = ttk.Entry(main_frame)
quantity_entry.grid(row=3, column=1)

category_id_label = ttk.Label(main_frame, text="ID Catégorie")
category_id_label.grid(row=4, column=0, padx=(0, 10))
category_id_entry = ttk.Entry(main_frame)
category_id_entry.grid(row=4, column=1)

add_button = ttk.Button(main_frame, text="Ajouter", command=on_add_product)
add_button.grid(row=5, column=0, pady=(10, 0))

delete_button = ttk.Button(main_frame, text="Supprimer", command=on_delete_product)
delete_button.grid(row=5, column=1, pady=(10, 0))

update_button = ttk.Button(main_frame, text="Modifier", command=on_update_product)
update_button.grid(row=5, column=2, pady=(10, 0))

products_list = tk.Listbox(main_frame, width=80)
products_list.grid(row=6, column=0, columnspan=3, pady=(10, 0))

status_label = ttk.Label(main_frame, text="")
status_label.grid(row=7, column=0, columnspan=3, pady=(10, 0))

refresh_list()

root.mainloop()