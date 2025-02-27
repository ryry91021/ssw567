import requests, json

def main(user):
    url=f"https://api.github.com/users/{user}/repos"

    response=requests.get(url)
    if response.status_code!=200:
        print("User may not exist")
        raise Exception(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
    else:
        account=response.json()
        for project in account:
            print(project['name'])

    



if __name__=="__main__":
    user=None

    if user==None:
        user=input("Enter a GitHub username to view their repositories. Leave blank to default to mine.")
        user='ryry91021'
    
    main(user)