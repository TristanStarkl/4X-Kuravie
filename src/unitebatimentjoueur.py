# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:04:27 2015

@author: t..rety
"""

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
    self.initialisation_stats
        
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
    self.initialisation_stats


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
    self.initialisation_stats

		 
		 
"""Cr??ation des b??timents"""		 
         
