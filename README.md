# Bitly url shorterer

This program shortens your link via bit.ly or views how many times your bitlink have been clicked on.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Before launching the program your personal generic oauth token from bit.ly (the instructions how to get one are described on the [bit.ly web-site](https://dev.bitly.com/get_started.html)) has to be put in .env file, whick looks like:
```
ACCESS_TOKEN=
```

To run the script you are to use the following bash command (make sure you have opened the directory with url_shorterer.py in command line):
```
python main.py your_link
```

or, if there is a conflict with Python2:
```
python3 main.py your_link
```

where `your_link` could be:

1. any url - e.g. [http://google.com](http://google.com) - the script will create a bitlink for it;

2. any bitlink - e.g. [bit.ly/2ZHJWq4](http://bit.ly/2ZHJWq4) - the script will show the amount of the clicks on that link since it was created. Links start with 'http://' or 'https://' work as well.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).