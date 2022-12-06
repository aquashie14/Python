#This code shows the anaemia diagnosis in males
#Hb-haemoglobin count 
#MCV-Mean corpiscular volume in percentage
#RC-Reticulocyte count 
#RBC-Red blood cells count 


H =float(input("Enter the hermatocrit of the patient: "))
RBC =float(input("Enter the rbc of the patient: "))
R =float(input("Enter the reticulocycte in the rbc of the patient: "))

#Compute
MCV = (Hct * 10) / RBC
Hb = (MCV * RBC) / 29.8
RC = (R * 100) / 1000

time.sleep(6.0)
print("Analysing...")

#Diagnosis
if (Hb < 14.0 and RC < 0.2 and MCV < 80):
    print("Your MCV is low and the anaemia is due to the following; \n Iron deficiency secondary chronic blood loss \n Thalassemia")
elif (Hb < 14.0 and RC < 0.2 and 80 <= MCV <= 100):
    print("Your MCV is normal and the anaemia is due to the following; \n ACD \n Antiviral drugs \n Tumor in bone marrow \n Infection in bone marrow")
elif (Hb < 14.0 and RC < 0.2 and MCV > 100):
    print("Your MCV is high and the anaemia is due to the following; \n Medications \n Cancer chemotherapy \n B12 deficiency \n Folic acid deficiency \n Myelodysplasia \n Alcohol abuse \n Liver disease")
else:
    print("Diagnosis yet to be determined")
