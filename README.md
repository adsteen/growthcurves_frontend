# Notes on growthcurves_frontend

This is the nascent [streamlit](https://streamlit.io) app that will act as the frontend of code by David Talmy and Spiro Papoulis to fit models to bacterial growth curves.


# Instructions 

## Environment

I'm using python 3.7.3. Streamlit runs on python 2.7.0 or python >= 3.6. An important feature, annoyingly called ['magic'](https://streamlit.io/docs/api.html#magic-commands), does not work on python 2.

## To use

Enter the path of a .csv file (which must have at least 2 columns of data) as a text string into the box. If you have `git clone`ed the git repo, there will be a .csv file called `data/test.csv` - it may be important to have that there at the start.

The app loads the .csv file, adds random numbers to column 1 of the data, and plots column 1 and column 1 + normal random data (mean = 0, sd = 1) to column 0. When you press 're-run', it will calculate new random data. 

## Notes on streamlit

Streamlit has a neat design philosophy: a streamlit app is simply a python script that runs start to finish. Any time the user interacts with the app in any way, it runs start to finish again. It has a few functions to create inputs (`button()`, `checkbox()`, `selectbox()`, etc.), a few to create outputs (`text()`, `pyplot()`, `dataframe()`) and the 'Swiss Army knife' function `write()`.

The one major exception to this start-to-finish is the concept that code elements can be cached. These elements will not run again unless one of the following has changed:
1. The bytecode of the function that is cached
2. Anything that the function depends on
3. Input parameters to that function

One result of this is that you shouldn't modify objects that come from cached functions: this will cause problems. Instead, make a copy and modify that. 

### Notes to Drew

To run: I'm using a virtualenv managed by conda with python 3.7.3. 

Before running, I need to run `conda activate growthcurves_frontend`. 

To install modules, I need to use `~/anaconda/envs/growthcurves_frontend/bin/pip install packagename`
