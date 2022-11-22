def showPage1D():
    # main module for the 1D collision simulator

    from pygame.locals import HWSURFACE, RESIZABLE
    from __init__ import pg, sys
    from __init__ import width, height, screen, ENV1D_MAX_PARTICLES
    from __init__ import Environment1D

    from page_elements.base_dimensions import getBaseDimensions
    from page_elements.page_containers import PageContainers
    from page_elements.page_1D.page_1D_buttons import Page1DButtons
    from page_elements.page_sliders import PageSliders
    from page_elements.page_1D.page_1D_property_labels import PropertyLabels1D
    from page_elements.page_1D.page_1D_property_in_out import PropertyInOut1D

    from graphs.write_to_file import writePointsToFile

    # initialise page elements and environment

    monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
    (width, height) = (monitor_size[0], monitor_size[1])
    screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

    mainWidth, mainHeight, margin = getBaseDimensions(width, height)
    containers = PageContainers(width, height, mainWidth, mainHeight, margin, screen)

    Env1D = Environment1D(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV1D_MAX_PARTICLES)

    buttons = Page1DButtons(width, height, mainWidth, mainHeight, margin, screen, Env1D)
    propertyLabels = PropertyLabels1D(width, height, mainWidth, mainHeight, margin, screen)
    propertyInOut = PropertyInOut1D(width, height, mainWidth, mainHeight, margin, screen, Env1D)
    sliders = PageSliders(width, height, mainWidth, mainHeight, margin, screen, Env1D)

    clock = pg.time.Clock()

    timeElapsed = 500
    selectedParticleIndex = None
    running = True

    while running:
        
        events = pg.event.get()
        for event in events:

            if event.type == pg.QUIT: 
                running = False
                sys.exit()

            if event.type == pg.VIDEORESIZE:
                # re-initialise page elements and environment when screen is resized

                width, height = event.w, event.h
                screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)

                mainWidth, mainHeight, margin = getBaseDimensions(width, height)
                containers = PageContainers(width, height, mainWidth, mainHeight, margin, screen)

                Env1D = Environment1D(screen, containers.collisionW, containers.collisionH, containers.collisionPos, ENV1D_MAX_PARTICLES)

                buttons = Page1DButtons(width, height, mainWidth, mainHeight, margin, screen, Env1D)
                propertyLabels = PropertyLabels1D(width, height, mainWidth, mainHeight, margin, screen)
                propertyInOut = PropertyInOut1D(width, height, mainWidth, mainHeight, margin, screen, Env1D)
                sliders = PageSliders(width, height, mainWidth, mainHeight, margin, screen, Env1D)

            # check whether a particle in the environment has been selected
            if event.type == pg.MOUSEBUTTONDOWN:
                selectedParticleIndex = Env1D.selectParticle()

            # there are no selected particles when the mouse is not clicked
            if event.type == pg.MOUSEBUTTONUP:
                selectedParticleIndex = None
                Env1D.updateParticlePosSizeList()

        # move particle to new position if selected
        if selectedParticleIndex is not None:
            Env1D.repositionParticle(selectedParticleIndex)

        if Env1D.run:

            # increments time elapsed every ms
            dt = clock.tick()
            timeElapsed += dt

            # stores the speed and momentum at a given time every 500 ms
            if timeElapsed > 500:
                for i in range(ENV1D_MAX_PARTICLES):
                    try:
                        Env1D.storeSpeedPoint(Env1D.getParticleFromList(i).getSpeedMagnitude(), i)
                        Env1D.storeMomentumPoint(Env1D.getParticleFromList(i).getMomentumMagnitude(), i)
                    except IndexError:
                        Env1D.storeSpeedPoint(0, i)
                        Env1D.storeMomentumPoint(0, i)
                timeElapsed = 0

        # writes the speed and momentum points for graphs to files only when the simulation is not running to avoid latency
        elif not Env1D.run:
            for i, point in enumerate(Env1D.getSpeedTimePoints()):
                writePointsToFile(point, f"speed_data{i+1}")
            for i, point in enumerate(Env1D.getMomentumTimePoints()):
                writePointsToFile(point, f"momentum_data{i+1}")


        # draw page elements to the screen
        containers.drawContainers()
        buttons.drawButtons(events)
        sliders.drawSliders(events)
        propertyLabels.drawPropertyLabels()
        propertyInOut.drawPropertyInOut(events)


        Env1D.update()

        pg.display.flip()


if __name__ == "__main__":
    showPage1D()