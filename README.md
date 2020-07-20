{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# cookieswap\n",
    "\n",
    "*Taking online community offline*\n",
    "\n",
    "This project was completed while a New York Insight Data Science Fellow, Summer 2020 by Noëlle Bittner\n",
    "\n",
    "# Introduction\n",
    "\n",
    "The Food52 Holiday Swap is an annual \"Secret Santa\" style event where members of the Food52.com community can opt to send packages to other participants around the world of homemade sweets and local sweets. Since its inception in 2010, it has steadily grown to include over 1,200 participants yearly. Here, we developed a model to identify Food52 users who are likely to be good Holiday Swap participants based on their user profiles but have not yet joined. The use case for this model is specific and to be used once yearly during ramp-up to the Holiday Swap when we are advertising in October/November. \n",
    "\n",
    "# Requirements\n",
    "* python 3.8.3\n",
    "* numpy 1.18.5\n",
    "* pandas 1.0.3\n",
    "* beautifulsoup 4.9.1\n",
    "* scikit-learn 0.22.1\n",
    "* seaborn 0.10.1\n",
    "* matplotlib 3.2.2\n",
    "\n",
    "# Contents\n",
    "+ **scrape_F52.py** - Used to scrape information from Food52 profiles of either a list of known users or any number of random profiles\n",
    "+ **randomforest_binary.ipynb** - model development for binary classification\n",
    "+ **randomforest_multi.ipynb** - model development for multi-class classification (future use)\n",
    "+ **cookieswap_run.py** - participant classifier \n",
    "\n",
    "# Usage\n",
    "\n",
    "This project uses aspects of usage information reported on Food52 user profiles and leverages them to understand current participants in the Food52 swap and predict future participants. '\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
