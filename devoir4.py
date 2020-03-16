#coding: utf-8 

#tout d'abord, j'importe les modules qui seront nécessaires au bon fonctionnement de mon programme 
import csv, spacy
from collections import Counter

#J'importe aussi le module core news md 
md = spacy.load("fr_core_news_md")

#Je crée la variable qui va contenir le fichier csv que je veux étudier 
fichier = "martino.csv"

f = open(fichier) #je fais ça pour ouvrir le fichier,
chroniques = csv.reader(f) #je créer une variable pour le lire, 
next(chroniques) #et je fais ça pour ne pas utiliser la première ligne du fichier csv

#Je crée une liste vide pour y ajouter toutes les paires de mots 
paires = []

md.Defaults.stop_words.add("y") #Je fais ceci parce que je vais utiliser les mots vides, et je veux y ajouter le "y"  
md.Defaults.stop_words.remove("gens") #Ici, c'est pour retirer le mot "gens" des mots vides (qui y est automatiquement)

#Je crée la boucle des chroniques 
for chronique in chroniques:
    #Je fais une variable dans laquelle il y a le nom des chroniques (et nom la date, le lien ou autre). C'est le 4ème élément de la liste (donc 3 parce qu'on compte le 0)
    nom = md(chronique[3])
    #Je fais une variable qui contiendera tous les mots lemmatisés, sans les mots vides 
    lemmes = [token.lemma_ for token in nom if token.is_stop == False and token.is_punct == False] 
    # if lemmes == "islam" or lemmes == "musulm": J'ai fait cette condition pour faire un test, mais cela n'a pas l'air de fonctionner (le print était indenté lorsque j'ai testé). J'ai donc mis en commentaire. J'essaierai plus tard de créer cette condition
    print(lemmes) #Je vérifie la ligne 28 et tout ce qui est en dessus (sauf ligne 29 qui ne marche pas) fonctionne. Cela a fonctionné, alors je mets le print en commentaire. 

    #Je crée cette boucle pour créer les paires, tout en extrayant le dernier mot (:-1)
    for x, y in enumerate(lemmes[:-1]):
        paires.append("{} {}".format(lemmes[x], lemmes[x+1])) 
        #Je créee une condition, pour voir si cela fonctionne ici. A ce que j'ai compris, le x c'est le numéro d'index, et le y c'est l'élément, donc c'est le y qui devrait etre égal à "islam" ou "musulm"
        if y == "islam" or "musulm":
            #Maintenant, j'essaye d'imprimer le résultat : 
            print(len(paires))
            freq = Counter(paires) #Je rajoute cette ligne pour faire un calcul de fréquence 
            print(freq.most_common(50)) #Je rajoute celle-ci pour que ma variable n'affiche que les 50 paires de mots parlant d'islam les plus fréquentes 

#Cela a l'air de fonctionner et de me faire des paires de mots, mais pas de m'afficher celles qui parlent de l'islam. Pourtant cela ne m'affiche pas d'erreur, donc je ne vois pas d'où vient le problème 
#J'ai essayé de changer ma ligne 36 plusieurs fois, voici les différentes versions que j'ai essayé : 
# if y == "islam" or y == "musulm":
# if y == "islam" or "musulm":
#Peut-être que je n'avais pas compris la différence entre le x et le y : 
# if x == "islam" or x == "musulm":
# if x == "islam" or "musulm":
#Selon cette ligne, parfois dans mon résultat (notamment avec l'essai ici ligne 44, cela ne me mettait même plus de paires, mais juste des mots. Je ne comprend pas)
#Avec la ligne 45, il y a des paires mais elles se répetent, sans le mot "islam" ou "musulm" dedans 
#Comme j'ai fait de nombreux tests et n'ai pas compris d'où venait le souci, j'ai fini par abandonner. Navrée. Je suis déjà contente d'être arrivée jusque là ! 








