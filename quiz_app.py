total_point = 0
answer = input("Are you downbad for el?")

if answer.lower() == "yes":
    print ("good boy")
    total_point = total_point + 1
else:
    print ("Killyourself <3")
    total_point = total_point + 0

answer_2 = input("is she good looking?")
if answer_2 == "very much so":
    print ("good boy")
    total_point = total_point + 1
else:
    print ("Killyourself <3")
    total_point = total_point + 0

answer_3 = input("Are you going to be her boyfriend?")
if answer_3 == "already am":
    print ("of course you are")
    total_point = total_point + 1
else:
    print ("Stay single then<3")
    total_point = total_point + 0

answer_4 = input("What's her favorite activity?")
if answer_4 == "sleeping":
    print ("you know her well")
    total_point = total_point + 1
else:
    print ("you spend THAT much time with her and you dont even know her?")
    total_point = total_point + 0

answer_5 = input("would you let anyone else have her?")
if answer_5 == "fuck no, she's mine and mine only":
    print ("at it boy")
    total_point = total_point + 1
else:
    print ("you're just gonna let someone else take her? you disgust me")
    total_point = total_point + 0
    
print (total_point)
if total_point > 4:
    print ("congratulation!!! you're deserving of el")
else:
    print ("Don't you ever talk to her ever again")