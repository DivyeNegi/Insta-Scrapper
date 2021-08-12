import instaloader

bot=instaloader.Instaloader()
username=str(input('Enter your username: '))
bot.interactive_login(username)
key='yes'
while key!='no':
    print('')
    prof=str(input('Enter the profile: '))
    profile = instaloader.Profile.from_username(bot.context, prof)
    print("Username: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers: ", profile.followers)
    print("Followees: ", profile.followees)
    print("Bio: ", profile.biography)
    print('External Site: ',profile.external_url)
    print('Retreiving followers who dont follow back: ')
    followers = [follower.username for follower in profile.get_followers()]
    followees = [followee.username for followee in profile.get_followees()]
    for a in followees:
        if a not in followers:
            print(f'{a} doesnt follow you back!')
    key=str(input('\n Do you want to scrape another profile? (yes/no)'))