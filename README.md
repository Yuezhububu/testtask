# Runtime requirements
* Python 2 or Python 3
* Latest version of Django

# Setup instructions
## Setup sqlite database
Assuming `python` is the Python executable, go to the `task/` directory and execute the following commands:
```
python ../manage.py makemigrations task
python ../manage.py migrate
```

## Start server
From the `task/` directory, the command
```
python ../manage.py runserver 8000
```
will start the server listening on localhost port `8000`.

## Open website
Open a browser, then open the url `localhost:8000/task/`.
