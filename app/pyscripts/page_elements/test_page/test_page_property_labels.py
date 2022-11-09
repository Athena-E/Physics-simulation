from page_elements.question_page.question_page_property_labels import QuestionPagePropertyLabels

# class to set and initialise labels for test page
# inherits from QuestionPagePropertyLabels
class TestPagePropertyLabels(QuestionPagePropertyLabels):

    def __init__(self, width, height, mainWidth, mainHeight, margin, screen):
        # inherits properties from parent class
        super().__init__(width, height, mainWidth, mainHeight, margin, screen)

        