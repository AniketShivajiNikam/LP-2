'''
QUESTIONS = [
    'Do you have cough?',
    'Do you have a sore throat?',
    'Do you have a fever?',
    'Are you noticing any unexplained excessive sweating?',
    'Do you have an itchy throat?',
    'Do you have a runny nose?',
    'Do you have a stuffy nose?',
    'Do you have a headache?',
    'Do you feel tired without actually exhausting yourself?'
]


THRESHOLD = {
    'Mild': 30,
    'Severe': 50,
    'Extreme': 75
}


def expertSystem(questions, threshold):

    score = 0

    for question in questions:
        print(question+" (Y/N) ")
        ans = input("> ")
        if ans.lower() == 'y':
            print('On a scale of 1-10 how bad is it ?')
            ip = input('> ')
            while((not ip.isnumeric()) or int(ip) < 1 or int(ip) > 10):
                print('Enter a valid input !')
                ip = input('> ')
            score += int(ip)

    print()
    print()

    if score >= threshold['Extreme']:
        print("You are showing symptoms of having EXTREME COVID-19")
        print("Please call +91 8112233445 immediately to immediate assistance")
        print("Based on your symptoms, You will need Immediate Hospitalization")

    elif score >= threshold['Severe']:
        print("Based on your answers You are showing Symptoms of SEVERE COVID-19")
        print("You are advised to contact a COVID-19 Specialist ASAP")
        print("You are prescribed with Favipriavir, Dolo 650 / Crocin 500, Paracetamol, Brufane")
        print("Also coduct a COVID-19 Lab Test ASAP at your own convenience as this might be a false Positive")
        print()
        print()
        print("Lab Testing: https://www.metropolisindia.com/parameter/pune/covid-19-rt-pcr-test")

    elif score >= threshold['Mild']:
        print("Based on your answers You are showing Symptoms of VERY MILD COVID-19")
        print("Please Isolate yourself Immediately on a precautionary basis")
        print("As this has a possibility of being a false positive , please consider testing yourself")
        print("At home testing using Self-Testing kits is recommended , but you can get Lab Tests as well")
        print()
        print()
        print("Self testing : https://www.flipkart.com/mylab-coviself-covid-19-rapid-antigen-test-kit/p/itm4d34ea09cad97")
        print("Lab Testing  : https://www.metropolisindia.com/parameter/pune/covid-19-rt-pcr-test")

    else:
        print("You are Showing NO Symptoms of COVID-19")
        print("This might be a false negative, If you feel unsure , please get Tested")
        print("As this has a possibility of being a false negative , please consider testing yourself")
        print("At home testing using Self-Testing kits is recommended")
        print()
        print()
        print("Self testing : https://www.flipkart.com/mylab-coviself-covid-19-rapid-antigen-test-kit/p/itm4d34ea09cad97")

    print()
    print()
    print("For any further queries visit : https://www.aarogyasetu.gov.in/")
    print()
    print()


if '__main__' == __name__:

    print("\n\n\t\tWelcome To The COVID-19 EXPERT SYSTEM\n")
    print("\tNote : Please answer the following questions very honestly\n\n")
    expertSystem(QUESTIONS, THRESHOLD)


# change this code


print('Vedant s COVID-19 Expert system')
covidSuspisionCounter=0


severity=0
asym=0
oxylevel=0
temp=0
questions=['Let me know your body temparature','Let me know your oxygen level','How many vaccines have you taken','What is your age']
yesnoqs=['Do you have cough and cold','Are you able to recognize smell and taste','Are you suffering from sore throat','Are you suffering from headache','Are you suffering from BP/ diabetes','Have you come in a contact of a Covid suspicious person']
for i in range(6):
    print(yesnoqs[i])
    print()
    ans=input()
    if(i!=1 and ans=='yes'):
        covidSuspisionCounter+=1
    elif(i==1 and ans=='no'):
        covidSuspisionCounter+=1
for i in range(4):
    print(questions[i])
    print()
    if(i==0):
        ans=float(input())
        if(ans>=101.0):
            severity+=2
            covidSuspisionCounter+=1
            temp=1
        elif(ans<101.0 and ans>=99.6):
            severity+=1
        else:
            severity+=0
    if(i==1):
        ans=int(input())
        if(ans>=94):
            severity+=0
        elif(ans<94 and ans>87):
            severity+=1
        else:
            severity+=2
            covidSuspisionCounter+=1
            oxylevel=1
    if(i==2):
        ans=int(input())
        if(ans==0):
            severity+=2
        elif(ans==1):
            severity+=1
        else:
            severity+=0
    if(i==3):
        ans=int(input())
        if(ans>12 and ans<31):
            severity+=0
        elif(ans>31 and ans<51):
            severity+=1
        else:
            severity+=2
if(covidSuspisionCounter>3):
    print('The patient is probably covid positive')
    print()
    if(severity<3):
        print('It looks like the symptoms are mild\nhome quarantine')
    elif(severity>=3 and severity<6):
        print('The patient can get an admission in the general ward')
    else:
        print('The patient looks critical')
else:
    print('It looks like patient is not Covid positive')
print()
if(oxylevel==1):
    print("Keep monitoring patient's oxygen level")
if(temp==1):
    print("Keep monitoring patient's body temperature")
'''
