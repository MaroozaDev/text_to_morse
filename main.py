import subprocess
import time

intro = """ 

████████╗███████╗██╗  ██╗████████╗         ██╗      ███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝         ╚██╗     ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝
   ██║   █████╗   ╚███╔╝    ██║       █████╗╚██╗    ██╔████╔██║██║   ██║██████╔╝███████╗█████╗  
   ██║   ██╔══╝   ██╔██╗    ██║       ╚════╝██╔╝    ██║╚██╔╝██║██║   ██║██╔══██╗╚════██║██╔══╝  
   ██║   ███████╗██╔╝ ██╗   ██║            ██╔╝     ██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝            ╚═╝      ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
 ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗                    
██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗                   
██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝                   
██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗                   
╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║                   
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                   
                                                                                                                                                                                        
"""

# Making a Dictionary from two lists because its less tedious work.
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ")
morse_code = ['*- ', '-*** ', '-*-* ', '-** ', '* ', '**-* ', '--* ', '**** ', '** ', '*--- ', '-*-', '*-** ', '-- ', '-* ', '--- ', '*--* ', '--*- ', '*-* ', '*** ', '- ', '**- ', '***- ', '*-- ', '-**- ', '-*-- ', '--** ', '*---- ', '**--- ', '***-- ', '****- ', '***** ', '-**** ', '--*** ', '---** ', '----* ', '----- ', '       ']

code_dict = {alphabet[i]: morse_code[i] for i in range(len(alphabet))}


###################
#    Function(s)  #
###################

def convert_to_morse(message):
    morse_code = []
    message = message.upper()
    message = list(message)
    for char in message:
        # In case the user, uses characters that are not in my code_dict
        try:
            morse_letter = code_dict[char]
            morse_code.append(morse_letter)
        except KeyError:
            continue
    return ''.join(morse_code)


def play_morse(morse_code):
    for character in morse_code:
        if character == "-":
            subprocess.call(['afplay', 'dah.wav'])
        if character == '*':
            subprocess.call(['afplay', 'dit.wav'])
        elif character == "       ":
            time.sleep(.5)
        else:
            time.sleep(.2)

#####################
#       main        #
#####################


print(intro)
while True:
    message = input("Please input a text, that you want to convert to Morse Code or type q to quit: ")
    if message == "q":
        exit()
    else:
        print(convert_to_morse(message))
        play_morse(convert_to_morse(message))








