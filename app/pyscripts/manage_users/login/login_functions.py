from question_page import showQuestionPage
from page2D import showPage2D
import config

# functions accessed from main page to display features depending on user login status

def showQuestionPageLoggedIn():
    # shows question page only if user is logged in

    print("isLoggedIn:", config.isLoggedIn)
    if config.isLoggedIn:
        showQuestionPage()
    else:
        print("Not logged in")
        showPage2D()

def logOut():
    # sets global variables when user logs out

    config.isLoggedIn = False
    config.userID = None
    config.isStudent = False
    config.isTeacher = False
    showPage2D()

