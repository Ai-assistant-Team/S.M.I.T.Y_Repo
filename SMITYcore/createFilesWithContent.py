#
# Script created by Theodore Economides (Θόδωρος Οικονομίδης)
#

# Constants

DIRNAME = 'Keywords'
FILENAMES_FILE = 'filenames.txt'
FILECONTENTS_FILE = 'contents.txt'

# Main


def getNames(filenamesFileName):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------
    
    filenamesFile = open(filenamesFileName, "r")

    names = filenamesFile.read()

    list_of_names = names.splitlines()

    filenamesFile.close()

    return list_of_names


def getContent(fileContentsFileName):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    fileContentsFile = open(fileContentsFileName, "r")

    content_of_all_files = fileContentsFile.read()

    content_of_file = content_of_all_files.splitlines()

    fileContentsFile.close()

    return content_of_file


def createFiles(directory, list_of_file_names, list_of_file_contents):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    import os

    if not os.path.exists(directory):
        os.mkdir(directory)

    if len(list_of_file_names) == len(list_of_file_contents):

        for i in range(len(list_of_file_names)):
            filename = list_of_file_names[i]
            content = list_of_file_contents[i]
            with open(os.path.join(directory, filename + '.txt'), 'w') as file:
                file.write(content)

        print('Successfully Created Files!')

    else:
        print('Unequal number of lines in files!')
        print('names : ', len(list_of_file_names), ' content : ', len(list_of_file_contents))
        exit(1)


def main():
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    list_of_names = getNames(FILENAMES_FILE)
    content_of_files = getContent(FILECONTENTS_FILE)
    createFiles(DIRNAME, list_of_names, content_of_files)



main()
