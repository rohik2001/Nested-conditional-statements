
units=int(input('Enter number of units you consumed: '))
if units<70:
    amount=units*3.80
    surcharge=25
    total_amount=amount+surcharge
    print (f"your total amount {total_amount}")
if units<200:
    amount=units*5.14
    surcharge=40
    total_amount=amount+surcharge
    print (f"your total amount {total_amount}")
if units<300:
    amount=units*5.36
    surcharge=75
    total_amount=amount+surcharge
    print (f"your total amount {total_amount}")
if units<400:
    amount=units*5.63
    surcharge=90
    total_amount=amount+surcharge
    print (f"your total amount {total_amount}")
else:
    print('Wrong Input')