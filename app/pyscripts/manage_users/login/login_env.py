from manage_users.__init__ import create_client, Client, supabase, hashlib
from question_page import showQuestionPage
from page2D import showPage2D
import config

# class containing properties/methods to handle user log in 
class LoginEnvironment():

    def __init__(self):
        # flag to indicate when go has been clicked
        self.goClicked = False

        # flag to indicate user type
        self.isTeacher, self.isStudent = False, False

        self.errorAlert = ""

    def onClickGo(self):
        self.goClicked = True

    def onClickStudent(self):
        # set global variables for when user is a student
        self.isStudent = True
        self.isTeacher = False

    def onClickTeacher(self):
        # set global variables for when user is a teacher
        self.isTeacher = True
        self.isStudent = False


    def getUserLoginData(self, table, username):
        # fetch and return user data from database 
        try:
            userLoginData = supabase.table(f"{table}").select("*").eq("username", f"{username}").execute().data
            # API response returns empty list if user is not found
            if userLoginData == []:
                self.errorAlert = "user not found"
                return None
            else:
                return userLoginData
        except:
            # return error if exception raised
            print("record does not exist")
            self.errorAlert = "user not found"

    def getErrorAlert(self):
        return self.errorAlert



    def hashPassword(self, enteredPassword, userLoginData):
        # apply MD5 hashing algorithm to input password and return digest
        salt = userLoginData[0]["salt"]
        saltedPassword = enteredPassword+salt
        hashedPassword = hashlib.md5(saltedPassword.encode())

        return hashedPassword.hexdigest()

    def verifyPassword(self, enteredPassword, userLoginData):
        # compares hash of input password to hash stored in database and returns true if it matches
        passwordHash = userLoginData[0]["passwordHash"]
        enteredPasswordHash = self.hashPassword(enteredPassword, userLoginData)
        if passwordHash == enteredPasswordHash:
            return True
        else:
            print("incorrect password")
            self.errorAlert = "password is incorrect"
            return False
        

    def fieldsNotNull(self, usernameField, passwordField):
        # checks input fields are not null and returns True if none are null
        if usernameField == "" and passwordField == "":
            print("empty fields")
            self.errorAlert = "please enter a username and password"
            return False
        elif usernameField == "":
            print("empty username field")
            self.errorAlert = "please enter a username"
            return False
        elif passwordField == "":
            print("empty password field")
            self.errorAlert = "please enter a password"
            return False
        else:
            return True


    def getStudentTeacherTbl(self):
        # gets table name depending on user type
        if self.isStudent:
            return "tblStudents"
        elif self.isTeacher:
            return "tblTeachers"
        else:
            # returns None if neither user type is selected
            print("student/teacher not selected")
            self.errorAlert = "please select student/teacher"
            return None


    def getUserID(self, table, username):
        # get database ID of user
        userLoginData = self.getUserLoginData(table, username)
        if self.isStudent:
            return userLoginData[0]["studentID"]
        elif self.isTeacher:
            return userLoginData[0]["teacherID"]


    def setUserID(self, table, username):
        # set gloabl userID variable to current logged in user's user ID
        ID = self.getUserID(table, username)
        config.userID = ID
        config.isTeacher = self.isTeacher
        config.isStudent = self.isStudent



