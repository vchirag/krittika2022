# XSM-Analysis-KSP3.0

## Branch guidelines

- Everyone should work on their respective branches and not commit to master branch.

- Whenever master branch is updated, you should rebase your branch to merge the changes.  
  Use the following set of commands to do this when asked to:

```
# Assuming you are in your branch
git stash
git checkout master
git pull
git checkout your-branch
git rebase master
git stash pop
```

## Structure of the repository

### Data files

- The data should only be present in data/ directory - be it input or output (results).
- Do not upload any data to the repository. Instead use gitkeep to keep the structure of the repository.
- For now, lc, zip and png files are excluded.
- If you have any doubts and/or want any changes in the generic structure, post it on the slack channel.
- Appropriate changes will be made in master branch and pushed to the repository.

### Code files

- Add only python script - no notebooks.
- At the top of your python script, add instructions on running it.
- Also, mention the data files used in the script.
- Essentially, make the script generic and reusable by other people.
