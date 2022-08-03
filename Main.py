from git import Repo
import os, json, shutil


with open("./config.json", mode="r") as file:
    data = json.loads(file.read())

username = data["username"]
github_token = data["github_token"]
target_dir = input("Target directory to clone to: ")
repo = input("Repo owner and its name: ")
branch = input("Branch of the repo to clone: ")
remote = f"https://{username}:{github_token}@github.com/{repo}.git"

try:
    shutil.rmtree(target_dir)
    print(f"Directory {target_dir} was removed successfully")
except FileNotFoundError:
    os.mkdir(target_dir)
print("Started cloning the repo...")
Repo.clone_from(remote, target_dir, branch=branch)
print("Cloned successfully")