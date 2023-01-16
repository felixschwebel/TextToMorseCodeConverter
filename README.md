# TextToMorseCodeConverter
A simple text-based program to convert text to morse code.

To get the morse-alphabet I’ve used BeautifulSoup.  I scraped this information from the website *http://www.sckans.edu/~sireland/radio/code.html* and put it into a dictionary. I’ve done this in a separate class to declutter my code and to practice OOP.

The program is very simple. The user can provide a word or sentence to translate into morse-code. Only letters and numbers are allowed otherwise the KeyError will be raised and the program restarts. 

