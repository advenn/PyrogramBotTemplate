# For database I use this or any other database:
# It is written using `Tortoise-orm` (https://tortoise-orm.readthedocs.io/en/latest/#)
# it is very alike to django-orm, but it is async, and it is very easy to use.
# it maybe a bit trickey to at first, but it is very easy to use after you get used to it.
# At first use this models, add any other models you want, and then run the bot with `generate=True` in app.py
# install a library called `aerich` - `pip install aerich`
# 1. open the terminal and run `aerich init -t data.config.TORTOISE_ORM`
# it will create a file called `pyproject.toml` and mogrations folder
# then open data.config file, edit the models inside TORTOISE_ORM,
# add `aerich.models` to the models.models list
# 2. run `aerich -c pyproject.toml init-db` to create initial ddl code for the database
# 3. run `aerich -c pyproject.toml migrate` to create the database
# 4. run `aerich -c pyproject.toml upgrade` to upgrade the database
#
# next time repeat 3 and 4 steps when you change the models


from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    username = fields.CharField(max_length=255, unique=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255, null=True)
    language_code = fields.CharField(max_length=255, null=True)
    date_joined = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"<User: {self.username}>"

    def __repr__(self):
        return self.__str__()


__all__ = ["User"]
