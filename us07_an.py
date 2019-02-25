def us_07(birth,death,Age,i):
    if Age!='NA' and Age!='Invalid':
        if Age>=150:
            if death!='NA':
                return "Error US07 in line "+ str(birth[1]) +" or line "+ str(death[1])+":Age of person is 150 years with "+ i +" id"
            else:
                return "Error US07 in line "+ str(birth[1]) +":Age of person is 150 years with "+ i +" id"
        else:
            return 0
    else:
        return 0

def parse_data_07(ind):
    for x in ind:
        answer=us_07(ind[x]['BIRT_DATE'],ind[x]['DEAT_DATE'],ind[x]['AGE'],x)
        if answer!=0:
            print(answer)
    return 0