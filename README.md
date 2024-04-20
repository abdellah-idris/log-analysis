# Rapport Test et Vérification

# 1. Crane
Durant cette exercice nous allons analysé des fichiers representant la postion de différents marquers.

## EDA
On anylisant les deux fichiers on remraque que le nombre de valeur de MarkersValid a False est significativement plus petit que les valeurs a True.

![img](<TPnote/TPnote/1. Crane/images/LpsData_TILsts_Count of MarkersValid_Values.png>)
![img](<TPnote/TPnote/1. Crane/images/sts405_count_MarkesrsValid.png>)

## Observation des marqueurs:
On visualisant les changement de position des 3 marquers, on remarque la présence d'une modification brusque et subite de la postion d'un ou plusieurs marquers. la forme tirnagulaire ne persiste plus vraiment a certain moment.

Si la vidéo ne marche pas vous y avait accées dans le dossier video sous le nom de tracker.mp4 


<video width="320" height="240" controls>
  <source src="TPnote/TPnote/1. Crane/video/tracker.mp4" type="video/mp4">
</video>

## Features
Dans le but d'améliorer le modéles, plusieurs features sont mise en place:
    -   **Vitesse des marqueurs**: la vittesse est calculé selon la formule de la distance, on peut supposer que les déplacements a des vitesses différentes des différent marquers permetrra didentifier des logs erroné.
    -   **Déplacement des marqueurs** selon l'axe x et y : On réalise une soustraction entre m1[i] et m1[i+1] sur l'axe x et y afin d'avoir l'information sur le taux de dépalacement. 
    -   Calcule de la **surface du trinagle**: Variable ajouté sans observation précise, remarqué.

## Affichage de la matrice de correlation
   -  LpsData_STS405b :
        -   Il y a une forte correlation entre TrolleyPos et les position sur l'axe y de m1,m2 et m3 avec une valeurs de -0.89
        -   La position des marqueurs  selon l'axe x et y est fortement corrélé  (m1_x foretemnt corrélé avec m1_y)
        -   TrolleyPos est moyennement corrélé avec MarkersValid
        -   Les vitesses des marqueurs présente une correlation moyenne entre eux avec des valeurs avoisinent 0.5

      ![img](<TPnote/TPnote/1. Crane/images/correlation_matrix_df_LpsData_STS405b.png>)


   - LpsData_TILsts :
        -   TrolleyPos est moyennement corrélé avec Hoistpos, et ne présenta pas de corrélation avec MarkersValid
        -   Les vitesses des marqueurs présente une correlation forte entre eux avec des valeurs avoisinent 0.9
        -   La supérficie du tringle formé par les marqueurs est moyennement corélé avec les vitesses
        -   La position des marqueurs  selon l'axe x et y est moyennement corrélé  (m1_x moyennement corrélé avec m1_y)

      ![img](<TPnote/TPnote/1. Crane/images/Correlation Heatmap df_LpsData_TILsts.png>)     

## Détection des erreurs : Résultats

  - **LpsData_TILsts :**
    - without speed
        - Logistic Regression: Accuracy - 0.948
        - Random Forest: Accuracy - 0.969
        - Support Vector Machine: Accuracy - 0.948
        - Gradient Boosting Classifier: Accuracy - 0.952

    - with speed
        - Logistic Regression: Accuracy - 0.948
        - Random Forest: Accuracy - 0.921
        - Support Vector Machine: Accuracy - 0.948
        - Gradient Boosting Classifier: Accuracy - 0.930

    - All feature
        - Logistic Regression: Accuracy - 0.948
        - Random Forest: Accuracy - 0.939
        - Support Vector Machine: Accuracy - 0.948
        - Gradient Boosting Classifier: Accuracy - 0.939

- **LpsData_STS405b :**
    - without speed
        - Logistic Regression: Accuracy - 0.744
        - Random Forest: Accuracy - 0.889
        - Support Vector Machine: Accuracy - 0.749
        - Gradient Boosting Classifier: Accuracy - 0.815

    - with speed
        - Logistic Regression: Accuracy - 0.749
        - Random Forest: Accuracy - 0.739
        - Support Vector Machine: Accuracy - 0.749
        - Gradient Boosting Classifier: Accuracy - 0.736

    - All feature
        - Logistic Regression: Accuracy - 0.761
        - Random Forest: Accuracy - 0.815
        - Support Vector Machine: Accuracy - 0.749
        - Gradient Boosting Classifier: Accuracy - 0.786


## Analyse des resultats: 
En examinant les rapports de classification, nous pouvons observer les performances des divers modèles d'apprentissage automatique entraînés sur nos ensembles de données, avec et sans l'inclusion des différéntes caractéristiques  vitesse, déplacement et surface. Voici ce que nous avons remarqué :

   **Régression logistique :**

   La régression logistique présente des performances similaires pour les deux ensembles de données, qu'elles contiennent ou non les caractéristiques de vitesse.
   Les résultats montrent une difficulté du modèle à bien classifier les instances de la classe 0 (MarkersValid : False), ce qui se traduit par des scores de précision, de rappel et de F1 relativement faibles pour cette classe.
   En revanche, le modèle se comporte bien dans la classification de la classe 1 (MarkersValid : True), avec des scores de précision, de rappel et de F1 élevés.

   **Random Forest :**
   Sans les caractéristiques de vitesse, le modèle Random Forest obtient une précision plus élevée que la régression logistique pour les deux ensembles de données.
   L'introduction des caractéristiques de vitesse entraîne une légère baisse de la précision, surtout pour l'ensemble de données LpsData_STS405b.
   Globalement, le modèle Random Forest donne de bons résultats dans la classification des deux classes, avec des scores de précision, de rappel et de F1 relativement élevés pour chacune.

   **Machine à vecteurs de support (SVM) :**

   Les performances de SVM sont comparables à celles de la régression logistique, montrant des résultats similaires en termes de précision et de mesure de performance.
   Toutefois, comme la régression logistique, SVM éprouve des difficultés à classifier correctement les instances de la classe 0 (MarkersValid : False), ce qui entraîne des scores de précision, de rappel et de F1 plus bas pour cette classe.

   **Gradient Boosting Classifier :**

   Le Gradient Boosting Classifier se comporte bien en termes de précision, en particulier pour l'ensemble de données LpsData_STS405b.
   Ce modèle affiche une performance équilibrée dans la classification des deux classes, avec des scores de précision, de rappel et de F1 relativement élevés pour chacune.

 **Conclusion**
Les modèles Random Forest et Gradient Boosting ont tendance à mieux performer que la régression logistique et SVM en termes de précision et de performance équilibrée sur les deux classes. Cependant, l'ajout des caractéristiques de vitesse n'améliore pas systématiquement les performances de ces modèles, et dans certains cas, cela conduit même à une légère diminution de la précision. Cela suggère que les caractéristiques de vitesse ne fournissent pas nécessairement d'informations supplémentaires significatives pour la tâche de classification.


# 2. Trafic

Durant cette exercice nous allons effectué une analyse des packets réseau. Dans l'objectif est d'identifier les sessions en erreurs.

## Carectéristic du trafic
En premier lieu nous allons analyser les packets dans WireShark afin d'identifier les caractéristique des deux fichiers.

   -  capture 1
![alt text](<TPnote/TPnote/2. Traffic réseau/images/capture1.png>)

   -  capture 2
![alt text](<TPnote/TPnote/2. Traffic réseau/images/capture2.png>)

   On remarque que le nombre de packets dans le fichier de capture 2 est  supérieurs au packets de la capture 1. Par contre en moyenne les packets de la capture 1 sont supérieurs en terme de taille.


## Extraction des caractéristique avec python & clustering
   -  **packets**

      -  **Informations**
         ![img](<TPnote/TPnote/2. Traffic réseau/images/packets/informations.png>)

      -  **Clustering**
         ![img](<TPnote/TPnote/2. Traffic réseau/images/packets/cluster1.png>)
         ![img](<TPnote/TPnote/2. Traffic réseau/images/packets/cluster2.png>)
         ![img](<TPnote/TPnote/2. Traffic réseau/images/packets/cluster3.png>)
         ![img](<TPnote/TPnote/2. Traffic réseau/images/packets/cluster4.png>)

   -  **sessions**
      -  **Informations**
         ![img](<TPnote/TPnote/2. Traffic réseau/images/session/informations.png>)
      
      - **Clustering**
         ![img](<TPnote/TPnote/2. Traffic réseau/images/session/cluster1.png>)
         ![img](<TPnote/TPnote/2. Traffic réseau/images/session/cluster2.png>)
         ![img](<TPnote/TPnote/2. Traffic réseau/images/session/cluster3.png>)
         ![img](<TPnote/TPnote/2. Traffic réseau/images/session/cluster4.png>)
   
   Avec le Clustering, on remarque la separation des différentes classe pour l'esnsembles des variables utilisées.
   

## Détection d'anomalie
   - Afin de reconnaintre les paquets en erreurs nous allons utiliser un filtre "tcp.analysis.flags". Ce dernier permet de récupérer les packets TCP  présenantant des anomalies.

   - **Filtre**: ((((((((((((((tls.record.length.invalid) || (dns.retransmit_request)) || (quic.decryption_failed)) || (dns.retransmit_response)) || (dns.retransmit_request)) || (tls.ignored_unknown_record)) || (tcp.analysis.ack_lost_segment)) || (esp.sequence-analysis.wrong-sequence-number)) || (quic.coalesced_padding_data)) || (quic.retransmission)) || (tcp.options.sack_perm.absent)) || (tcp.analysis.duplicate_ack)) || (tcp.connection.syn)) || (http.chat)) || (http.chat)

   -  Nous procédent ensuite à la détection des anomalies dans l'ensemble des session. 



## **Résulats**

   **Logistic Regression:**
   |     | precision | recall | f1-score | support |
   |-----|-----------|--------|----------|---------|
   | 0   | 0.97      | 1.00   | 0.98     | 536     |
   | 1   | 1.00      | 0.05   | 0.10     | 19      |
   |-----|-----------|--------|----------|---------|
   | accuracy |           |        | 0.97     | 555     |
   | macro avg| 0.98      | 0.53   | 0.54     | 555     |
   | weighted avg | 0.97  | 0.97   | 0.95     | 555     |

   **SVM:**
   |     | precision | recall | f1-score | support |
   |-----|-----------|--------|----------|---------|
   | 0   | 0.97      | 1.00   | 0.98     | 536     |
   | 1   | 0.00      | 0.00   | 0.00     | 19      |
   |-----|-----------|--------|----------|---------|
   | accuracy |           |        | 0.97     | 555     |
   | macro avg| 0.48      | 0.50   | 0.49     | 555     |
   | weighted avg | 0.93  | 0.97   | 0.95     | 555     |

   **Random Forest:**
   |     | precision | recall | f1-score | support |
   |-----|-----------|--------|----------|---------|
   | 0   | 0.98      | 0.97   | 0.98     | 536     |
   | 1   | 0.38      | 0.47   | 0.42     | 19      |
   |-----|-----------|--------|----------|---------|
   | accuracy |           |        | 0.95     | 555     |
   | macro avg| 0.68      | 0.72   | 0.70     | 555     |
   | weighted avg | 0.96  | 0.95   | 0.96     | 555     |

   
## **Analyse**

   Basé sur le rapport de classification fourni, analysons les résultats pour chaque modèle :

   **Régression logistique :**

   * La précision pour la classe 0 est de 0.97, ce qui indique que lorsque le modèle prédit la classe 0, il a raison 97 % du temps.
   * Le rappel pour la classe 0 est de 1.00, ce qui signifie que le modèle identifie correctement toutes les instances de la classe 0.
   * La précision pour la classe 1 est de 1.00, ce qui indique que lorsque le modèle prédit la classe 1, il a toujours raison. Cependant, le rappel pour la classe 1 n'est que de 0.05, ce qui signifie que le modèle n'est capable d'identifier que 5 % des instances réelles de la classe 1.
   * La précision globale du modèle est de 0.97.

   **SVM :**

   * La précision pour la classe 0 est de 0.97, ce qui indique que lorsque le modèle prédit la classe 0, il a raison 97 % du temps.
   * Le rappel pour la classe 0 est de 1.00, ce qui signifie que le modèle identifie correctement toutes les instances de la classe 0.
   * La précision et le rappel pour la classe 1 sont tous deux de 0.00, ce qui indique que le modèle échoue à prédire correctement les instances de la classe 1.
   * La précision globale du modèle est de 0.97.

   **Random Forest :**

   * La précision pour la classe 0 est de 0.98, ce qui indique que lorsque le modèle prédit la classe 0, il a raison 98 % du temps.
   * Le rappel pour la classe 0 est de 0.97, ce qui signifie que le modèle identifie correctement 97 % des instances de la classe 0.
   * La précision pour la classe 1 est de 0.38, ce qui indique que lorsque le modèle prédit la classe 1, il a raison 38 % du temps. Le rappel pour la classe 1 est de 0.47, ce qui signifie que le modèle est capable d'identifier 47 % des instances réelles de la classe 1.
   * La précision globale du modèle est de 0.95.

   En résumé, les trois modèles fonctionnent bien pour identifier les instances de la classe 0, avec des scores de précision et de rappel élevés. Cependant, ils éprouvent des difficultés à identifier les instances de la classe 1, le modèle de régression logistique ayant le score de rappel le plus élevé de 0.05 parmi eux. Le modèle Random Forest a la meilleure équilibre entre précision et rappel pour la classe 1, avec des scores respectifs de 0.38 et 0.47. La précision globale est la plus élevée pour le modèle de régression logistique (0.97), suivi du modèle Random Forest (0.95) et du modèle SVM (0.97). Cependant, les scores de précision élevés sont principalement dus au jeu de données déséquilibré, où la classe 0 a significativement plus d'instances que la classe 1.



#  3. Analyse de Sentiment

Nous allons réalisé une étude d'identification des sentiments des revues sur des restaurants.

## EDA
   En analysant le fichier le nombre de review positive et négative est le meme 500 pour chaque.

   Plusieurs features seront ajoutés afin d'améliorer les predictions des modéles.

   - 1. **Taille des reviews** : D'après le diagramme en boîte, la longueur moyenne des commentaires Disliked se situe entre 30 et 80 caractères, pour les commentaire liked entre 30 et 70. Il y a plus de variabilité dans la longueur des commentaires liked que dans les commentaires Disliked. On peut également constater que les commentaires Disliked semble plus long.

   ![alt text](<TPnote/TPnote/3- Restaurant/images/length by liked.png>)

   - 2. **nombre de mots** : La médiane des commmentaires Disliked est plus levée que celle des commentaires aimé. Ce qui signifie que le nombre de mots est généralement plus grand lors des commentaire Disliked.
   Il y a aussi  quelques commentaires Liked qui sont beaucoup plus longs que la plupart des autres commentaires.
   
   ![alt text](<TPnote/TPnote/3- Restaurant/images/word count.png>)

   
   - 3. **Nombre de lettre en majiscule**
   L'utilisation des majuscules est plus fréquente dans les commentaires "Disliked" que dans les commentaires "Liked".
   Il y a quelques commentaires "Disliked" qui ont beaucoup plus de majuscules que la plupart des autres commentaires. Les majuscules sont souvent utilisées au début des phrases et des noms propres, et peuvent également être utilisées pour mettre l'accent sur certains mots ou phrases.
   
   ![alt text](<TPnote/TPnote/3- Restaurant/images/upper case.png>)


   - 4. **La présence du mot not**
   l'utilisation du mot "not" est plus élevé dans les commmentaires "Disliked". L'utilisation de la négation est souvent utilisé dans ces cas la.
   
   ![alt text](<TPnote/TPnote/3- Restaurant/images/has not.png>)


## Modelisation
   -  Only Reviews
      | Model              | Vectorizer          | Accuracy |
      |--------------------|---------------------|----------|
      | Logistic Regression| vectorizer_BOW      | 0.81     |
      | Logistic Regression| vectorizer_TF_IDF   | 0.80     |
      | Logistic Regression| vectorizer_BOW_bigram | 0.81  |
      | Logistic Regression| vectorizer_TF_IDF_bigram | 0.79 |
      | SVM                | vectorizer_BOW      | 0.74     |
      | SVM                | vectorizer_TF_IDF   | 0.81     |
      | SVM                | vectorizer_BOW_bigram | 0.74  |
      | SVM                | vectorizer_TF_IDF_bigram | 0.81 |
      | Random Forest      | vectorizer_BOW      | 0.77     |
      | Random Forest      | vectorizer_TF_IDF   | 0.73     |
      | Random Forest      | vectorizer_BOW_bigram | 0.76  |
      | Random Forest      | vectorizer_TF_IDF_bigram | 0.73 |

      
      D'après les scores de précision fournis, le meilleur modèle parmi ceux testés semble être le modèle de régression logistique avec les vectoriseurs vectorizer_BOW (Bag-of-Words) et vectorizer_BOW_bigram (Bag-of-Words avec bigramme), atteignant tous deux une précision de 0,81. Ces modèles ont été constamment performants par rapport aux autres à travers différentes techniques de vectorisation.

      Les modèles SVM avec vectorizer_TF_IDF et vectorizer_TF_IDF_bigram ont également bien performé, atteignant une précision de 0,81, légèrement inférieure aux modèles de régression logistique les plus performants.

      Les modèles de forêt aléatoire ont montré des précisions plus faibles par rapport aux modèles de régression logistique et SVM avec toutes les techniques de vectorisation.

      Dans l'ensemble, basé uniquement sur la précision, les modèles de régression logistique avec la vectorisation Bag-of-Words et les caractéristiques de bigramme semblent être le meilleur choix parmi les modèles testés. 

   -  **Features**
      
      -  ['Word_Count', 'Review_Length']

         | Model              | Accuracy |
         |--------------------|----------|
         | Logistic Regression| 0.55     |
         | SVM                | 0.51     |
         | Random Forest      | 0.47     |

         À partir des résultats fournis, il est évident que le modèle de régression logistique a mieux performé parmi les modèles testés, avec une précision de 0.55. Le modèle SVM a atteint une précision de 0.51, tandis que le modèle de Forêt Aléatoire a eu la plus faible précision de 0.47.
         
      -  ['Word_Count', 'Review_Length', 'Uppercase_Count']
      
      | Modèle              | Précision |
      |---------------------|-----------|
      | Régression Logistique | 0.55      |
      | SVM                 | 0.51      |
      | Forêt Aléatoire     | 0.47      |
      
      Les résultats restent similaires à ceux précédemment analysés, avec la régression logistique ayant la meilleure performance, suivie du SVM, puis de la forêt aléatoire.

      -  ['Word_Count', 'Review_Length', 'Has_Not']

      | Modèle              | Précision |
      |---------------------|-----------|
      | Régression Logistique | 0.58      |
      | SVM                 | 0.50      |
      | Forêt Aléatoire     | 0.50      |

      Encore une fois, la régression logistique obtient la meilleure précision, suivie du SVM et de la forêt aléatoire, mais les différences de performances entre les modèles sont moins prononcées dans ce cas.

   -  Review + Word_Count

   | Modèle                                       | Précision |
   |----------------------------------------------|-----------|
   | Régression Logistique (BOW)                  | 0.81      |
   | Régression Logistique (TF-IDF)               | 0.77      |
   | Régression Logistique (BOW bigram)           | 0.81      |
   | Régression Logistique (TF-IDF bigram)        | 0.72      |
   | SVM (BOW)                                    | 0.59      |
   | SVM (TF-IDF)                                 | 0.51      |
   | SVM (BOW bigram)                             | 0.61      |
   | SVM (TF-IDF bigram)                          | 0.51      |
   | Forêt Aléatoire (BOW)                        | 0.74      |
   | Forêt Aléatoire (TF-IDF)                     | 0.70      |
   | Forêt Aléatoire (BOW bigram)                 | 0.77      |
   | Forêt Aléatoire (TF-IDF bigram)              | 0.70      |

   Une fois de plus, la régression logistique avec la vectorisation BOW bigram donne la meilleure précision, suivie de près par la régression logistique avec la vectorisation BOW et la forêt aléatoire avec la vectorisation BOW bigram. Les performances des modèles varient en fonction du type de vectorisation utilisé.


   -  Usage of multiple Review
      - Bow for word and char
         - Régression Logistique avec vectoriseur de mots et caractére : 0.77
         - SVM avec vectoriseur de mots et caractére: 0.65
         - Forêt Aléatoire avec vectoriseur de mots et caractére : 0.71

      - Bow for word and char ngram(1,2) and ngram (1,5)
         - Régression Logistique avec vectoriseur de mots : 0.85
         - SVM avec vectoriseur de mots  : 0.72
         - Forêt Aléatoire avec vectoriseur de mots  : 0.77
      
      - Bow for word and char ngram(1,2) and ngram (2,5)
         - Régression Logistique avec vectoriseur de mots : 0.84
         - SVM avec vectoriseur de mots  : 0.71
         - Forêt Aléatoire avec vectoriseur de mots  : 0.80

      Les performances des modèles avec des n-grammes de taille plus grande (par exemple, (1,5)) sont meilleures que celles avec des n-grammes plus petits (par exemple, (1,2)). Cela indique que la prise en compte de séquences de mots plus longues peut capturer des informations plus riches et conduire à de meilleures prédictions.

      La régression logistique semble être le modèle le plus performant dans la plupart des cas, suivie de la forêt aléatoire. Le SVM obtient généralement les performances les plus faibles, bien qu'il puisse être sensible aux réglages des hyperparamètres.

## Conclusion:
La régression logistique s'est avérée être le choix le plus fiable parmi les modèles testés, offrant des performances solides et cohérentes sur une variété de techniques de vectorisation et de caractéristiques. L'utilisation de bigrammes a amélioré la précision des prédictions. L'esnsemble des feature ajoutés n'a fait que rajouté du bruit et complexifier le modéle.


# 4. Covid

Dans ce derniere exercice nous allons travailler sur un DataSet du covid 19.

Le jeu de données brut contient un vaste nombre d'informations relatives aux patients anonymisés, y compris les préconditions. Le jeu de données brut comprend 21 caractéristiques différentes et 1 048 576 patients uniques. Dans les caractéristiques booléennes, 1 signifie "oui" et 2 signifie "non". Les valeurs 97 et 99 sont des données manquantes.

| Feature                         | Description (French)                                                                                     |
|--------------------------------|--------------------------------------------------------------------------------------------------------|
| MEDICAL_UNIT                   | Type d'institution du système national de santé ayant fourni les soins.                               |
| SEX                            | 1 - féminin. 2 - masculin                                                                               |
| PATIENT_TYPE                   | Type de soin reçu par le patient dans l'unité. 1 pour un retour à domicile et 2 pour une hospitalisation. |
| DATE_DIED                      | Si le patient est décédé, indique la date de décès, et 9999-99-99 sinon.                              |
| INTUBED                        | Indique si le patient était relié au ventilateur.                                                       |
| PNEUMONIA                      | Indique si le patient a déjà une inflammation des sacs aériens ou non.                                   |
| AGE                            | Âge du patient.                                                                                          |
| PREGNANT                       | Indique si le patient est enceinte ou non.                                                               |
| DIABETES                       | Indique si le patient est diabétique ou non.                                                             |
| COPD                           | Indique si le patient est atteint de bronchopneumopathie chronique obstructive ou non.                |
| ASTHMA                         | Indique si le patient est asthmatique ou non.                                                            |
| INMSUPR                        | Indique si le patient est immunodéprimé ou non.                                                          |
| HIPERTENSION                  | Indique si le patient est hypertendu ou non.                                                             |
| OTHER_DISEASE                  | Indique si le patient a une autre maladie ou non.                                                        |
| CARDIOVASCULAR                 | Indique si le patient a une maladie cardiaque ou vasculaire.                                             |
| OBESITY                        | Indique si le patient est obèse ou non.                                                                  |
| RENAL_CHRONIC                  | Indique si le patient souffre d'insuffisance rénale chronique ou non.                                    |
| TOBACCO                        | Indique si le patient est un utilisateur de tabac.                                                       |
| CLASIFFICATION_FINAL           | Résultats du test Covid. Voir la description des données.                                                 |
| ICU                            | Indique si le patient a été admis en unité de soins intensifs.                                             |


## Traitement des données
Nous allons commencé par traité les données manquentes ainsi que la création d'une colonne a prédire "DEAD".

-  **Données Manquantes**
   -  On va commencé par voir les valeurs uniques de chaque colonne. 
   On peut on déduire que pour cetrtaine colonne  dans les quelles on expecte avoir uniquement 2 valeurs, on retrouve 3 à 4 comme  par exemple PNEUMONIA, TABACO. Pour palier a cela nous allons garder uniquement les lignes avec les valeurs 1 et 2.

   - On analysant le compte de chaque valeur unique, on remarque que les variables ICU, PREGNANT et INTUBED présente plusieurs valeurs unique. On décidras de ce passer de ces dérniéres.

      ![alt text](<TPnote/TPnote/4- Covid/images/icu droped.png>)

      ![alt text](<TPnote/TPnote/4- Covid/images/intubed droped.png>)

      ![alt text](<TPnote/TPnote/4- Covid/images/pregnant droped.png>)

   - La colonne "DATE_DIED" posséde des dates réel  ou la personne est morte, ainsi que la valeur 9999-99-99, dans ce cas la la personne a survécu. Une colonne 2 DEAD est crée, 2 pour les personne ayant survécu et 1 une personne morte.


## Data Visualisation
Nous allons analyser nos données grace des graphe de distribution.
   -  Distribution de la variable DEAD et le sex de la personne : on remarque que plus d'homme sont mort que de femme.

   ![alt text](<TPnote/TPnote/4- Covid/images/dead vs sex.png>)

   -  Distribution de la variable DEAD et l'age: Avec l'augmentation de l'age, on remarque plus de personne mourante.

   ![alt text](<TPnote/TPnote/4- Covid/images/dead vs alive.png>)

   -  Distribution de la variable DEAD et PNEUMONIA : on remarque que les personne ayant une pnomie sont plus susceptible de mourir.

   ![alt text](<TPnote/TPnote/4- Covid/images/dead vs pneumonia.png>)


## Modelisation.
On commencera par analyser la matrice de confusion, afin d'obtenir les variables les plus snignificatif.
Les varible qui n'aposte rien sont : "SEX","COPD","ASTHMA","INMSUPR", "OTHER_DISEASE","CARDIOVASCULAR","OBESITY","TOBACCO".



   - Used models : Logistic Regression, Decision Tree and  Random Forest

      - All features

         -  Logistic Regression: 0.9346
         -  Decision Tree: 0.9323
         -  Random Forest: 0.9326

      - Feature Set 1: ["AGE", "PATIENT_TYPE", "PNEUMONIA"]

         -  Logistic Regression: 0.9337
         -  Decision Tree: 0.9338
         -  Random Forest: 0.9338

      -  Feature Set 2: ["AGE", "PATIENT_TYPE", "HIPERTENSION", "PNEUMONIA", "DIABETES"]

         -  Logistic Regression: 0.9338
         -  Decision Tree: 0.9337
         -  Random Forest: 0.9339

   
Dans l'ensemble, tous les modèles ont obtenu des précisions similaires, allant d'environ 93,37 % à 93,39 %. Cela suggère que le choix de l'ensemble de fonctionnalités n'a pas d'impact significatif sur les performances des modèles. Cependant, il est important de noter que les précisions sont relativement élevées, ce qui indique que les modèles se comportent bien dans la prédiction de la variable cible.

