multi_word_replace = {
    "pick up": "pick_up",
    "put down": "put_down",
}

single_word_replace = {
    "h": "help",
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "i": "inventory",
    "inv": "inventory",
    "l": "look",
    "g": "get",
    "d": "drop",
    "u": "use"
}

ignore_words = (
    "the",
    "a",
    "an",
    "and"
)

actions = (
    "help",
    "inventory",
    "get",
    "drop",
    "look",
    "use",
    "attack",
    "give",
    "say"
)

prepositions = (
    "with",
    "using",
    "at",
    "toward",
    "to",
    "about",
    "beneath",
    "underneath",
    "under",
    "below",
    "above",
    "atop",
    "over",
    "on",
    "onto",
    "upon",
    "by",
    "in",
    "inside",
    "into",
    "up_to",
    "against",
    "from",
    "out_of"
)

movement_adverbs = (
    "north",
    "south",
    "east",
    "west",
    "up",
    "down",
    "in",
    "out",
)

action_synonyms = {
    "examine": "look",
    "inspect": "look",
    "take": "get",
    "leave": "drop",
    "pick_up": "get",
    "put_down": "drop",
    "fight": "attack",
    "battle": "attack",
    "hit": "attack",
    "kill": "attack",
    "walk": "go",
    "travel": "go",
    "shout": "say",
    "speak": "say"
}

# Function to help interpret player commands
def parse_command(command):
    def error(text="generic error"):
        return {
            "act": None,
            "adv": None,
            "d_obj": None,
            "prep": None,
            "i_obj": None,
            "error": text
        }
    # Edge case
    if len(command) == 0: return error("no input")

    # Check input for any phrases to be simplified
    for i in multi_word_replace:
        if i in command:
            command = command.replace(i, multi_word_replace[i])

    # Split input into words
    command = command.split()

    # Remove unnecessary words
    command = [i for i in command if not i in ignore_words]

    # Check input for any words to replace with recognized commands
    for i in range(len(command)):
        if command[i] in single_word_replace:
            command[i] = single_word_replace[command[i]]
    
   
    # Declare return object
    result = {
        "act": None,
        "adv": None,
        "d_obj": None,
        "prep": None,
        "i_obj": None,
        "error": None
    }

    # Check for movement shortcuts
    if len(command) == 1 and command[0] in movement_adverbs:
        return {
            "act": "go",
            "adv": command[0],
            "d_obj": None,
            "prep": None,
            "i_obj": None,
            "error": None
        }

    # Check for command "go" and synonyms
    if command[0] in (["go", "walk", "travel"]):
        if len(command) == 2 and command[1] in movement_adverbs:
            return {
                "act": command[0],
                "adv": command[1],
                "d_obj": None,
                "prep": None,
                "i_obj": None,
                "error": None
            }

    # Check for action, set it and filter it out of the command
    if command[0] in actions:
        result["act"] = command.pop(0)
    else:
        return error("action not recognized")

    # Check for preposition, define indirect object if one is found
    prep = None
    for i in range(len(command)):
        if command[i] in prepositions:
            if prep:
                return error("too many prepositions")
            prep = command[i]
            try:
                i_obj = command[i + 1]
            except:
                return error("dangling preposition (no indirect object)")

    # Filter out preposition, indirect object
    if prep:
        command.remove(prep)
        command.remove(i_obj)
    
    # if anything is left, it's the direct object
    if len(command) > 1:
        return error("too many words")
    
    # Set items in result and return
    try:
        result["d_obj"] = command[0]
    except:
        pass
    try: 
        result["prep"] = prep
    except:
        pass
    try: 
        result["i_obj"] = i_obj
    except:
        pass

    return result
