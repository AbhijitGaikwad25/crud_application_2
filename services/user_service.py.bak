from models.user_model import users

def create_user_service(data):
    user_id = data.get("id")
    if user_id in users:
        return {"message": "User already exists"}, 400

    # users[user_id] = {
    #     "name": data.get("name"),
    #     "email": data.get("email")
    # }
    return {"message": "User created", "user": users[user_id]}, 201

def get_user_service(user_id):
    user = users.get(user_id)
    if not user:
        return {"message": "User not found"}, 404
    return user, 200

def get_all_users_service():
    return users, 200

def update_user_service(user_id, data):
    if user_id not in users:
        return {"message": "User not found"}, 404

    # if "name" in data:
    #     users[user_id]["name"] = data["name"]
    # if "email" in data:
    #     users[user_id]["email"] = data["email"]

    return {"message": "User updated", "user": users[user_id]}, 200

def delete_user_service(user_id):
    if user_id not in users:
        return {"message": "User not found"}, 404
    del users[user_id]
    return {"message": "User deleted"}, 200
