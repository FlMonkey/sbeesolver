import pyautogui
import time

w1 = input("Enter the first letter: ")
w2 = input("Enter the second letter: ")
w3 = input("Enter the third letter: ")
w4 = input("Enter the fourth letter: ")
w5 = input("Enter the fifth letter: ")
w6 = input("Enter the sixth letter: ")
w7 = input("Enter the center letter: ")

settot = set([w1, w2, w3, w4, w5, w6, w7])
print(settot)

goodwords = []

with open("words_alpha.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    for word in words:
        setword = set(word)
        if setword.issubset(settot) and w7 in word:
            goodwords.append(word)


for word in goodwords:
    if len(word) <= 3:
        goodwords.remove(word)
        
print(goodwords)
    
input("press enter to start typing words")
time.sleep(2)


for word in goodwords:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.7)
