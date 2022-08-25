from github import Github

g= Github('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')
repo_name= input("Enter the reop path( username/repository_name ): ")
repo = g.get_repo(repo_name)


# repo = g.get_repo("PyGithub/PyGithub")
contentsa = "from github import Github g= Github('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')repo_name= input(Enter the reop path( username/repository_name ): repo = g.get_repo(repo_name)"


# repo = g.get_repo("PyGithub/PyGithub")

# repo.create_file("File_Handling.py", "Hello","Enter your Content Here",  branch="Diwasdrpm")
repo.create_file("File_Handlin.py", "Hello",contentsa,  branch="Diwasdrpm")