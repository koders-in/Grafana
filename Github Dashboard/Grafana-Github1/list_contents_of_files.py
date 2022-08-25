from github import Github

g= Github('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')
repo_name= input("Enter the reop path( username/repository_name ): ")
repo = g.get_repo(repo_name)
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        print(file_content)

print("")
print("")
x = input("Enter the name of any file(path) availiable above to list all the contents of that file : ")
file_content = repo.get_contents(x)
print(file_content.decoded_content.decode())