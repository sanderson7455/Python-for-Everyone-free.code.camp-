def computepay(hours, rate):
    #print('In computepay', hours, rate)
    if hours>40:
        print('Overtime')
        reg=rate*hours
        otp=(hours-40)*(rate*.5)
        pay=otp+reg
    else:
        print('Regular')
        pay=hours*rate
    return pay

sh=input('Enter Hours:')
sr=input('Enter Rate:')
fh=float(sh)
fr=float(sr)
#print(fh, fr)
xp=computepay (fh,fr)

print ('Pay:',xp)
