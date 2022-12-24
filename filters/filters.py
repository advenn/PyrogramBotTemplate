from pyrogram import filters
from data import config


# Filters
def is_admin(_, client, message):
    """
    If the user's ID is in the list of admins, return True

    :param _: This is a placeholder for the function's first parameter, which is the bot itself
    :param client: The client that is running the bot
    :param message: the message object
    :return: The function is_admin is returning the id of the user who sent the message.
    """
    return int(message.from_user.id) in config.admins


# Creating a filter that will be used to check if the user is an admin.
is_admin_filter = filters.create(is_admin)

