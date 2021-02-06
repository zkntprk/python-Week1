### All Rights Reserved ###

#Copyright (c) ${BodyMassIndexCalculation.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

# Project : BODY MASS INDEX CALCULATION
# FORMULA = Body Mass Index (BMI) = Body Weight (kg.) / Square of height (m2.)
answer='Y'
print('BODY MASS INDEX CALCULATION STARTED')
while(answer=='Y'):
    weight=int(input('Please enter your weight as kg (kilogram) unit: '))
    height=float(input('Please enter your weight as m (meter) unit (Exp=1.73): '))
    index=weight/(height**2)
    print('Your Body Mass Index is ',index)
    if (index<18.5):
        print('You are Underweight')
    elif (18.5<=index and index<25):
        print('You are Normal weight')
    elif (25<=index and index<30):
        print('You are Overweight')
    else:
        print('You are Obesity')
    answer=str(input('Do you want to make another calculation?(Y/N)'))


### All Rights Reserved ###

#Copyright (c) ${BodyMassIndexCalculation.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.