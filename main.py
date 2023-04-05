from instagrapi import Client

username = input("Username: ") 
password = input("Password: ")
client = Client()
client.login(username,password)


hastag = input("Hastag: ")
amount = int(input("Amount: "))
posts = client.hashtag_medias_recent(hastag,amount)

for i in range(amount):
    print("Post " + str(i +1))
    client.media_like(posts[i].id)
    print("Liked post")
    client.user_follow(posts[i].user.pk)
    print("Followed " + posts[i].user.username)
    
    
    
    
    