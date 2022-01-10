from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    #on binarise et localise l'image à comparer
    im=image.binarisation(S)
    im=im.localisation()
    
    #on stocke le taux de similitude le plus important 
    sim_max =0
    #on stocke l'entier dont le taux de similitude est le plus grand
    entier_ress = 0
    
    #on parcourt la liste des images
    for i in range (len(liste_modeles)):
        #on redimensionne l'image à comparer avec celle de la liste
        im=im.resize(liste_modeles[i].H, liste_modeles[i].W)
        
        #si le taux de similitude est supérieur, on l'affecte à sim_max
        if sim_max<im.similitude(liste_modeles[i]) :
            sim_max = im.similitude(liste_modeles[i])
            #on stocke le chiffre correspondant à l'image la plus proche
            entier_ress = i
            
    #on renvoie le chiffre trouvé
    return entier_ress

