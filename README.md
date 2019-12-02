# Compare-Images-Python
Automate to figure out if N pairs of images are different


Assumptions:
1. Please make sure Input CSV file and all the images to be compared are in same folder
2. Make sure the name you provide for image 1 and image 2 are only image name with format imagename.png or imagename.png
3. You will see the csv output file in the same folder
4. Make sure you clone the file compareimage.py in the same folder
5. Make sure you clone the repo only from Master branch
6. Make sure the column name of input csv file of first column has to be "image1" and second column name has to be "image2"


The script can be executed on both Linux(Ubuntu) and Windows platforms.
For Ubuntu Users:

Basic setup:
First thing’s first,
1. we have to install git to use it! We can do it quick and easy using apt:
sudo apt install git-all

Go ahead and navigate to the directory you want to setup version control for in the terminal using the standard “cd” command.

you can specify the path of the directory where git needs to make a clone. So, to clone in a target directory use the following command
git clone -b <name_of_the_branch> --single-branch <url_of_the_repo> <path_of_the_empty_directory>

Cloning a specific branch(Master) only:
git pull origin master


If you’d like, you can go ahead and save your git username and email so that you won’t have to enter them in again for future git commands.
git config --global user.name "User Name"
git config --global user.email "email"

2. We have to install Python to use it!

How to install Python on Linux?
To manage software packages for Python, let’s install pip:

On terminal type the following:
sudo apt-get update
sudo apt-get install python-pip
pip3 install python
python will get installed
execute below command to check python version
python --version 

You will need to install the pillow for the code to work.
pip install Pillow

cd to the directory and run imagedf.py, after the script finish its execution it will generate result.csv file which you can use 


For Windows Users:

How to install Python on Windows?
Python is available from its website, Python.org. Once there, hover your mouse over the Downloads menu, then over the Windows option, and then click the button to download the latest release.

Once the package is downloaded, open it to start the installer.

It is safe to accept the default install location, and it's vital to add Python to PATH. If you don't add Python to your PATH, then Python applications won't know where to find Python (which they require in order to run). This is not selected by default, so activate it at the bottom of the install window before continuing!

open terminal and execute below command
python --version

You will need to install the pillow for the code to work.
pip install Pillow

Congratulations! Setup completed!
