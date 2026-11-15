# Copilot instructions for this project

This is a uv project. Always run Python and Robot commands with `uv run ...`.

## Run app

```bash
cd /home/max/palautusrepositorio/viikko3/login
uv run python src/index.py
```

The Flask app runs on `http://localhost:5001`.

## Run Robot tests

The app must be running before the Robot tests are executed.

```bash
cd /home/max/palautusrepositorio/viikko3/login
uv run robot src/tests
```

Single test case example:

```bash
cd /home/max/palautusrepositorio/viikko3/login
uv run robot -t "Login With Correct Credentials" src/tests/login.robot
```

## Architecture

- `src/app.py` defines the Flask routes and request handling.
- `src/services/user_service.py` contains the user/business logic.
- `src/repositories/user_repository.py` stores users in memory (list-based repository, no database).
- `src/tests/` contains Robot Framework browser tests.

## Validation rules

Username/password validation happens in `src/services/user_service.py`:

- `UserService.validate()` checks required values, username length, duplicate usernames, and password length.
- `UserService.check_credentials()` checks whether the username exists and whether the password matches.

Keep validation logic in the service layer, not in Flask route functions.
