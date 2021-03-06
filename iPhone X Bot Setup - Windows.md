# iPhone X Bot Setup - Windows
**Before setting up the bot, please go to your Apple account and add your credit card information as well as your shipping information. This is so the bot can check you out faster!**

Also, please have the latest version of Chrome installed. This will only work on Chrome!

### Installing Python
Python is the programming language that the bot was written in.
The first step is to figure out if you have an AMD or Intel processor. You can figure out which one you have by following the steps on this website: 

> https://amiduos.com/support/knowledge-base/article/how-do-i-know-if-i-have-an-intel-or-amd-cpu

If you have an AMD processor, then download: https://www.python.org/ftp/python/3.6.3/python-3.6.3-amd64.exe

If you have an Intel processor, then download: https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe

Once you download the file, open it up. At the bottom, check the box saying 'Add Python 3.6 to PATH'. Then press 'Install Now'. When installation is finished, press 'Disable path length limit', then press 'close'. Restart your computer.

### Installing Selenium
Selenium is a codebase that this bot relies on to run. It can be installed to Python by first opening up the start menu and typing in 'cmd' (without the quotation marks). Right click on the program and press 'Run as administrator'. Finally, type in:
> pip install -U selenium

and press enter. Once it finishes installing, restart your computer.

Download this file: https://chromedriver.storage.googleapis.com/2.33/chromedriver_win32.zip

and then extract this file into the directory where the scripts are.

### Running The Setup File
Open up the folder containing all the files. Right click the file called *setup.py* and navigate to 'Open with', and press 'Python'. Follow the setup instructions. **Please double check that the information you entered is correct.**

### Running The Bot
**Right before the preorder starts** open up the Python application that was downloaded. Go to File > Open and navigate to where you stored 'main.py', and open it. When the preorder goes live, go to Run > Run Module. Let the bot order the iPhone for you!

Please run the bot before the preorder goes live to make sure that it loads up the browser. The bot should not work yet, because the preorders haven't gone live.

Note: If the bot pauses, for longer than 20 seconds, then please continue the pre-order manually. This shouldn't happen because Apple's servers are very good, especially on pre-order pages.
