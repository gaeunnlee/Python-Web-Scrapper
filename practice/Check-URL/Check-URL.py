import requests
import os

while True :
    print('Welcome to IsItDown.py!')
    print('Please write a URL or URLs you want to check. (seperated by comma)')
    count = 0
    url_data = input().split(',')
    for url in url_data:
        if "." not in url:
            print(f'{url} is not a valid URL.')
            while True:
                print('Do you want to start over? y/n')
                retry = input()
                if retry == 'y' :
                    break
                elif retry == 'n' :
                    print('Ok, bye!')
                    quit()
                else : 
                    print("That's not a valid answer")
                    continue
            os.system('cls')
            continue
        else:
            count += 1
            url = url.strip()    
            if 'http://' not in url:
                url = 'http://' + url
        
            try:
                response = requests.get(url)
                print(f'{url} is up!')
            except:
                print(f'{url} is down!')

                        
            if count == len(url_data):
                while True:
                    print('Do you want to start over? y/n')
                    retry = input()
                    if retry == 'y' :
                        break
                    elif retry == 'n' :
                        print('Ok, bye!')
                        quit()
                    else : 
                        print("That's not a valid answer")
                        continue
                os.system('cls')
                continue