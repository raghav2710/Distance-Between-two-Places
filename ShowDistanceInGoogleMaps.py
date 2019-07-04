import webbrowser


startPoint = input("Choose starting point: ")
endPoint = input("Choose ending point: ")


list_startPoint = list(startPoint)
new_startList = ["+" if x == " " else x for x in list_startPoint]
new_startAddress = (''.join(new_startList))


list_endPoint = list(endPoint)
new_endList = ["+" if x == " " else x for x in list_endPoint]
new_endAddress = (''.join(new_endList))

link = "https://www.google.com/maps/dir/" + new_startAddress + "/" + new_endAddress
webbrowser.open(link)
