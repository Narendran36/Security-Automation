#!/usr/bin/env python3

import os

# Created by Narendran S Nair for testing subdomain takeover using findomain, subbrute and subzy

print('\n###########################')
print('Test for Subdomain Takeover')
print('###########################\n')
choice = input('Do you want to setup the prerequisites? (y/n): ')

if (choice=='y' or choice =='Y'):
    os.system('mkdir sdto_prerequisites; cd sdto_prerequisites; wget https://github.com/findomain/findomain/releases/latest/download/findomain-linux; chmod +x findomain-linux; git clone https://github.com/LukaSikic/subzy; sudo apt install golang-go -y; go build subzy/subzy.go; chmod +x subzy/subzy.go; git clone https://github.com/TheRook/subbrute; chmod +x subbrute/subbrute.py')

domain = input('Enter domain for testing: ')
category = input('Do you want an in depth analysis (note that this can take a much longer time) (y/n): ')

print('Enumerating possible subdomains....')
os.system('./sdto_prerequisites/findomain-linux -r -o -t ' + domain)

if (category=='y' or category=='Y'):
    print('Starting in-depth analysis....')
    os.system('cd ./sdto_prerequisites/subbrute/; ./subbrute.py ' + domain + ' -o bruteforce_result.txt')
    os.system('cd ./sdto_prerequisites/subbrute/; cat bruteforce_result.txt >> ../../' + domain + '.txt; cd ../../')
    
print('Testing for possible subdomain takeover')
os.system('go run ./sdto_prerequisites/subzy/subzy.go -targets ' + domain + '.txt')
