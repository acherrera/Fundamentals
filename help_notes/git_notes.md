# Git commands used often


## Initializing a repo on local machine

    git init                # Start git repo

    git remote add origin http://IP/path/to/repository #will add the directory as 'origin' for later

Will store credentials for 15 minutes

    git config --global credential.helper cache

## Repo Info

    git status              # get the status of the repo
    git log                 # get a log of the repo
    git diff                # changes not stage
    git diff --staged       # changes staged but not commited


## Common Commands

    git pull origin master  # get all changes in master
    git add -A              # add all files to the waiting list
                            # Can also specify which files to add
    git commit -m 'comment' # add the files to the repository, make 
                            # comment about the commit
    git push -u origin xx   # push xx to the remote repository branch


## Branching

    git branch              # shows branches and current
    git branch xx           # add branch
    git checkout xx         # checkout branch
    git merge xx            # merge xx to master
    git branch -d xx        # will delete the branch 


# Other Notes 
## In case you delete local files on accident and need them

    git reset -- hard origin/master