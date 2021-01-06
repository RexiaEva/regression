import pandas
# 1.2.1 Créez un code qui lit le fichier "housing.csv" et affiche ses premières lignes. Pour ce faire,
# utilisez les fonctions "read_csv" et "head" de la bibliothèque pandas. Sachant que la valeur
# cible est "median_house_value", traitons-nous un problème de classification ou de régression
# ?
df = pandas.read_csv('housing.csv')
# C'est une problèmes de régression
print(df.head())

# 1.2.2 Créez un code qui affiche le nombre de lignes et de colonnes des données, le type des attributs
# et le nombre de valeurs non nulles. Quelle remarque sur l’attribut "total_bedrooms"
# par rapport aux autres attributs ?
print('nb de lignes =', len(df.index), '\n\nb de colonnes =', len(df.columns), '\n\ntype des colonnes :\n', df.dtypes, '\n')
for col in df:
    print('nb de valeur non null dans', col, ':', (df[col].notnull()).sum())
# La colonne total_bedrooms a 7 valeurs null

# 1.2.3 A travers la question précédente, vous avez du remarquez que le type dans valeurs utilisées
# dans l’attribut "ocean_proximity" est un objet (forcément un texte vu qu’on manipule un
# fichier CSV). Il est intéressant de connaître ses valeurs. Pour cette finalité, créez un code qui
# affiche l’occurrence des valeurs utilisées dans cet attribut.
print(df['ocean_proximity'].value_counts())

# 1.2.4 Créez un code qui affiche des statistiques sur les attributs de ton jeu de données.
print(df.describe(include = 'all'))

from matplotlib import pyplot
# 1.2.5 Créez un code qui affiche les histogrammes des différents attributs. Le nombre de "bins" à
# saisir est 50 et la taille de chaque histogramme "figsize=(20,15)".
for x in df:
    pyplot.figure(figsize = (20, 15))
    pyplot.hist(df[x], range = (df[x].min(), df[x].max()), bins = 50)
    pyplot.title(x)
    pyplot.show()

# 1.3.1 Créez un code qui partitionne les données en base d’apprentissage et base de test. Optez
# pour 80% pour l’apprentissage et 20% pour le test.
nbligne = len(df.index)
pourcentage = int(nbligne * 80/100)
apprent = df.head(pourcentage)
teste = df.tail(nbligne-pourcentage)


# 1.4.2 Créez un code qui permet d’avoir une idée sur le lien entre la position géographique et le
# prix des maisons (target). Optez pour une valeur égale à False de "sharex".
pyplot.plot(apprent['longitude'], apprent['latitude'], linestyle = 'none', marker = 'o', c = 'lime',
  markersize = 1)
print(apprent['longitude'].min(), apprent['longitude'].max(), apprent['latitude'].min(), apprent['latitude'].max())
pyplot.xlim(-125, -110)
pyplot.ylim(30, 45)
pyplot.show()