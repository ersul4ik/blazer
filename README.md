### Definition
The service responsible to generate fake data according to created data-fixture.


### Tech

Using the below technologies:

* [Python3](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu).
* [Django3](https://tecadmin.net/install-django-on-ubuntu/)
* [Pytest](https://docs.pytest.org/en/stable/).


### How I can run the app.

The demo:
   - https://powerful-wave-39036.herokuapp.com . Login/password you can receive from @ersul4ik (Telegram).

Locally:
- `pyenv install 3.8` - note, that you need specity the exact version of Python3.8, pyenv will show you
- `pipenv --python ~/.pyenv/versions/3.8.x/bin/python install` - for installing python environment
- `pipenv shell` - to activate virtual environment
- `pipenv install` - to install needed package from Pipfile
- `./manage.py migrate` - apply database migration with minimal changes
- For running the server you have to set required env variables:  
````
SECRET_KEY=
ALLOWED_HOSTS=
DATABASE_URL=
REDIS_URL=
````
- `./manage.py runserver 8000` - for running the web-server.
- `celery -A config worker -l info` - for running the celery worker.

When the project is up you should see smth like this:
- Screen Auth


### Tests
- `pytest`. Use this command to make sure that everything is ok.


### Project structure

- config/ - The core application that contains all project settings.
- factories/ - The app that responsible for the whole logic of preparing/generating/download CSV files.
- templates/ - The ordinary folder to store HTML files.

