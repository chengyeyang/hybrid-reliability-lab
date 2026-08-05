# Git Related Operations

---

## Link Local Repository to GitHub

1. Add remote repository URL
   ```bash
   git remote add origin [https://github.com/your_account/hybrid-reliability-lab.git](https://github.com/your_account/hybrid-reliability-lab.git)

2. Verify the remote connection
   ```bash
   git remote -v

3. Rename the current branch to main
    ```bash
   git branch -M main
   
4. Push the local branch and set it to track the remote main branch
   ```bash
   git push -u origin main

* Note, this operation only needs to be done once when initializing the project.

---
## Change Git Authentication to SSH

1. Check for existing SSH keys
    ```bash
   ls -al ~/.ssh

2. Generate a new SSH key (if none exists)
    ```bash
   ssh-keygen -t ed25519 -C "your_github_email@example.com"
   
3. Start the SSH agent
    ```bash
   eval "$(ssh-agent -s)"
   
4. Add the SSH key to the agent
    ```bash
   ssh-add ~/.ssh/id_ed25519
   
5. Copy the public key  
   After you enter the command, you will then see something like `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI...`, copy it.
    ```bash
    cat ~/.ssh/id_ed25519.pub
   
6. Add the SSH key to GitHub  
   `Navigate to GitHub` -> `Settings` -> `SSH and GPG keys` -> `New SSH key` -> `Paste the copied public key and save`


7. Test the SSH connection
   ```bash
   ssh -T git@github.com
   
8. Update remote URL to SSH
    ```bash
   git remote set-url origin git@github.com:your_github_account/hybrid-reliability-lab.git
   
9. Verify the remote URL
    ```bash
   git remote -v
   
---
## Git Commands

## 1. Initialize Git
    git init

## 2. Check the status of working directory and staging area 
    git status

## 3. Add all the changes to staging area
    git add .

## 4. Commit the staged files to the Git repository to create a new version record.
    git commit -m "description of the change"

## 5. Push the local commit to the remote GitHub repository
    git push

---

### To-Do List
- [ ] To add more details, notes, and illustration for **Change Git Authentication to SSH** section 
- [ ] To find a way to better document these commands. Perhaps categorize them by functions and with explanation.
