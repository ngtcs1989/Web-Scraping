import facebook    #sudo pip install facebook-sdk
from collections import Counter
import itertools
# the access token should be stored as a string(expired)
access_token = "EAACEdEose0cBAJcBI30Ah5YvzOJAHkZBc1tGRbOhZCCm2tPptON4ZAANhwHHygIFWDG7Uid7H9iHppNNDJLFojI7TI8QQdoZAOPhodudwYC7uMVs1mtHv3C7FzpQlYmBUV8VcBY9t4EfCd6jlsZBWerQZBClMTFz2RDZBYxJ9jBaQZDZD"
g = facebook.GraphAPI(access_token) #creating connection to the Facebook Graph API through facebook-sdk
friends = g.get_connections("me", "invitable_friends")['data'] #getting the name and id of friends
print(friends)
