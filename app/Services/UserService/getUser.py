from flask import request, jsonify
from app.database.table.users.models import User

def get_user_logic():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)

    pagination = User.query.filter_by(deleted_at=None).paginate(page=page, per_page=per_page, error_out=False)
    users = pagination.items

    user_list = []
    for user in users:
        user_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'birthday': user.birthday.isoformat() if user.birthday else None,
            'phone': user.phone,
            'address': user.address
        })

    return jsonify({
        'users': user_list,
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': pagination.page,
        'per_page': pagination.per_page
    })