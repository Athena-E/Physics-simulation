def showLoginPage():

    from pygame.locals import HWSURFACE, RESIZABLE
    from __init__ import pg, sys, LoginEnvironment
    from __init__ import width, height, screen

    from page_elements.base_dimensions import getBaseDimensions
    from page_elements.login_page.login_page_containers import LoginPageContainers
    from page_elements.login_page.login_page_buttons import LoginPageButtons
    from page_elements.login_page.login_page_in_out import LoginPageInOut

    import config

    from page2D import showPage2D

    # initialise page elements and environment

    monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
    (width, height) = (monitor_size[0], monitor_size[1])
    screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
    config.isStudent, config.isTeacher = False, False

    LoginEnv = LoginEnvironment()

    mainWidth, mainHeight, margin = getBaseDimensions(width, height)
    containers = LoginPageContainers(width, height, mainWidth, mainHeight, margin, screen)
    buttons = LoginPageButtons(width, height, mainWidth, mainHeight, margin, screen, LoginEnv)
    inOut = LoginPageInOut(width, height, mainWidth, mainHeight, margin, screen, LoginEnv)


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
                containers = LoginPageContainers(width, height, mainWidth, mainHeight, margin, screen)
                buttons = LoginPageButtons(width, height, mainWidth, mainHeight, margin, screen, LoginEnv)
                inOut = LoginPageInOut(width, height, mainWidth, mainHeight, margin, screen, LoginEnv)

        # initiate login process when user clicks 'go' button to log in 
        if LoginEnv.goClicked:
            LoginEnv.goClicked = False
            # get username and password from input boxes
            username = inOut.usernameInputBox.getText()
            enteredPassword = inOut.passwordInputBox.getText()

            # returns database table name based on user type
            # verify fields are not null
            tableName = LoginEnv.getStudentTeacherTbl()
            areFieldsNull = LoginEnv.fieldsNotNull(username, enteredPassword)

            if areFieldsNull and tableName is not None:
                # fetches user login data from database
                userLoginData = LoginEnv.getUserLoginData(f"{tableName}", username)
                
                if userLoginData is not None:
                    # calls function to verify password is correct
                    passwordVerified = LoginEnv.verifyPassword(enteredPassword, userLoginData)
                    
                    if passwordVerified and (LoginEnv.isTeacher or LoginEnv.isStudent):
                        # allows user to log in once password is verified
                        config.isLoggedIn = True
                        LoginEnv.setUserID(tableName, username)
                        # returns user to main page
                        showPage2D()

        # draw page elements to screen
        containers.drawContainers()
        buttons.drawButtons(events)
        inOut.drawInOut(events)

        pg.display.flip()


if __name__ == "__main__":
    showLoginPage()    