AWQDEC
Regardez le fichier config.txt pour vérifier que le clavier par défaut correspond à votre clavier
Sinon, entrez les lettres des 4 lignes principales de votre clavier

Par exemple, pour un clavier Français :
&é"'(-è_çà
azertyuiop
qsdfghjklm
wxcvbn,;:!

Pour lancer l'interpréteur : python awqdec.py
Attention, pour l'instant ne fonctionne qu'avec un terminal de largeur 80!
Il vous sera ensuite demandé d'entrer une commade : par exemple, copiez-collez une des commandes suivantes :
(version clavier FR)
HELLO
\&ze' a&wqd"c b(è(tutb, ç >&wc (b, o >a éaqxdeé \&zer bb \&ze g( >p a>p a >p a >p a
CBNA
\&ze "éaqxc b(-yj,b : >w&v' n_: jk ! >w \aéer e >w qz'(yh-çlnbvcstge \aée' ezqs n \&zer >ènb- & >! & >: a >p a
Poisson sous la mer :
\&éer & w>& w!>w!>w! \aé"' à>! à&>à&>à& ap>ap>ap \az"r mq>mq>mq >& \&ze' hbvdrthu,h >q m>q \aéer vgr( ;li>m q>m a>! &

(version clavier BE)
Smiley
\&ée "q>&w>&dh!>w&>h'& \aée qw fv >è \&ze jnbf >= & >=



Chaque touche du clavier correspond à une position
Dessiner : entrer successivement les touches du clavier qui correspondent à ce que vous voulez dessiner
Par exemple : cbtec dessine un carré
Soulever le "crayon" : espace. 
Par exemple : cb te dessine deux lignes
Par exemple : cc bb tt ee dessine quatre points

Changer de Couleur : \azer azer étant le code couleur terminal RGBL 
Par exemple : \&ze est rouge parce que la 1re colonne (rouge) est plus haut
Par exemple : \&ée' est jaune (clair) car rouge et vert son haut, et la 4e colonne est haut
Par exemple : \&éer est jaune foncé parce que le 4e caractère (optionnel) est bas

Vitesse : +w w étant une valeur de la ligne du bas, ! (ou =) tout à droite étant instantané
w (tout à gauche) étant le plus lent. 
(/!\ pour l'instant ne sert qu'à mettre des pauses entre les actions)

Changer les origines :
>a décide que le point actuel est a
Utile pour faire des sauts relatifs, par exemple >a p >a saute un écran à droite