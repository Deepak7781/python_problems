def printText(userInput):
    unitsMapping = {'0':'', '1':' One', '2':' Two', '3':' Three', '4':' Four', '5':' Five', '6':' Six', '7':' Seven',
                    '8':' Eight', '9':' Nine'}
    tensMapping = {'0':'', '2':' Twenty', '3':' Thirty', '4':' Fourty', '5':' Fifty', '6':' Sixty', '7':' Seventy',
                    '8':' Eighty','9':' Ninety'}
    teensMapping = {'10':' Ten', '11':' Eleven','12':' Twelve' , '13':' Thirteen', '14':' Fourteen', '15':' Fifteen',
                      '16':' Sixteen', '17':' Seventeen', '18':' Eighteen', '19':' Nineteen'}
    numLength = len(userInput)
    numText = ''

    units = userInput[numLength - 1] if numLength >= 1 else '0'
    tens = userInput[numLength - 2] if numLength >= 2 else '0'
    hundreds = userInput[numLength - 3] if numLength >= 3 else '0'
    if numLength > 3 and numLength <= 6:
        thousands = userInput[:numLength - 3] 
    elif numLength > 6 and numLength <= 9:
        thousands = userInput[numLength - 6:numLength - 3] 
    else:
        thousands = '0'
    
    if numLength > 6 and numLength <= 9:
        millions = userInput[:numLength - 6]
    else:
        millions = '0'

    if numLength > 9:
        billions = userInput[:numLength - 9]
    else:
        billions= '0'

    if billions != '0':
        numText += printText(billions) + ' Billion'
        
    if millions != '0':
        numText = printText(millions) + ' Million'


    if thousands != '0' and int(thousands) > 0:
        numText += printText(thousands) + ' Thousand'

    if hundreds != '0':
        numText += unitsMapping[hundreds] + ' Hundred'
    if int(userInput) > 99 and int(userInput)%100 != 0:
        numText += ' and'

    if tens == '1':
        numText += teensMapping[tens+units]
    elif tens == '0':
        numText += unitsMapping[units]
    else:
        numText += tensMapping[tens] + unitsMapping[units]

    return numText

userInput = input('Enter an integer smaller than 1000 :')
while True:
    try:
        userNum = int(userInput)
        if userNum > 9999999999:
            userInput = input("The number is too big. Enter an integer smaller than 1000:")
        else:
            break
    except valueError:
        userInput = input('You did not enter an integer. Enter an integer smaller than 1000:')

print(f'In words :{printText(userInput.strip())}')