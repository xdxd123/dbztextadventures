#Dragon Ball Text Adventure Version 1.5.0 (UNFINISHED EDIT)
#By Jaren Edwards
#First digit is a seperation between game copies
#Version 2.0.0 is vastly separated from 1.0.0 in its edition
#Version 1.3.0 would be very close to 1.3.1 and close to 1.2.0
#Second digit stands for update version of an edition
#The third digit stands for a patch to a version incase of bugs or unwanted things.
#So follow this:
# Edition, Version, Patch Number
import random
import pickle


def do_save(self, arg):
   saveGame = open('savegame.txt', 'wb')
   saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
   pickle.dump(saveValues, saveGame)
   saveGame.close()


def do_load(self, arg):
   loadGame = open('savegame.txt', 'rb')
   loadValues = pickle.load(loadGame)
   pl = loadValues[0]
   e1ft = loadValues[1]
   e2ft = loadValues[2]
   e3ft = loadValues[3]
   e4ft = loadValues[4]
   loadGame.close()


def do_save2(self, arg):
   saveGame2 = open('savegame2.txt', 'wb')
   saveValues2 = (pl, e1ft, e2ft, e3ft, e4ft)
   pickle.dump(saveValues2, saveGame2)
   saveGame2.close()


def do_load2(self, arg):
   loadGame2 = open('savegame2.txt', 'rb')
   loadValues2 = pickle.load(loadGame2)
   pl = loadValues2[0]
   e1ft = loadValues2[1]
   e2ft = loadValues2[2]
   e3ft = loadValues2[3]
   e4ft = loadValues2[4]
   loadGame2.close()
pl = (5)
hdb = (pl*0.075)
hst = (pl*0.1)
hag = (pl*0.15)
hitl = (0)
hhp = (pl*0.05)
#e stands for enemy, 1 stands for the enemy number.
#s is strength, d is durability, h is health, a is agility.
#Story System variables
s1ch1 = "Saiyan Saga"
s1ch1completed = (0)








#End of Story System variables




#Enemy 1 stats
e1ft = (0)
e1s = (10)
e1d = (25)
e1h = (15)
e1a = (10)
#Closing of Enemy 1 stats


#Enemy 2 stats
e2ft = (0)
e2d = (30)
e2s = (35)
e2h = (25)
e2a = (20)
#Closing of Enemy 2 stats


#Enemy 3 stats
e3ft = (0)
e3d = (200)
e3s = (185)
e3h = (225)
e3a = (150)
#Closing of Enemy 3 stats


#Enemy 4 stats
e4ft = (0)
e4d = (1350)
e4s = (1800)
e4h = (900)
e4a = (2700)
#Closing of Enemy 4 stats


rc = input("Enter a race human saiyan majin frieza namekian demon ")


while (rc == "human" and pl <= 500):
   e1ft = (0)
   print("Type A to train with martial artists. Press B to lift weights.")
   print("Type C-Z for set of enemies. Then do AA-ZZ for next set of enemies.")
   print("to save your game type the word save. to load your saved game type the word load")
   th1 = input("Select a choice. ")
   if (th1 == "A"):
       pl = (pl + random.randint(1,25))
       print(pl)
       hst = (pl*0.1)
       hhp = (pl*0.05)
       hag = (pl*0.15)
       hdb = (pl*0.075)
       print("Str: " + str(hst) + " ")
       print("HP: " + str(hhp) + " ")
       print("Agl: " + str(hag) + " ")
       print("Dura: " + str(hdb) + " ")
   elif (th1 == "B"):
       pl = (pl + random.randint(1, 15))
       print(pl)
       hst = (pl*0.1)
       hhp = (pl*0.05)
       hag = (pl*0.15)
       hdb = (pl*0.075)
       print("HP: " + str(hhp) + " ")
       print("Agl: " + str(hag) + " ")
       print("Dura: " + str(hdb) + " ")
       print("Str: " + str(hst) + " ")
   elif (th1 == "C"):
       elft = (0)
       eld = (10)
       els = (25)
       elh = (15)
       ela = (10)
       if (e1ft == 1):
           print("You have already beaten this opponent.")
       elif (hst >= e1d and hag >= e1a and hhp >= e1s and e1ft == 0):
           print("You are fighting Goku Raditz Saga")
           print("You win this fight.")
           e1ft = (1)
           pl = (pl + 200)
       elif (e1ft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
           print("You are fighting Goku Raditz Saga")
           print("You have died.")
           break
   elif(th1 == "D"):
       e2ft = (e2ft)
       e2d = (90)
       e2s = (120)
       e2h = (60)
       e2a = (180)
       if (e2ft == 1):
           print("You have already beaten this opponent.")
       elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
           print("You are fighting Raditz")
           print("You win this fight.")
           e2ft = (1)
           pl = (pl + 500)
       elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
           print("You are fighting Raditz.")
           print("You have died.")
           break
   elif(th1 == "E"):
       e3ft = (e3ft)
       e3d = (200)
       e3s = (185)
       e3h = (225)
       e3a = (150)
       if (e3ft == 1):
           print("You have already beaten this opponent.")  
       elif (hst >= e3d and hag >= e3a and hhp >= e3s and e3ft == 0):
           print("You are fighting Nappa.")    
           print("You win this fight.")
           e3ft = (1)
           pl = (pl + 1000)
       elif (e3ft == 0 and hst < e3d or e3ft == 0 and hag < e3a or e3ft == 0 and hhp < e3s):
           print("You are fighting Nappa.")
           print("You have died.")
           break
   elif(th1 == "F"):
       e4ft = (e4ft)
       e4d = (1350)
       e4s = (1800)
       e4h = (900)
       e4a = (2700)
       if (e4ft == 1):
           print("You have already beaten this opponent.")
       elif (hst >= e4d and hag >= e4a and hhp >= e4s and e4ft == 0):
           print("You are fighting Vegeta Saiyan Saga.")    
           print("You win this fight.")
           e4ft = (1)
           pl = (pl + 2500)
       elif (e4ft == 0 and hst < e4d or e4ft == 0 and hag < e4a or e4ft == 0 and hhp < e4s):
           print("You are fighting Vegeta Saiyan Saga.")
           print("You have died.")
           break
   elif(th1 == "save"):
       saveGame = open('savegame.txt', 'wb')
       saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
       do_save(saveValues, saveGame)
   elif(th1 == "load"):
       loadGame = open('savegame.txt', 'rb')
       loadValues = pickle.load(loadGame)
       pl = loadValues[0]
       e1ft = loadValues[1]
       e2ft = loadValues[2]
       e3ft = loadValues[3]
       e4ft = loadValues[4]
       do_load(loadValues, loadGame)
       print(pl)
   elif (th1 == "continuestory"):
     if (s1ch1completed == 0):
       print("You walk along the countryside, wondering if anything interesting would happen. \tYou suddenly hear a loud crashing noise as something pounds into the surface in front of you.\tYou see a figure with long hair and weird looking armor step out from a crater filled with smoke.\tThis person charges at you without warning.\tBEGIN FIGHT")
       if (hst < e2d and s1ch1completed == 0 or hag < e2a and s1ch1completed == 0 or hhp < e2s and s1ch1completed == 0):
          print("You suddenly get hit with a beam of energy right through your heart and drop dead.")
          break
       elif (hst >= e2d and hag >= e2a and hhp >= e2s and s1ch1completed == 0):
         s1ch1choice1g3prob3 = ("You block the punch and headbutt the figure into a lake.")
         s1ch1choice1g3prob2 = ("You fail to block the punch but headbutt the figure into a rock.")
         s1ch1choice1g3prob3 = ("You block the punch but get hit back when you headbutt the figure.")
         s1ch1choice1g3prob = random.choice(s1ch1choice1g3prob1, s1ch1choice1g3prob2, s1ch1choice1g3prob3)
         s1ch1choice1g2prob1 = ("You dodge the punch and skid to the side unharmed.")
         s1ch1choice1g2prob2 = ("You dodge the punch but get kicked off your feet.")
         s1ch1choice1g2prob3 = ("You fail to dodge the punch and get sent flying into a tree.")
         s1ch1choice1g2prob = random.choice(s1ch1choice1g2prob1, s1ch1choice1g2prob2, s1ch1choice1g2prob3)
         s1ch1choice1prob1 = ("You block it but your arm gets ki blasted back.")
         s1ch1choice1prob2 = ("You block it and gut punch the figure.")
         s1ch1choice1prob3 = ("You fail to block it and get your arm broken trying to gut punch him.")
         s1ch1choice1prob = random.choice(s1ch1choice1prob1, s1ch1choice1prob2, s1ch1choice1prob3)
         print("Your first choice options: BLOCKANDGUTPUNCH DODGE BLOCKANDHEADBASH")
         s1ch1choice1 = input("You are about to be punched in the face. What do you do?")
         if (s1ch1choice1 =="BLOCKANDGUTPUNCH" and s1ch1choice1prob == s1ch1choice1prob1):
            s1ch1choice2prob1 = ("You block the kick and guard for the next attack.")
            s1ch1choice2prob2 = ("You block the kick but get punched hard.")
            s1ch1choice2prob3 = ("You fail to block the kick and strain your arm.")
            s1ch1choice2prob = random.choice(s1ch1choice2prob1, s1ch1choice2prob2, s1ch1choice2prob3)
            print(s1ch1choice1prob1)
            print("The figure lifts his leg up, ready to kick you.")
            print("Your choices are: BLOCK GRABLEGANDSLAMDOWN")
            s1ch1choice2 = input("What do you do?")
            if (s1ch1choice2 == "BLOCK" and s1ch1choice2prob == s1ch1choice2prob1):
               print(s1ch1choice2prob1)
               print("The figure is tired and retreats to the skies. END FIGHT.")
               break
         elif(s1ch1choice1 =="BLOCKANDGUTPUNCH" and s1ch1choice1prob == s1ch1choice1prob2):
         	print(s1ch1choice1prob2)
         	print("The figure lifts his leg up, ready to kick you.")
         	print("Your choices are: BLOCK GRABLEGANDSLAMDOWN")
         	s1ch1choice2 = input("What do you do?")
         	if (s1ch1choice2 == "BLOCK" and s1ch1choice2prob == s1ch1choice2prob1):
         	  	s1ch1choice3prob1 = ("You punch the figure in the side and send the figure flying.")
         	  	s1ch1choice3prob2 = ("You punch the figure in the side but it doesnt effect him.")
         	  	s1ch1choice3prob3 = ("The figure grabs your fist and negates the energy, throwing you back.")
         	  	s1ch1choice3prob = random.choice(s1ch1choice3prob1, s1ch1choice3prob2, s1ch1choice3prob3)
         	  	s1ch1choice3g2prob1 = ("You clash fists with the figure and send him flying into multiple trees.")
         	  	s1ch1choice3g2prob2 = ("You clash fists with the figure and you both are sent flying into mountains.")
         	  	s1ch1choice3g2prob3 = ("You clash fists with the figure and you are sent flying into the ground.")
         	  	s1ch1choice3g2prob = random.choice(s1ch1choice3g2prob1, s1ch1choice3g2prob2, s1ch1choice3g2prob3)
         	  	print("s1ch1choice2prob1")
         	  	print("The figure has an angry expression on his face.\nThe figure charges you with a punch.")
         	  	print("Your choices are: KIPUNCH CLASHPUNCHES")
         	  	s1ch1choice3 = input("What will you do?")
         	  	if (s1ch1choice3 == "KIPUNCH" and s1ch1choice3prob == s1ch1choice3prob1):
         	  		print(s1ch1choice3prob1)
         	  		print("The figure retreats to the skies.\nEND FIGHT")
         	  		break
         elif(s1ch1choice1 == "BLOCKANDDGUTPUNCH" and s1ch1choice1prob == s1ch1choice1prob3):
         	print(s1ch1choice1prob3)
         	s1ch1choice2prob1 = ("You get pushed back and fall out of the way of the beam, sustaining heavy damage.")
         	s1ch1choice2prob2 = ("You get pushed back and you are incinerated in the beam of energy.")
         	s1ch1choice2prob = random.choice(s1ch1choice2prob1, s1ch1choice2prob2)
         	print("The figure charges two purple balls of energy as he lifts his arms above and behind his head.")
         	print("Your choices are: BEAMCLASH ENERGYBARRIER")
         	s1ch1choice2 = input("What will you do?")
       if(s1ch1choice2 == "BEAMCLASH" and s1ch1choice2prob == s1ch1choice2prob1):
             print(s1ch1choice2prob1)
             s1ch1choice3prob1 = ("You dash forward but get kicked down before you are out of reach.")
             s1ch1choice3prob2 = ("You dash forward and turn to face the figure.")
             s1ch1choice3prob = random.choice(s1ch1choice3prob1, s1ch1choice3prob2)
             print("The figure appears behind you, beginning to strike.")
             print("Your only choice is: DASHFORWARD")
             s1ch1choice3 = ("What will you do?")
             if(s1ch1choice3 == "DASHFORWARD" and s1ch1choice3prob == s1ch1choice3prob1):
               print(s1ch1choice3prob1)
               print("The figure laughs at you and flies away.")
       elif(s1ch1choice1 == "BLOCKANDGUTPUNCH" and s1ch1choice1prob == s1ch1choice1prob3):
           print(s1ch1choice1prob3)
           print("The figure begins to raise his leg to kick.")
           print("Your choices are: GRABANDLEGSLAMDOWN BLOCK")
           s1ch1choice2 = ("What do you do?")
           if (s1ch1choice2 == "BLOCK"):
             print("You attempt to block with your remaining arm but cannot block effectively.")
             print("The figure stares over you and blasts you into a million dust particles.")
             break
           elif (s1ch1choice2 == "GRABANDLEGSLAMDOWN"):
             print("You attempt to lift the figures whole weight with your remaining arm and strain yourself.")
             print("You fall down slowly as a glowing beam of light begins to surroud you as you disappear into dust.")
             break
else:
          while (rc == "human" and pl <= 2000 and pl > 500):
             print("Type A to train with chi masters. Press B to lift giant boulders.")
             print("Type C-Z for set of enemies. Then do AA-ZZ for next set of enemies.")
             print("to save your game type the word save. to load your saved game type the word load")
             th2 = input("Select a choice. ")
             if (th2 == "A"):
                pl = (pl + random.randint(5, 40))
                print(pl)
                hst = (pl*0.1)
                hhp = (pl*0.05)
                hag = (pl*0.15)
                hdb = (pl*0.075)
                print("Str: " + str(hst) + " ")
                print("HP: " + str(hhp) + " ")
                print("Agl: " + str(hag) + " ")
                print("Dura: " + str(hdb) + " ")
             elif (th2 == "B"):
               pl = (pl + random.randint(5, 30))
               print(pl)
               hst = (pl*0.1)
               hhp = (pl*0.05)
               hag = (pl*0.15)
               hdb = (pl*0.075)
               print("Str: " + str(hst) + " ")
               print("HP: " + str(hhp) + " ")
               print("Agl: " + str(hag) + " ")
               print("Dura: " + str(hdb) + " ")
             elif (th2 == "C"):
                e1ft = (e1ft)
                eld = (10)
                els = (25)
                elh = (15)
                ela = (10)
                if (e1ft == 1):
                   print("You have already beaten this opponent.")
                elif (hst >= eld and hag >= ela and hhp >= els and e1ft == 0):
                   print("You are fighting Goku Raditz Saga")
                   print("You win this fight.")
                   e1ft = (1)
                   pl = (pl + 200)
                elif (elft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
                   print("You are fighting Goku Raditz Saga")
                   print("You have died.")
                   break
             elif(th2 == "D"):
                e2ft = (e2ft)
                e2d = (90)
                e2s = (120)
                e2h = (60)
                e2a = (180)
                if (e2ft == 1):
                   print("You have already beaten this opponent.")
                elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
                   print("You are fighting Raditz")
                   print("You win this fight.")
                   e2ft = (1)
                   pl = (pl + 500)
                elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
                   print("You are fighting Raditz")
                   print("You have died.")
                   break
             elif(th2 == "E"):
                e3ft = (e3ft)
                e3d = (200)
                e3s = (185)
                e3h = (225)
                e3a = (150)
                if (e3ft == 1):
                   print("You have already beaten this opponent.")  
                elif (hst >= e3d and hag >= e3a and hhp >= e3s and e3ft == 0):
                  print("You are fighting Nappa.")
                  print("You win this fight.")
                  e3ft = (1)
                  pl = (pl + 1000)
                elif (e3ft == 0 and hst < e3d or e3ft == 0 and hag < e3a or e3ft == 0 and hhp < e3s):
                  print("You are fighting Nappa.")
                  print("You have died.")
                  break
             elif(th2 == "F"):
                e4ft = (e4ft)
                e4d = (1350)
                e4s = (1800)
                e4h = (900)
                e4a = (2700)
                if (e4ft == 1):
                   print("You have already beaten this opponent.")
                elif (hst >= e4d and hag >= e4a and hhp >= e4s and e4ft == 0):
                   print("You are fighting Vegeta Saiyan Saga.")
                   print("You win this fight.")
                   e4ft = (1)
                   pl = (pl + 2500)
                elif (e4ft == 0 and hst < e4d or e4ft == 0 and hag < e4a or e4ft == 0 and hhp < e4s):
                   print("You are fighting Vegeta Saiyan Saga.")
                   print("You have died.")
                   break
             elif(th2 == "save"):
                saveGame = open('savegame.txt', 'wb')
                saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
                do_save(saveValues, saveGame)
             elif(th2 == "load"):
                LoadGame = open('savegame.txt', 'rb')
                loadValues = pickle.load(LoadGame)
                pl = loadValues[0]
                e1ft = loadValues[1]
                e2ft = loadValues[2]
                e3ft = loadValues[3]
                e4ft = loadValues[4]
                do_load(loadValues, LoadGame)
                print(pl)
             elif (th2 == "continuestory"):
               if (s1ch1completed == 0):
                 print("You walk along the countryside, wondering if anything interesting would happen. \tYou suddenly hear a loud crashing noise as something pounds into the surface in front of you.\tYou see a figure with long hair and weird looking armor step out from a crater filled with smoke.\tThis person charges at you without warning.\tBEGIN FIGHT")
                 if (hst < e2d and s1ch1completed == 0 or hag < e2a and s1ch1completed == 0 or hhp < e2s and s1ch1completed == 0):
                   print("You suddenly get hit with a beam of energy right through your heart and drop dead.")
                   break
                 elif (hst >= e2d and hag >= e2a and hhp >= e2s and s1ch1completed == 0):
                   s1ch1choice1g3prob1 = ("You block the punch and headbutt the figure into a lake.")
                   s1ch1choice1g3prob2 = ("You fail to block the punch but headbutt the figure into a rock.")
                   s1ch1choice1g3prob3 = ("You block the punch but get hit back when you headbutt the figure.")
                   s1ch1choice1g2prob1 = ("You dodge the punch and skid to the side unharmed.")
                   s1ch1choice1g2prob2 = ("You dodge the punch but get kicked off your feet.")
                   s1ch1choice1g2prob3 = ("You fail to dodge the punch and get sent flying into a tree.")
                   s1ch1choice1g3problist = (s1ch1choice1g3prob1, s1ch1choice1g3prob2, s1ch1choice1g3prob3)
                   s1ch1choice1g3prob = random.choice(s1ch1choice1g3problist)
                   s1ch1choice1g2problist = (s1ch1choice1g2prob1, s1ch1choice1g2prob2, s1ch1choice1g2prob3)
                   s1ch1choice1g2prob = random.choice(s1ch1choice1g2problist)
                   s1ch1choice1prob1 = ("You block it but your arm gets ki blasted back.")
                   s1ch1choice1prob2 = ("You block it and gut punch the figure.")
                   s1ch1choice1prob3 = ("You fail to block it and get your arm broken trying to gut punch him.")
                   s1ch1choice1problist = (s1ch1choice1prob1, s1ch1choice1prob2, s1ch1choice1prob3)
                   s1ch1choice1prob = random.choice(s1ch1choice1problist)
                   print("Your first choice options: BLOCKANDGUTPUNCH DODGE BLOCKANDHEADBASH")
                   s1ch1choice1 = input("You are about to be punched in the face. What do you do?")
                   if (s1ch1choice1 =="BLOCKANDGUTPUNCH" and s1ch1choice1prob == s1ch1choice1prob1):
                     s1ch1choice2prob1 = ("You block the kick and guard for the next attack.")
                     s1ch1choice2prob2 = ("You block the kick but get punched hard.")
                     s1ch1choice2prob3 = ("You fail to block the kick and strain your arm.")
                     s1ch1choice2problist = (s1ch1choice2prob1, s1ch1choice2prob2, s1ch1choice2prob3)
                     s1ch1choice2prob = random.choice(s1ch1choice2problist)
                     print(s1ch1choice1prob1)
                     print("The figure lifts his leg up, ready to kick you.")
                     print("Your choices are: BLOCK GRABLEGANDSLAMDOWN")
                     s1ch1choice2 = input("What do you do?")
                     if (s1ch1choice2 == "BLOCK" and s1ch1choice2prob == s1ch1choice2prob1):
                       print(s1ch1choice2prob1)
                       print("The figure is tired and retreats to the skies. END FIGHT.")
                       s1ch1completed = (1)
                     elif(s1ch1choice1 =="BLOCKANDGUTPUNCH" and s1ch1choice1prob == s1ch1choice1prob2):
                       print(s1ch1choice1prob2)
                       print("The figure lifts his leg up, ready to kick you.")
                       print("Your choices are: BLOCK GRABLEGANDSLAMDOWN")
                       s1ch1choice2 = input("What do you do?")
                       if (s1ch1choice2 == "BLOCK" and s1ch1choice2prob == s1ch1choice2prob1):
                         s1ch1choice3prob1 = ("You punch the figure in the side and send the figure flying.")
                         s1ch1choice3prob2 = ("You punch the figure in the side but it doesnt effect him.")
                         s1ch1choice3prob3 = ("The figure grabs your fist and negates the energy, throwing you back.")
                         s1ch1choice3prob = random.choice(s1ch1choice3prob1, s1ch1choice3prob2, s1ch1choice3prob3)
                         s1ch1choice3g2prob1 = ("You clash fists with the figure and send him flying into multiple trees.")
                         s1ch1choice3g2prob2 = ("You clash fists with the figure and you both are sent flying into mountains.")
                         s1ch1choice3g2prob3 = ("You clash fists with the figure and you are sent flying into the ground.")
                         s1ch1choice3g2prob = random.choice(s1ch1choice3g2prob1, s1ch1choice3g2prob2, s1ch1choice3g2prob3)
                         print("s1ch1choice2prob1")
                         print("The figure has an angry expression on his face.\nThe figure charges you with a punch.")
                         print("Your choices are: KIPUNCH CLASHPUNCHES")
                         s1ch1choice3 = input("What will you do?")
                         if (s1ch1choice3 == "KIPUNCH" and s1ch1choice3prob == s1ch1choice3prob1):
                           print(s1ch1choice3prob1)
                           print("The figure retreats to the skies.\nEND FIGHT")
                           s1ch1completed = (1)
                         elif(s1ch1choice1 == "BLOCKANDDGUTPUNCH" and s1ch1choice1prob == s1ch1choice1prob3):
                           print(s1ch1choice1prob3)
                           s1ch1choice2prob1 = ("You get pushed back and fall out of the way of the beam, sustaining heavy damage.")
                           s1ch1choice2prob2 = ("You get pushed back and you are incinerated in the beam of energy.")
                           s1ch1choice2problist = (s1ch1choice2prob1, s1ch1choice2prob2)
                           s1ch1choice2prob = random.choice(s1ch1choice2problist)
                           print("The figure charges two purple balls of energy as he lifts his arms above and behind his head.")
                           print("Your choices are: BEAMCLASH ENERGYBARRIER")
                           s1ch1choice2 = input("What will you do?")
                           if(s1ch1choice2 == "BEAMCLASH" and s1ch1choice2prob == s1ch1choice2prob1):
                             print(s1ch1choice2prob1)
                             s1ch1choice3prob1 = ("You dash forward but get kicked down before you are out of reach.")
                             s1ch1choice3prob2 = ("You dash forward and turn to face the figure.")
                             s1ch1choice3prob = random.choice(s1ch1choice3prob1, s1ch1choice3prob2)
                             print("The figure appears behind you, beginning to strike.")
                             print("Your only choice is: DASHFORWARD")
                             s1ch1choice3 = ("What will you do?")
                             if(s1ch1choice3 == "DASHFORWARD" and s1ch1choice3prob == s1ch1choice3prob1):
                               print(s1ch1choice3prob1)
                               print("The figure laughs at you and flies away.")
                         elif(s1ch1choice1 == "BLOCKANDGUTPUNCH" and s1ch1choice1prob == s1ch1choice1prob3):
                           print(s1ch1choice1prob3)
                           print("The figure begins to raise his leg to kick.")
                           print("Your choices are: GRABANDLEGSLAMDOWN BLOCK")
                           s1ch1choice2 = ("What do you do?")
                           if (s1ch1choice2 == "BLOCK"):
                             print("You attempt to block with your remaining arm but cannot block effectively.")
                             print("The figure stares over you and blasts you into a million dust particles.")
                             break
                           elif (s1ch1choice2 == "GRABANDLEGSLAMDOWN"):
                             print("You attempt to lift the figures whole weight with your remaining arm and strain yourself.")
                             print("You fall down slowly as a glowing beam of light begins to surroud you as you disappear into dust.")
                             break
             else:
               while (rc == "human" and pl <= 9000 and pl > 2000):
                   print("Type A to train with Shadow Clones. Press B to lift mountains.")
                   print("Type C-Z for set of enemies. Then do AA-ZZ for next set of enemies.")
                   print("to save your game type the word save. to load your saved game type the word load")
                   th3 = input("Select a choice. ")
                   if (th3 == "A"):
                       pl = (pl + random.randint(25, 75))
                       print(pl)
                       hst = (pl*0.1)
                       hhp = (pl*0.05)
                       hag = (pl*0.15)
                       hdb = (pl*0.075)
                       print("Str: " + str(hst) + " ")
                       print("HP: " + str(hhp) + " ")
                       print("Agl: " + str(hag) + " ")
                       print("Dura: " + str(hdb) + " ")
                   elif (th3 == "B"):
                       pl = (pl + random.randint(15, 50))
                       print(pl)
                       hst = (pl*0.1)
                       hhp = (pl*0.05)
                       hag = (pl*0.15)
                       hdb = (pl*0.075)
                       print("Str: " + str(hst) + " ")
                       print("HP: " + str(hhp) + " ")
                       print("Agl: " + str(hag) + " ")
                       print("Dura: " + str(hdb) + " ")
                   elif (th3 == "C"):
                       e1ft = (e1ft)
                       eld = (10)
                       els = (25)
                       elh = (15)
                       ela = (10)
                       if (e1ft == 1):
                           print("You have already beaten this opponent.")
                       elif (hst >= eld and hag >= ela and hhp >= els and e1ft == 0):
                           print("You are fighting Goku Raditz Saga")
                           print("You win this fight.")
                           e1ft = (1)
                           pl = (pl+200)
                       elif (elft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
                           print("You are fighting Goku Raditz Saga")
                           print("You have died.")
                           break
                   elif(th3 == "D"):
                       e2ft = (e2ft)
                       e2d = (90)
                       e2s = (120)
                       e2h = (60)
                       e2a = (180)
                       if (e2ft == 1):
                           print("You have already beaten this opponent.")
                       elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
                           print("You are fighting Raditz")
                           print("You win this fight.")
                           e2ft = (1)
                           pl = (pl+500)
                       elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
                           print("You are fighting Raditz")
                           print("You have died.")
                           break
                   elif(th3 == "E"):
                       e3ft = (e3ft)
                       e3d = (200)
                       e3s = (185)
                       e3h = (225)
                       e3a = (150)
                       if (e3ft == 1):
                           print("You have already beaten this opponent.")  
                       elif (hst >= e3d and hag >= e3a and hhp >= e3s and e3ft == 0):
                           print("You are fighting Nappa.")    
                           print("You win this fight.")
                           e3ft = (1)
                           pl = (pl + 1000)
                       elif (e3ft == 0 and hst < e3d or e3ft == 0 and hag < e3a or e3ft == 0 and hhp < e3s):
                           print("You are fighting Nappa.")
                           print("You have died.")
                           break
                   elif(th3 == "F"):
                       e4ft = (e4ft)
                       e4d = (1350)
                       e4s = (1800)
                       e4h = (900)
                       e4a = (2700)
                       if (e4ft == 1):
                           print("You have already beaten this opponent.")
                       elif (hst >= e4d and hag >= e4a and hhp >= e4s and e4ft == 0):
                           print("You are fighting Vegeta Saiyan Saga.")    
                           print("You win this fight.")
                           e4ft = (1)
                           pl = (pl + 2500)
                       elif (e4ft == 0 and hst < e4d or e4ft == 0 and hag < e4a or e4ft == 0 and hhp < e4s):
                           print("You are fighting Vegeta Saiyan Saga.")
                           print("You have died.")
                           break
                   elif(th3 == "save"):
                       saveGame = open('savegame.txt', 'wb')
                       saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
                       do_save(saveValues, saveGame)
                   elif(th3 == "load"):
                       loadGame = open('savegame.txt', 'rb')
                       loadValues = pickle.load(loadGame)
                       pl = loadValues[0]
                       e1ft = loadValues[1]
                       e2ft = loadValues[2]
                       e3ft = loadValues[3]
                       e4ft = loadValues[4]
                       do_load(loadValues, loadGame)
                       print(pl)
                   else:
                       while(rc == "human" and pl <= 120000 and pl > 9000):
                           print("Type A to train with Frieza Race Weaklings. Press B to exercise with 2 ton weighted clothing (8 tons total).")
                           print("Type C-Z for set of enemies. Then do AA-ZZ for next set of enemies.")
                           print("to save your game type the word save. to load your saved game type the word load")
                           th3 = input("Select a choice. ")
                           if (th3 == "A"):
                               pl = (pl + random.randint(50, 100))
                               print(pl)
                               hst = (pl*0.1)
                               hhp = (pl*0.05)
                               hag = (pl*0.15)
                               hdb = (pl*0.075)
                               print("Str: " + str(hst) + " ")
                               print("HP: " + str(hhp) + " ")
                               print("Agl: " + str(hag) + " ")
                               print("Dura: " + str(hdb) + " ")
                           elif (th3 == "B"):
                               pl = (pl + random.randint(50, 75))
                               print(pl)
                               hst = (pl*0.1)
                               hhp = (pl*0.05)
                               hag = (pl*0.15)
                               hdb = (pl*0.075)
                               print("Str: " + str(hst) + " ")
                               print("HP: " + str(hhp) + " ")
                               print("Agl: " + str(hag) + " ")
                               print("Dura: " + str(hdb) + " ")
                           elif (th3 == "C"):
                               e1ft = (e1ft)
                               eld = (10)
                               els = (25)
                               elh = (15)
                               ela = (10)
                               if (e1ft == 1):
                                   print("You have already beaten this opponent.")
                               elif (hst >= eld and hag >= ela and hhp >= els and e1ft == 0):
                                   print("You are fighting Goku Raditz Saga")
                                   print("You win this fight.")
                                   e1ft = (1)
                                   pl = (pl+200)
                               elif (elft == 0 and hst < eld or elft == 0 and hag < ela or elft == 0 and hhp < els):
                                   print("You are fighting Goku Raditz Saga")
                                   print("You have died.")
                                   break
                           elif(th3 == "D"):
                               e2ft = (e2ft)
                               e2d = (90)
                               e2s = (120)
                               e2h = (60)
                               e2a = (180)
                               if (e2ft == 1):
                                   print("You have already beaten this opponent.")
                               elif (hst >= e2d and hag >= e2a and hhp >= e2s and e2ft == 0):
                                   print("You are fighting Raditz")
                                   print("You win this fight.")
                                   e2ft = (1)
                                   pl = (pl+500)
                               elif (e2ft == 0 and hst < e2d or e2ft == 0 and hag < e2a or e2ft == 0 and hhp < e2s):
                                   print("You are fighting Raditz")
                                   print("You have died.")
                                   break
                           elif(th3 == "E"):
                               e3ft = (e3ft)
                               e3d = (200)
                               e3s = (185)
                               e3h = (225)
                               e3a = (150)
                               if (e3ft == 1):
                                   print("You have already beaten this opponent.")
                               elif (hst >= e3d and hag >= e3a and hhp >= e3s and e3ft == 0):
                                   print("You are fighting Nappa.")
                                   print("You win this fight.")
                                   e3ft = (1)
                                   pl = (pl + 1000)
                               elif (e3ft == 0 and hst < e3d or e3ft == 0 and hag < e3a or e3ft == 0 and hhp < e3s):
                                   print("You are fighting Nappa.")
                                   print("You have died.")
                                   break
                           elif(th3 == "F"):
                               e4ft = (e4ft)
                               e4d = (1350)
                               e4s = (1800)
                               e4h = (900)
                               e4a = (2700)
                               if (e4ft == 1):
                                   print("You have already beaten this opponent.")
                               elif (hst >= e4d and hag >= e4a and hhp >= e4s and e4ft == 0):
                                   print("You are fighting Vegeta Saiyan Saga.")
                                   print("You win this fight.")
                                   e4ft = (1)
                                   pl = (pl + 2500)
                               elif (e4ft == 0 and hst < e4d or e4ft == 0 and hag < e4a or e4ft == 0 and hhp < e4s):
                                   print("You are fighting Vegeta Saiyan Saga.")
                                   print("You have died.")
                                   break
                           elif(th3 == "save"):
                               saveGame = open('savegame.txt', 'wb')
                               saveValues = (pl, e1ft, e2ft, e3ft, e4ft)
                               do_save(saveValues, saveGame)
                           elif(th3 == "load"):
                               loadGame = open('savegame.txt', 'rb')
                               loadValues = pickle.load(loadGame)
                               pl = loadValues[0]
                               e1ft = loadValues[1]
                               e2ft = loadValues[2]
                               e3ft = loadValues[3]
                               e4ft = loadValues[4]
                               do_load(loadValues, loadGame)
                               print(pl)