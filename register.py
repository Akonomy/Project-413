#FILES TEXT STIIL ON LOGS

with open("card.txt","rt") as hjkg:
    lines=hjkg.readlines()
        
lines[1]="568\n"

with open("card.txt","wt") as po:
    po.writelines(lines)
    
po.close()    
    
    