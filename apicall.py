# import repo data from github
#-*- coding:utf-8 -*-
from datetime import datetime
import json
import requests
import os
import pandas as pd

t1 = datetime.now()

def get_access_token():

    with open('access_token.txt', 'r') as f:
        return f.read().strip()

def call_api(api,headers):
    """
    use requests to call github api
    """
    r = requests.get(api,headers=headers)
    if r.status_code != 200:
        raise ValueError('Can not retrieve from {}'.format(api))

    repos_dict = json.loads(r.content.decode('utf-8'))

    return repos_dict


def get_all_repos():
    """
    # get  repos with most stars 
    """
    access_token = get_access_token()
    
    api = 'https://api.github.com/search/repositories?q=stars:>100&sort=stars&access_token={}'.format(access_token)
    headers = {'Accept': 'application/vnd.github.mercy-preview+json'} 

    repos_dict = call_api(api,headers)
    repos = repos_dict['items']
    return repos

if __name__=="__main__":

    os.chdir("C:\\Users\\Ray\\Documents\\vscodes\\")

    repos = get_all_repos()
    df = pd.DataFrame.from_dict(repos)
    cols = ["id", "full_name", "url", "created_at", "updated_at", "description", "stargazers_count"]
    df = df[cols]
    df.columns = ["id", "full_name", "url", "created_at", "updated_at", "description", "stars_count"]
    df.to_csv('result.csv',index=False)
    print("Total time: {}s".format((datetime.now()-t1).total_seconds()))
