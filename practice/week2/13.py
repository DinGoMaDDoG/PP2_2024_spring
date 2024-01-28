biglist=list(("Left", "Leave", "Light","Lemon", "Let"))
biglist[2]="Dark"
print (biglist)


biglist[2:4]=["Dark", "Orange"]
print (biglist)


biglist2=list(("Left", "Leave", "Light","Lemon", "Let"))
biglist2[2:3]=["Dark", "Orange"]
print (biglist2)


biglist3=list(("Left", "Leave", "Light","Lemon", "Let"))
biglist3[2:4]=["Hi"]
print (biglist3)


biglist4=list(("Left", "Leave", "Light","Lemon", "Let"))
biglist4.insert (3, "GG")
print (biglist4)
