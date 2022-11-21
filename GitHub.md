#  How To setup Git Step wise Step
## Before start you must have any gmail Account

# Step 1:
1. Create a github account - https://github.com/
2. After Login in Github Account -> Click on button create a new repositoty
3. Eneter Repository name (choose any name related to your work)
4. Enter Description (not mandatory)
5. Choose public option
6. Click on Add a README file option
7. Now Click on button Create repository
8. Your repository is created successfully
9. On left hand side click on your repository link you have just created.
10. Now click on Code Button in your screen, and you will see three option
Https, SSH, Github CLI, and we will use SSH option to clone and push code

# Step 2: Create a SSH key

# See Image:
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/github-key-1.jpg.jpg?raw=true)

1. Open your terminal and type ssh-keygen
2. This will ask you 
    Enter file in which to save the key (/home/tech/.ssh/id_rsa):
    Here It is asking for you path and filename where it will store your public key
    Here my path of ssh file is /home/tech/.ssh your path can be different 
    (No problem copy your path and paste after this line like below)
    Enter file in which to save the key (/home/tech/.ssh/id_rsa):/home/tech/.ssh/codeeasy_multi
    Here you can put any name inplace of codeeasy_multi and press enter
3. Now It will ask for Enter passphrase (empty for no passphrase): 
    Do not right anything only press enter
4. Now It will again ask Enter same passphrase again: 
    Do not right anything only press enter
    It will generate a pub file like below
    Your public key has been saved in /home/tech/.ssh/codeeasy_multi.pub
5. Now right a next command - (cat command)
    cat /home/tech/.ssh/codeeasy_multi.pub (this is public key file path, your path can be different)

6. Copy generated key to github

# Step 3: Where to copy this code?

# See Image:
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/github-step1.jpg?raw=true)

1. Open your github account you have just created and log in if not.
2. Go to top right corner of the page and click on profile icon.
3. Click on setting option
4. Find "SSH and GPG keys" on Left Side of Navigation and Click
5. Click on button New SSH key
6. Enter any unique name in title or anything
7. Copy generate SSH key from your terminal and Paste here in Key Textbox
8. Click on button Add SSH key
Now your SSH key has been saved

# Step 4: Configure github Config

# See Image: config file

![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/github-config.jpg?raw=true)

1. open terminal and type : touch ~/.ssh/config
2. Now open Create config file : sudo nano ~/.ssh/config
3. Add Below code:
#Account-4
Host github.com-codeeasymulti
  HostName github.com
 # IgnoreUnknown UseKeychain
 # UseKeychain yes
  IdentityFile ~/.ssh/codeeasy_multi

Note: In IdentityFile "codeeasy_multi" is name which you have created to store public
key in second step.

4. Now Press Ctrl+s and Ctrl+x to save file and exit.

# Step 5: Clone your project

# See Image: config file

![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/github-clone.jpg?raw=true)

1. open Github.com and login if not
2. Click on your repository url on left side
3. Click on Code button and copy SSH url
4. Open terminal and type git clone <paste your copied url>
Ex: git clone git@github.com:codeeasy97/flask.git
This will clone your project
5. Go to your project folder -> right click -> choose open terminal
6. Now you can open this project on your code editor (vscode)
7. add or create any new file
8. Go to terminal
9. type command : git status (it will show you modified files)
10. Commit changes type command : git commit -am "first commit"
11. Push changes to github Command : git push origin main
12. Your Changes are successfully added to github.com
13. Open github.com click on your repository and check new file which you have created on your local system has been pushed to github repository.

Thanks!