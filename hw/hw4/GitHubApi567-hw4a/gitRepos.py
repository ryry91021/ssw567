import requests, json
import os
from dotenv import load_dotenv

def main(user):
    load_dotenv()
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    print(f"Token Loaded: {'FOUND' if GITHUB_TOKEN else 'NOT FOUND'}")
    HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}


    repoUrl=f"https://api.github.com/users/{user}/repos"
    
    #HTTP request for repository information (names)
    repoResponse=requests.get(repoUrl, headers=HEADERS)
    if repoResponse.status_code!=200:
        if repoResponse.status_code==403:
             raise Exception("Too many GitHub API calls. Wait a while.")
        print("User may not exist")
        raise Exception(f"Failed to retrieve data. HTTP Status code: {repoResponse.status_code}")
    
    else:
        account=repoResponse.json()
        data={}
        #Fetch names
        for project in account:
            
            #Get commit counts
            commitUrl=f"https://api.github.com/repos/{project['full_name']}/commits"
            #print(commitUrl)

            #print()
            commitResponse=requests.get(commitUrl, headers=HEADERS)
            #print()
            if commitResponse.status_code!=200:
                print("Project may not exist")
                raise Exception(f"Failed to retreive {project['name']} and its commits on status code: {commitResponse.status_code}")
            if commitResponse.status_code == 409:
                print(f"Warning: Repository {project['name']} has no commits (empty repo).")
                data[project['name']] = 0

            else:
                data[project['name']] = len(commitResponse.json())


            
    for repository, commits in data.items():
        print(f"Repo: {repository}. Number of commits: {commits}")

    return data




    



if __name__=="__main__":
    user=None


    user=input("Enter a GitHub username to view their repositories. Leave blank to default to mine: ")
    if not user:
        user='ryry91021'
    
    main(user)
    