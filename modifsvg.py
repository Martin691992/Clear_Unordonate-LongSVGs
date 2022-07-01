
##Martin BONNARD
## Mini script qui me permet de clarifier les fichiers SVG qui parfois sont en ligne.
# Le script ouvre le fichier qui lui est attribué, le lit et recherche le caractère '<' (balise)
# quand la balise est trouvé on ajoute un espace
# finalement on réécris sur le fichier la nouvelle chaines


class ModificateurTexte:
    def __init__(self,fichier) -> None:
        self.file = fichier
    def modifierSVG(self):
        reader = open(self.file,"r")
        data = reader.read()

        newString= ""

        for enumData in data :
            if enumData == "<" : 
                newString =newString+"\n"+enumData
            else:
                newString= newString + enumData

        print(newString)
        reader.close()

        ndreader = open(self.file,"w")

        ndreader.write(newString)
        ndreader.close()

file = "text.txt"
modif = ModificateurTexte(file)
modif.modifierSVG()
