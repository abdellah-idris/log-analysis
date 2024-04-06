# log-analysis

# Crane

## EDA
On anylisant les deux fichiers on remrque que le nombre de valeur de MarkersValid a False est significativement plus petit que les valeurs a True.

## Observation des marqueurs:
On visualisant les changement de position des 3 marquers, on remarque la présence d'une modification brusque et subite de la postion d'un ou plusieurs marquers. la forme tirnagulaire ne persiste plus.

## Features
Dans le but d'améliorer le modéles, plusieurs features sont mise en place:
    -   Vitesse des marquers: la vittesse est calculé selon la formule de la distance, on peut supposer que les déplacements a des vitesses différentes des différent marquers permetrra didentifier des logs erroné.
    -   Déplacement des marquers selon l'axe x et y : On réalise une soustraction entre m1[i] et m1[i+1] sur l'axe x et y afin d'avoir l'information sur le taux de dépalacement. 
    -   Calcule de la surface du trinagle: Variable ajouté sans observation précise, remarqué.

## Affichage de la matrice de correlation
    - **LpsData_STS405b :**
        -   Il y a une forte correlation entre TrolleyPos et les position sur l'axe y de m1,m2 et m3 avec une valeurs de -0.89
        -   La position des marques  selon l'axe x et y est fortement corrélé  (m1_x foretemnt corrélé avec m1_y)
        -   TrolleyPos est moyennement corrélé avec MarkersValid
        -   Les vitesses des marque présente une correlation moyenne entre eux avec des valeurs avoisinent 0.5
    - **LpsData_TILsts :**
        -   TrolleyPos est moyennement corrélé avec Hoistpos, et ne présenta pas de corrélation avec MarkersValid
        -   Les vitesses des marque présente une correlation forte entre eux avec des valeurs avoisinent 0.9
        -   La supérficie du tringle formé par les marquers est moyennement corélé avec les vitesses
        -   La position des marques  selon l'axe x et y est moyennement corrélé  (m1_x moyennement corrélé avec m1_y)

## Détection des erreurs

    - **LpsData_TILsts :**
        - without speed
        Logistic Regression:
Accuracy: 0.9475982532751092
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00        12
           1       0.95      1.00      0.97       217

    accuracy                           0.95       229
   macro avg       0.97      0.50      0.49       229
weighted avg       0.95      0.95      0.92       229


Random Forest:
Accuracy: 0.9694323144104804
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.42      0.59        12
           1       0.97      1.00      0.98       217

    accuracy                           0.97       229
   macro avg       0.98      0.71      0.79       229
weighted avg       0.97      0.97      0.96       229


Support Vector Machine:
Accuracy: 0.9475982532751092
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00        12
           1       0.95      1.00      0.97       217

    accuracy                           0.95       229
   macro avg       0.97      0.50      0.49       229
weighted avg       0.95      0.95      0.92       229


Gradient Boosting Classifier:
Accuracy: 0.9519650655021834
Classification Report:
              precision    recall  f1-score   support

           0       0.67      0.17      0.27        12
           1       0.96      1.00      0.98       217

    accuracy                           0.95       229
   macro avg       0.81      0.58      0.62       229
weighted avg       0.94      0.95      0.94       229

        - with speed

        Logistic Regression:
Accuracy: 0.9475982532751092
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00        12
           1       0.95      1.00      0.97       217

    accuracy                           0.95       229
   macro avg       0.97      0.50      0.49       229
weighted avg       0.95      0.95      0.92       229


Random Forest:
Accuracy: 0.9213973799126638
Classification Report:
              precision    recall  f1-score   support

           0       0.12      0.08      0.10        12
           1       0.95      0.97      0.96       217

    accuracy                           0.92       229
   macro avg       0.54      0.53      0.53       229
weighted avg       0.91      0.92      0.91       229


Support Vector Machine:
Accuracy: 0.9475982532751092
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00        12
           1       0.95      1.00      0.97       217

    accuracy                           0.95       229
   macro avg       0.97      0.50      0.49       229
weighted avg       0.95      0.95      0.92       229


Gradient Boosting Classifier:
Accuracy: 0.9301310043668122
Classification Report:
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        12
           1       0.95      0.98      0.96       217

    accuracy                           0.93       229
   macro avg       0.47      0.49      0.48       229
weighted avg       0.90      0.93      0.91       229
        - All feature
        Logistic Regression:
Accuracy: 0.9475982532751092
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00        12
           1       0.95      1.00      0.97       217

    accuracy                           0.95       229
   macro avg       0.97      0.50      0.49       229
weighted avg       0.95      0.95      0.92       229


Random Forest:
Accuracy: 0.9388646288209607
Classification Report:
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        12
           1       0.95      0.99      0.97       217

    accuracy                           0.94       229
   macro avg       0.47      0.50      0.48       229
weighted avg       0.90      0.94      0.92       229


Support Vector Machine:
Accuracy: 0.9475982532751092
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00        12
           1       0.95      1.00      0.97       217

    accuracy                           0.95       229
   macro avg       0.97      0.50      0.49       229
weighted avg       0.95      0.95      0.92       229


Gradient Boosting Classifier:
Accuracy: 0.9388646288209607
Classification Report:
              precision    recall  f1-score   support

           0       0.25      0.08      0.12        12
           1       0.95      0.99      0.97       217

    accuracy                           0.94       229
   macro avg       0.60      0.53      0.55       229
weighted avg       0.91      0.94      0.92       229


    - **LpsData_STS405b :**
        - without speed
        Logistic Regression:
Accuracy: 0.7438423645320197
Classification Report:
              precision    recall  f1-score   support

           0       0.43      0.06      0.10       102
           1       0.76      0.97      0.85       304

    accuracy                           0.74       406
   macro avg       0.59      0.52      0.48       406
weighted avg       0.67      0.74      0.66       406


Random Forest:
Accuracy: 0.8891625615763546
Classification Report:
              precision    recall  f1-score   support

           0       0.83      0.71      0.76       102
           1       0.91      0.95      0.93       304

    accuracy                           0.89       406
   macro avg       0.87      0.83      0.84       406
weighted avg       0.89      0.89      0.89       406


Support Vector Machine:
Accuracy: 0.7487684729064039
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00       102
           1       0.75      1.00      0.86       304

    accuracy                           0.75       406
   macro avg       0.87      0.50      0.43       406
weighted avg       0.81      0.75      0.64       406


Gradient Boosting Classifier:
Accuracy: 0.8152709359605911
Classification Report:
              precision    recall  f1-score   support

           0       0.75      0.40      0.52       102
           1       0.83      0.95      0.89       304

    accuracy                           0.82       406
   macro avg       0.79      0.68      0.70       406
weighted avg       0.81      0.82      0.79       406

        - with speed
Logistic Regression:
Accuracy: 0.7487684729064039
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00       102
           1       0.75      1.00      0.86       304

    accuracy                           0.75       406
   macro avg       0.87      0.50      0.43       406
weighted avg       0.81      0.75      0.64       406


Random Forest:
Accuracy: 0.7389162561576355
Classification Report:
              precision    recall  f1-score   support

           0       0.47      0.27      0.35       102
           1       0.79      0.89      0.84       304

    accuracy                           0.74       406
   macro avg       0.63      0.58      0.59       406
weighted avg       0.71      0.74      0.71       406


Support Vector Machine:
Accuracy: 0.7487684729064039
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00       102
           1       0.75      1.00      0.86       304

    accuracy                           0.75       406
   macro avg       0.87      0.50      0.43       406
weighted avg       0.81      0.75      0.64       406


Gradient Boosting Classifier:
Accuracy: 0.7364532019704434
Classification Report:
              precision    recall  f1-score   support

           0       0.43      0.16      0.23       102
           1       0.77      0.93      0.84       304

    accuracy                           0.74       406
   macro avg       0.60      0.54      0.54       406
weighted avg       0.68      0.74      0.69       406


        - All feature

Logistic Regression:
Accuracy: 0.7610837438423645
Classification Report:
              precision    recall  f1-score   support

           0       0.62      0.13      0.21       102
           1       0.77      0.97      0.86       304

    accuracy                           0.76       406
   macro avg       0.69      0.55      0.54       406
weighted avg       0.73      0.76      0.70       406


Random Forest:
Accuracy: 0.8152709359605911
Classification Report:
              precision    recall  f1-score   support

           0       0.73      0.42      0.53       102
           1       0.83      0.95      0.88       304

    accuracy                           0.82       406
   macro avg       0.78      0.68      0.71       406
weighted avg       0.80      0.82      0.80       406


Support Vector Machine:
Accuracy: 0.7487684729064039
Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.00      0.00       102
           1       0.75      1.00      0.86       304

    accuracy                           0.75       406
   macro avg       0.87      0.50      0.43       406
weighted avg       0.81      0.75      0.64       406


Gradient Boosting Classifier:
Accuracy: 0.7857142857142857
Classification Report:
              precision    recall  f1-score   support

           0       0.65      0.31      0.42       102
           1       0.80      0.94      0.87       304

    accuracy                           0.79       406
   macro avg       0.73      0.63      0.65       406
weighted avg       0.77      0.79      0.76       406

## Analyse des resultats: 
En examinant les rapports de classification, nous pouvons observer les performances des divers modèles d'apprentissage automatique entraînés sur nos ensembles de données, avec et sans l'inclusion des caractéristiques de vitesse. Voici ce que nous avons remarqué :

Régression logistique :

La régression logistique présente des performances similaires pour les deux ensembles de données, qu'elles contiennent ou non les caractéristiques de vitesse.
Les résultats montrent une difficulté du modèle à bien classifier les instances de la classe 0 (MarkersValid : False), ce qui se traduit par des scores de précision, de rappel et de F1 relativement faibles pour cette classe.
En revanche, le modèle se comporte bien dans la classification de la classe 1 (MarkersValid : True), avec des scores de précision, de rappel et de F1 élevés.
Random Forest :

Sans les caractéristiques de vitesse, le modèle Random Forest obtient une précision plus élevée que la régression logistique pour les deux ensembles de données.
L'introduction des caractéristiques de vitesse entraîne une légère baisse de la précision, surtout pour l'ensemble de données LpsData_STS405b.
Globalement, le modèle Random Forest donne de bons résultats dans la classification des deux classes, avec des scores de précision, de rappel et de F1 relativement élevés pour chacune.
Machine à vecteurs de support (SVM) :

Les performances de SVM sont comparables à celles de la régression logistique, montrant des résultats similaires en termes de précision et de mesure de performance.
Toutefois, comme la régression logistique, SVM éprouve des difficultés à classifier correctement les instances de la classe 0 (MarkersValid : False), ce qui entraîne des scores de précision, de rappel et de F1 plus bas pour cette classe.
Gradient Boosting Classifier :

Le Gradient Boosting Classifier se comporte bien en termes de précision, en particulier pour l'ensemble de données LpsData_STS405b.
Ce modèle affiche une performance équilibrée dans la classification des deux classes, avec des scores de précision, de rappel et de F1 relativement élevés pour chacune.
En conclusion, les modèles Random Forest et Gradient Boosting ont tendance à mieux performer que la régression logistique et SVM en termes de précision et de performance équilibrée sur les deux classes. Cependant, l'ajout des caractéristiques de vitesse n'améliore pas systématiquement les performances de ces modèles, et dans certains cas, cela conduit même à une légère diminution de la précision. Cela suggère que les caractéristiques de vitesse ne fournissent pas nécessairement d'informations supplémentaires significatives pour la tâche de classification.


# EXO2








