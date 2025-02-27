import requests, json

def main(user):
    repoUrl=f"https://api.github.com/users/{user}/repos"
    
    #HTTP request for repository information (names)
    repoResponse=requests.get(repoUrl)
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
            print(project['name'])

            #Get commit counts
            commitUrl=f"https://api.github.com/{project['full_name']}/commits"
            print(commitUrl)

            print()
            commitResponse=requests.get(commitUrl)
            print()
            if commitResponse.status_code!=200:
                print("Project may not exist")
                raise Exception(f"Failed to retreive {project['name']} and its commits on status code: {commitResponse.status_code}")
            elif commitResponse.status_code==409:
                        print(f"Warning: Repository {project['name']} has no commits (empty repo).")
            else:
                 data[str(project)]=len(commitResponse.json())

            
    for repository in data:
         print(f"Repo: {data.keys(repository)}. Number of commits: {data.items(repository)}")



    



if __name__=="__main__":
    user=None

    if user==None:
        user=input("Enter a GitHub username to view their repositories. Leave blank to default to mine.")
        user='ryry91021'
    
    main(user)