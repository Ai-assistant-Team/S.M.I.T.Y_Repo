#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

# Sources : https://stackoverflow.com/questions/6227590/finding-the-users-my-documents-path
import os

from SMITY.definePATH import *
from pathlib import Path


def create():
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    try:
        # create Recourses Dir
        Path(RESOURCES_PATH).mkdir(parents=True, exist_ok=True)

        ## Create Subdirectories for each script that needs them
        # News
        Path(PATH_TO_NEWS).mkdir(parents=True, exist_ok=True)
        # GUI
        Path().mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'About')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Add_Aplications')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Add_website')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Aplications')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'change_location')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Home_page')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'my_websites')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Users_Aplications')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Settings')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Calendar')).mkdir(parents=True, exist_ok=True)
        # Calendar Subfolders
        Path(os.path.join(PATH_TO_GUI, 'Calendar', 'Months_Imagies')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Calendar', 'today_numbers')).mkdir(parents=True, exist_ok=True)
        Path(os.path.join(PATH_TO_GUI, 'Calendar', 'year_numbers')).mkdir(parents=True, exist_ok=True)

        # Settings
        Path(PATH_TO_SETTINGS).mkdir(parents=True, exist_ok=True)
        # AlarmClock
        Path(PATH_TO_ALARM_CLOCK).mkdir(parents=True, exist_ok=True)
        # Checklists
        Path(PATH_TO_CHECKLISTS).mkdir(parents=True, exist_ok=True)

    except PermissionError:
        pass

