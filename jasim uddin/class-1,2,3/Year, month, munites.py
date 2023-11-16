# #take hour and munites
hour=int(input('Enter hour:'))
minutes=int(input('Enter minutes: '))
totalmin=(hour*60)+ minutes
print('inputet our is', hour)
print('inputet min', minutes)
print('Total minutes is',totalmin)

#take only minutes
getmin=int(input('Enter minutes'))
hour=getmin//60
min=getmin%60
print('input minutes', getmin)
print('total hour is', hour)
print('total mimutes is',min)


