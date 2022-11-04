from bs4 import BeautifulSoup
import requests

class GetMorseCode:
    def __init__(self):
        self.morse_code = {}

        #Get Morse Code from sckans.edu
        contents = requests.get('http://www.sckans.edu/~sireland/radio/code.html').text

        #Use bs4 for scraping
        soup = BeautifulSoup(contents, 'html.parser')
        elements = soup.find_all(name='td')

        #Find pattern for the letters and translation
        #print(elements[0].text.strip()) #A
        #print(elements[1].text.strip()) #*-
        #print(elements[8].text.strip()) #B
        #print(elements[9].text.strip()) #-***

        #for letters
        for i in range(0, 204, 8):
            #print(f"{elements[i].text.strip()} - {elements[i+1].text.strip()}")
            self.morse_code[elements[i].text.strip()] = elements[i+1].text.strip()

        #for numbers
        for i in range(208, 248, 4):
            #print(f"{elements[i].text.strip()} - {elements[i + 1].text.strip()}")
            self.morse_code[elements[i].text.strip()] = elements[i + 1].text.strip()







