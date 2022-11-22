from manage_users.__init__ import create_client, Client, supabase, hashlib, random, re
import config

# class to handle user registration
class RegEnvironment():

    def __init__(self):

        self.createAccountClicked = False
        self.userType = None
        self.currentForename = ""
        self.currentSurname = ""

        self.errorAlert = ""


    def onClickCreateAccount(self):
        self.createAccountClicked = True

    def getErrorAlert(self):
        return self.errorAlert


    def insertNewUser(self, table, forename, surname, username, email, passwordHash, salt):
        # creates new record of user in the database

        newUserData = {
            "forename": forename.capitalize(),
            "surname": surname.capitalize(),
            "username": username,
            "email": email,
            "passwordHash": passwordHash,
            "salt": salt
        }

        supabase.table(f"{table}").insert(newUserData).execute()


    def getHashedPassword(self, password, salt):
        # creates hash of password by concatenating password string and salt string
        saltedPassword = password+salt
        hashedPassword = hashlib.md5(saltedPassword.encode())

        return hashedPassword.hexdigest()


    def generateSalt(self):
        # generates random alphanumeric string to represent password salt
        salt = ""

        for _ in range(12):
            randChar = chr(random.randint(33, 126))
            salt += randChar

        return salt

    def generateUsername(self, table, forename, surname):
        # generates a username in the format firstname+lastname+number

        count = 0

        while True:
            if (forename == "" and surname == "") or not(forename.isalpha() or forename == "") or not(surname.isalpha() or surname == ""):
                username = ""
                break
            # increment number at the end of username if username already exists
            count += 1
            username = f"{forename.lower()}{surname.lower()}{count}"
            # checks if username is already in the database
            usernameInTable = supabase.table(f"{table}").select("*").eq("username", username).execute().data
            # API response returns empty list if username not found
            if usernameInTable == []:
                break

        return username


    def validatePassword(self, password):
        # checks whether password meets the security requirements

        passwordRgx = "(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)"
        try:
            isMatch = re.search(passwordRgx, password)
            if isMatch is not None and len(password) >= 6:
                return True
            else:
                print("invalid password")
                self.errorAlert = "invalid password"
            return False
        except:
            self.errorAlert = "invalid password"
            return False


    def validatedConfirmedPassword(self, password, confirmedPassword):
        # checks whether inputs in password and confirm password fields are the same
        try:
            if password == confirmedPassword:
                return True
            else:
                print("passwords do not match")
                self.errorAlert = "passwords do not match"
                return False
        except:
            self.errorAlert = "passwords do not match"
            return False


    def validateEmail(self, email):

        # matches emails in formats i.e.:
        # joe.bloggs@email.com, janedoe123@email.com
        emailRgx = ".+@{1}([a-z]|[A-Z])+\.{1}([a-z]|[A-Z])+"
        try:
            isMatch = re.search(emailRgx, email)
            if isMatch is not None:
                return True
            print("invalid email")
            self.errorAlert = "invalid email"
            return False
        except:
            self.errorAlert = "invalid email"
            return False


    def fieldsNotNull(self, fieldsList):
        # checks whether fields are null and returns true if none are
        if "" not in fieldsList:
            return True
        else:
            print("fields null")
            self.errorAlert = "mandatory fields are empty"
            return False


    def getUserType(self, teacherCodeInput):
        # gets user type depending on teacher code input
        # returns True if teacher, returns False if student where code is not entered or is incorrect
        if teacherCodeInput == "": # or teacherCodeInput != config.teacherCode:
            return False 
        elif teacherCodeInput == config.teacherCode:
            return True
        else:
            return None


    def studentTeacherTbl(self, isTeacher):
        # gets table name depending on user type
        if isTeacher == True:
            return "tblTeachers"
        elif isTeacher == False:
            return "tblStudents"
        else:
            return None

    def validateTeacherCode(self, teacherCodeInput):
        # checks teacher code is valid or empty else error raised
        if teacherCodeInput == "" or teacherCodeInput == config.teacherCode:
            return True
        else:
            self.errorAlert = "invalid teacher code"
            return False


    def validateNames(self, forename, surname):
        # validates user inputs for names only contain letters
        if forename.isalpha() and surname.isalpha():
            return True
        else:
            print("invalid name")
            self.errorAlert = "invalid name"
            return False








