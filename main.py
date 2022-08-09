from os import mkdir
from shutil import rmtree

from git import Repo

from config import GITHUB_TOKEN, USERNAME

target_dir: str = input('Target directory to clone to: ')
repo: str = input('Repo owner and its name: ')
branch: str = input('Branch of the repo to clone: ')

remote: str = f'https://{USERNAME}:{GITHUB_TOKEN}@github.com/{repo}.git'

try:
    rmtree(target_dir)
    print(f'Directory {target_dir} was removed successfully')
    
except FileNotFoundError:
    mkdir(target_dir)

print('Started cloning the repo...')
Repo.clone_from(remote, target_dir, branch=branch)
print('Cloned successfully')
