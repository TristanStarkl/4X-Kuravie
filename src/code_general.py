# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 12:18:35 2014

@author: Thomas RETY
"""


"""Les importations de modules"""


import math
import tkinter

class khuraves:
    def creation_joueur(self):
        self.nom = self
        self.tresor = 10000 #chiffre random
        self.pv = 100
        self.nombre_infanterie = 1
        self.nombre_blinde = 0
        self.nombre_artillerie = 0
        self.nombre_bateaux = 0
        self.nombre_avions = 0
        self.revenu = 500
        self.construction = 1
        
        
class scartes:
    def creation_joueur(self):
        self.nom = self
        self.tresor = 10000 #chiffre random
        self.pv = 100
        self.nombre_infanterie = 1
        self.nombre_blinde = 0
        self.nombre_artillerie = 0
        self.nombre_bateaux = 0
        self.nombre_avions = 0
        self.revenu = 400
        self.construction = 1












"""Batiment"""

class ouvrage:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'none'
        
class fort:
    def construction(self):
        self.cout = 2500
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'ouvrage'
        self.temps_construction = 4
        self.augmente = 'none'
        
class bastion:
    def construction(self):
        self.cout = 4000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'fort'
        self.temps_construction = 6
        self.augmente = 'none'
        
class forteresse:
    def construction(self):
        self.cout = 6500
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'bastion'
        self.temps_construction = 8
        self.augmente = 'none'
        
        
class citadelle:
    def construction(self):
        self.cout = 10000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'forteresse'
        self.temps_construction = 10
        self.augmente = 'none'
        
class bourg:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 500
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'construction'
        
class ville:
    def construction(self):
        self.cout = 2500
        self.nombre_construit = 0
        self.rapporte = 1000
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'bourg'
        self.temps_construction = 4
        self.augmente = 'construction'
        
class grande_ville:
    def construction(self):
        self.cout = 4000
        self.nombre_construit = 0
        self.rapporte = 1750
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'ville'
        self.temps_construction = 6
        self.augmente = 'construction'
        
class cit??:
    def construction(self):
        self.cout = 6500
        self.nombre_construit = 0
        self.rapporte = 2500
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'grande_ville'
        self.temps_construction = 8
        self.augmente = 'construction'
        
class chef_lieu:
    def construction(self):
        self.cout = 10000
        self.nombre_construit = 0
        self.rapporte = 5000
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'cit??'
        self.temps_construction = 10
        self.augmente = 'construction'


class champs_de_tir:
    def construction(self):
        self.cout = 500
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'artillerie'


class dep??t_de_campagne:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'champs_de_tir'
        self.temps_construction = 4
        self.augmente = 'artillerie'

class acad??mie_artillerie:
    def construction(self):
        self.cout = 2000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'dep??t_de_campagne'
        self.temps_construction = 6
        self.augmente = 'artillerie'

class arsenal:
    def construction(self):
        self.cout = 4000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'acad??mie_artillerie'
        self.temps_construction = 8
        self.augmente = 'artillerie'
        
        
        
class tr??sorerie:
    def construction(self):
        self.cout = 500
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'commerce 250'
        

        

class bureau_du_commerce:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'tr??sorerie'
        self.temps_construction = 4
        self.augmente = 'commerce 750'
        
        
        
class quartier_financier:
    def construction(self):
        self.cout = 2000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'bureau_du_commerce'
        self.temps_construction = 6
        self.augmente = 'commerce 1500'


class bourse:
    def construction(self):
        self.cout = 4000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'quartier_financier'
        self.temps_construction = 8
        self.augmente = 'commerce 2000'




class artisan:
    def construction(self):
        self.cout = 750
        self.nombre_construit = 0
        self.rapporte = 500
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'none'


class atelier:
    def construction(self):
        self.cout = 1250
        self.nombre_construit = 0
        self.rapporte = 750
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'artisan'
        self.temps_construction = 4
        self.augmente = 'none'

class fabrique:
    def construction(self):
        self.cout = 2250
        self.nombre_construit = 0
        self.rapporte = 1000
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'atelier'
        self.temps_construction = 6
        self.augmente = 'none'



class usine:
    def construction(self):
        self.cout = 5000
        self.nombre_construit = 0
        self.rapporte = 2500
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'fabrique'
        self.temps_construction = 8
        self.augmente = 'none'


class bureau_recrutement:
    def construction(self):
        self.cout = 500
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'infanterie'


class caserne:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'bureau_recrutement'
        self.temps_construction = 4
        self.augmente = 'infanterie'


class coll??ge_millitaire:
    def construction(self):
        self.cout = 2000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'caserne'
        self.temps_construction = 6
        self.augmente = 'infanterie'
        
        
class acad??mie_infanterie:
    def construction(self):
        self.cout = 4000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'coll??ge_millitaire'
        self.temps_construction = 8
        self.augmente = 'infanterie'




class poste_assemblage:
    def construction(self):
        self.cout = 750
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'blind??'
        
        
class atelier_m??canique:
    def construction(self):
        self.cout = 1250
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'poste_asemblage'
        self.temps_construction = 4
        self.augmente = 'blind??'
        
        
class fabrique_de_blind??:
    def construction(self):
        self.cout = 2250
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'atelier_m??canique'
        self.temps_construction = 6
        self.augmente = 'blind??'
        
        
class usine_lourde:
    def construction(self):
        self.cout = 5000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'fabrique_de_blind??'
        self.temps_construction = 8
        self.augmente = 'blind??'       

		
		
class atelier_maritime:
    def construction(self):
        self.cout = 750
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'bateau'



class port:
    def construction(self):
        self.cout = 1250
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'atelier_maritime'
        self.temps_construction = 4
        self.augmente = 'bateau'

class port_militaire:
    def construction(self):
        self.cout = 2250
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'port'
        self.temps_construction = 6
        self.augmente = 'bateau'


class chantier_naval:
    def construction(self):
        self.cout = 5000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'port_militaire'
        self.temps_construction = 8
        self.augmente = 'bateau'
		
class poste_fronti??re:
    def construction(self):
        self.cout = 500
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'd??fense'

class fronti??re_s??curis??e:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'poste_fronti??re'
        self.temps_construction = 4
        self.augmente = 'd??fense'
		
class fronti??re_ferm??e:
    def construction(self):
        self.cout = 2000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'fronti??re_s??curis??e'
        self.temps_construction = 6
        self.augmente = 'd??fense'



class ligne_d??fense:
    def construction(self):
        self.cout = 4000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'fronti??re_ferm??e'
        self.temps_construction = 8
        self.augmente = 'd??fense'

class piste_atterrissage:
    def construction(self):
        self.cout = 750
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'avion'

class relais_a??rien:
    def construction(self):
        self.cout = 1250
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'piste_atterrissage'
        self.temps_construction = 4
        self.augmente = 'avion'


class a??roport_militaire:
    def construction(self):
        self.cout = 2250
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'relais_a??rien'
        self.temps_construction = 6
        self.augmente = 'avion'


class base_a??rienne:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'a??roport_militaire'
        self.temps_construction = 8
        self.augmente = 'avion'



class voie_a_pied:
    def construction(self):
        self.cout = 250
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'ravittaillement'
		
class route_terre:
    def construction(self):
        self.cout = 500
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'voie_a_pied'
        self.temps_construction = 4
        self.augmente = 'ravittaillement'

class route_goudronn??e:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 6
        self.augmente = 'ravittaillement'
		
class chemin_fer:
    def construction(self):
        self.cout = 5000
        self.nombre_construit = 0
        self.rapporte = 0
        self.materiaux_spec = 'none'
        self.case_spec = 'none'
        self.need = 'none'
        self.temps_construction = 8
        self.augmente = 'ravittaillement'

class mine_fer:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 250
        self.materiaux_spec = 'none'
        self.case_spec = 'fer'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'commerce'
		
class aci??rie:
    def construction(self):
        self.cout = 3000
        self.nombre_construit = 0
        self.rapporte = 500
        self.materiaux_spec = 'none'
        self.case_spec = 'fer'
        self.need = 'mine_fer'
        self.temps_construction = 4
        self.augmente = 'commerce'

class usine_sid??rurgique:
    def construction(self):
        self.cout = 5000
        self.nombre_construit = 0
        self.rapporte = 750
        self.materiaux_spec = 'none'
        self.case_spec = 'fer'
        self.need = 'aci??rie'
        self.temps_construction = 6
        self.augmente = 'commerce'

		
class mine_or:
    def construction(self):
        self.cout = 1500
        self.nombre_construit = 0
        self.rapporte = 250
        self.materiaux_spec = 'none'
        self.case_spec = 'or'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'commerce'
		
class fonderie:
    def construction(self):
        self.cout = 4000
        self.nombre_construit = 0
        self.rapporte = 500
        self.materiaux_spec = 'none'
        self.case_spec = 'or'
        self.need = 'mine_or'
        self.temps_construction = 4
        self.augmente = 'commerce'

class usine_traitement_aurif??re:
    def construction(self):
        self.cout = 6500
        self.nombre_construit = 0
        self.rapporte = 750
        self.materiaux_spec = 'none'
        self.case_spec = 'or'
        self.need = 'fonderie'
        self.temps_construction = 6
        self.augmente = 'commerce'
		
class mine_cuivre:
    def construction(self):
        self.cout = 1000
        self.nombre_construit = 0
        self.rapporte = 250
        self.materiaux_spec = 'none'
        self.case_spec = 'cuivre'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'commerce'
		
class raffinerie_m??tallurgique:
    def construction(self):
        self.cout = 3000
        self.nombre_construit = 0
        self.rapporte = 500
        self.materiaux_spec = 'none'
        self.case_spec = 'cuivre'
        self.need = 'mine_cuivre'
        self.temps_construction = 4
        self.augmente = 'commerce'

class forge:
    def construction(self):
        self.cout = 5000
        self.nombre_construit = 0
        self.rapporte = 750
        self.materiaux_spec = 'none'
        self.case_spec = 'cuivre'
        self.need = 'raffinerie_m??tallurgique'
        self.temps_construction = 6
        self.augmente = 'commerce'

class puits_p??trole:
    def construction(self):
        self.cout = 1250
        self.nombre_construit = 0
        self.rapporte = 250
        self.materiaux_spec = 'none'
        self.case_spec = 'petrole'
        self.need = 'none'
        self.temps_construction = 2
        self.augmente = 'commerce'
		
class excavation:
    def construction(self):
        self.cout = 3500
        self.nombre_construit = 0
        self.rapporte = 500
        self.materiaux_spec = 'none'
        self.case_spec = 'petrole'
        self.need = 'puits_p??trole'
        self.temps_construction = 4
        self.augmente = 'commerce'		
class raffinerie:
    def construction(self):
        self.cout = 6000
        self.nombre_construit = 0
        self.rapporte = 750
        self.materiaux_spec = 'none'
        self.case_spec = 'petrole'
        self.need = 'excavation'
        self.temps_construction = 6
        self.augmente = 'commerce'	

"""Cr??ation des unit??s KURAVES"""
""" D??but des unit??s d'infanterie"""
class milice_imperiale:
    def initialisation_stats(self, nom):
            self.points_de_vie = 20
            self.precision = 65
            self.degat_infanterie = 15
            self.degat_char = 0
            self.portee = 3
            self.visibilit?? = 4
            self.nombre_de_membre = 50
            self.blindage = 0
            self.d??fense = 20
            self.couverture = 70
            self.point_de_mouvement = 4
            self.vitesse_d??placement = 80
            self.nombre_de_tir = 2
            self.munitions = 150
            self.plan_de_vie = 1
            self.tractation = 0
            self.cout = 400
            self.materiaux_speciaux = 00
            self.technologie_requise = 00
            self.moral = 2500
            self.experience = 00
            self.niveaux_experience = 00
            self.position = 10
            self.consommation_munitions = 00
            self.case_x= 10
            self.case_y= 0            
            self.tour_presence = 10
            self.type = nom
            self.classe = 'infanterie'
			
            
class fusiliers:
   def initialisation_stats(self, nom):
         self.points_de_vie = 60
         self.precision = 75
         self.degat_infanterie = 20
         self.degat_char = 0
         self.portee = 2
         self.visibilit?? = 3
         self.nombre_de_membre = 30
         self.blindage = 0
         self.d??fense = 15
         self.couverture = 60
         self.point_de_mouvement = 2
         self.vitesse_d??placement = 60
         self.nombre_de_tir = 1
         self.munitions = 80
         self.plan_de_vie = 1
         self.tractation = 00
         self.cout = 600
         self.materiaux_speciaux = 00
         self.technologie_requise = 00
         self.moral = 2500
         self.experience = 00
         self.niveaux_experience = 00
         self.position = 10
         self.consommation_munitions = 00
         self.case_x= 10
         self.case_y= 0         
         self.tour_presence = 10
         self.type = nom
         self.classe = 'infanterie'

            
class grenadier:
    def initialisation_stats(self, nom):
         self.points_de_vie = 75
         self.precision = 80
         self.degat_infanterie = 30
         self.degat_char = 10
         self.portee = 2
         self.visibilit?? = 2
         self.nombre_de_membre = 20
         self.blindage = 1
         self.d??fense = 10
         self.couverture = 45
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 40
         self.nombre_de_tir = 1
         self.munitions = 80
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 600
         self.materiaux_speciaux = 00
         self.technologie_requise = 00
         self.moral = 2500
         self.experience = 00
         self.niveaux_experience = 00
         self.position = 10
         self.consommation_munitions = 00
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 10
         self.type = nom
         self.classe = 'infanterie'
         
         
class jager:
   def initialisation_stats(self, nom):
         self.points_de_vie = 42
         self.precision = 100
         self.degat_infanterie = 80
         self.degat_char = 5
         self.portee = 4
         self.visibilit?? = 5
         self.nombre_de_membre = 2
         self.blindage = 0
         self.d??fense = 60
         self.couverture = 75
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 90
         self.nombre_de_tir = 1
         self.munitions = 40
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 25000
         self.materiaux_speciaux = 00
         self.technologie_requise = 00
         self.moral = 2500
         self.experience = 00
         self.niveaux_experience = 00
         self.position = 10
         self.consommation_munitions = 00
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 10
         self.type = nom
         self.classe = 'infanterie'

class tete_de_charge:
   def initialisation_stats(self, nom):
         self.points_de_vie = 20
         self.precision = 60
         self.degat_infanterie = 15
         self.degat_char = 0
         self.portee = 2
         self.visibilit?? = 3
         self.nombre_de_membre = 1
         self.blindage = 0
         self.d??fense = 20
         self.couverture = 40
         self.point_de_mouvement = 4
         self.vitesse_d??placement = 60
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 650
         self.materiaux_speciaux = 0
         self.technologie_requise = 0
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 1
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'
         
class eclaireur:
   def initialisation_stats(self, nom):
         self.points_de_vie = 40
         self.precision = 25
         self.degat_infanterie = 10
         self.degat_char = 0
         self.portee = 10
         self.visibilit?? = 5
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 10
         self.couverture = 60
         self.point_de_mouvement = 4
         self.vitesse_d??placement = 60
         self.nombre_de_tir = 1
         self.munitions = 40
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 350
         self.materiaux_speciaux = 0
         self.technologie_requise = 0
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 1
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'
         
         



class fusilier_de_la_garde:
   def initialisation_stats(self, nom):
         self.points_de_vie = 60
         self.precision = 60
         self.degat_infanterie = 15
         self.degat_char = 4
         self.portee = 2
         self.visibilit?? = 3
         self.nombre_de_membre = 50
         self.blindage = 0
         self.d??fense = 10
         self.couverture = 40
         self.point_de_mouvement = 2
         self.vitesse_d??placement = 40
         self.nombre_de_tir = 1
         self.munitions = 100
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1500
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 1
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'
         
class grenadier_lourds:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe ='infanterie'
         
class lieutenant:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'
         
class officier_senior:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'
         
class officier_communication:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'
         
class rustungschreck:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'     

class pionnier:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'


class mitrailleuse_sokolov:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'
         

class officier_imperiaux:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'infanterie'

"""Cr??ation des CHARS"""
class rustungmobil:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'char'
         
         

class getter:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'char'
         

class nashorn:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'char'

class hummel:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'char'

class kazak:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe ='char'

class wespe:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'char'         
         
         
         
class mammut:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'char'
        

class titantoter:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'char'
         
class behemot:
   def initialisation_stats(self, nom):
         self.points_de_vie = 80
         self.precision = 60
         self.degat_infanterie = 20
         self.degat_char = 9
         self.portee = 1
         self.visibilit?? = 2
         self.nombre_de_membre = 50
         self.blindage = 3
         self.d??fense = 10
         self.couverture = 30
         self.point_de_mouvement = 1
         self.vitesse_d??placement = 30
         self.nombre_de_tir = 2
         self.munitions = 10
         self.plan_de_vie = 1
         self.tractation = 0
         self.cout = 1750
         self.materiaux_speciaux = 0
         self.technologie_requise = 1
         self.moral = 500
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 0
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'char'
         

         
""" Cr??ation des unit??s d'artillerie""" 

class kugelwerfer:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'artillerie'
         

class rustungbrecher:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'artillerie'
         
         
class eric_nikolai:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'artillerie'


class madgebern_nikolai:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'artillerie'
         
class lance_fusee:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'artillerie'
         
"""Cr??ation des unit??s de Marine"""

class naizer:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'marine'
         
class zuka:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'marine'
         
class loch:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'marine'
         
         
class rugboot:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'marine'
         

class gewitter:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'marine'


class sturm:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'marine'

class hurrikan:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'marine'


class baron:
       def initialisation_stats(self, nom):
         self.points_de_vie = 12
         self.precision = 20
         self.degat_infanterie = 80
         self.degat_char = 80
         self.portee = 3
         self.visibilit?? = 1
         self.nombre_de_membre = 20
         self.blindage = 0
         self.d??fense = 0
         self.couverture = 1
         self.point_de_mouvement = 0.01
         self.vitesse_d??placement = 1
         self.nombre_de_tir = 1
         self.munitions = 20
         self.plan_de_vie = 1
         self.tractation = 1
         self.cout = 2500
         self.materiaux_speciaux = 0
         self.technologie_requise = ''
         self.moral = 0
         self.experience = 0
         self.niveaux_experience = 0
         self.position = 0
         self.consommation_munitions = 0
         self.case_x= 10
         self.case_y= 0
         self.tour_presence = 0
         self.type = nom
         self.classe = 'marine'

		 
		 
"""Cr??ation des b??timents"""		 
         
		 

"""Fonction du combat + pertes """

def combat(unit??1, unit??2):
    if unit??1.classe == 'infanterie' and unit??2.classe == 'infanterie':
        distance = math.sqrt(((unit??2.case_x - unit??1.case_x)**2) +((unit??2.case_y - unit??1.case_y)**2))
        tir1 = 0
        tir2 = 0
    
        #test de port??e
        if distance >unit??1.portee and distance >unit??2.portee:
            print(unit??2.type  + ' est trop loin!!!')
        
        elif distance <= unit??1.portee and distance<= unit??2.portee: #si les deux port??es sont bonnes
        
        
            defense1 = (unit??1.d??fense * unit??1.couverture)% unit??1.vitesse_d??placement + unit??1.blindage
            defense2 = (unit??2.d??fense * unit??2.couverture)% unit??2.vitesse_d??placement + unit??2.blindage
            nombre_depart1 = unit??1.nombre_de_membre
            nombre_depart2 = unit??2.nombre_de_membre
            tir1 = ((unit??1.precision/100) * unit??1.degat_char * unit??1.nombre_de_tir * unit??1.nombre_de_membre)-defense2
    
            if tir1 <0: #v??rification du tir1
                tir1 = 0
                #Emp??che d'avoir des tirs n??gatifs
            else:
                unit??2.nombre_de_membre = unit??2.nombre_de_membre - int(tir1/unit??2.points_de_vie)
                    # print(defense1)
    
            if unit??2.nombre_de_membre  <=0:
                print(unit??2.type+ ' morte!!!!')
                
            elif unit??2.nombre_de_membre >0:
				#l'unit??2 tire
                tir2 = ((unit??2.precision/100) * unit??2.degat_char * unit??2.nombre_de_tir * unit??2.nombre_de_membre)-defense1
        
                       if tir2 <0: #v??rification du tir2
					tir2 = 0
				unit??1.nombre_de_membre = unit??1.nombre_de_membre - int(tir2/unit??1.points_de_vie)
           
				morts1 = nombre_depart1 - unit??1.nombre_de_membre
				morts2 = nombre_depart2 - unit??2.nombre_de_membre

				if unit??1.nombre_de_membre <= 0:
					print(unit??1.type+' est mort!')
            
				elif unit??1.nombre_de_membre >0:
                    print(unit??1.type +' a perdu '+ str(morts1) +' membres!!!!')
            
            
                print(unit??2.type+' a perdu '+ str(morts2) +' membres!!!')
                
                
        elif distance <= unit??1.portee and distance > unit??2.portee: #Si l'unit?? 2 est dans la port??e de l'unit??1
            defense2 = (unit??2.d??fense * unit??2.couverture)% unit??2.vitesse_d??placement + unit??2.blindage
            nombre_depart2 = unit??2.nombre_de_membre
            tir1 = ((unit??1.precision/100) * unit??1.degat_char * unit??1.nombre_de_tir * unit??1.nombre_de_membre)-defense2
            
            if tir1 <0: #v??rification du tir1
                tir1 = 0
                #Emp??che d'avoir des tirs n??gatifs
    
            unit??2.nombre_de_membre = unit??2.nombre_de_membre - int(tir1/unit??2.points_de_vie)
            morts2 = nombre_depart2 - unit??2.nombre_de_membre

            if unit??2.nombre_de_membre  <=0:
                print(unit??2.type+ ' morte!!!!')
            else:
                print(unit??2.type+' a perdu '+ str(morts2) +' membres!!!')
                
            
        elif distance > unit??1.portee and distance <= unit??2.portee: #Si l'unit?? 1 est dans la port??e de l'unit??2
            defense1 = (unit??1.d??fense * unit??1.couverture)% unit??1.vitesse_d??placement + unit??1.blindage
            tir2 = ((unit??2.precision/100) * unit??2.degat_char * unit??2.nombre_de_tir * unit??2.nombre_de_membre)-defense1
        
            if tir2 < 0:
                tir2 = 0
                
			nombre_depart1 = unit??1.nombre_de_membre
			unit??1.nombre_de_membre = unit??1.nombre_de_membre - int(tir2/unit??1.points_de_vie)
			morts1 = nombre_depart1 - unit??1.nombre_de_membre

			if unit??1.nombre_de_membre  <=0:
				print(unit??1.type+ ' morte!!!!')
			else:
				print(unit??1.type+' a perdu '+ str(morts1) +' membres!!!')
    
    elif unit??1.classe == 'char' and unit??2.classe == 'char':
        distance = math.sqrt(((unit??2.case_x - unit??1.case_x)**2) +((unit??2.case_y - unit??1.case_y)**2))
        tir1 = 0
        tir2 = 0
    
        #test de port??e
        if distance >unit??1.portee and distance >unit??2.portee:
            print(unit??2.type  + ' est trop loin!!!')
        
        elif distance <= unit??1.portee and distance<= unit??2.portee: #si les deux port??es sont bonnes
        
        
            defense1 = (unit??1.d??fense * unit??1.couverture)% unit??1.vitesse_d??placement + unit??1.blindage
            defense2 = (unit??2.d??fense * unit??2.couverture)% unit??2.vitesse_d??placement + unit??2.blindage
            nombre_depart1 = unit??1.nombre_de_membre
            nombre_depart2 = unit??2.nombre_de_membre
            tir1 = ((unit??1.precision/100) * unit??1.degat_char * unit??1.nombre_de_tir * unit??1.nombre_de_membre)-defense2
    
            if tir1 <0: #v??rification du tir1
                tir1 = 0
                #Emp??che d'avoir des tirs n??gatifs
            else:
                unit??2.nombre_de_membre = unit??2.nombre_de_membre - int(tir1/unit??2.points_de_vie)
                    # print(defense1)
    
            if unit??2.nombre_de_membre  <=0:
                print(unit??2.type+ ' morte!!!!')
                
            elif unit??2.nombre_de_membre >0:
                tir2 = ((unit??2.precision/100) * unit??2.degat_char * unit??2.nombre_de_tir * unit??2.nombre_de_membre)-defense1
        
            if tir2 <0: #v??rification du tir2
                tir2 = 0
            unit??1.nombre_de_membre = unit??1.nombre_de_membre - int(tir2/unit??1.points_de_vie)
           
            morts1 = nombre_depart1 - unit??1.nombre_de_membre
            morts2 = nombre_depart2 - unit??2.nombre_de_membre

            if unit??1.nombre_de_membre <= 0:
                print(unit??1.type+' est mort!')
            
            elif unit??1.nombre_de_membre >0:
                    print(unit??1.type +' a perdu '+ str(morts1) +' membres!!!!')
            
            if unit??2.nombre_de_membre >0:
                print(unit??2.type+' a perdu '+ str(morts2) +' membres!!!')
                
                
        elif distance <= unit??1.portee and distance > unit??2.portee: #Si l'unit?? 2 est dans la port??e de l'unit??1
            defense2 = (unit??2.d??fense * unit??2.couverture)% unit??2.vitesse_d??placement + unit??2.blindage
            nombre_depart2 = unit??2.nombre_de_membre
            tir1 = ((unit??1.precision/100) * unit??1.degat_char * unit??1.nombre_de_tir * unit??1.nombre_de_membre)-defense2
            
            if tir1 <0: #v??rification du tir1
                tir1 = 0
                #Emp??che d'avoir des tirs n??gatifs
    
            unit??2.nombre_de_membre = unit??2.nombre_de_membre - int(tir1/unit??2.points_de_vie)
            morts2 = nombre_depart2 - unit??2.nombre_de_membre

            if unit??2.nombre_de_membre  <=0:
                print(unit??2.type+ ' morte!!!!')
            else:
                print(unit??2.type+' a perdu '+ str(morts2) +' membres!!!')
                
            
        elif distance > unit??1.portee and distance <= unit??2.portee: #Si l'unit?? 1 est dans la port??e e l'unit??2
            defense1 = (unit??1.d??fense * unit??1.couverture)% unit??1.vitesse_d??placement + unit??1.blindage
            tir2 = ((unit??2.precision/100) * unit??2.degat_char * unit??2.nombre_de_tir * unit??2.nombre_de_membre)-defense1
        
            if tir2 < 0:
                tir2 = 0
                
            nombre_depart1 = unit??1.nombre_de_membre
            unit??1.nombre_de_membre = unit??1.nombre_de_membre - int(tir2/unit??1.points_de_vie)
            morts1 = nombre_depart1 - unit??1.nombre_de_membre

			if unit??1.nombre_de_membre  <=0:
				print(unit??1.type+ ' morte!!!!')
			else:
				print(unit??1.type+' a perdu '+ str(morts1) +' membres!!!')
    
   
    
""" Fin du combat """


"""D??placement"""



def deplacement(unit??, case):
	distance = sqrt((unit??.case_x-case.case_x)**2 + (unit??.case_y - case.case_y)**2)
	if distance> unit??.point_de_mouvement:
		print('La distance est trop grande')
		
	else:
		unit??.case_x = case.case_x
		unit??.case_y = case.case_y
		unit??.point_de_mouvement = unit??.point_de_mouvement- int(distance)
		print(unit??.type + ' as boug?? de '+ int(distance))

	
	
	
"""Cr??ation d'une unit??"""
def creation(nom, classe):
    nom = classe
    nom.initialisation_stats(nom, classe)


"""Cr??ation  de quelques unit??s test"""
paul = grenadier
paul.initialisation_stats(paul, 'grenadier')
paul.case_x = 0
paul.case_y = 0
paul.portee = 11

poney = grenadier_lourds
poney.initialisation_stats(poney, 'grenadier lourds')
poney.case_y = 10
poney.case_x = 0


mark = fusiliers
mark.initialisation_stats(mark, 'infanterie_legere')

thomas = jager
thomas.initialisation_stats(thomas, 'tireur d\'??lite')

docteur_swagg = fusilier_de_la_garde
docteur_swagg.initialisation_stats(docteur_swagg, 'infanterie')
"""Fin des test """


def cration(nom, classe):
    nom = classe
    nom.inisialisation_stats(nom, classe)


""" D??but de l\interface graphique"""



fenetre = tkinter.Tk()
fenetre.geometry("500x220")
fenetre.title("L\'Hiver Rouge")


affichage = tkinter.Label(fenetre, text="Donnez le nom de l'unit?? ", width=30 )
antoine = tkinter.Entry(fenetre)
affichage2 = tkinter.Label(fenetre, text="Donnez la classe de l'unit?? ", width=30 )
miguel = tkinter.Entry(fenetre)
bouton_combat = tkinter.Button(fenetre,text="Cr??ation!", command = creation ,width=20)
resulat = tkinter.Label(fenetre, text = '', width = 30)
affichage.place(x = 1, y=100)
antoine.place(x = 1, y = 150)
affichage2.place(x = 1, y = 200)
miguel.place(x = 1, y= 250)
bouton_combat.place(x=1,y=300)
resulat.place(x = 1, y = 350)




class Interface(Frame):
    
    """Notre fen??tre principale.
    Tous les widgets sont stock??s comme attributs de cette fen??tre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=450, **kwargs)
        self.place(fenetre,x=640, y=450 )        
        
    
    def cliquer_sur_unit??(self):
        """Il y a eu un clic sur le bouton.
        
        On change la valeur du label message."""
        











































fenetre.mainloop())