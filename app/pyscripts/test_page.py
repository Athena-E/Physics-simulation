def showTestPage():

    from pygame.locals import HWSURFACE, RESIZABLE
    from __init__ import pg, sys
    from __init__ import width, height, screen, ENV1D_MAX_PARTICLES
    from __init__ import TestEnvironment

    from page_elements.base_dimensions import getBaseDimensions
    from page_elements.test_page.test_page_containers import TestPageContainers
    from page_elements.test_page.test_page_property_labels import TestPagePropertyLabels
    from page_elements.test_page.test_page_buttons import TestPageButtons
    from page_elements.test_page.test_page_property_in_out import TestPagePropertyInOut

    from page2D import showPage2D

    from manage_questions.test_functions import getRandomQuestionData, extractQuestionData, uploadScores

    import config

    clock = pg.time.Clock()

    # initialise page elements and environment

    monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
    (width, height) = (monitor_size[0], monitor_size[1])
    screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)

    mainWidth, mainHeight, margin = getBaseDimensions(width, height)
    containers = TestPageContainers(width, height, mainWidth, mainHeight, margin, screen)
    propertyLabels = TestPagePropertyLabels(width, height, mainWidth, mainHeight, margin, screen)

    TestEnv = TestEnvironment(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV1D_MAX_PARTICLES)

    buttons = TestPageButtons(width, height, mainWidth, mainHeight, margin, screen, TestEnv)
    inOut = TestPagePropertyInOut(width, height, mainWidth, mainHeight, margin, screen, TestEnv)


    totalScore = 0
    maxScore = 0
    hiddenData = {}
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
                containers = TestPageContainers(width, height, mainWidth, mainHeight, margin, screen)
                propertyLabels = TestPagePropertyLabels(width, height, mainWidth, mainHeight, margin, screen)

                TestEnv = TestEnvironment(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV1D_MAX_PARTICLES)

                buttons = TestPageButtons(width, height, mainWidth, mainHeight, margin, screen, TestEnv)
                inOut = TestPagePropertyInOut(width, height, mainWidth, mainHeight, margin, screen, TestEnv)


        if TestEnv.run:
            TestEnv.compareV()

        # resets test page and environment if user clicks 'new question' button
        if TestEnv.nextClicked:
            TestEnv.nextClicked = False

            questionData = getRandomQuestionData()
            simulationData = extractQuestionData(questionData, "simulationProperties")
            environmentData = extractQuestionData(questionData, "environmentProperties")
            particleData = extractQuestionData(questionData, "particleProperties")
            hiddenData = extractQuestionData(questionData, "hiddenProperties")
            
            (width, height) = (simulationData.get("screenW"), simulationData.get("screenH"))
            screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)

            mainWidth, mainHeight, margin = getBaseDimensions(width, height)
            containers = TestPageContainers(width, height, mainWidth, mainHeight, margin, screen)
            propertyLabels = TestPagePropertyLabels(width, height, mainWidth, mainHeight, margin, screen)

            TestEnv = TestEnvironment(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV1D_MAX_PARTICLES)
            TestEnv.setTotalScore(totalScore)
            TestEnv.setMaxScore(maxScore)

            buttons = TestPageButtons(width, height, mainWidth, mainHeight, margin, screen, TestEnv)
            inOut = TestPagePropertyInOut(width, height, mainWidth, mainHeight, margin, screen, TestEnv)

            TestEnv.setQuestionEnvProperties(environmentData)
            TestEnv.setQuestionParticleProperties(particleData)
            TestEnv.setQuestionHiddenProperties(hiddenData)

            inOut.hidePropertyInOut(hiddenData)

        # initialises processes to check answers if 'submit' button clicked
        if TestEnv.submitClicked and len(hiddenData) != 0:
            TestEnv.submitClicked = False
            # check if answers are correct
            answerInput = inOut.getAnswerInput(hiddenData)
            answersCorrect = TestEnv.checkAnswers(answerInput)
            inOut.markAnswerInput(answersCorrect)
            # calculate marks for question
            TestEnv.calculateScore(answersCorrect)
            totalScore = TestEnv.getTotalScore()
            maxScore = TestEnv.getMaxScore()


        if TestEnv.revealClicked and len(hiddenData) != 0:
            # reveal answers if 'reveal' button clicked
            TestEnv.onClickReveal()
            inOut.revealAnswers(hiddenData)


        if TestEnv.finishClicked and len(hiddenData) != 0:
            # upload final scores if 'finish' button clicked
            TestEnv.finishClicked = False
            userID = config.userID
            uploadScores(userID, totalScore, maxScore)
            showPage2D()

        # displays page elemnents to screen
        containers.drawContainers()
        buttons.drawButtons(events)

        if len(hiddenData) != 0:
            propertyLabels.drawPropertyLabels()
            inOut.drawPropertyInOut(events, hiddenData)

        inOut.updateVOutput(hiddenData)

        TestEnv.update()

        pg.display.flip()


if __name__ == "__main__":
    showTestPage()


