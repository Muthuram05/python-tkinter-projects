import pyshorteners as ps
url = input("enter")
u = ps.Shortener().tinyurl.short(url)
print(u)