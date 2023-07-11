# Class Arbre

class Arbre:
#   constructeur
    def __init__(self, valeur) -> None:
        self.valeur = valeur
        self.children = []
        
#   ajouter_enfant    
    def ajouter_enfant(self, noeud):
        self.children.append(noeud)
    
#   vérifier si on est une feuille    
    def est_une_feuille(self) ->True:
        if len(self.children) > 0:
            return False
        else:
            return True

#   trouver profondeur de l'arbre
    def trouver_profondeur(self) -> int:
        if self.est_une_feuille():
            return 0
        else:
            liste_profondeur_enfants = []
            for enfant in self.children:
                liste_profondeur_enfants.append(enfant.trouver_profondeur())
            return max(liste_profondeur_enfants) + 1
    
    def __str__(self) -> str:
        return str(self.valeur)

#   parcours en profondeur
    def parcourir_en_profondeur(self):
                
        if self.est_une_feuille():  
            
            return "Ce n'est pas un arbre !"
        
        else:
            
            for enfant in self.children:
                
                if enfant.est_une_feuille():
                    
                    print("0 / " + str(enfant.valeur))
                
                else:
                    
                    enfant.parcourir_en_profondeur()

        return 
   
        
#   parcours en largeur
        
racine = Arbre(0)
noeud1 = Arbre(1)
noeud2 = Arbre(2)

racine.ajouter_enfant(noeud1)
racine.ajouter_enfant(noeud2)

noeud3 = Arbre(3)
noeud4 = Arbre(4)

noeud2.ajouter_enfant(noeud3)
noeud2.ajouter_enfant(noeud4)

noeud5 = Arbre(5)

noeud3.ajouter_enfant(noeud5)

noeud6 = Arbre(6)

noeud5.ajouter_enfant(noeud6)


#print(len(racine.children))
print(racine.parcourir_en_profondeur())





        
        
