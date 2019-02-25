#from main import *
#print(ind)
#print(family)

def us_04(mar,div,i):   
    if div!='NA' and mar!='NA' and mar[0]!='Invalid' and div[0]!='Invalid':
        if mar[0]>div[0]:
            return "Error US04 in line " + str(div[1]) +" or line "+ str(mar[1])+":Marriage date occurs after Divorce date in "+ i +" family"
        else:
            return 0
    else:
        return 0

def parse_data_04(family):
    for x in family:
        answer=us_04(family[x]['MARR_DATE'],family[x]['DIV_DATE'],x)
        if answer!=0:
            print(answer)