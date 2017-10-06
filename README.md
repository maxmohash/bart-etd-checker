# BART ETD Checker

## Check BART ETD from a station to a station plus get latest delays and advisories

Best practice to use the virtualenv by following the below steps:

```
sudo easy_install pip
pip install virtualenv
pip install -Ur requirements.txt
virtualenv venv
source venv/bin/activate
```

#### Now to get the BART ETD just type in terminal:

`python bartetdchecker.py`

#### You can also use Makefile commands to install everything:

`make clean freshstart`

##### Example Output:

```
Next train to Dublin/Pleasanton from Mont in 8 minutes

Next train to Dublin/Pleasanton from Mont in 22 minutes

Next train to Dublin/Pleasanton from Mont in 37 minutes

No delays reported.

No advisories at the moment!
```

##### Read this https://api.bart.gov/docs/overview/ to know more about BART api.

##### Credits to https://api.bart.gov/api/ for making this possible!

### Now go and catch BART and enjoy the ride safely!