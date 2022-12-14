![image](https://user-images.githubusercontent.com/101386337/202465189-780329e3-3c63-455e-a217-b3c6af18b451.jpeg)

# steg
steg 🐕 is an easy to use python 🐍  library for requests

# Install
```
git clone https://github.com/Rayan25062011/steggy
```
## setup
Run the following to begin
```
./setup.sh
```

# How to use

## Sending data
```python
from steg import *

s = steg()

s = s.send(site="https://example.com", data="this is an example", display_response=True)
```
Definition:

site: Site is the website on which you would like to perform your activity

data: Data is the data you would like to send to the requested website

display_response: display_response means you would like to show the response from the website

## Getting data
```python
from steg import *

s = steg()

s = s.find(site="https://example.com", data="example2", display_response=True, content=True, headers="")
```
New definitions:

content: content is the content received by the website, if you enable it, it will show the content received

headers: headers is an HTTP header you can use while getting some data

## Page source code
This option is for getting the source code of a specific page
```python
from steg import *
s = steg()
s = s.source(site="http://example.com/page.php?id=value")
```

# Terms of use
Do not use this for any malicious activity, i am not responsible for any of your actions. Use this responsibly.
