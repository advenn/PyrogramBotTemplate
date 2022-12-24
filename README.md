# Public template for running a pyrogram userbot
## Usage:
1. Install requirements
2. change the name `.env.dist` to `.env`
3. change the values in `.env`
4. run the bot with python app.py


## Database
For database I use this or any other database:
It is written using `tortoise-orm` (https://tortoise-orm.readthedocs.io/en/latest/#).

it is very alike to django-orm, but it is async, and it is very easy to use.

it maybe a bit tricky to at first, but it is very easy to use after you get used to it.

At first use this models, add any other models you want, and then run the bot with `generate=True` in app.py
install a library called `aerich` - `pip install aerich`

1. open the terminal and run `aerich init -t data.config.TORTOISE_ORM`
it will create a file called `pyproject.toml` and `migrations` folder
then open `data.config` file, edit the models inside `TORTOISE_ORM`,
add `aerich.models` to the models.models list
2. run `aerich -c pyproject.toml init-db` to create initial `DDL` code for the database
3. run `aerich -c pyproject.toml migrate` to create the database
4. run `aerich -c pyproject.toml upgrade` to upgrade the database

next time repeat 3 and 4 steps when you change the models

## for smart plugins in pyrogram look through official docs:
https://docs.pyrogram.org/topics/smart-plugins