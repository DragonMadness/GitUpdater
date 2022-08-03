from git import Repo
import os, json


with open("./config.json", mode="r") as file:
    data = json.loads(file.read())

username = data["username"]
github_token = data["github_token"]
target_dir = "./code"
repo = "DragonMadness/P2PExchangeBot"
branch = "provided_api"
remote = f"https://{username}:{github_token}@github.com/{repo}.git"

try:
    os.remove(target_dir)
except FileNotFoundError:
    os.mkdir(target_dir)
    Repo.clone_from(remote, target_dir, branch=branch)
    print("Cloned successfully")