import config
import os
import praw
import requests


def bot_login():
    print("loggin in ")
    var = praw.Reddit(username=config.username,  # getting username etc for loggin in
                      password=config.password,  # user_agent lets reddit identify who you are
                      client_id=config.client_id,
                      client_secret=config.client_secret,
                      user_agent="rjmessibarca dog comment responder")
    print("logged in")
    return var


def run_bot(r, l):
    for comment in r.subreddit('rjmessibarca').comments(
            limit=25):  # no /r/test ..instead of comment any variable could be put will find every link in the
        # subreddit 25 tests for the first 25 comments in the link
        if "!joke" in comment.body and comment.id not in l:
            l.append(comment.id)
            print("string found " + comment.id)

            reply = "Here is the Chuck Norris joke that you requested \n\n>"
            joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']
            reply += joke
            comment.reply(reply)

            with open("comments_replied_to.txt", 'a') as f:
                f.write(comment.id + '\n')


def get_saved_comments():  # saving the ids which have already been replied
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)  # removes ' ' from comments_replied_to
    return comments_replied_to


r = bot_login()
l = get_saved_comments()
# l=[]
# print l
while True:
    run_bot(r, l)
