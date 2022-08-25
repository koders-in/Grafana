from github import Github
from numpy import number
g = Github('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')

repo_name= input("Enter the reop path( username/repository_name ): ")
repo = g.get_repo(repo_name)
list_of_issues = []
open_issues = repo.get_issues(state='open')
try:
     for issue in open_issues:
          list_of_issues.append(issue)
          print(issue)

except:
     print("No issues were opened")

print("")
print("")
for line in list_of_issues:
     print(line)

print("")
print("")
x = int(input("Enter the number of your issue you want to see: "))
print("")
try:
     for line in list_of_issues:
          if(x in list_of_issues):
               print("This issue is open: Details of this issue is: ")
               
               break
          else:
               print(repo.get_issue(x))
               break
except:
     print("This issue was closed: Details of this issue is: ")
     print(repo.get_issue(x))

print("")

x = int(input("Enter the number of the issue you want to comment: "))
print("")
y = input("Enter the comment for "+str(x)+" : ")
issue = repo.get_issue(x)
issue.create_comment(y)
print("")
print("Successfully commented")
