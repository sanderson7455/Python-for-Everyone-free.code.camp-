sh=input('Enter Hours:')
sr=input('Enter Rate:')
try:
    fh=float(sh)
    fr=float(sr)
except:
    print('Error, please enter numeric input')
    quit()
if fh>40:
    reg=fr*fh
    otp=(fh-40)*(fr*.5)
    xp=otp+reg
else:
    xp=fh*fr
print ('xyzPay:',xp)
