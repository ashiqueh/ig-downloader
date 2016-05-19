ig-downloader

This is a program to download the photos and videos of an instagram user. Please note that I'm still working on this, so the code could break at any time.

Currently it downloads all the pictures with no option to download fewer.

Some things to be aware of if you're using this:
  - The code as written requires chrome to be installed on your system, chromedriver.exe in the specified path, and of course selenium installed in your virtualenv.
  - Running this program takes a very long time for users with many pictures, but it can be done in the background.
  - This program uses non-trivial bandwidth, so if you're limited on that, I'd be careful.
  - Selenium settings can be a little finicky, so you might need to do some troubleshooting.

To use:
  - clone/download the repo
  - install Selenium in virtualenv, run virtualenv
  - run download.py (python download.py in command line)

Please do not use the pictures you download without consent from the owner.