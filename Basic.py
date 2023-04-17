
def afficher_informations_person(nom, age, taille=0):
    print("Vous vous appelez "+ nom + ", vous avez " + str(age) + " ans")
    print(f"Vous vous appelez {nom}, vous avez {age} ans")
    print("Vous vous appelez %s,vous avez %s ans" % (nom, age))
    print("L'an prochain vous aurez " + str(age+1) + " ans")
    print("L'an prochain vous aurez %s ans" % (age + 1))

    if age == 17:
        print("Vous etes presque majeur")
    elif 12 >= age < 18 :
        print("Vous etes adolesent")
    elif age == 1 or age == 2:
        print("vous etes bebe")
    elif age == 18:
        print("Tout justes majeur : Felicitation")
    elif age > 60:
        print("Vous etes senior")
    elif age < 10:
        print("Vous etes enfent")
    elif age >= 18:
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")
    
    # afficher la taille
    if not taille==0:
        print("Votre taille : " + str(taille) + " m")

def demande_nom():
    nom_reponse = ""
    while nom_reponse == "":
        nom_reponse = input("Quel est votre nom ? ")
    return nom_reponse



def demander_age(nom_person):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_person + " quel est votre age ?")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERROR: Vous devez rentre un nombre pour l'age")
    return age_int    

# Demander nom
# nom1 = demande_nom()
# nom2 = demande_nom()
# nom1 ="paul"
# nom2 ="peter"

# Demander age
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# Afficher resultat
# afficher_informations_person(nom1, age1)
# afficher_informations_person(nom2, age2)
NB_PERSONNE = 1

for i in range(0,NB_PERSONNE):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_informations_person(nom, age, 1.90)
