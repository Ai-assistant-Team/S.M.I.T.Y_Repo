#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#

# Sources : https://stackoverflow.com/questions/6227590/finding-the-users-my-documents-path

## This script defines constants that store the paths to the root (RESOURCES)
## and and first level directories that contain the needed files for the other scripts to work
import os

# Get absolute path to user's Documents Folder
root = os.path.expanduser('~\\Documents')
# Get absolute path of project's root Folder
# root = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

# Root
ROOT_PATH = os.path.join(root, 'SMITY')

# Resources Folder (contains everything S.M.I.T.Y. needs)
RESOURCES_PATH = os.path.join(ROOT_PATH, 'Resources')

# First Level Resources Subfolders
PATH_TO_NEWS = os.path.join(RESOURCES_PATH, 'News')
PATH_TO_GUI = os.path.join(RESOURCES_PATH, 'GUI')
MY_OUTPUT = os.path.join(PATH_TO_GUI, 'output.txt')
PATH_TO_SETTINGS = os.path.join(RESOURCES_PATH, 'Settings')
PATH_TO_ALARM_CLOCK = os.path.join(RESOURCES_PATH, 'AlarmClock')
PATH_TO_CHECKLISTS = os.path.join(RESOURCES_PATH, 'Checklists')
