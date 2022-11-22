##   How To Install Python On Linux/Ubuntu 20.04 LTS


####    Step 1: Update system repositories
    ```
    sudo apt update
    ```

####    Step 2: Install prerequisite package
    ```
    sudo apt install software-properties-common
    ```

####    Step 3: Add “deadsnakes” PPA (Personal Package Archives)
    ```
    sudo add-apt-repository ppa:deadsnakes/ppa
    ```

####    Step 4: Python 3.9 installation on Ubuntu 22.04
    ```
    sudo apt install python3.9
    ```

####    Step 5: Verify Python version
    ```
    python3.9 --version
    ```

### Uninstall python Linux/Ubuntu
```
    1.  sudo apt-get clean

    2.  sudo apt-get autoremove --purge

    3.  sudo apt-get remove python3.9

    4.  sudo apt-get autoremove

```