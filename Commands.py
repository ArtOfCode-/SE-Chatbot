# contains commands which do not depend on any variables in the WordAssociationChatbot class
import random
import sys
from datetime import datetime
import Points

Points.init()

def command_alive(args, msg, event, chatbot):
    possibles = ["Yes, I'm alive.", "Not dead yet.", "and kicking.", "Of course.", "Define *alive*.", "Well I'm a non-sentient computer program... how alive can I *really* be?", "Awaiting instruction.", "<sarcasm>No, I'm dead.</sarcasm>"]
    return random.choice(possibles)


def command_random(args, msg, event, chatbot):
    return str(random.random())


def command_randomint(args, msg, event, chatbot):
    if len(args) == 0:
        return str(random.randint(0, sys.maxint))
    if len(args) == 1:
        try:
            max_ = int(args[0])
        except ValueError:
            return "Invalid arguments."
        min_ = 0
        if min_ > max_:
            return "Min cannot be greater than max."
        return str(random.randint(min_, max_))
    if len(args) == 2:
        try:
            min_ = int(args[0])
            max_ = int(args[1])
        except ValueError:
            return "Invalid arguments."
        if min_ > max_:
            return "Min cannot be greater than max."
        return str(random.randint(min_, max_))
    return "Too many arguments."


def command_randomchoice(args, msg, event, chatbot):
    if len(args) < 1:
        return "Not enough arguments."
    return random.choice(args)


def command_shuffle(args, msg, event, chatbot):
    if len(args) < 1:
        return "Not enough arguments."
    list_to_shuffle = list(args)
    random.shuffle(list_to_shuffle)
    return " ".join(list_to_shuffle)


def command_utc(args, msg, event, chatbot):
    return datetime.utcnow().ctime()


def command_xkcdrandomnumber(args, msg, event, chatbot):
    return "[4 // Chosen by fair dice roll. Guaranteed to be random.](http://xkcd.com/221/)"


def command_xkcd(args, msg, event, chatbot):
    if len(args) < 1:
        return "Not enough arguments."
    try:
        id_ = int(args[0])
    except:
        return "Invalid arguments."
    return "http://xkcd.com/%i/" % id_
    
def command_points(args, msg, event, chatbot):
    if len(args) < 1:
        return "Not enough arguments."
    if args[0] == "give":
        return Points.give_points(args, msg, event, chatbot)
    elif args[0] == "get":
        return Points.get_points(args, msg, event, chatbot)
    elif args[0] == "admin":
        return Points.admin_points(args, msg, event, chatbot)
    elif args[0] == "star":
        return Points.star(args, msg, event, chatbot)
    elif args[0] == "pin":
        return Points.pin(args, msg, event, chatbot)
    elif args[0] == "unstar":
        return Points.unstar(args, msg, event, chatbot)
    elif args[0] == "unpin":
        return Points.unstar(args, msg, event, chatbot)
    else:
        return "Command not found."
