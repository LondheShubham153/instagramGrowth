from InstagramAPI import InstagramAPI
from config import password
import pprint
from time import sleep

users_list = []
following_users = []
follower_users = []

class InstaBot:

    def __init__(self):
        self.api = InstagramAPI("testingggggit123",password)

    def get_likes_list(self,username):
        api = self.api
        api.login()
        api.searchUsername(username)
        result = api.LastJson
        username_id = result['user']['pk']
        user_posts = api.getUserFeed(username_id)
        result = api.LastJson
        media_id = result['items'][0]['id']

        api.getMediaLikers(media_id)
        users = api.LastJson['users']
        for user in users:
            users_list.append({'pk':user['pk'], 'username':user['username']})
        pprint.pprint(users_list)

    def follow_users(self,users_list):
        api = self.api
        api.login()
        api.getSelfUsersFollowing()
        result = api.LastJson

        for user in result['users']:
            following_users.append(user['pk'])
        for user in users_list:
            if user['pk'] in following_users:
                print("Bot is already following @"+user['username'])
            else:
                print("Bot is now following @"+user['username'])
                api.follow(user['pk'])
                sleep(20)

    def unfollow_users(self):
        api = self.api
        api.login()
        api.getSelfUserFollowers()
        result = api.LastJson
        for user in result['users']:
            follower_users.append({'pk':user['pk'],'username':user['username']})
        
        api.getSelfUsersFollowing()
        result = api.LastJson

        for user in result['users']:
            following_users.append({'pk':user['pk'],'username':user['username']})
        
        for user in following_users:
            if not user['pk'] in follower_users:
                print("Unfollowing @"+user['username'])
                api.unfollow(user['pk'])
                sleep(20)
        





my_bot = InstaBot()
# my_bot.get_likes_list("instagram")
# my_bot.follow_users(users_list)
my_bot.unfollow_users()
