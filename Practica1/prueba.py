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

    if (opcion == 1):
        os.system("cls")
        print("\t\t...::: Test to validate grade :::...")
        print("\n\tEquivalence Partitioning(EP)")
        for x in range(0, 3):
            data[x] = int(input("\n\tData test: "))
            er = str(input("\tExpect result: "))
            expectResult[x] = er.upper()
        print("\n\n\tTest Data\tExpect Result\tActual Result\tPass/Fail\n")
        for x in range(0, 3):
            ar, pf = "", ""
            if (funcion.validGrade(data[x]) == expectResult[x]):
                ar = funcion.validGrade(data[x])
                pf = "Pass"
            else:
                ar = funcion.validGrade(data[x])
                pf = "Fail"
            print("\n\t", data[x], "\t\t", expectResult[x], "  \t", ar, "\t", pf)
    if (opcion == 2):
        os.system("cls")
        print("\t\t...::: Test to validate grade :::...")
        print("\n\tBoundary Value Analysis(BVA)")
        for x in range(0, 4):
            data[x] = int(input("\n\tData test: "))
            er = str(input("\tExpect result: "))
            expectResult[x] = er.upper()
        print("\n\n\tTest Data\tExpect Result\tActual Result\tPass/Fail\n")
        for x in range(0, 4):
            ar, pf = "", ""
            if (funcion.validGrade(data[x]) == expectResult[x]):
                ar = funcion.validGrade(data[x])
                pf = "Pass"
            else:
                ar = funcion.validGrade(data[x])
                pf = "Fail"
            print("\n\t", data[x], "\t\t", expectResult[x], "  \t", ar, "\t", pf)
            
    opcion = int(input("\n\n\tDo you want to exit? (3.Yes 4.No): "))