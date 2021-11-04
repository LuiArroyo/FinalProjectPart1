# Luis Arroyo
# PSID: 2037081
# CIS 2348

#default to fetch
import csv
import datetime
from operator import itemgetter

#preparing lists
manufacturerlist=[]
pricelist=[]
servicedateslist=[]

#pulling data from csv files, with statement closes file once done
with open('ManufacturerList.csv') as manulist:
    manlist=csv.reader(manulist)
    for line in manlist:
        manufacturerlist.append(line)
with open('PriceList.csv') as prilist:
    prlist=csv.reader(prilist)
    for line in prlist:
        pricelist.append(line)
with open('ServiceDatesList.csv') as servlist:
    slist=csv.reader(servlist)
    for line in slist:
        servicedateslist.append(line)

#sort the lists by Order ID, use itemgetter
update_manufacturerlist=(sorted(manufacturerlist, key=itemgetter (0)))
update_pricelist=(sorted(pricelist, key=itemgetter (0)))
update_servicedateslist=(sorted(servicedateslist, key=itemgetter (0)))

#inserting pricelist and servicelist to manufacturinglist before the damaged column
for update in range (0, len(update_manufacturerlist)):
    update_manufacturerlist[update].insert(3, pricelist[update][1])
for update in range (0, len(update_manufacturerlist)):
    update_manufacturerlist[update].insert(4, servicedateslist[update][1])

#newest manufacture
newestlist=manufacturerlist
fullinventory=(sorted(newestlist, key=itemgetter(1)))

#write FullInventory using w command if file does not exist
with open('FullInventory.csv', 'w') as masterfile:
    write=csv.writer(masterfile)
    for f in range (0, len(fullinventory)):
        write.writerow(fullinventory[f])

#inventory list by the three item types
laptoponly=[]
phoneonly=[]
toweronly=[]

#finding each item type in the 2nd column of FullInventory
for f in range(0, len(fullinventory)):
    if fullinventory[f][2]=='laptop':
        laptoponly.append(fullinventory[f])
    elif fullinventory[f][2]=='phone':
        phoneonly.append(fullinventory[f])
    elif fullinventory[f][2]=='tower':
        toweronly.append(fullinventory[f])

#writing new files for items
with open('LaptopInventory.csv', 'w') as llist:
    write=csv.writer(llist)
    for f in range (0, len(laptoponly)):
        write.writerow(laptoponly[f])
with open('PhoneInventory.csv', 'w') as plist:
    write=csv.writer(plist)
    for f in range (0, len(phoneonly)):
        write.writerow(phoneonly[f])
with open('TowerInventory.csv', 'w') as tlist:
    write=csv.writer(tlist)
    for f in range (0, len(toweronly)):
        write.writerow(toweronly[f])

#preparing past service date list
pastsdlist=[]
today = datetime.date.today()
todayreal = today.strftime("%m/%d/%Y").replace('/0', '/')

#finding date in file
for f in range(0, len(fullinventory)):
    testdate = fullinventory[f][4]
    # testdate = datetime.date.fullinventory[f][4] <-test dummy code
    if fullinventory[f][4] <= todayreal:
        pastsdlist.append(fullinventory[f])
pastsdlist=(sorted(pastsdlist, key=itemgetter(4), reverse=True))

#writing pastdate file
with open('PastServiceDateInventory.csv', 'w') as psdfile:
    write=csv.writer(psdfile)
    for f in range (0, len(pastsdlist)):
        write.writerow(pastsdlist[f])

#preparing damaged list
damagedlist=[]

#finding damage in file
for f in range(0, len(fullinventory)):
    if fullinventory[f][5] == "damaged":
        damagedlist.append(fullinventory[f])
damagedlist=(sorted(damagedlist, key=itemgetter(3), reverse=True))

#writing damaged file using w function
with open('DamagedInventory.csv', 'w') as dfile:
    write=csv.writer(dfile)
    for f in range (0, len(damagedlist)):
        write.writerow(damagedlist[f])
# print(todayreal) <- dummy test code
# print (testdate) <- dummy test code