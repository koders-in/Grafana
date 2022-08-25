from github import Github

g= Github('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')
repo_name= input("Enter the reop path( username/repository_name ): ")
repo = g.get_repo(repo_name)
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)
