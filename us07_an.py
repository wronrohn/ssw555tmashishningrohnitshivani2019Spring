def us_07(birth,death,Age,i):
    if Age!='NA' and Age!='Invalid':
        if Age>=150:
            return "Error US07:Age of person is 150 years with "+ i +" id"
        elif Age<0:
            return "Error US07 in line "+ str(birth[1]) + ":Birth date is after death date with "+ i +" id"
        else:
            return 0
    else:
        if birth=='NA':
            if death=="Invalid":
                return "Warning US07:Birth date is not given and Death date is invalid in "+ i +" id"
            else:
                return "Warning US07:Birth date is not given in "+ i +" id"
        elif birth=='Invalid':
            if death=="Invalid":
                return "Warning US07:Birth date and Death date is invalid in "+ i +" id"
            else:
                return "Warning US07:Birth date is invalid in "+ i +" id"
        elif death=='Invalid':
                return "Warning US07:Death date is invalid in "+ i +" id"
        else:
            return 0

def parse_data_07(ind):
    for x in ind:
        answer=us_07(ind[x]['BIRT_DATE'],ind[x]['DEAT_DATE'],ind[x]['AGE'],x)
        if answer!=0:
            print(answer)