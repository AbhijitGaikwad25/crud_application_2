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

# demo commit 1
# demo commit 2
# demo commit 3
# demo commit 4
def get_user_service(user_id):
    try:
        user = users.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user, 200
    except Exception as e:
        return {"message": "An error occurred: " + str(e)}, 500

# demo commit 5
# demo commit 6
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
        return {"message": "User deleted"}, 204
    except Exception as e:
        return {"message": "An error occurred: " + str(e)}, 500


def update_user_service(user_id, data):
    try:
        if user_id not in users:
            return {"message": "User not found"}, 404
        users[user_id].update({
            "name": data.get("name", users[user_id]["name"]),
            "email": data.get("email", users[user_id]["email"])
        })
        return {"message": "User updated", "user": users[user_id]}, 200
    except Exception as e:
        return {"message": "An error occurred: " + str(e)}, 500