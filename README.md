# verily-hello-vc

Hello T9Hacks! Welcome to Verily's Introduction to Version Control talk. Today, we'll be walking you through the basics of how to use Github for Version control.

## A. Prerequisite: Sign up for a Github account and install Git

Git installation: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

We also need to add you as a collaborator to the Github project.

## B. Fork the Repo and Create a Pull Request

1. Go to https://github.com/KilimAnnejaro/verily-hello-vc ([t.ly/ZqjP](https://t.ly/ZqjP)).

2. Click the fork button in the top right

![image](https://user-images.githubusercontent.com/3752732/154769938-56171260-59c6-45ec-a1bd-a5ff1caebfce.png)

3. Wait until fork completes

![image](https://user-images.githubusercontent.com/3752732/154769926-ede99504-1401-4735-8618-0dc5dee39a9b.png)

4. Click `favorite_built_in_modules.py`

![image](https://user-images.githubusercontent.com/3752732/154770639-cf908545-27fd-47fc-b5b0-cb66f1e9c78e.png)

5. Click the edit button

![image](https://user-images.githubusercontent.com/3752732/154770729-2a52ad14-eee5-40af-bfc3-9f6c96add60e.png)

6. Make your changes

Just for an example, lets pretend we wanted to share our favorite python built in modules with a program like this.

All of us will add to this file, what our favorite module is, e.g.

![image](https://user-images.githubusercontent.com/3752732/154771299-e7f0cddb-b715-4308-9794-22b3153f93b0.png)

7. Add a commit message

![image](https://user-images.githubusercontent.com/3752732/154771346-87fe1ad2-2287-4181-a672-14bc18de60ca.png)

8. Commit directly to your fork's main branch

![image](https://user-images.githubusercontent.com/3752732/154771652-8a9cdb0d-5f8c-4043-bb4c-c0e9d3b850bc.png)

9. Click "Commit changes"

![image](https://user-images.githubusercontent.com/3752732/154771665-119b9b65-6e34-413d-ac6d-5de3dd3b028d.png)

10. Go back to the original repository

![image](https://user-images.githubusercontent.com/3752732/154771703-fd6e8243-6256-448f-bc51-39d66ca9eda1.png)

11. Click "Compare & pull request"

 ![image](https://user-images.githubusercontent.com/3752732/154771736-96ce3f1f-d217-4f3b-9132-8f6e587b01d4.png)

12. Click "Create pull request"

![image](https://user-images.githubusercontent.com/3752732/154771790-1c45cb8c-dce9-4c10-80e3-42dddfe43d69.png)

## C. Code Review

> **NOTE:**
> * A typical workflow is to request a reviewer, e.g.
> ![image](https://user-images.githubusercontent.com/3752732/154776429-3fedacc9-df5e-452c-afb5-be743bf2389d.png)

1. Find a buddy to review each other's code.

2. Ask your buddy to open the pull request

![image](https://user-images.githubusercontent.com/3752732/154772146-009552f1-32dc-4d71-9c67-6bd625f0ea38.png)

3. Click "Files changed" then "Review changes"

![image](https://user-images.githubusercontent.com/3752732/154772209-1f27f5b7-8ca8-449c-9de7-b79f026c7de9.png)

4. Write a message then click "Submit review"

![image](https://user-images.githubusercontent.com/3752732/154772263-31889fe5-3a34-4242-9455-f4c46f610c44.png)

5. Once reviewed, ask Annie or John to merge the PR

## D. Conflicts

Some of you will encounter conflicts:

1. Conflicts look like this:

![image](https://user-images.githubusercontent.com/3752732/154773203-625f67f2-d108-4c47-b94b-06d411d1b9d8.png)

2. Resolve your conflicts inline:

![image](https://user-images.githubusercontent.com/3752732/154773247-69256fb2-87a4-4e5d-b8f4-4e5ba393c209.png)

## E. Optional: fix a commit that went wrong

So far in this tutorial, we've mostly discussed the happy path: you code something cool, then submit it for review. But what happens if you submit a commit you don't want? Version control with git offers us a way to fix this issue!

Prerequisite: creating a commit that you don't like.

1. Run the command `git log` to print a list of all commits, then copy to clipboard the hash of the commit preceding the one you want to remove. Type `q` at the command prompt to return to your command line interface.
2. There are a lot of ways to roll back commits you don't want; some of them are detailed at <https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit>.
3. The command for completely wiping out your bad commit is `git revert <hash>` where `<hash>` is the hash of the commit you want to remove.
4. If you've already pushed bad code to a pull request, you can use the force push option to push the branch with the bad commit removed to origin. The command is `git push -f origin <branch-name>`.

## F. Cleanup

To keep your local clone neat and tidy, you'll want to wrap up your development for the day with some cleanup. You can delete your working branch with the option -D (as in, `git branch -D <branch-name>`) and update your local clone using the `git pull` command, which pulls the latest code from the remote repository.

## G. Extra credit
- How version control works: <https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain>
- Open source licensing link: <https://opensource.org/faq>
