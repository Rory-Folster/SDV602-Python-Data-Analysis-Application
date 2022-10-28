"""
Python application created for data analysists to read and interact with 3 pre-set DES.
The users will be able to sign-in, create an account, upload CSV files to be plotted
and chat between each other.

Highest crime window is currently being used for main file but login/register screen will be used in future.
"""

import highest_crime_module
import login_module

if __name__ == "__main__":
    # highest_crime_module.highest_crime_areas()
    login_module.loginScreen()