def showRegisterPage():

    from pygame.locals import HWSURFACE, RESIZABLE
    from __init__ import pg, sys, RegEnvironment
    from __init__ import width, height, screen

    from page_elements.base_dimensions import getBaseDimensions
    from page_elements.register_page.register_page_containers import RegPageContainers
    from page_elements.register_page.register_page_buttons import RegPageButtons
    from page_elements.register_page.register_page_in_out import RegPageInOut

    from login_page import showLoginPage

    # initialise page elements and environment

    RegEnv = RegEnvironment()

    monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
    (width, height) = (monitor_size[0], monitor_size[1])
    screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)

    mainWidth, mainHeight, margin = getBaseDimensions(width, height)
    containers = RegPageContainers(width, height, mainWidth, mainHeight, margin, screen)
    buttons = RegPageButtons(width, height, mainWidth, mainHeight, margin, screen, RegEnv)
    inOut = RegPageInOut(width, height, mainWidth, mainHeight, margin, screen, RegEnv)


    running = True

    # main events loop
    while running:

        events = pg.event.get()

        for event in events:

            if event.type == pg.QUIT:
                running = False
                sys.exit()

            if event.type == pg.VIDEORESIZE:
                # re-initialise page elements and environment when the screen is resized             
                width, height = event.w, event.h
                screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)

                mainWidth, mainHeight, margin = getBaseDimensions(width, height)
                containers = RegPageContainers(width, height, mainWidth, mainHeight, margin, screen)
                buttons = RegPageButtons(width, height, mainWidth, mainHeight, margin, screen)
                inOut = RegPageInOut(width, height, mainWidth, mainHeight, margin, screen)

        # get input text in name and teacher code fields 
        forename = inOut.firstNameInputBox.text
        surname = inOut.lastNameInputBox.text
        teacherCodeInput = inOut.codeInputBox.text
        # validate if user is teacher and get the name of appropriate table
        isTeacher = RegEnv.getUserType(teacherCodeInput)
        table = RegEnv.studentTeacherTbl(isTeacher)
        # generates unique username for user 
        if table is not None and (RegEnv.userType != isTeacher or (RegEnv.currentForename != forename or RegEnv.currentSurname != surname)):
            username = RegEnv.generateUsername(table, forename, surname)
            inOut.usernameText.update(username)
            RegEnv.userType = isTeacher
            RegEnv.currentForename, RegEnv.currentSurname = forename, surname

        # initiate register process when user clicks 'create account' button
        if RegEnv.createAccountClicked:

            RegEnv.createAccountClicked = False

            # get inputs from fields
            email = inOut.emailInputBox.text
            password = inOut.passwordInputBox.text
            confirmedPassword = inOut.confirmPasswordInputBox.text
            fields = [forename, surname, email, password, confirmedPassword]
            
            # verify that fields are not null
            if RegEnv.fieldsNotNull(fields):
                # validate inputs for fields before continuing registration
                if RegEnv.validatedConfirmedPassword(password, confirmedPassword) and RegEnv.validatePassword(password) and RegEnv.validateEmail(email) and RegEnv.validateNames(forename, surname) and RegEnv.validateTeacherCode(teacherCodeInput):
                    # generate password salt and hash to store to database
                    salt = RegEnv.generateSalt()
                    passwordHash = RegEnv.getHashedPassword(password, salt)
                    # create new record in user table
                    RegEnv.insertNewUser(table, forename, surname, username, email, passwordHash, salt)
                    # return user to login page
                    showLoginPage()

        # draw page elements to screen
        containers.drawContainers()
        buttons.drawButtons(events)
        inOut.drawInOut(events)

        pg.display.flip()


if __name__ == "__main__":
    showRegisterPage()

