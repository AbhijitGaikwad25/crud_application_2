from models.user_model import users

def create_user_service(data):
    try:
        user_id = data.get("id")
        if user_id in users:
            return {"message": "User already exists"}, 400

        users[user_id] = {
            "name": data.get("name"),
            "email": data.get("email")
        }
        return {"message": "User created", "user": users[user_id]}, 201
    except Exception as e:
        return {"message": "An error occurred: " + str(e)}, 500

def get_user_service(user_id):
    try:
        user = users.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user, 200
    except Exception as e:
        return {"message": "An error occurred: " + str(e)}, 500

def get_all_users_service():
    try:
        return users, 200
    except Exception as e:
        return {"message": "An error occurred: " + str(e)}, 500


def delete_user_service(user_id):
    try:
        if user_id not in users:
            return {"message": "User not found"}, 404
        del users[user_id]
        return {"message": "User deleted successfully"}, 200
    except Exception as e:
        return {"message": "An error occurred: " + str(e)}, 500
