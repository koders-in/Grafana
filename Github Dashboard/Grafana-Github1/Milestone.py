from github import Github
from numpy import number
g = Github('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')

repo_name= input("Enter the reop path( username/repository_name ): ")
repo = g.get_repo(repo_name)
# repo = g.get_repo('PyGithub/PyGithub')
open_milestones = repo.get_milestones(state='closed')
for milestone in open_milestones:
    print(milestone)

repo_name_1= input("Enter the reop path( username/repository_name ): ")
repo_1 = g.get_repo(repo_name_1)
repo_1.create_milestone(title= "DES Algorithm")

