import pyshorteners

l= input("Enter the url for shorting :")
shortener=pyshorteners.Shortener()

new=shortener.tinyurl.short(l)

print("newURL:",new)
