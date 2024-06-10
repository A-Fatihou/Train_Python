# Programme de connexion à un compte utilisateur
def login():

    utilisateur = input("Entrez votre nom d'utilisateur: ")
    mot_de_passe = input("Entrez votre mot de passe: ")

    if utilisateur == "Adamou" and mot_de_passe == "Bakayaro123":
        print("Connexion réussie!")
    else:    
        print("Nom d'utilisateur ou mot de passe incorrect.")
    
login()















