import read
import send


def test1(n) :
    read.show_emails(n)



def test2(body="", email="", subject="") :
    send.create_send(body, email, subject)
    

test1(2)
#Test with number 2 which shows the latest 2 emails

test1(100000000)
#Test with a really large number, I limitted it to max 20 latest emails

test2("hello", "rgererge@egerg", "subject")
#Test with an email that does not exist

test2("hello", "dai19078@uom.edu.gr")
#Test without a subject

test2("hello", "dai19078@uom.edu.gr", "This is the subject")
#Test with every parameter
