

## Common Commands


    git clone https:/blah   # Used to download a repository. Need to get the
                            # webside address somehow. Github is very easy


    git status              # **VERY** useful. Good way to see what is going on
                            # without having to go to website all the time
                            # Use often, doesn't mess with anything 
    git pull                # Good enough for most pulls
    git pull origin master  # get all changes in master branch. Useful if
                            # working with branches
    git add -A              # add all files to the waiting list
                            # Can also specify which files to add
    git commit -m 'comment' # add the files to the repository, make 
                            # comment about the commit
    git push                # Good enough for most pushes. 
    git push -u origin xx   # push xx to the remote repository branch.
                            # Used for branching




## Typical Working flow - updating repo

    git status              # Check for changes
    git add -A              # Add all files to repo
    git commit -m 'comment' # Commit with comment
    git push                # push to current branch. 


## .gitignore file
.gitignore is a file that tells git what is should avoid adding. For example,
to avoid adding image files to the repos and a folder called "examples" add
this to the .gitignore. 

    *.jpg
    examples/


## Credential helper - not needed for AWS
Will store credentials for 15 minutes

    git config --global credential.helper cache

## Repo Info

    git status              # get the status of the repo
    git log                 # get a log of the repo
    git diff                # changes not stage
    git diff --staged       # changes staged but not commited


## Branching
Be careful with branching. Very useful, but messes things up in a hurry

    git branch              # shows branches and current
    git branch xx           # add branch
    git checkout xx         # checkout branch
    git merge xx            # merge xx to master
    git branch -d xx        # will delete the branch 


# Other Notes 
## In case you delete local files on accident and need them

    git reset -- hard origin/master
