from random import *
from system import *
import time

reasons = ["Physical Injury", "Viruses", "Intoxications", "Inspection", "Surgery", "Cosmetic Surgery", "Check-Up", "Medication", "Other"]
doctors = ["Dr. Ahmet Zere", "Dr. Mehmet Karakum", "Dr. R.Ferruh Ilter", "Dr. Mustafa Selek", "Dr. A.Oguz Tezcan"]
degree = ["Normal Degree (*)", "High Degree (**)", "Fatal Degree (***)"]

print("\n*** Hospital Registration Process ***")

pName = str(input("Patient's Name: "))
time.sleep(0.3)
pSurname = str(input("Patient's Surname: "))
time.sleep(0.3)
pAge = int(input("Patient's Age: "))
time.sleep(0.3)

print("\n*** Hospitalization Reason ***")
for i in range(len(reasons)):
    print("{}) {}".format(i, reasons[i]))

pReason = int(input("Reason: "))
pReason = reasons[pReason]
time.sleep(0.3)

pDegree = int(input("\n*** Enter The Reason Degree *** \n1){} \n2){} \n3){} \nDegree: ".format(degree[0], degree[1], degree[2])))

x = Patient(pName, pSurname, pAge, pReason, pDegree)

movementsStr = ["Get Patient's Info", "Change Reason Degree", "Change Admin Doctor", "Add Hospitalization Duration", "Discharging The Patient"]
movements = [x.getInfo, x.cDegree, x.cAdminDR, x.addHD, x.discharge]

while x.isActive == True:
    time.sleep(0.5)
    print("\n*** Movements ***")
    for i in range(0, len(movementsStr)):
        print("{}) {}".format(i, movementsStr[i]))
    selection = int(input("Move:"))
    time.sleep(0.5)
    movements[selection]()
    