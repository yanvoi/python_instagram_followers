from instabot import Bot
from shutil import rmtree


bot = Bot()

bot.login(username="your_instagram_username", password="your_instagram_password")

non_followers = list(set(bot.following) - set(bot.followers))

for user in non_followers:
    name = bot.get_username_from_user_id(user)
    print(name)
    bot.small_delay()

rmtree('config', ignore_errors=True, onerror=None)
