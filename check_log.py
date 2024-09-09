import re

''' 
Challenge: write a function that checks a log file to determine 
which users might have had bruteforce attempts against them. (Specific wording, I do not remember)
'''

# https://github.com/logpai/loghub/blob/master/OpenSSH/OpenSSH_2k.log
# Found this online, which looks to be the same sample of 2k as the original challenge

def check_bruteforce(file: str, pattern: str) -> dict:
    users = {} 
    
    with open(file, 'r') as f: # helps avoid lock issues https://stackoverflow.com/questions/21275836/if-youre-opening-a-file-using-the-with-statement-do-you-still-need-to-close
        for line in f:
            match = re.search(pattern,line)
            
            if match:
                username = match.group(1)
                
                if username not in users: # I wanted a faster lookup on usernames, used dict
                    users[username] = 0 
                users[username]    += 1
                
    return users

pattern = r"Failed password for invalid user ([\w.-]+)" #decided to try to use groups to learn the regex syntax a bit better
attempts_and_users = check_bruteforce("OpenSSH_2k.log", pattern)

for username, attempts in attempts_and_users.items():
    print(f"Username: {username} had {attempts} invalid password attempts.")
    


