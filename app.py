from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial Users List
users = [
    {
        "id": 1,
        "name": "Sarah", 
        "age": 24, 
        "games_and_playcount": [
                ("Skyrim", 2), 
                ("Stardew Valley", 6), 
                ("Pokemon Go", 1),
            ], 
    },
    {
        "id": 2,
        "name": "Tom", 
        "age": 36, 
        "games_and_playcount": [
                ("Super Smash Brothers", 400),
                ("Elden Ring", 1),
            ], 
    },
    {
        "id": 3,
        "name": "Jerry", 
        "age": 18, 
        "games_and_playcount": [
                ("Pokemon Unite", 49),
                ("Mario Kart", 66),
            ], 
    }
]

# User functions
def _find_next_id():
    return max(user["id"] for user in users) + 1

@app.get("/users")
def get_users():
    return jsonify(users)

@app.post("/users")
def update_users():
    if request.is_json:
        edit_user = request.get_json()
        if "id" not in edit_user:
            return {"error": "User id required to edit a user"}, 400

        for user in users:
            if user["id"] == edit_user["id"]:
                if "name" in edit_user:
                    user["name"] = edit_user["name"]
                if "age" in edit_user:
                    user["age"] = edit_user["age"]
                if "games_and_playcount" in edit_user:
                    user["games_and_playcount"] = edit_user["games_and_playcount"]
                return user, 200

    return {"error": "Request must be JSON"}, 415

@app.post("/add_user")
def add_user():
    if request.is_json:
        user = request.get_json()
        user["id"] = _find_next_id()
        # Check that name, age, and games list are all populated
        if ("name" in user) and ("age" in user) and ("games_and_playcount" in user):
            users.append(user)
            return user, 200
        else:
            return {"error": "Request must include name, age, and games list"}, 415
    return {"error": "Request must be JSON"}, 415

@app.post("/delete_user")
def delete_user():
    if request.is_json:
        deleted_user = request.get_json()
        if "id" not in deleted_user:
            return {"error": "User id required to delete a user"}, 400

        del_id = int(deleted_user["id"])

        # Check if ID to be deleted is in users list
        for i in range(len(users)):
            # Remove user from users list
            if users[i]["id"] == del_id:
                del users[i]
                return jsonify(users), 200

        return {"error": "User id not found in user list"}, 404
    return {"error": "Request must be JSON"}, 415
