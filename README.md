# stock_picker

by Joe Hahn,<br />
jmh.datasciences@gmail.com,<br />
14 March 2018<br />
git branch=master

### Summary:
tbd...

### Setup:

Clone this repo:

    git clone https://github.com/joehahn/stock_picker.git
    cd stock_picker

Install the following libraries if on OSX:

    wget https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
    chmod +x ./Miniconda2-latest-MacOSX-x86_64.sh
    ./Miniconda2-latest-MacOSX-x86_64.sh -b -p ~/miniconda2
    ~/miniconda2/bin/conda install -y jupyter
    ~/miniconda2/bin/conda install -y keras
    ~/miniconda2/bin/conda install -y seaborn
    ~/miniconda2/bin/conda install -y scikit-learn

Then clone this demo's source code from this private repo:

    git clone https://github.com/joehahn/stock_picker_source.git


### Execute:

1 The following selects the tickers that will be modeled:

    ./select_tickers.py

this reads the 2017 NYSE data and selects the top 509 tickers (out of 3131 possible tickers)
responsible for 80% of the market's dollar-volume. This demo assumes that most of the signal
in the market data resides in the most-traded tickers, and so the remainder of
this demo will focus on the top %16 of tickers that drive %80 of the market value.
A list of those tickers is stored in data/selected_tickers.pkl, with a plot also getting
stored in figs/selected_tickers_volume.png .

2 Get openers:

    ./stock_picker_source/get_openers.py

this saves in file data/openers.pkl the opening price and volume for all tickers,
which are used later to fill data gaps for those tickers that start trading after 2013.

3 Prep historical training data

3 Train model on historical data

4 Loop over successive dates and predict+train



