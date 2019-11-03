import time
time = time.time()
now = 1970 + int((time)//(365*24*3600))

yeari = int(input("What's the year today?\n"))

if yeari != now:
    print("No it isn't, you dumbass. It's %s.\nAnyway," %now)
else:
    print("Alright,")

autism = input('What do you like?\n')
print("Ah, yes. I, too, like %s." %autism)

frnd = []

frndname = str(input("Tell me the names of your friends. (Type 'Done' when over)\n"))

while frndname != "Done" and frndname != "done":
    frnd.append(frndname)
    if frnd.count(frndname) == 2:
        frnd.remove(frndname)
        frndname = input("You already said that name.\n")
    else:
        frndname = input("Mhm,\n")

ni = str(frnd)
length = len(ni)

print("Oh, well,", ni[1:length-1], "thinks otherwise.")
