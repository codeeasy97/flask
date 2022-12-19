#Python PIP

#What is PIP?
"""
PIP is a package manager for Python packages, or modules if you like.

"""
#what is module?
"""
The module is a simple Python file that contains collections of functions 
and global variables and with having a .py extension file
Datetime
Regex
Random
"""

#What is a Package?

"""
The package is a simple directory having collections of modules.
Numpy 
Pandas
"""

#what is library?
"""
It is a reusable chunk of code that we can use by importing it into our program
Matplotlib
Pytorch
Pygame
Seaborn
"""

#Install PIP in windows

"""
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

"""

#Install PIP in ubuntu
"""
sudo apt install python3-pip
"""

#Check if PIP is Installed

"""
pip3 --version
"""

#Download a Package

"""
pip3 install numpy
"""

#Using a Package
"""
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])

"""
import numpy as np
arr = np.array([1,2,3,4])
print(arr[0])

#Find Packages
"""
Find more packages at https://pypi.org/.
"""
#Remove a Package
"""
pip3 uninstall numpy
"""
#List Packages
"""
pip3 list
"""
