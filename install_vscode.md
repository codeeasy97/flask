##  Install Vscode on ubuntu 20.04

####    Method 1: Install Visual Studio Code with Snap

	```
    sudo snap install --classic code
	code --version

    ```
	
####   Method 2: Install Visual Studio Code with apt

	```
    sudo apt update

	sudo apt install software-properties-common apt-transport-https wget -y

	wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -

	sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

	sudo apt install code

	code --version
    ```

####    Method 3: Install Using the GUI
```

	Open Ubuntu Software Center
	
	type vscode in search
	
	Click on install button
```

####    Method 4: Using vscode website
```

	Open Browser and go to https://code.visualstudio.com/
	click on .deb button for ubuntu and for windows click on windows download button
	Now Install the downloaded exe file
    ```


