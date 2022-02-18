## A. Clone this repo locally

In this section, we'll show you how to pull this repo down locally so you can write the code in a more convenient environment than the web text editor.

> **NOTE:** 
> * This section provides instruction on how to clone your repository with SSH.
>   * If that isn't working for you, feel free to clone with the HTTPS option instead.
>   * SSH is considered best practice for security reasons, and once configured it is very convenient in practice too!
> * If you already have an ssh key configured with your GitHub account, skip ahead to step 10 below.

1. [Create your ssh key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), e.g. open a command line (with terminal on Linux and MacOS or Git Bash on Windows) and run `ssh-keygen -t ed25519` while accepting all the defaults by hitting the enter key at each prompt as shown below:

```
$ ssh-keygen -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/jdimatteo/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/jdimatteo/.ssh/id_ed25519
Your public key has been saved in /home/jdimatteo/.ssh/id_ed25519.pub
```

2. Copy your **public** key to the clipboard, e.g. back on the command line run `cat ~/.ssh/id_ed25519.pub` then select the printed line and copy it to your clipboard (CTRL-SHIFT-C on Linux and Windows or CMD-C on MacOS). The text should be a long line starting with `ssh-ed25519`. Paste this text to  After you've generated a key locally, use the Linux `cat` command to output the file to your terminal.

3. Open your [GitHub user settings](https://github.com/settings/profile)

![image](https://user-images.githubusercontent.com/3752732/154405056-d9683886-7f9b-49fd-bd6f-983eaf75f498.png)

4. Drill down to [SSH and GPG keys](https://github.com/settings/keys)

![image](https://user-images.githubusercontent.com/3752732/154405195-5e092bd7-3511-487b-99c6-2d2ce1817b1f.png)

5. Click [New SSH key](https://github.com/settings/ssh/new)

![image](https://user-images.githubusercontent.com/3752732/154405268-3a8ba4fa-4bd2-4708-82ab-4535a52bdc06.png)

6. Paste your public key (copied to the clipboard in step #2) to the "Key" text box:

![image](https://user-images.githubusercontent.com/3752732/154407383-de2ff24f-6ea8-48ad-8e7e-4f477f53bcbd.png)

7. Click "Add SSH Key"

![image](https://user-images.githubusercontent.com/3752732/154407488-32385a1d-6d29-4d43-bf21-e43586a1c100.png)

8. Follow these directions to test your SSH connection: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection

9. Finally, you can clone the repo locally with ssh! Go back to the main page of this repository (if you are having trouble finding it, click [Your repositories](https://user-images.githubusercontent.com/3752732/154408379-c6d2c9c5-9b9e-4140-83e5-f3958f4b57c1.png)) and click on the Fork button. This creates a new repo that you own.

10. Click on the "Clone" button in the upper right corner of your newly created repository, then choose the SSH option, then click the copy to clipboard button, like this:

![image](https://user-images.githubusercontent.com/3752732/154408715-d6b88db5-e738-4e73-8768-eabab5bccee6.png)

10. Go back to your command line and type `git clone ` followed by pasting your clipboard (CTRL-SHIFT-V on Linux and Windows or CMD-V on MacOS).

11. You should now be able to see this repo cloned into your home directory (or anywhere you choose to place it).

## B. Make a branch

One of the most powerful features that developing code with version control offers is the ability to try experiments on your code and save the results without making potentially disasterous changes to your production code. This ability is enabled via _branching_. In this section, we'll walk through creating a branch for code.

1. If you haven't already, change directory into the repository you cloned using the `cd` command on the command line.
2. To create a branch, use the command `git branch <your branch name>`. You can check it was created by running the `git branch` command without any options and checking that the output contains the name of your branch.
3. To move into your code branch, you can use the command `git checkout <your branch name>`.

**TIP:** You can combine the above two commands into one with the syntax `git checkout -b <your branch name>`.

## C. Make a commit and create a pull request

You can save changes to your code by making commits. Let's walk through a typical process of making a change and committing it. (Before you start, make sure you're still in the branch you created above!)

1. Start by creating a new file, using `touch hello.py` or a command / text editor of your choice.

2. Add a print statement to the file, like `print("hello <your name>")`.

3. Using the command `git status`, you can see the new file you created and a notation of its status, e.g.

![image](https://user-images.githubusercontent.com/3752732/154410602-9cf48f2a-cf3c-42f9-a900-1f6f63c467e4.png)

- "Untracked" indicates the addition of a new file. If instead you had chosen to change an already existing file (like the README), the file would be listed as "Modified".

4. To add all changed files to the list, use the command `git add .` If you only want to add a specific file to the commit, replace the `.` with the file name

5. Use `git status` again and check what files are set to be added to the commit. If you've added something you don't want, this is an easy place to remove the undesired change from the commit (using the prompt from terminal output).

![image](https://user-images.githubusercontent.com/3752732/154410708-2ae51945-a7fe-44af-b260-bf159fad84a6.png)

6. Next, you'll need to add the commit to your history. You can use the command `git commit -m "<something descriptive>"` for this.

7. Finally, you'll be able to create a pull request for your commit! The command is `git push origin <your branch name>`. You'll see a link in the terminal to create a pull request on Github. Follow the link and fill out the form.

![image](https://user-images.githubusercontent.com/3752732/154410438-a902e18a-d992-46a8-a20d-7ef375b7bbc5.png)
