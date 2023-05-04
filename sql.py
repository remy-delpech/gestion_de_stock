import mysql.connector

# Connectez-vous au serveur MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Natalia280988!"
)

# Créez un curseur pour exécuter des commandes SQL
cursor = connection.cursor()

# Créez la base de données "boutique"
cursor.execute("CREATE DATABASE IF NOT EXISTS boutique")

# Utilisez la base de données "boutique"
cursor.execute("USE boutique")

# Créez la table "categorie"
cursor.execute("""
CREATE TABLE IF NOT EXISTS categorie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255)
)
""")

# Créez la table "produit"
cursor.execute("""
CREATE TABLE IF NOT EXISTS produit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    description TEXT,
    prix INT,
    quantite INT,
    id_categorie INT,
    FOREIGN KEY (id_categorie) REFERENCES categorie (id)
)
""")

# Insérez des catégories et des produits
cursor.execute("INSERT INTO categorie (nom) VALUES ('Électronique')")
cursor.execute("INSERT INTO categorie (nom) VALUES ('Vêtements')")
cursor.execute("INSERT INTO categorie (nom) VALUES ('Jouets')")

cursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES ('iPhone', 'Téléphone intelligent', 1000, 10, 1)")
cursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES ('T-shirt', 'Vêtement', 20, 50, 2)")
cursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES ('Lego', 'Jouet de construction', 30, 25, 3)")

# Validez les changements et fermez la connexion
connection.commit()
cursor.close()
connection.close()