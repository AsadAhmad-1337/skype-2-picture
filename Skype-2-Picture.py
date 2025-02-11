import os
import sys
import requests
from colorama import init, Fore


init()

def print_rainbow_text(text):
    
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)  
        sys.stdout.flush()
    print(Fore.RESET)  

def create_folder(folder_name):
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    return folder_name

def hex_decode(hex_string):
    
    if sys.version_info[0] < 3:
        return hex_string.decode("hex")  
    else:
        return bytes.fromhex(hex_string).decode("utf-8")  

def fetch_skype_avatar(username, folder):
    
    
    obfuscated_api_url = (
        "68747470733a2f2f6176617461722e736b7970652e636f6d2f76312f617661746172732f7b757365726e616d657d2f7075626c6963"
    )
    
    
    api_url_template = hex_decode(obfuscated_api_url)
    
    
    api_url = api_url_template.format(username=username)
    
    try:
        
        response = requests.get(api_url)
        
        
        if response.status_code == 200:
            
            file_path = os.path.join(folder, "{}_avatar.jpg".format(username))
            with open(file_path, "wb") as file:
                file.write(response.content)
            print("Avatar for '{}' has been saved as '{}'.".format(username, file_path))
        else:
            print("Failed to fetch avatar for '{}'. Status code: {}".format(username, response.status_code))
    except Exception as e:
        print("An error occurred while fetching avatar for '{}': {}".format(username, e))

def main():
    
    print_rainbow_text("  ____  _                            ____         ____  _      _ ")                  
    print_rainbow_text(" / ___|| | ___   _ _ __   ___       |___ \       |  _ \(_) ___| |_ _   _ _ __ ___ ") 
    print_rainbow_text(" \___ \| |/ / | | | '_ \ / _ \        __) |      | |_) | |/ __| __| | | | '__/ _ \ ")
    print_rainbow_text("  ___) |   <| |_| | |_) |  __/       / __/       |  __/| | (__| |_| |_| | | |  __/ ")
    print_rainbow_text(" |____/|_|\_\\__, | .__/ \___|       |_____|      |_|   |_|\___|\__|\__,_|_|  \___| ")
    print_rainbow_text("             |___/|_|                                                  Asad Ahmad ") 
    
    
    folder_name = "Skype Profiles"
    folder = create_folder(folder_name)
    
    
    try:
        if sys.version_info[0] < 3:
            usernames_input = raw_input(Fore.GREEN + "Enter Skype Username or Usernames (separated by commas): " + Fore.RESET).strip()  # Python 2
        else:
            usernames_input = input(Fore.GREEN + "Enter Skype Username or Usernames (separated by commas) " + Fore.RESET).strip()  # Python 3
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(1)
    
    
    usernames = [username.strip() for username in usernames_input.split(",") if username.strip()]
    
    if usernames:
        for username in usernames:
            fetch_skype_avatar(username, folder)
    else:
        print("No valid usernames provided.")

if __name__ == "__main__":
    main()
