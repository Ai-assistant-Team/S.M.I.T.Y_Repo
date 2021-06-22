# -*- coding: utf-8 -*-

#
# Script created by Theodore Economides
#
import subprocess


def lookFor(filename):
    ## ------------------------------------------------------
    ## created by Theodore Economides
    ## ------------------------------------------------------

    ## This function could raise a UnicodeDecodeError.
    ## This error is not Handled internally, but is expected to be handled by the calling function.

    # runs the "where" command on windows shell, as a subprocess
    out = subprocess.Popen(['where', filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()

    stdout = stdout.splitlines()[0]  # if more than one lines are returned, the first one is used
    stdout = stdout.decode()   # removes the carriage return characters from the end of the string and turns b string to string
    if stderr is None:
        # according to the results, it either
        if stdout == 'INFO: Could not find files for the given pattern(s).':
            # returns an error code to notify that file was not found
            return 3        # 3 : File Not Found
        # or returns the file's absolute path
        return stdout
    else:
        return 1        # 1: Something Went Wrong (General Error)
