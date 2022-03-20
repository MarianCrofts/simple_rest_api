# Project: Games API
### Author: Marian Crofts

## Prompt
We'd like you to build a small HTTP API (GraphQL or REST) that can provide information about users and games they've played. 

In particular, the API should allow us to: 
- Fetch a list of users that includes their name, age, the list of games they've played, and the number of times those games have been played.
- Update a user's information (i.e. name, age, and the number of times they've played a game).

- For the sake of time, this should be a self-contained project. Using a volatile, in-memory store for values is 100% acceptable 
    (i.e. data that is cleared/reset on service restart). We do not expect this project to require an external data store.
- We do not expect any test code.
- We expect that we can clone your project and immediately run it (e.g. via `npm start`).


## Testing
### Run Server:
```bash
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
```

### Update User
```bash
curl -i http://127.0.0.1:5000/users \
-X POST \
-H 'Content-Type: application/json' \
-d '{"age":19,"games_and_playcount":[["Pokemon Unite",50],["Mario Kart",66]],"id":3,"name":"Jerry"}'
```

### Add user
```bash
curl -i http://127.0.0.1:5000/add_user \
-X POST \
-H 'Content-Type: application/json' \
-d '{"age":29,"games_and_playcount":[["Animal Crossing", 1]],"name":"Betty"}'
```
### Delete user
```bash
curl -i http://127.0.0.1:5000/delete_user \
-X POST \
-H 'Content-Type: application/json' \
-d '{"id":4}'
```