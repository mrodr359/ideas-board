# app.py

from flask import Flask, request, jsonify
from models import db, Idea

app = Flask(__name__)

# DB config (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

@app.route('/')
def home():
    return "Welcome to the Ideas Board API! 🚀"

@app.route('/ideas', methods=['POST'])
def create_idea():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    new_idea = Idea(title=data['title'], description=data.get('description'))

    db.session.add(new_idea)
    db.session.commit()
    return jsonify({"message": "Idea created successfully", "idea": new_idea.id}), 201

@app.route('/ideas', methods=['GET'])
def get_ideas():
    ideas = Idea.query.all()
    ideas_list = []
    for idea in ideas:
        ideas_list.append({
            "id": idea.id,
            "title": idea.title,
            "description": idea.description,
            "created_at": idea.created_at.isoformat()
        })
    return jsonify(ideas_list), 200

@app.route('/ideas/<int:idea_id>', methods=['GET'])
def get_idea(idea_id):
    idea = Idea.query.get_or_404(idea_id)
    return jsonify({
        "id": idea.id,
        "title": idea.title,
        "description": idea.description,
        "created_at": idea.created_at.isoformat()
    }), 200

@app.route('/ideas/<int:idea_id>', methods=['DELETE'])
def delete_idea(idea_id):
    idea = Idea.query.get_or_404(idea_id)
    db.session.delete(idea)
    db.session.commit()
    return jsonify({"message": "Idea deleted successfully"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables
    # Run the Flask app
    app.run(debug=True, host="0.0.0.0", port=5001)
