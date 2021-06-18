#
# Script created by Theodore Economides (Θεόδωρος Οικονομίδης)
#
import subprocess


def lookFor(filename):
    ## ------------------------------------------------------
    ## created by Theodore Economides (Θεόδωρος Οικονομίδης)
    ## ------------------------------------------------------

    out = subprocess.Popen(['where', filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()

    stdout = stdout.splitlines()[0]
    stdout = stdout.decode()   # removes the carriage return characters from the end of the string and turns b string to string
    if stderr is None:
        if stdout == 'INFO: Could not find files for the given pattern(s).':
            return 3
        return stdout
    else:
        return 1

