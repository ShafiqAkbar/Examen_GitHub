#### Repository : repertoire de travail

git init

#### Lire le contenu du directory sur lequel vous êtes

ls/dir --> git bash ok pour les deux

#### Ajjouter les élements à l'index (Staging) --> Etape intermédiare avant le commit

git add .

#### Check des fichiers en instance d'être commiter

git status

#### Repository local: ajouter une tache

git commit -m "Examen_GitHub"

#### Ajouter le repertoire de travail distant à la tache

git remote add github https://github.com/ShafiqAkbar/Examen_GitHub

#### Lister l'ensemble des repository distants enregistrés

git remote -v

#### Uploader les fichiers sur le repository distant choisi

git push -u github master 