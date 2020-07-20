# cookieswap

*Taking online community offline*

This project was completed while a New York Insight Data Science Fellow, Summer 2020 by Noëlle Bittner

# Introduction

The Food52 Holiday Swap is an annual "Secret Santa" style event where members of the Food52.com community can opt to send packages to other participants around the world of homemade sweets and local sweets. Since its inception in 2010, it has steadily grown to include over 1,200 participants yearly. Here, we developed a model to identify Food52 users who are likely to be good Holiday Swap participants based on their user profiles but have not yet joined. The use case for this model is specific and to be used once yearly during ramp-up to the Holiday Swap when we are advertising in October/November. 

# Requirements
* python 3.8.3
* numpy 1.18.5
* pandas 1.0.3
* beautifulsoup 4.9.1
* scikit-learn 0.22.1
* seaborn 0.10.1
* matplotlib 3.2.2

# Contents
+ **scrape_F52.py** - Used to scrape information from Food52 profiles of either a list of known users or any number of random profiles
+ **randomforest_binary.ipynb** - model development for binary classification
+ **randomforest_multi.ipynb** - model development for multi-class classification (future use)
+ **cookieswap_run.py** - participant classifier 

# Usage

This project uses aspects of usage information reported on Food52 user profiles and leverages them to understand current participants in the Food52 swap and predict future participants. `scrape_F52.py` has two use cases. To scrape profile information from a known list of profiles (formatted either https://food52.com/users/profilenumber or https://food52.com/users/profilenumber/username): 

`python3 scrape_F52.py PATHTOINPUTFILE TREATMENTCODE OUTFILE.csv`

To scrape profile information from a random number of users:

`python3 scrape_F52.py NUMBEROFPROFILES TREATMENTCODE OUTFILE.csv`

Please note, profiles that have been deleted cannot be scraped so overestimate the number of profiles you require. 

`cookieswap_run.py` requires an input csv containing all scraped profile information and will output a list of profiles. 

# Acknowledgements
The author appreciates the help of the Insight Program Directors and fellow fellows for their constructive comments and enthusiasm as well as all of the previous Food52 Holiday Swap participants for creating this database. 

