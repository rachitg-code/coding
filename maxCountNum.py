def numFreq(lst):
    track={}
    for i in lst:
        if i in track:
            track[i]=track[i]+1
        else:
            track[i]=1
    return track


def maxCountNum(lst):
    vM=-1
    vMn=-1
    dct=numFreq(lst)
    print(dct)
    for i in dct:
        if dct[i] > vM:
            print(str(vMn) +" has freq "+ str(vM)+" but "+str(i)+" has freq "+str(dct[i]))
            vM=dct[i]
            vMn=i
    
    print(str(vMn) +" has freq "+ str(vM))


maxCountNum([2,3,4,8,8,5,2,4,8,7])