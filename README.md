# Picture Poster

A Django API for posting pictures.

## Running the app locally

1. Create and activate a Python virtual environment then install dependencies with the
   following commands, using Python 3.11.4. I recommend using
   [pyenv](https://github.com/pyenv/pyenv) for version management.

```
$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.dev.txt
```

2. Run the following command to start a Docker container running PostgreSQL:

```
$ docker compose up
```

3. Run these commands to run migrations, create a superuser and run your local web
   server.

```
$ src/manage.py migrate

$ src/manage.py createsuperuser

$ src/manage.py runserver
```

6. Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials you just
   created.

7. Set your user's account tier - this unlocks different features in the API.
    - Visit http://127.0.0.1:8000/admin/auth/user/ and click your username.
    - Scroll to the bottom of the page. Under the heading `ACCOUNT`, you will see a
      field allowing you to change your user's account tier.

8. Use the API - try the following URLs in your browser with different account tiers.
    - Listing images: http://127.0.0.1:8000/images/
    - Uploading images: http://127.0.0.1:8000/images/create


### Local development

#### Testing

Run the following commands for testing and linting tools:

- `pytest` to run tests.

- `flake8` for linting.

- `mypy .` for type checking. (TODO: django-stubs still needs to be configured properly
  so there are currently several errors in models.py)

- `black --check src` for formatting.


## TODOs / things to do with more time

- Add interfaces for creating disappearing links - I have created a model and some
  back-end functions to support this, but we need a view to create new links, and a view
  that redirects from a disappearing link's URL
  (e.g. `http://127.0.0.1:8000/<disappearing_link.slug>`) to the URL of its related
  Image's original file.

- Add more tests.

- Add the ability to run the web app in Docker too.

- Make settings more production-like, e.g. setting SECRET_KEY etc. with environment variables.

- Configure token authentication.

- Configure s3 file storage, using something like localstack for local emulation.

- Rethink the account tiers - is there a way they could be done with Django permissions?
  Is there a better way to set up the default tiers than a data migration - maybe
  hard-code the defaults and allow extra tiers to be added via the database?
