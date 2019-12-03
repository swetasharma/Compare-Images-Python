# Compare-Images-Python
Automate to figure out if N pairs of images are different.

## Assumptions:
1. Please make sure Input CSV file and all the images to be compared are in ```Compare-Images-Python```.
2. Make sure the name you provide for image 1 and image 2 are only image name with format imagename.png or imagename.gif.
3. You will see the csv output file in the same folder.
4. Make sure you clone the file compareimages.py in the same folder.
5. Make sure you clone the repo only from ```master``` branch.
6. Make sure the column name of input csv file of first column has to be "image1" and second column name has to be "image2".
7. The user takes the backup of the generated output csv file in some other folder before running the script again. The user will lose the output data if the back up is not taken of different input image file to be compared.

The script can be executed on both Linux(Ubuntu) and Windows platform.
## Basic setup:
First thing’s first,
1. we have to install git to use it! We can do it quick and easy using apt:
```
sudo apt install git
git --version
```
### 1. Clone this repo
```
git clone https://github.com/swetasharma/Compare-Images-Python.git
cd Compare-Images-Python
```

### 2. We have to install Python to use it!
How to install Python on Linux?
To manage software packages for Python, let’s install pip:

On terminal type the following:

```
sudo apt-get update
sudo apt-get install python-pip
pip3 install python
```
python will get installed.
execute below command to check python version
```
python --version 
```

### 3. You will need to install the pillow for the code to work.

```
pip install Pillow
```

cd to the Compare-Images-Python directory and run compareimages.py, after the script finish its execution it will generate result.csv file where you will see 2 other columns similar and elapsed which will help you to identify which images are different.


## For Windows Users:

### 1. Install Git on Windows:
To download the latest version of Git, click on the link:
https://git-scm.com/download/win/

After your download is complete, Run the .exe file in your system.
Use Git From Git Bash Only

### 2. How to install Python on Windows?
Python is available from its website, Python.org. Once there, hover your mouse over the Downloads menu, then over the Windows option, and then click the button to download the latest release.

Once the package is downloaded, open it to start the installer.

It is safe to accept the default install location, and it's vital to add Python to PATH. If you don't add Python to your PATH, then Python applications won't know where to find Python (which they require in order to run). This is not selected by default, so activate it at the bottom of the install window before continuing!

open terminal and execute below command
python --version

Repeat step 3 given above for windows as well.

Congratulations! Setup completed!


