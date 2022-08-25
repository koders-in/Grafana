from github import Github
from datetime import datetime

repos = {}
i =0
g = Github('Enter the token here')
for repo in g.get_user().get_repos():
    master = repo.get_branch('master')
    sha_drpm = master.commit
    sha_drpm = str(sha_drpm).split('Commit(sha="')
    sha_drpm = sha_drpm[1].split('")')
    sha_drpm = sha_drpm[0]
    commit = repo.get_commit(sha_drpm)
    repo = str(repo).split('Repository(full_name="Dextron12/')
    
    timeObj = commit.commit.author.date
    timeStamp = timeObj.strftime("%d-%b-%Y (%H:%M:%S)")
    
    repos[repo[0]] = timeStamp


print(repos)

print("Latest repository added or commit changesis : ")

for i in repo:
    print(i)
    
