#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#


## This script defines constants that store the paths to the root (RESOURCES)
## and and first level directories that contain the needed files for the other scripts to work
import os

# Get absolute path of root Folder
root = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

# Root
RESOURCES_PATH = os.path.join(root, 'Resources')

# First Level Subfolders
PATH_TO_NEWS = os.path.join(root, RESOURCES_PATH, 'News')
PATH_TO_GUI = os.path.join(root, RESOURCES_PATH, 'GUI')
MY_OUTPUT = os.path.join(root, PATH_TO_GUI, 'output.txt')
PATH_TO_SETTINGS = os.path.join(root, RESOURCES_PATH, 'Settings')
PATH_TO_ALARM_CLOCK = os.path.join(root, RESOURCES_PATH, 'AlarmClock')
PATH_TO_CHECKLISTS = os.path.join(root, RESOURCES_PATH, 'Checklists')
