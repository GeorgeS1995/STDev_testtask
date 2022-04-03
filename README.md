# STDev_testtask

STDev test task.
# Original description
Test task for Python developer
Overview
The game is like "Who Wants to Be a Millionaire?"
* During each game, the player is asked 5 questions randomly selected from the base and not repeated during one game. For each question there are possible answer options (n number) and only one of them is correct. When the player chooses one of the answer options, the system informs about the problem being right or wrong.
* Each question has its corresponding point. (for example, according to its complexity). If the answer is correct, the point for the given question is added to the points calculated for the given game, and each question can have 5-20 points. In case of an incorrect answer, the points are not added and the player is notified about the correct answer.
* At the end of the game, the player is shown the number of points he has collected. This is the main problem where you need to manually add data to the Database; the content of the questions, of course, is not essential.
* After completing this part, send it to us and continue working on the rest. Add Login Admin who can add / delete / modify questions, options for answering those questions and the right option, as well as the point for each question. Create a sign-in and log-in possibility (Name, Surname, Password). Playing is possible only after logging in. The best result is calculated for each user and the top ten is displayed on the screen (names and the
Good luck highest score) based on the users’ best results.

# Prepare venv
* Install [poetry](https://python-poetry.org/)
* Create venv
* Run poetry install in venv

# Deploy test server
## Migrate DB
`python manage.py migrate`
## Run server
`python manage.py runserver`
## Optional use `test_db.sql` to deploy test db

### It's a simple test task why here no env, all settings hardcoded in settings.py, no tests, and SQLite DB.
