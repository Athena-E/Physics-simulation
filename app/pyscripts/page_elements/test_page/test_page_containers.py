from page_elements.question_page.question_page_containers import QuestionPageContainers

# class to set and initialise containers for test page
# inherits from QuestionPageContainers
class TestPageContainers(QuestionPageContainers):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
         # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)


    

