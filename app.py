from flask import Flask, request, jsonify

app = Flask(__name__)

# Définir un point d'accès pour une requête GET
@app.route('/api', methods=['GET'])
def api_root():
    return jsonify({
        "message": "Bienvenue sur votre première API Flask!"
    })

# Définir un point d'accès pour une requête POST qui reçoit des données JSON
@app.route('/api/contact', methods=['POST'])
def create_contact():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400
    
    # Exemple: récupérer des données JSON du POST
    lastname = data.get('lastname')
    firstname = data.get('firstname')
    
    if not lastname or not firstname:
        return jsonify({"error": "Nom ou prénom manquant"}), 400
    
    # Simuler un traitement de données
    return jsonify({
        "message": f"Contact {firstname} {lastname} créé avec succès!"
    }), 201

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=False)
