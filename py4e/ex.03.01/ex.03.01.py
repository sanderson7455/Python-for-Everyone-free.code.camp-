sh=input('Enter Hours:')
sr=input('Enter Rate:')
fh=float(sh)
fr=float(sr)
#print(fh, fr)
if fh>40:
    print('Overtime')
    reg=fr*fh
    otp=(fh-40)*(fr*.5)
    xp=otp+reg
else:
    print('Regular')
    xp=fh*fr
print ('Pay:',xp)
