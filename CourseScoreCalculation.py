### All Rights Reserved ###

#Copyright (c) ${CourseScoreCalculation.2021} ${Ozkan TOPRAK}

#Created by InfitecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#for 4 course we will get input info of student name-surname-number-midtermPoint-FinalPoint
#%40 of midterm exam point + %60 of final exam point = Score
#For pass to course, students need to get score>=50

stdname=[]
stdsurname=[]
stdnumber=[]
courses=[]
midterm=[]
final=[]
score=[]
status=[]

for i in range (0,4):
    courses.insert(i,str(input('Enter the name of the course you want to enter grades: ')))
    cevap ='Y'
    a=0
    while (cevap =='Y' or cevap =='y'):
        
        stdname.insert(a,str(input('Enter the name of the student: ')))
        stdsurname.insert(a,str(input("Enter the student's surname:")))
        stdnumber.insert(a,str(input("Enter the student's number: ")))
        midterm.insert(a,int(input("Enter the student's midterm grade: ")))
        final.insert(a,int(input("Enter the student's final grade: ")))
        score.insert(a,(midterm[a]*0.4+final[a]*0.6))
        if (score[a]>=50):
            status.insert(a,'PASS')
        else:
            status.insert(a,'FAIL')
        a=a+1

        b=0
        while (b==0):
            cevap=str(input('Would you like to add other students to this course? (Y/N)'))
            if (cevap=='Y' or cevap=='y'):
                cevap='y'
                b=b+1
            elif (cevap=='N' or cevap=='n'):
                break
            else:
                print('You entered a wrong statement !')
                b=0

    c=0
    print(' NAME ',' SURNAME ', ' NUMBER ', '  COURSE ','  STATUS ')
    while (c<a):
        print(stdname[c],'',stdsurname[c],'',stdnumber[c],'',courses[i],'',status[c])
        c+=1
        
### All Rights Reserved ###

#Copyright (c) ${CourseScoreCalculation.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.