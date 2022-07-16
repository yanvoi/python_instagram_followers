# before running the program again
# make sure that the 'config/' directory is deleted
# it's in the same dir as the program
# although the last line of code should take care of it

from instabot import Bot
from shutil import rmtree


bot = Bot()

# change the arguments below

bot.login(username="your_instagram_username", password="your_instagram_password")

# creating a list of people who do not follow the account back

non_followers = list(set(bot.following) - set(bot.followers))

# the list now contains IDs of people
# in order to get their nicknames, we do the following

for user in non_followers:
    name = bot.get_username_from_user_id(user)
    print(name)

    # the delay will make sure that instagram will not block our access to the server
    bot.small_delay()

# this is the function that deletes the directory 'config/'
rmtree('config', ignore_errors=True, onerror=None)
