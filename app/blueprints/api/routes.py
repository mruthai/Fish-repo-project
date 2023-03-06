from . import bp as api_bp
from app.blueprints.social.models import Livestock



@api_bp.route('/collectanimals', methods=['GET', 'POST'])
def api_livestock():
    result = []
    fishs = Livestock.query.all()
    for fish in fishs:
        result.append({
            'id': fish.id,
            'species': fish.species,
            'timestamp': fish.timestamp,
            'user_id': fish.user_id
            
        })
    return result

@api_bp.route('/collectanimals', methods=['GET', 'POST'])
def api_livestocks():
    fishs = Livestock.query.all()
    return{
        'id': fishs.id,
        'species': fishs.species,
        'timestamp': fishs.timestamp,
        'user_id': fishs.user_id
        }