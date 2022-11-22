def showGasPage():
    # main module for the gas collision simulation

    from pygame.locals import HWSURFACE, RESIZABLE
    from __init__ import pg, sys
    from __init__ import width, height, screen, GASENV_MAX_PARTICLES
    from __init__ import GasEnvironment

    from page_elements.base_dimensions import getBaseDimensions
    from page_elements.gas_page.gas_page_containers import GasPageContainers
    from page_elements.gas_page.gas_page_sliders import GasPageSliders
    from page_elements.gas_page.gas_page_buttons import GasPageButtons

    # initialise page elements and environment

    monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
    (width, height) = (monitor_size[0], monitor_size[1])
    screen = pg.display.set_mode((width, height), HWSURFACE|RESIZABLE)
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

    mainWidth, mainHeight, margin = getBaseDimensions(width, height)
    containers = GasPageContainers(width, height, mainWidth, mainHeight, margin, screen)

    GasEnv = GasEnvironment(screen, containers.collisionW, containers.collisionH, containers.collisionPos, GASENV_MAX_PARTICLES)

    sliders = GasPageSliders(width, height, mainWidth, mainHeight, margin, screen, GasEnv)
    buttons = GasPageButtons(width, height, mainWidth, mainHeight, margin, screen, GasEnv)

    wallSelected = False
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
                containers = GasPageContainers(width, height, mainWidth, mainHeight, margin, screen)

                GasEnv = GasEnvironment(screen, containers.collisionW, containers.collisionH, containers.collisionPos, GASENV_MAX_PARTICLES)

                sliders = GasPageSliders(width, height, mainWidth, mainHeight, margin, screen, GasEnv)
                buttons = GasPageButtons(width, height, mainWidth, mainHeight, margin, screen, GasEnv)

            # handle gas particle collisions if mouse is 
            if event.type == pg.MOUSEMOTION:
                # gets the change in x and y positions of mouse since event was last called
                vx, vy = event.rel
                GasEnv.mouseCollision(vx, vy)

            # checks whether the wall has been selected
            if event.type == pg.MOUSEBUTTONDOWN:
                wallSelected = GasEnv.selectWall()

            # deselects wall when mouse is not clicked
            if event.type == pg.MOUSEBUTTONUP:
                wallSelected = False

        # move wall to new position if selected
        if wallSelected:
            GasEnv.moveWall()

        # draws page elements to screen
        containers.drawContainers()
        sliders.drawSlidersAndLabels(events)
        buttons.drawButtons(events)

        GasEnv.update()
        GasEnv.mouseInteraction()

        pg.display.flip()


if __name__ == "__main__":
    showGasPage()