##  Install MySQL Workbench

#### Step1: Download Deb Package: https://dev.mysql.com/downloads/repo/apt/
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-workbench/1.png?raw=true)

####  Step2: Click No thanks, just start my download
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-workbench/2.png?raw=true)

####  Step3: When the dialogue box appears, select the Save file option and click Ok.
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-workbench/3.png?raw=true)
 
#### Step4: Wait for the download to complete. Then, open a terminal window (Ctrl + Alt + t) to add the MySQL apt repository.

#### Step5: In most cases, the saved file will be located in the Downloads folder. To verify its location, navigate to Downloads and list the content of the directory:

```
cd ~/Downloads
ls
```
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-workbench/4.jpg?raw=true)

#### Step6: Next, add the official MySQL repository to the apt source list by running the command:
```
sudo apt install ./mysql-apt-config_0.8.22-1_all.deb
```
If above will not work use
```
sudo snap install ./mysql-apt-config_0.8.22-1_all.deb
```

#### Step7. A pop-up window appears asking which MySQL product to install. As the required product is preselected, scroll down to Ok and hit Enter to continue installing.
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-workbench/5.png?raw=true)

Wait for the installation to complete.

#### Step8: Then, update the apt cache to add the new repository source:
```
sudo apt update
```

Step9: Finally, install MySQL Workbench by running:
```
sudo apt install mysql-workbench-community
```

OR IF above not Workbench
```
sudo snap install mysql-workbench-community
```

#### Step10: Press y when asked to confirm the installation and wait for the process to complete.

Launch MySQL Workbench
```
mysql-workbench
```

#### Step11: IF error occur while connecting database to workbench like below
![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-workbench/7.png?raw=true)

####    Run command to solve issue
```
sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service
```

![alt text](https://github.com/codeeasy97/flask/blob/main/images/git/mysql-workbench/8.png?raw=true)


####    To Remove MySQL-workbench
```
sudo snap remove mysql-workbench
```