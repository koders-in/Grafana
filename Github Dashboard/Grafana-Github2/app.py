from github import Github
import requests
from prettytable import PrettyTable

access_token = Github("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")
github_username  = "Gauravkumar45"
repo = "News-Application"
login  = access_token
user  = login.get_user()

#-------------------------------------------------------
# all information about my account...

print("********************************       Github account info        **********************************")
table = PrettyTable()
table.field_names = ["Key", "Value"]
api_url = f"https://api.github.com/users/{github_username}"
response = requests.get(api_url)
data =  response.json()

for key, value in data.items():
    table.add_row([key, value])
print(table)

#----------------------------------------------------------
# Repository information

print("***************************************       Repo information         ************************************")
table = PrettyTable()
table.field_names = ["Id","Repository Name", "Private", "Public","Created Date","Language"]
my_repos = user.get_repos()

for repository in my_repos:
    id = repository.id
    name =  repository.name
    private,public = repository.private, not(repository.private)
    created_date = repository.created_at
    language = repository.language
    table.add_row([id,name, private, public, created_date, language])

print(table)
repo_count  = my_repos.totalCount
print("Total Numbers of Repo is :",repo_count)

#----------------------------------------------------------
# issue information

print("*********************************         Issue Information       **************************************")
table = PrettyTable()
table.field_names = ["Issue Numbers", "Description", "Author"]
repo = user.get_repo('Calculator')
open_issues = repo.get_issues(state="open")

for issue in open_issues:
    total_issue_numbers =  issue.number
    description = issue.title
    author = issue.user
    table.add_row([total_issue_numbers,description,author])
print(table)
issue_count = open_issues.totalCount
print("Total numbers of issues is :",issue_count)

#-----------------------------------------------
# commit information

print("**************************        Commit information         ********************************")
table = PrettyTable()
table.field_names = ["Total Commit Numbers", "Commit Description","Author","Date"]
repo = user.get_repo('Calculator')
commits = repo.get_commits()
commits_sha_list = []
for commit in commits:
    commit = commit.commit
    description = commit.sha
    author= commit.author
    date = commit.committer
    commits_sha_list.append(commit.sha)
    table.add_row([commit,description,author,date])
print(table)

#----------------------------------------------------------
# pull request

print("****************************         Pull requests       ****************************")
table = PrettyTable()
table.field_names = ["Total Pull Request", "Active Pull Request"]
pulls = repo.get_pulls()
for pull in pulls:
    total_pull_request = pull.number
    active_pull_request = pull.comments
    table.add_row([total_pull_request,active_pull_request])
print(table)
pull_count = pulls.totalCount
print("Total numbers of Pull requests is :",pull_count)

#----------------------------------------------------------
# request

print("****************************        Event requests       ****************************")
table = PrettyTable()
table.field_names = ["Id", "Type","Created At","Repo"]
events = repo.get_events()
for event in events:
    id = event.id
    type = event.type
    create = event.created_at
    repo = event.repo
    table.add_row([id,type,create,repo])
print(table)
event_count = events.totalCount
print("Total numbers of events : ",event_count)

#----------------------------------------------------------

#pull the repo
print("********************************     create new repo     *****************************")
repository_name= "gaurav_repo"
new_repo = user.create_repo(repository_name)
new_repo.create_file("New-File.txt", "new commit", "pull by python code")
print("Successfully pull the new repo!")