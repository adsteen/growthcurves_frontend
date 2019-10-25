# Notes on growthcurves_frontend

This is the nascent [streamlit](https://streamlit.io) app that will act as the frontend of code by David Talmy and Spiro Papoulis to fit models to bacterial growth curves.

## To run

I'm using python 3.7.3. Streamlit runs on python 2.7.0 or python >= 3.6. An important feature, annoyingly called ['magic'](https://streamlit.io/docs/api.html#magic-commands), does not work on python 2.

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
