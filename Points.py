from Config import Config
import SaveIO

Points = {
    # "username": 100
    # Format is key username: value points
    "KarmaBot": 9999999999999999999999
}

Stars = {
    # 20357294: "username"
    # Format is key message id: value username of starrer
}

Pins = {
    # 20357294: "username"
    # Format is key message id: value username of pinner
}

def init():
    global Points
    global Stars
    global Pins
    Points = SaveIO.load(SaveIO.data_path)
    Stars = SaveIO.load(SaveIO.stars_path)
    Pins = SaveIO.load(SaveIO.pins_path)

def close():
    global Points
    global Stars
    global Pins
    SaveIO.save(SaveIO.data_path, Points)
    SaveIO.save(SaveIO.stars_path, Stars)
    SaveIO.save(SaveIO.pins_path, Pins)

def change_points(user, amount, is_admin=False):
    if user not in Points:
        Points[user] = 200
    if Points[user] + amount < 0:
        if not is_admin:
            return False
    else:
        Points[user] += amount
        return "Changed points for " + user + " by " + str(amount) + ". New total: " + str(Points[user])
        
def give_points(args, msg, event, chatbot):
    if len(args) < 3:
        return "Not enough arguments."
    
    user = args[1]
    amount = args[2]
    
    if "-" in amount:
        return "You cannot take points from a user."
    try:
        amount = int(amount)
    except:
        return "Invalid amount."
    
    negAmount = -amount;
    negUser = event.user.name
    
    remove = change_points(negUser, negAmount)
    if remove == False:
        return "You do not have enough points to give that many away."
    result = change_points(user, amount)
    return result
    
def admin_points(args, msg, event, chatbot):
    for i in Config.General["owners"]:
        if event.user.id == i["stackexchange.com"]:
            break
        else:
            continue
    else:
        return "You don't have permission to administrate points."
    
    if len(args) < 3:
        return "Not enough arguments."
    
    user = args[1]
    amount = args[2]
    
    try:
        amount = int(amount)
    except:
        return "Invalid amount."

    result = change_points(user, amount, True)
    return result
    
def get_points(args, msg, event, chatbot):
    user = ""
    if len(args) == 1:
        user = event.user.name
    elif len(args) >= 2:
        user = args[1]
    if user in Points:
        return str(Points[user])
    else:
        Points[user] = 200
        return "200"

def star(args, msg, event, chatbot):
    if len(args) < 2:
        return "Not enough arguments."
    id = args[1]
    user = event.user.name
    try:
        id = int(id)
    except:
        return "Invalid arguments."
    message = chatbot.client.get_message(id)
    if message.starred_by_you or id in Stars:
        return "This message has already been starred by someone else."
    if message.owner.name == "KarmaBot":
        return "I can't star my own messages."
    message.star()
    change_points(user, -100)
    Stars[id] = user
    
def pin(args, msg, event, chatbot):
    if len(args) < 2:
        return "Not enough arguments."
    id = args[1]
    user = event.user.name
    try:
        id = int(id)
    except:
        return "Invalid arguments."
    chatbot.client.get_message(id).pin()
    change_points(user, -100)
