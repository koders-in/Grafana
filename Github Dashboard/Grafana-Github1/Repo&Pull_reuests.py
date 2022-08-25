from github import Github
g = Github('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')
username = input("Enter user name to display repos: ")
user = g.get_user(username) 
repos = user.get_repos()
i = 0
list_of_repos = []
for repo in user.get_repos():
        list_of_repos.append(repo.name)
        print(list_of_repos[i])
        i=i+1

print("")
print("")
print("")


# Pull request
repo_name= input("Enter the reop path(username/repository_name): ")
repo = g.get_repo(repo_name)
pulls = repo.get_pulls(state='open', sort='created', base='master')
count = 0
print("Pull requests which are still opened in:" + repo_name)
for numbers in pulls:
    print("#"+str(numbers.number))
    count+=1
    print("")
    # print(numbers.assignees)

print("Total Pull requests in this repo are: ")
print(count)



# Commits, Description

