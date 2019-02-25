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

  


