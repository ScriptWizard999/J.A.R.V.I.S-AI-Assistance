import random

command_1 = ['hello','wake up','hey buddy','jarvis','hii','lets go']

reply_1 = ['Hello sir, Welcome back!','Always for you Sir!','How can i help you?','welcome back sir, How can i help you?','hi sir , is there any work for me?','nice meeting you again sir...','hope you missed me! how can i help you']

command_2 = ['bye jarvis','see you again','good bye']

reply_2 = ['ok bye sir...','have a good day sir...','if you need any help just ask...']



def ChatterBot(Text):

    for word in Text.split():

        if word in command_1:

            return random.choice(reply_1) 

        elif word in command_2:

            return random.choice(reply_2)
