from random import *

reasons = ["Physical Injury", "Viruses", "Intoxications", "Inspection", "Surgery", "Cosmetic Surgery", "Check-Up", "Medication", "Other"]
doctors = ["Dr. Ahmet Zere", "Dr. Mehmet Karakum", "Dr. R.Ferruh Ilter", "Dr. Mustafa Selek", "Dr. A.Oguz Tezcan"]
degree = ["Normal Degree (*)", "High Degree (**)", "Fatal Degree (***)"]

class Patient:
    def __init__(self, name, surname, age, reason, degreeRatio, isActive=True):
        print("\n*** Patient Registery Successful! ***")
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.age = age
        self.reason = reason
        self.pDegree = degree[degreeRatio - 1]
        self.degreeRatio = degreeRatio
        self.adminDR = doctors[randrange(0, 2)]
        self.isActive = isActive

        if self.degreeRatio == 1:
            self.hDuration = 5
        elif self.degreeRatio == 2:
            self.hDuration = 12
        else:
            self.hDuration = 20

    def getInfo(self):
        print("\n*** Patient Informations ***")
        print("Name: {} \nSurname: {} \nAge: {} \nReason: {} \nReason Degree: {} \nHospitalization Duration: {} Days \nAdminastor Doctor: {}".format(self.name, self.surname, self.age, self.reason, self.pDegree, self.hDuration, self.adminDR))
        input("<-- Press Any Key For Go Back!")

    def discharge(self):
        print("\n*** Patient Discharge Process ***")
        auth = str(input("Are You Sure About Patient Discharging Process? (Y/N) \nAnswer: "))
        if auth.lower() == "y":
            pSignature = randrange(10000, 99999)
            cSignature = int(input("Enter The Patient's Signature Please! ({}) \nSignature: ".format(pSignature)))
            if cSignature == pSignature:
                print("Signature is Correct Discharge Successful!")
                print("Thanks For Selected To Us!..")
                self.isActive = False
                input("<-- Press Any Key For Go Back!")
            else:
                print("Discharge Process Canceled!")
                input("<-- Press Any Key For Go Back!")
        else:
            print("Discharge Process Canceled!")
            input("<-- Press Any Key For Go Back!")

    def cDegree(self): ## Degree Change Process Doesn't Change The Admin Doctor!
        print("\n*** Reason Degree Change Process ***")
        newD = int(input("\n*** Enter The New Reason Degree *** \n1){} \n2){} \n3){} \nDegree: ".format(degree[0], degree[1], degree[2])))
        self.degreeRatio = newD
        self.pDegree = degree[newD - 1]
        if newD == 1:
            self.hDuration = 5
        elif newD == 2:
            self.hDuration = 12
        else:
            self.hDuration = 20
        input("<-- Press Any Key For Go Back!")
        
    def cAdminDR(self):
        print("\n*** Admin Doctor Change Process ***")
        print("Your Active Admin Doctor: ",self.adminDR)
        print("\n*** Doctors ***")
        for i in range(len(doctors)):
            print("{}) {}".format(i, doctors[i]))

        drNum = int(input("Enter New Doctor's Number \nNumber: "))
        if self.adminDR == doctors[drNum]:
            print("You Selected Same Doctor!")
            input("<-- Press Any Key For Go Back!")
        else:
            self.adminDR = doctors[drNum]
            print("Admin Doctor Changed As {}".format(self.adminDR))
            input("<-- Press Any Key For Go Back!")

    def addHD(self):
        print("\n*** Hospitalization Duration Appending Process ***")
        amount = int(input("Enter The Append Amount \nAmount:"))
        self.hDuration += amount
        print("New Hospitalization Duration: {} Days".format(self.hDuration))
        input("<-- Press Any Key For Go Back!")
    
