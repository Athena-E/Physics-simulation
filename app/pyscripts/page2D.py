def showPage2D():
    # main module for the 2D collision simulation

    from pygame.locals import HWSURFACE, RESIZABLE
    from __init__ import pg, sys
    from __init__ import width, height, screen, ENV2D_MAX_PARTICLES
    from __init__ import Environment2D

    from page_elements.base_dimensions import getBaseDimensions
    from page_elements.page_containers import PageContainers
    from page_elements.page_sliders import PageSliders
    from page_elements.page_2D.page_2D_property_labels import PropertyLabels2D
    from page_elements.page_2D.page_2D_property_in_out import PropertyInOut2D
    from page_elements.page_2D.page_2D_buttons import Page2DButtons

    from graphs.write_to_file import writePointsToFile

    # initialise page elements and environment

    monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
    (width, height) = (monitor_size[0], monitor_size[1])
    screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

    mainWidth, mainHeight, margin = getBaseDimensions(width, height)
    containers = PageContainers(width, height, mainWidth, mainHeight, margin, screen)

    Env2D = Environment2D(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV2D_MAX_PARTICLES)

    buttons = Page2DButtons(width, height, mainWidth, mainHeight, margin, screen, Env2D)
    propertyLabels = PropertyLabels2D(width, height, mainWidth, mainHeight, margin, screen)
    propertyInOut = PropertyInOut2D(width, height, mainWidth, mainHeight, margin, screen, Env2D)
    sliders = PageSliders(width, height, mainWidth, mainHeight, margin, screen, Env2D)

    clock = pg.time.Clock()


    timeElapsed = 500
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
                containers = PageContainers(width, height, mainWidth, mainHeight, margin, screen)

                Env2D = Environment2D(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV2D_MAX_PARTICLES)

                mainWidth, mainHeight, margin = getBaseDimensions(width, height)
                containers = PageContainers(width, height, mainWidth, mainHeight, margin, screen)
                buttons = Page2DButtons(width, height, mainWidth, mainHeight, margin, screen, Env2D)
                propertyLabels = PropertyLabels2D(width, height, mainWidth, mainHeight, margin, screen)
                propertyInOut = PropertyInOut2D(width, height, mainWidth, mainHeight, margin, screen, Env2D)
                sliders = PageSliders(width, height, mainWidth, mainHeight, margin, screen, Env2D)

            # check whether a particle in the environment has been selected
            if event.type == pg.MOUSEBUTTONDOWN:
                selectedParticleIndex = Env2D.selectParticle()

            # there are no selected particles when the mouse is not clicked
            if event.type == pg.MOUSEBUTTONUP:
                selectedParticleIndex = None
                # update positions and sizes if there are no mouse interactions
                Env2D.updateParticlePosSizeList()

        # move particle to new position if selected
        if selectedParticleIndex is not None:
            Env2D.repositionParticle(selectedParticleIndex)
                
        if Env2D.run:

            # increments time elapsed every ms
            dt = clock.tick()
            timeElapsed += dt

            # stores the speed and momentum at a given time every 500 ms
            if timeElapsed > 500:
                for i in range(ENV2D_MAX_PARTICLES):
                    try:
                        Env2D.storeSpeedPoint(Env2D.getParticleFromList(i).getSpeedMagnitude(), i)
                        Env2D.storeMomentumPoint(Env2D.getParticleFromList(i).getMomentumMagnitude(), i)
                    except:
                        Env2D.storeSpeedPoint(0, i)
                        Env2D.storeMomentumPoint(0, i)
                timeElapsed = 0

        # writes the speed and momentum points for graphs to files only when the simulation is not running to avoid latency
        elif not Env2D.run:
            for i, point in enumerate(Env2D.getSpeedTimePoints()):
                writePointsToFile(point, f"speed_data{i+1}")
            for i, point in enumerate(Env2D.getMomentumTimePoints()):
                writePointsToFile(point, f"momentum_data{i+1}")

        # change cursor icon
        if any(button.isOnButton for button in buttons.buttons) or any(slider.isOnSlider for slider in sliders.sliders) or any(button.isOnButton for button in propertyInOut.inputButtons):
            # changes cursor icon to hand when hovering over button
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        elif any(inputBox.isOnBox for inputBox in propertyInOut.inputBoxes) or any(slider.sliderInputBox.isOnBox for slider in sliders.sliders):
            # changes cursor icon to beam when hovering over text box
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_IBEAM)
        else:
            # default arrow cursor icon
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        # draw all page elements to the screen
        containers.drawContainers()
        buttons.drawButtons(events)
        sliders.drawSliders(events)
        propertyLabels.drawPropertyLabels()
        propertyInOut.drawPropertyInOut(events)

        Env2D.update()

        pg.display.flip()


if __name__ == "__main__":
    showPage2D()
