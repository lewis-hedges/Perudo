from random import randint as roll
import numpy as np
def binomial_cdf(x,n,p):
    cdf = 0
    b = 0
    for k in range(x):
        if k > 0:
            b += + np.log(n-k+1) - np.log(k) 
        log_pmf_k = b + k * np.log(p) + (n-k) * np.log(1-p)
        cdf += np.exp(log_pmf_k)
    return 1- cdf
def rolling():
    for x in range(dice):
        x=roll(1,6)
        turn.append(x)
    print('your roll is: ',turn)
    for x in range(compdice):
        x=roll(1,6)
        compturn.append(x)
def palifico():
    if (dice==1 or compdice==1) and winpalifico==False:
        return True
    else:
        return False

def get_mode(numbers): #this is to find max. mode, for consideration re: aces call
    counts = {k:numbers.count(k) for k in set(numbers)}
    modes = sorted(dict(filter(lambda x: x[1] == max(counts.values()), counts.items())).keys())
    if modes[-1]==1:
        return modes[-2]
    else:
        return modes[-1]
print('Welcome to Perudo. Here is your roll: ')
dice=5
compdice=5
winpalifico = False
while (dice>0 and compdice>0):
    if palifico() is True:
        print('This is a Palifico Round!')
        dudo = False
        turn=[]
        compturn=[]
        rolling()
        totalturn=compturn+turn
        prevquant=0
        prevnumb=0
        while dudo is False:
            print('prevquant: ',prevquant, 'prevnumb: ',prevnumb)
            if prevquant!=0:
                dudoCall=input('Do you call dudo? (y/n) ')
                if dudoCall=='y':
                    if totalturn.count(prevnumb)-prevquant>=0:
                        print('You rolled: ',turn)
                        print('Computer rolled: ', compturn)
                        print('That means there are ',totalturn.count(prevnumb),prevnumb,'s')
                        print('you lose')
                        dice-=1
                        dudo = True
                    else:
                        print('You rolled: ',turn)
                        print('Computer rolled: ', compturn)
                        print('That means there are ', totalturn.count(prevnumb),prevnumb,'s')
                        print('you win')
                        compdice-=1
                        dudo = True  
                        winpalifico=True
            elif dudoCall=='n':
                try:
                    quant=int(input('what is your call quantity? '))
                    numb=int(input('what is your number call? '))
                except ValueError:
                    print('you have not made a valid choice. please try again and use numbers this time')
                    continue
                if quant<prevquant:
                    print('your call is invalid (higher quantity needed). Please try again')
                    continue
                elif numb!=prevnumb:
                    print('your call is invalid (cannot change number). Please try again')
                    continue
                elif numb>6:
                    print('your call is invalid (can only call 1-6). Please try again')
                    continue
                elif binomial_cdf(quant-compturn.count(numb),len(turn),0.16666666)<0.3:
                    print('Computer calls Dudo')
                    print('total number is: ',totalturn.count(numb))
                    
                    if totalturn.count(numb)-quant>=0:
                        print('You rolled: ',turn)
                        print('Computer rolled: ', compturn)
                        print('That means there are ', totalturn.count(numb),numb,'s')
                        print('you win')
                        compdice-=1
                        dudo = True
                    else:
                        print('You rolled: ',turn)
                        print('Computer rolled: ', compturn)
                        print('That means there are ', totalturn.count(numb),numb,'s')
                        print('you lose')
                        dice-=1
                        dudo = True
            else:
                try:
                    quant=int(input('what is your call quantity? '))
                    numb=int(input('what is your number call? '))
                except ValueError:
                    print('you have not made a valid choice. please try again and use numbers this time')
                    continue
                if binomial_cdf(quant-compturn.count(numb),len(turn),0.1666666666)<0.3:
                    print('Computer calls Dudo')
                    if totalturn.count(numb)-quant>=0:
                        print('You rolled: ',turn)
                        print('Computer rolled: ', compturn)
                        print('That means there are ', totalturn.count(numb),numb,'s')
                        print('you win')
                        compdice-=1
                        dudo = True
                        winpalifico=True
                    else:
                        print('You rolled: ',turn)
                        print('Computer rolled: ', compturn)
                        print('That means there are ', totalturn.count(numb),numb,'s')
                        print('you lose')
                        dice-=1
                        dudo = True 
                else:
                    print('computer is thinking...')
                    print('Computer calls: ',
                                  'quantity: ',quant+1,
                                  'number: ',numb)
                    prevquant=quant+1
                    prevnumb=numb
                    print(prevquant)
    dudo = False
    turn=[]
    compturn=[]
    rolling()
    totalturn=compturn+turn
    prevquant=0
    prevnumb=0
    while dudo is False:
        print('prevquant: ',prevquant, 'prevnumb: ',prevnumb)
        if prevquant!=0:
            dudoCall=input('Do you call dudo? (y/n) ')
            if dudoCall=='y':
                if totalturn.count(prevnumb)+totalturn.count(1)-prevquant>=0:
                    print('You rolled: ',turn)
                    print('Computer rolled: ', compturn)
                    print('That means there are ',totalturn.count(prevnumb),prevnumb,'s')
                    print('and ', totalturn.count(1), 'aces')
                    print('you lose')
                    dice-=1
                    dudo = True
                else:
                    print('You rolled: ',turn)
                    print('Computer rolled: ', compturn)
                    print('That means there are ', totalturn.count(prevnumb),prevnumb,'s')
                    print('and', totalturn.count(1), 'aces')
                    print('you win')
                    compdice-=1
                    dudo = True
            elif dudoCall=='n':
                try:
                    quant=int(input('what is your call quantity? '))
                    numb=int(input('what is your number call? '))
                except ValueError:
                    print('you have not made a valid choice. please try again and use numbers this time')
                    continue
                if quant<prevquant and numb!=1:
                    print('your call is invalid (higher quantity needed). Please try again')
                    continue
                elif quant==prevquant and numb<=prevnumb and numb!=1:
                    print('your call is invalid (higher number needed). Please try again')
                    continue
                elif numb>6:
                    print('your call is invalid (can only call 1-6). Please try again')
                    continue
                elif quant<(prevquant*0.5) and numb==1:
                    print('your call is invalid (aces call must be greater than half the previous call. Please try again')
                    continue
                elif numb==1:
                    favnumb=get_mode(compturn)
                    if binomial_cdf(quant-compturn.count(numb), len(turn), 0.16666666)<0.4:
                        print('Computer calls Dudo')
                        print('total number is: ',totalturn.count(numb))
                        if totalturn.count(numb)-quant>=0:
                             print('You rolled: ',turn)
                             print('Computer rolled: ', compturn)
                             print('That means there are ', totalturn.count(numb),numb,'s')
                             print('you win')
                             compdice-=1
                             dudo = True
                        else:
                            print('You rolled: ',turn)
                            print('Computer rolled: ', compturn)
                            print('That means there are ', totalturn.count(numb),numb,'s')
                            print('you lose')
                            dice-=1
                            dudo = True
                    elif binomial_cdf(quant+1-compturn.count(numb),len(turn), 0.16666666)>=binomial_cdf((2*quant)+1-favnumb,len(turn),0.3333333):
                        print('computer is thinking...')
                        print('Computer calls: ',
                              'quantity: ',quant+1,
                              'number: ',numb)
                        prevquant=quant+1
                        prevnumb=numb
                        print(prevquant)
                    else:
                        print('Computer calls: ',
                              'quantity: ',2*quant+1,
                              'number: ',get_mode(compturn))
                        prevquant=2*quant+1
                        prevnumb=get_mode(compturn)
                        print(prevquant)          
                elif binomial_cdf(quant-compturn.count(numb)-compturn.count(1),len(turn),0.33333333)<0.4:
                    print('Computer calls Dudo')
                    print('total number is: ',totalturn.count(numb))
                    print('total number of aces is: ',totalturn.count(1))
                    if totalturn.count(numb)+totalturn.count(1)-quant>=0:
                        print('You rolled: ',turn)
                        print('Computer rolled: ', compturn)
                        print('That means there are ', totalturn.count(numb)+totalturn.count(1),numb,'s')
                        print('you win')
                        compdice-=1
                        dudo = True
                    else:
                        print('You rolled: ',turn)
                        print('Computer rolled: ', compturn)
                        print('That means there are ', totalturn.count(numb)+totalturn.count(1),numb,'s')
                        print('you lose')
                        dice-=1
                        dudo = True       
                else:
                    print('computer is thinking...')
                    if numb<=5:
                        if binomial_cdf((quant+1)-compturn.count(numb)-compturn.count(1),len(turn),0.3333333)>binomial_cdf(quant-compturn.count(numb+1)-compturn.count(1),len(turn),0.33333333):
                            print('Computer calls: ',
                                  'quantity: ',quant+1,
                                  'number: ',numb)
                            prevquant=quant+1
                            prevnumb=numb
                            print(prevquant, 'line 149')
                        else:
                            print('Computer calls: ',
                              'quantity: ',quant,
                              'number: ',numb+1)
                            prevnumb=numb+1
                            prevquant=quant
                            print(prevnumb, 'line 156')
                    else:
                        print('Computer calls: ',
                              'quantity: ',quant+1,
                              'number: ',get_mode(compturn))
                        prevnumb=get_mode(compturn)
                        prevquant=quant+1
                        print(prevnumb, 'line 163')
        else:
            try:
                quant=int(input('what is your call quantity? '))
                numb=int(input('what is your number call? '))
            except ValueError:
                print('you have not made a valid choice. please try again and use numbers this time')
                continue
            if binomial_cdf(quant-compturn.count(numb)-compturn.count(1),len(turn),0.333333)<0.4:
                print('Computer calls Dudo')
                if totalturn.count(numb)+totalturn.count(1)-quant>=0:
                    print('You rolled: ',turn)
                    print('Computer rolled: ', compturn)
                    print('That means there are ', totalturn.count(numb),numb,'s')
                    print('and there are ', totalturn.count(1), 'aces')
                    print('you win')
                    compdice-=1
                    dudo = True
                else:
                    print('You rolled: ',turn)
                    print('Computer rolled: ', compturn)
                    print('That means there are ', totalturn.count(numb),numb,'s')
                    print('and there are ', totalturn.count(1), 'aces')
                    print('you lose')
                    dice-=1
                    dudo = True 
            else:
                print('computer is thinking...')
                if quant>=0.6*(len(turn)):
                    if binomial_cdf((quant+1)-compturn.count(numb)-compturn.count(1)-int(0.6*(len(turn))),len(turn),0.3333333)>=binomial_cdf(quant-compturn.count(numb+1)-compturn.count(1),len(turn),0.33333333) and quant<6:
                        print('Computer calls: ',
                              'quantity: ',quant+1,
                              'number: ',numb)
                        prevquant=quant+1
                        prevnumb=numb
                    elif binomial_cdf((quant+1)-compturn.count(numb)-compturn.count(1),len(turn),0.33333333)==binomial_cdf(quant-compturn.count(numb+1)-compturn.count(1),len(turn),0.3333333):
                       print('Computer calls: ',
                              'quantity: ',quant+1,
                              'number: ',numb)
                       prevquant=quant+1
                       prevnumb=numb
                    else:
                        print('Computer calls: ',
                              'quantity: ',quant,
                              'number: ',numb+1)
                        prevnumb=numb+1
                        prevquant=quant                      
                else:       
                    if binomial_cdf((quant+1)-compturn.count(numb)-compturn.count(1),len(turn),0.33333333)>=binomial_cdf(quant-compturn.count(numb+1)-compturn.count(1),len(turn),0.33333333) and quant<6:
                        print('Computer calls: ',
                              'quantity: ',quant+1,
                              'number: ',numb)
                        prevquant=quant+1
                        prevnumb=numb
                        print(prevquant)
                    else:
                        print('Computer calls: ',
                              'quantity: ',quant+1,
                              'number: ',get_mode(compturn))
                        prevnumb=get_mode(compturn)
                        prevquant=quant+1            
print('you have reached the end')