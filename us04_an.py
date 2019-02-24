#from main import *
#print(ind)
#print(family)

def us_04(mar,div,i):   
    if div!='NA' and mar!='NA' and mar!='Invalid' and div!='Invalid':
        if mar[0]>div[0]:
            return "Error US04 in line " + str(div[1]) +":Marriage date occurs after Divorce date in "+ i +" family"
        else:
            return 0
    else:
        if mar=='NA':
            if div=="Invalid":
                return "Warning US04:Marriage date is not given and Divorce date is invalid in "+ i +" family"
            else:
                return "Warning US04:Marriage date is not given in "+ i +" family"
        elif mar=='Invalid':
            if div=="Invalid":
                return "Warning US04:Marriage date and Divorce date is invalid in "+ i +" family"
            else:
                return "Warning US04:Marriage date is invalid in "+ i +" family"
        elif div=='Invalid':
                return "WarningUS04:Divorce date is invalid in "+ i +" family"
        else:
            return 0

def parse_data_04(family):
    for x in family:
        answer=us_04(family[x]['MARR_DATE'],family[x]['DIV_DATE'],x)
        if answer!=0:
            print(answer)