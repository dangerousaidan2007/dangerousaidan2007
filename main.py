import pyshorteners

link = input("Which link would you like to shorten?:  ")

shortener=pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)
