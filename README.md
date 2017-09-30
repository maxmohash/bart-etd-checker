# BART ETD Checker

## Python way to check BART ETD from a station to a station

Best practice to use the virtualenv by following the below steps:

`sudo easy_install pip`

`pip install virtualenv`

`pip install -Ur requirements.txt`

`virtualenv venv`

`source venv/bin/activate`

#### Now to get the BART ETD just type in virtualenv or in terminal directly:

`python bartetdchecker.py`

#### You can also Use Makefile commands to install everything:

`make clean freshstart`

##### Example Output:

```
Next train to Dublin/Pleasanton from Mont in 16 minutes
Next train to Dublin/Pleasanton from Mont in 36 minutes
Next train to Dublin/Pleasanton from Mont in 56 minutes
```

##### Read this https://api.bart.gov/docs/overview/ to know more about BART api.

##### Credits to https://api.bart.gov/api/ for making this possible!

### Now go and catch BART and enjoy the ride safely!