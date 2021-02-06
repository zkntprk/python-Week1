### All Rights Reserved ###

#Copyright (c) ${RockPaperScissorsGame.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.


#Project: Rock-Paper-Scissors Game 
#10 Times you will play against PC

import random #For PC random selection we need to import random
game=['rock','paper','scissors']
counter=0 #sayac
UserScore=0
PcScore=0
while (counter<10):
    user=str(input("Please select one of your choice (rock / paper / scissors) : ")) #user choice
    a= user in game #true/false 
    while (a== False):
         user=input("Wrong Entry! Please select one of your choice (rock / paper / scissors) :")
         a=user in game
    pc=random.choice(game) # pc random selection
    print("PC selected : ",pc)
    if ((user=='rock' and pc=='scissors')or(user=='scissors'and pc=='paper')or(user=='paper' and pc=='rock')):
        UserScore+=1
        print("""You won this hand. Congratulations! Score status:
Siz   PC\n""", UserScore,'  ',PcScore)
    elif(user==pc):
        print("""This hand is a draw. Score status:
Siz   PC\n""", UserScore,'  ',PcScore)
    else:
        PcScore+=1
        print("""Pc won this hand. Score status:
Siz   PC\n""", UserScore,'  ',PcScore)
    counter+=1
print('Game Finished!')    
if (UserScore>PcScore):
    print("""Congratulations! You won! Endgame score:
Siz   PC\n""", UserScore,'  ',PcScore)
elif(PcScore>UserScore):
    print("""You lost! Endgame score:
Siz   PC\n""", UserScore,'  ',PcScore)
else:
    print("""The game is a draw! Endgame score:
Siz   PC\n""", UserScore,'  ',PcScore)


### All Rights Reserved ###

#Copyright (c) ${RockPaperScissorsGame.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.