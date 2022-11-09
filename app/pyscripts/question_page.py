def showQuestionPage():

    from pygame.locals import HWSURFACE, RESIZABLE
    from __init__ import pg, sys
    from __init__ import width, height, screen, ENV1D_MAX_PARTICLES
    from __init__ import QuestionEnvironment

    from page_elements.base_dimensions import getBaseDimensions
    from page_elements.question_page.question_page_containers import QuestionPageContainers
    from page_elements.question_page.question_page_property_labels import QuestionPagePropertyLabels
    from page_elements.question_page.question_page_property_in_out import QuestionPagePropertyInOut
    from page_elements.question_page.question_page_buttons import QuestionPageButtons
    from page_elements.question_page.question_page_sliders import QuestionPageSliders

    from manage_questions.question_functions import uploadQuestionData, getSimulationProperties, getQuestionData

    import config

    clock = pg.time.Clock()

    # initialise page elements and environment

    monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
    (width, height) = (monitor_size[0], monitor_size[1])
    screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)

    mainWidth, mainHeight, margin = getBaseDimensions(width, height)
    containers = QuestionPageContainers(width, height, mainWidth, mainHeight, margin, screen)
    propertyLabels = QuestionPagePropertyLabels(width, height, mainWidth, mainHeight, margin, screen)

    QEnv = QuestionEnvironment(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV1D_MAX_PARTICLES)

    propertyInOut = QuestionPagePropertyInOut(width, height, mainWidth, mainHeight, margin, screen, QEnv)
    buttons = QuestionPageButtons(width, height, mainWidth, mainHeight, margin, screen, QEnv)
    sliders = QuestionPageSliders(width, height, mainWidth, mainHeight, margin, screen, QEnv)

    timeElapsed = 0
    selectedParticleIndex = None
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
                containers = QuestionPageContainers(width, height, mainWidth, mainHeight, margin, screen)
                propertyLabels = QuestionPagePropertyLabels(width, height, mainWidth, mainHeight, margin, screen)

                QEnv = QuestionEnvironment(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV1D_MAX_PARTICLES)

                propertyInOut = QuestionPagePropertyInOut(width, height, mainWidth, mainHeight, margin, screen, QEnv)
                buttons = QuestionPageButtons(width, height, mainWidth, mainHeight, margin, screen, QEnv)
                sliders = QuestionPageSliders(width, height, mainWidth, mainHeight, margin, screen, QEnv)

            # check whether a particle in the environment has been selected
            if event.type == pg.MOUSEBUTTONDOWN:
                selectedParticleIndex = QEnv.selectParticle()

            # there are no selected particles when the mouse is not clicked
            if event.type == pg.MOUSEBUTTONUP:
                selectedParticleIndex = None
                # update positions and sizes if there are no mouse interactions
                QEnv.updateParticlePosSizeList()

        # move particle to new position if selected
        if selectedParticleIndex is not None:
            QEnv.repositionParticle(selectedParticleIndex)

        # increments time elapsed every ms
        if QEnv.run:
            dt = clock.tick()
            timeElapsed += dt
        # store the initial position of the particles
        elif not QEnv.run and not QEnv._startClicked:
            timeElapsed = 0
            QEnv.setInitialPos()

        # initiate saving process when 'save' button is clicked
        if QEnv._saveClicked:
            QEnv._saveClicked = False
            teacherID = config.userID
            # get JSON objects of question properties
            displayedParticleProperties = QEnv.getDisplayedParticleProperties()
            hiddenParticleProperties = QEnv.getHiddenParticleProperties()
            environmentProperties = QEnv.getEnvProperties()
            simulationProperties = getSimulationProperties(timeElapsed, width, height)

            # save question to database
            uploadQuestionData(teacherID, environmentProperties, displayedParticleProperties, simulationProperties, hiddenParticleProperties)
            print(getQuestionData(teacherID, environmentProperties, displayedParticleProperties, simulationProperties, hiddenParticleProperties))

        # display page elements to screen
        containers.drawContainers()
        propertyLabels.drawPropertyLabels()
        propertyInOut.drawPropertyInOut(events)
        buttons.drawButtons(events)
        sliders.drawSliders(events)
        propertyInOut.updateVOutput()

        QEnv.update()

        pg.display.flip()


if __name__ == "__main__":
    showQuestionPage()