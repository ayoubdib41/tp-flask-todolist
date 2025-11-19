# app.py

from flask import Flask, render_template, request, redirect, url_for

# Crée une instance de l'application Flask
app = Flask(__name__)

# Liste pour stocker les tâches en mémoire (simule une base de données)
# Une liste de dictionnaires. Chaque dictionnaire représente une tâche.
tasks = [
    {"id": 1, "title": "Acheter du pain", "done": False},
    {"id": 2, "title": "Réviser Flask", "done": True},
]

# --- ROUTES DE L'APPLICATION ---

@app.route('/')
def index():
    """Affiche la liste des tâches sur la page d'accueil."""
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    """Traite le formulaire d'ajout et ajoute une nouvelle tâche."""
    # Récupère le titre de la tâche depuis le formulaire
    title = request.form.get('title')
    
    # Vérifie si le titre n'est pas vide
    if title:
        # Trouve le plus grand ID existant et ajoute 1 pour le nouvel ID
        new_id = max([t['id'] for t in tasks]) + 1 if tasks else 1
        
        # Crée la nouvelle tâche
        new_task = {'id': new_id, 'title': title, 'done': False}
        
        # Ajoute la nouvelle tâche à la liste
        tasks.append(new_task)
    
    # Redirige l'utilisateur vers la page d'accueil
    return redirect(url_for('index'))

@app.route('/done/<int:task_id>')
def done(task_id):
    """Marque une tâche comme terminée."""
    # Cherche la tâche avec l'ID correspondant
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            break  # Sort de la boucle une fois la tâche trouvée
            
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    """Supprime une tâche de la liste."""
    global tasks
    # Recrée la liste en excluant la tâche avec l'ID à supprimer
    tasks = [task for task in tasks if task['id'] != task_id]
    
    return redirect(url_for('index'))

# --- DÉMARRAGE DE L'APPLICATION ---

if __name__ == '__main__':
    # Lance le serveur en mode debug pour le développement
    app.run(debug=True)