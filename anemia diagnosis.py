#This code shows the anaemia diagnosis in males
#Hb-haemoglobin count 
#MCV-Mean corpiscular volume in percentage
#RC-Reticulocyte count 
#RBC-Red blood cells count 


H =float(input("Enter the hermatocrit of the patient: "))
RBC =float(input("Enter the rbc of the patient: "))
R =float(input("Enter the reticulocycte in the rbc of the patient: "))

#Compute
MCV = (H * 10) / RBC
Hb = (MCV * RBC) / 29.8
RC = (R * 100) / 1000

#Diagnosis
if (Hb < 14.0):
    print("Hb is low")
elif (RC < 0.05):
    print("RC is also low check MCV")
elif (MCV < 95):
    print("Iron deificiency secondary leading to chronic blood loss")
    print("Thalassemia")
elif(95 <= MCV <= 100):
    print("ACD")
    print("Antiviral drugs")
    print("Tumor in the bone marrow")
    print("Infection in the bone marrow")
elif(MCV > 100):
    print("MCV high")
    print("Medications")
    print("liver disease")
    print("Cancer chemotherapy")
else:
    print("I do not know diagnosis")
