class us_rs:
    
    # UserStory 15
    def siblingCount(family):
        validity = True
        if(type(family) is not (dict)):
            print("Argument isn't an dict")
            validity = False
            return validity
        
        for x, values in family.items():
            
            if values.__contains__("CHIL"):
                length = len(values["CHIL"])    
            else:
                length = 0
            if length > 15:
                validity = False
                
                print("ERROR US15 in line " + str(values['CHIL'][0][1]) + " : There are more than 15 siblings for family. " )
                return validity

          
        return validity


    #Userstory 6 - Divorce can only occur before death of both spouses

    def divorceBeforeDeath(individual, family):
        flag = True
        error = []
        for famid, famvalue in family.items():
            divorceDate = famvalue['DIV_DATE']
            if divorceDate == "NA":
                flag = True
                continue
            divorceDate = divorceDate[0]
            husband = famvalue['HUSB'][0]
            husbandDeath = individual[husband]['DEAT_DATE']
            wife = famvalue['WIFE'][0]
            wifeDeath = individual[wife]['DEAT_DATE']
              
            if(husbandDeath[0] < divorceDate):
                error.append(husbandDeath[1])
                flag = False
            
            print(wife)
            print(wifeDeath)
            if(wifeDeath[0] < divorceDate):
                error.append(str(wifeDeath[1]))
                print(error)
                flag = False
        if(len(error)>0):
            for err in error:
                print("ERROR US_06: Check the Death Day at line number " + err + ". Divorce Date is after the death Day" )
        return flag
                

  


