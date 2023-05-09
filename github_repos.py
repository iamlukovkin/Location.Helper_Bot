from github import Github

# using an access token
g = Github("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")

# Github Enterprise with custom hostname
g = Github(base_url="https://github.com/iamlukovkin/Location_Helper_Methods", login_or_token="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")


for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))