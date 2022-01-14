from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        """Cette fonction permet de binariser une image 
        selon un seuil S défini par l'utilisateur"""
		# creation d'une image vide
        im_bin = Image()
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        h= im_bin.H
        w= im_bin.W 
        for i in range(h):
            for j in range(w):
                if self.pixels[i][j] >= S:
                    im_bin.pixels[i][j]=255
                else :
                    im_bin.pixels[i][j]  = 0

        # TODO: boucle imbriquees pour parcourir tous les pixels de l'image im_bin
        # et calculer l'image binaire
               
        return im_bin    


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        """Cette fonction permet de recadrer une image autour d'une forme"""
		# creation d'une image vide
        im_bin = Image()
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
       
        h= self.H
        w= self.W 
        l_min = self.H
        c_min = self.W
        l_max= 0
        c_max =0
        #initialisation des coordonnees du futur rectangle englobant la forme noire
        for l in range(h):
            for c in range(w):
                if self.pixels[l][c] == 0:
                    if l < l_min:
                        l_min = l
                    if c < c_min:
                        c_min = c
                    if l > l_max:
                        l_max = l
                    if c > c_max:
                        c_max =c
                    
        #on attribue à l'image ses nouvelles dimensions            
        im_bin.pixels=self.pixels[l_min:l_max+1,c_min:c_max+1]
        im_bin.H=l_max - l_min
        im_bin.W=c_max - c_min
        return (im_bin)
        

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        
        # creation d'une image vide
        newim = Image()
       
        #redimensionnement et conversion de l'image
        newim.pixels=resize(self.pixels, (new_H,new_W), 0)
        newim.pixels=np.uint8(newim.pixels*255)
        
        #affectation des nouveaux attributs
        newim.H= new_H
        newim.W= new_W
        return newim
    


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        #on redimensionne les images afin qu'elles aient la meme taille
        image2=im.resize(self.H, self.W)
        #calcul du nombre total de pixels
        nb_pix_tot=self.W*self.H
        #compteur du nombre de pixels similaires
        nb_pix_sim=0
        
        h= self.H
        w= self.W 
        
        for l in range(h):
            for c in range(w):
                if self.pixels[l][c]== image2.pixels[l][c]:
                    nb_pix_sim +=1
                    
        return nb_pix_sim/nb_pix_tot
                    
   
