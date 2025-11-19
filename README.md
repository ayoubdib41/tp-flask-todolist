# TP Flask – Mini application de gestion de tâches

Ceci est une petite application web développée avec le framework Python Flask. Elle permet de créer, afficher, marquer comme terminées et supprimer des tâches d'une liste.

Ce projet a été réalisé dans le cadre d'un TP visant à pratiquer les bases de Flask, Jinja, les formulaires et un peu de JavaScript.

## Fonctionnalités

*   Afficher la liste des tâches existantes.
*   Ajouter une nouvelle tâche via un formulaire.
*   Marquer une tâche comme "terminée", ce qui la barre visuellement.
*   Supprimer une tâche (avec une demande de confirmation en JavaScript).

## Instructions de Lancement

Pour lancer l'application en local, suivez ces étapes :

1.  **Clonez ou téléchargez le projet.**

2.  **Ouvrez un terminal** à la racine du projet.

3.  **Créez et activez un environnement virtuel :**
    ```bash
    # Créer l'environnement
    python -m venv venv
    # Activer l'environnement (sur Windows Command Prompt)
    .\venv\Scripts\activate
    ```

4.  **Installez les dépendances** (juste Flask pour ce projet) :
    ```bash
    pip install Flask
    ```

5.  **Lancez le serveur de développement :**
    ```bash
    flask run --debug
    ```

6.  **Ouvrez votre navigateur** et allez à l'adresse : [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Questions de Réflexion

#### 1. Quelle est la différence entre une requête GET et une requête POST dans le contexte d’un formulaire ?

La principale différence réside dans la manière dont les données sont envoyées et leur finalité :

*   **GET** : Les données du formulaire sont ajoutées à l'URL sous forme de paramètres (ex: `...?nom=valeur&...`). Cette méthode est visible, limitée en taille et doit être utilisée pour récupérer des données sans modifier l'état du serveur (par exemple, un formulaire de recherche).
*   **POST** : Les données du formulaire sont envoyées dans le corps de la requête HTTP, de manière invisible pour l'utilisateur. Cette méthode est plus sécurisée, n'a pas de limite de taille pratique et est utilisée pour envoyer des données qui modifient l'état du serveur (créer un utilisateur, ajouter une tâche, etc.).

#### 2. À quoi sert `redirect(url_for(...))` dans une application Flask ?

Cette instruction est cruciale et sert principalement à mettre en œuvre le design pattern **Post/Redirect/Get (PRG)**. Après qu'un utilisateur a soumis un formulaire via POST (par exemple, pour ajouter une tâche), le serveur traite la demande puis, au lieu de retourner directement une page, il envoie une redirection vers une autre URL (généralement la page d'accueil). Le navigateur effectue alors une nouvelle requête GET vers cette URL.

Cela a deux avantages majeurs :
1.  **Éviter la re-soumission du formulaire** : Si l'utilisateur actualise la page après une redirection, il ne fait que ré-exécuter la requête GET, ce qui est sans danger. Sans redirection, il renverrait les données du formulaire POST, créant potentiellement des doublons (par exemple, deux tâches identiques).
2.  **Séparer les actions des vues** : La route POST (`/add`) a un seul rôle : traiter les données. La route GET (`/`) a un seul rôle : afficher les données. C'est une organisation du code plus propre et plus logique.

`url_for('index')` est une fonction qui génère dynamiquement l'URL pour la route associée à la fonction `index`, ce qui rend le code plus robuste aux changements d'URL.

#### 3. Expliquez le rôle des blocs et de l’héritage de templates dans Jinja.

L'héritage et les blocs sont des fonctionnalités puissantes de Jinja qui permettent de respecter le principe **DRY (Don't Repeat Yourself)**, c'est-à-dire de ne pas répéter le même code.

*   **L'héritage (`{% extends "base.html" %}`)** : Permet à un template "enfant" (comme `index.html`) d'hériter de toute la structure d'un template "parent" (`base.html`). On définit ainsi une seule fois la structure commune à tout le site (le `<html>`, `<head>`, `<body>`, le header, le footer, les liens CSS/JS).
*   **Les blocs (`{% block content %}{% endblock %}`)** : Les blocs sont des "zones" définies dans le template parent que les templates enfants peuvent remplir avec leur propre contenu spécifique. Le template `index.html` remplit le `block content` de `base.html` avec la liste des tâches et le formulaire, mais hérite de tout le reste.

Ensemble, ils permettent de maintenir un code HTML très organisé, facile à modifier et à faire évoluer : pour changer le footer de tout le site, il suffit de modifier un seul fichier (`base.html`).

#### 4. Donnez un exemple de situation où JavaScript côté client est plus adapté que le traitement côté serveur en Python.

Un excellent exemple est la **demande de confirmation avant de supprimer une tâche**, que nous avons implémentée dans ce TP.

Utiliser JavaScript (`confirm()`) est bien plus adapté pour cette action car :
1.  **Instantanéité** : La boîte de dialogue apparaît immédiatement pour l'utilisateur, sans aucun temps de latence.
2.  **Économie de ressources** : L'action se passe entièrement dans le navigateur du client. Aucun aller-retour inutile vers le serveur n'est effectué si l'utilisateur clique sur "Annuler".
3.  **Meilleure expérience utilisateur (UX)** : L'interaction est fluide et directe. Si on devait le faire côté serveur, il faudrait d'abord naviguer vers une page "Êtes-vous sûr ?", puis cliquer sur un autre bouton pour confirmer, ce qui est beaucoup plus lourd et lent.

D'autres exemples incluent la validation de format d'un email en temps réel ou le filtrage d'une liste déjà affichée sans recharger la page.
