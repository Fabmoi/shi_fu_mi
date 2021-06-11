from random import randint


def ecrire(nombre):
    if nombre == 1:
        print("PIERRE", end="")
    elif nombre == 2:
        print("FEUILLE", end="")
    else:
        print("CISEAUX", end="")


def augmenter_scores(mon_signe, ton_signe):
    global mon_score, ton_score
    if mon_signe == 1 and ton_signe == 2:
        print("Ta feuille enveloppe ma pierre")
        ton_score += 1
    elif mon_signe == 2 and ton_signe == 1:
        print("Ma feuille enveloppe ta pierre")
        mon_score += 1
    elif mon_signe == 1 and ton_signe == 3:
        print("Ma pierre émousse tes ciseaux")
        mon_score += 1
    elif mon_signe == 3 and ton_signe == 1:
        print("Ta pierre émousse mes ciseaux")
        ton_score += 1
    elif mon_signe == 3 and ton_signe == 2:
        print("Mes ciseaux coupent ta feuille")
        mon_score += 1
    elif mon_signe == 2 and ton_signe == 3:
        print("Tes ciseaux coupent ma feuille")
        ton_score += 1
    else:
        print("Nous avons choisis le même signe et aucun ne bat l'autre")


ton_score = 0
mon_score = 0
fin = 5
print("PIERRE - FEUILLE - CISEAUX.")
print("Choisissez votre signe en écrivant le chiffre correspondant.")
print("Sans oublier de dire CHI FOU MI en fesant votre choix")
print("Le premier à " + str(fin) + " est le VAINQUEUR !")
print()


while mon_score < fin and ton_score < fin:
    ton_signe = int(input("1 = PIERRE, 2 = FEUILLE, 3 = CISEAUX ? "))
    while ton_signe < 1 or ton_signe > 3:
        ton_signe = int(input('1 = PIERRE, 2 = FEUILLE, 3 = CISEAUX ? '))
    print("Vous choisissez ", end="")
    ecrire(ton_signe)
    mon_signe = randint(1, 3)
    print(" - Je choisis ", end="")
    ecrire(mon_signe)
    print()
    augmenter_scores(mon_signe, ton_signe)
    print("Vous avez", ton_score, "J'ai", mon_score)
    print()


def afficher_resultats():
    if mon_score == fin:
        print("Je suis le meilleur")
    else:
        print("Tu es le vainqueur, je m'avoue vaincu")


afficher_resultats()

