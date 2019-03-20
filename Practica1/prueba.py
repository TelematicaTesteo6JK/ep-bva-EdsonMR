import os
import string
import funcion

opcion = 0

while opcion != 3:
    data = [0, 0, 0, 0] # Save data
    expectResult = ["", "", "", ""] # Save expect result for each data

    os.system("cls")
	# print("\t\t...::: Test to validate grade :::...")
    print("\n\t1. Equivalence Partitioning(EP)\n\t2. Boundary Value Analysis(BVA)")
    opcion = int(input("\n\tChoose one technique: "))

    if (opcion == 1): # Opcion EP
        os.system("cls")
        print("\t\t...::: Test to validate grade :::...")
        print("\n\tEquivalence Partitioning(EP)")
        for x in range(0, 3): # for to receive each data and his expected result
            data[x] = int(input("\n\tData test: ")) # save data in the list
            er = str(input("\tExpect result: "))
            expectResult[x] = er.upper() # use upper and save in the list
        
        # create a file.txt
        fEP = open("testEP.txt", "w")
        fEP.write("\t\t...::: Test to validate grade :::...")
        fEP.write("\n\n\t\tEquivalence Partitioning(EP)")
        fEP.write("\n\n\tTest Data\tExpect Result\tActual Result\tPass/Fail\n")

        print("\n\n\tTest Data\tExpect Result\tActual Result\tPass/Fail\n")
        for x in range(0, 3):
            ar, pf = "", ""
            if (funcion.validGrade(data[x]) == expectResult[x]):
                ar = funcion.validGrade(data[x])
                pf = "Pass"
            else:
                ar = funcion.validGrade(data[x])
                pf = "Fail"

            strEP = "\n\t" + str(data[x]) + "\t\t" + str(expectResult[x]) + "  \t" + ar + "\t" + pf
            fEP.write(strEP)    # Write in the text file
            
            print("\n\t", data[x], "\t\t", expectResult[x], "  \t", ar, "\t", pf)
        
        fEP.close() # close fEP
    
    elif (opcion == 2): # Opcion BVA
        os.system("cls")
        print("\t\t...::: Test to validate grade :::...")
        print("\n\tBoundary Value Analysis(BVA)")
        for x in range(0, 4):
            data[x] = int(input("\n\tData test: "))
            er = str(input("\tExpect result: "))
            expectResult[x] = er.upper()

        # create a file.txt
        fBVA = open("testBVA.txt", "w")
        fBVA.write("\t\t...::: Test to validate grade :::...")
        fBVA.write("\n\n\t\tBoundary Value Analysis(BVA)")
        fBVA.write("\n\n\tTest Data\tExpect Result\tActual Result\tPass/Fail\n")

        print("\n\n\tTest Data\tExpect Result\tActual Result\tPass/Fail\n")
        for x in range(0, 4):
            ar, pf = "", ""
            if (funcion.validGrade(data[x]) == expectResult[x]):
                ar = funcion.validGrade(data[x])
                pf = "Pass"
            else:
                ar = funcion.validGrade(data[x])
                pf = "Fail"

            strBVA = "\n\t" + str(data[x]) + "\t\t" + str(expectResult[x]) + "  \t" + ar + "\t" + pf
            fBVA.write(strBVA)    # Write in the text file

            print("\n\t", data[x], "\t\t", expectResult[x], "  \t", ar, "\t", pf)

        fBVA.close()    # close fBVA
            
    opcion = int(input("\n\n\tDo you want to exit? (3.Yes 4.No): "))