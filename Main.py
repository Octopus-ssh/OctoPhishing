import Screen # For screen stuffs
import Menu # For information 
import os # For clear terminal 
import Configuration

Configuration.download_library() # for installing/update library
os.system('cls' if os.name == 'nt' else 'clear') # for clear terminal LINUX/WINDOWS OS
Menu.functional_menu(Screen.OctoScreen()) # Menu and functional stuffs