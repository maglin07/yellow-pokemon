from simple_chatbot.responses import GenericRandomResponse


class GreetingResponse(GenericRandomResponse):
    choices = ('Hello, How can I help you today?')

class GoodbyeResponse(GenericRandomResponse):
    choices = ('goodby, I hope you have a perfect experience')

class AnswerResponse(GenericRandomResponse):
    choices=('click the home button, top left corner, then click sign up in the box with the blue log in button.')       