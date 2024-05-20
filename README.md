# PythonTelegramTools
Uploads profile picture to Telegram. If you want to, you can chose up to two pictures for something like light- and darkmode. 

## Prereqisites
- Make sure Python 3 is installed and working
- Make sure PIP is installed and working

## Installation
Go to https://my.telegram.org and login. If not already done, click on API developtment tools and create a new application. 
Copy your API id and your API hash. 

Create a .env-File and paste the following template:
```
API_ID=123456789                                                    # API-ID from my.telegram.org
API_HASH='e19a7b5d3c2f9a8b6d4e3c1a7b8d5e9a'                         # API-Hash from my.telegram.org
PICTURE_DAY='images/brownies-1.jpg'                                 # Path (relative to script or absolute) to desired image for light-mode
PICTURE_NIGHT='images/brownies-2.jpg'                               # Path (relative to script or absolute) to desired image for dark-mode
```

On the first run of the script, Telegram creates a session. In order to use it, you have to authenticate via your telephone-number (international format. e.g. +49123456789234)

## Usage
The script supports two arguments:
- --color: Control which color-mode is being used. "dark" and "night" trigger the nightmode everything else defaults to the lightmode.
- --file: Specify a certain file. When used, light- and darkmode will be ignored.

Example:
``` bash
python ./program.py --color dark
```