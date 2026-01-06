from models.user_model import users


def create_user_service(data):
    user_id = data.get("id")
    try:
        if user_id in users:
            return {"message": "User already exists"}, 400

        users[user_id] = {
            "name": data.get("name"),
            "email": data.get("email")
        }
        return {"message": "User created", "user": users[user_id]}, 201
    except Exception as e:
        return {"message": "Error creating user", "error": str(e)}, 500


def get_user_service(user_id):
    try:
        user = users.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user, 200
    except Exception as e:
        return {"message": "Error retrieving user", "error": str(e)}, 500


def get_all_users_service():
    try:
        return users, 200
    except Exception as e:
        return {"message": "Error retrieving users", "error": str(e)}, 500


def update_user_service(user_id, data):
    try:
        if user_id not in users:
            return {"message": "User not found"}, 404

        if "name" in data:
            users[user_id]["name"] = data["name"]
        if "email" in data:
            users[user_id]["email"] = data["email"]

        return {"message": "User updated", "user": users[user_id]}, 200
    except Exception as e:
        return {"message": "Error updating user", "error": str(e)}, 500