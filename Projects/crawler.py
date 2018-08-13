from praw.models import comment_forest
import praw
import sys
import time


username = 'no_flex_zone'
password = 'bisherk92'
client_id = 'RjI-0KSmJMWajg'
client_secret = 's9NyG7mnbKCSPcFkZ3osS3sC_vk'

def login():
    '''Returns logged in reddit instance'''
    print("Logging in...")
    r = praw.Reddit(username = username,
            password = password,
            client_id = client_id,
            client_secret = client_secret,
            user_agent = "learning to use bots")
    print("You are in!")
    return r



def get_subs(r,query):
    set_list = set(r.subreddits.search_by_name(query))
    [set_list.add(sub) for sub in r.subreddits.search(query) if str(query) in sub.title.lower()]
    return set_list


def scrape_threads(r,sub_list,keyword):
    organized_sub = []
    for subs in sub_list:
        sublist_posts = r.subreddit('{}'.format(subs)).hot(limit = 25)
        sub_dict = dict()
        for submission in sublist_posts:
            if keyword.lower() in submission.title.lower():
                sub_dict[submission.title] = submission.id
            else:
                continue
            organized_sub.append(sub_dict)
    return organized_sub


def DFT(parent_comment):
    comment_list = []
    children = [i for i in parent_comment]
    visited_dic = {i:False for i in children}
    if False not in visited_dic.values():
        return comment_list
    else:
        for k,v in visited_dic.items():
            if v == False:
                curr_child = k
                visited_dic[k] = True
                comment_list.append(curr_child.body)
            if curr_child.replies:
                comment_list.append(DFT(curr_child.replies))

    return comment_list


def submission_scrape(sub_id):
    submission = r.submission(id = sub_id)
    forest = comment_forest.CommentForest(submission,submission.comments)
    comment_list = DFT(forest)
    return comment_list


def run(param1,param2):
    r = login()
    subs = get_subs(r,param1)
    found_threads = scrape_threads(r,subs,param2)
    return found_threads
