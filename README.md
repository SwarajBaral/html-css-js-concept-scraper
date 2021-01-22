# html-css-js-concept-scraper
A python script to that extracts the concepts of html css and js from [w3schools](https://www.w3schools.com/) inside your terminal.
The folder 'Script and Requirements' contains all the required elements needed to execute this script inside your terminal

## Getting Started
##Packages
To install the required packages for this script. Navigate to the 'Script and Requirements' folder and run the following command in the terminal
```python
pip install -r requirements.txt
```
## Usage
To run the script
```python
python webscraper.py
```

## Built with
Python 3.8.3rc1

## Author
Swaraj Baral - *Student*

---
**NOTE**
: The script wont work if correct browser driver path isn't provided. The webdriver has to be chosen according to the user's web browser and browser version.
- To use a different web browser or a different version of a browser:- 
  1. Download the latest version of preferred browser
  2. Change the executable_path = ' ' parameter. Set it to the location of your driver.
  ```python3
  browser = wb.Chrome(executable_path='<path of driver>/<broswer driver>.exe', options=options)
  ```
---
