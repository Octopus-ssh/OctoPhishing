from rich import print  # For color
from rich.prompt import Prompt

def OctoScreen() :

    print('''
    [green]      
          ___       _        ____  _     _     _     _             
         / _ \  ___| |_ ___ |  _ \| |__ (_)___| |__ (_)_ __   __ _ 
        | | | |/ __| __/ _ \| |_) | '_ \| / __| '_ \| | '_ \ / _` |
        | |_| | (__| || (_) |  __/| | | | \__ \ | | | | | | | (_| |
         \___/ \___|\__\___/|_|   |_| |_|_|___/_| |_|_|_| |_|\__, |
                                                             |___/

                            [ Octopus-SSH tool ]

    [1] Netflix
    
          

    [99] exit                                               [00] information                             
    ''')

    choice = int(Prompt.ask("\n\n[yellow][+]  ")) # insert an option

    return choice 