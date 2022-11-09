def getBaseDimensions(width, height):
    # function to calculate dimensions of main rectangle and margin 

    margin = width/87
    mainWidth = width - margin
    mainHeight = mainWidth * (27/43) - margin

    if mainHeight > height:
        margin = height/55
        mainHeight = height - margin
        mainWidth = mainHeight * (43/27) - margin

    return mainWidth, mainHeight, margin


            

