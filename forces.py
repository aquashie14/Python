#This code will helps us compare two forces given some parameters
# m and M are mass of the body and earth respectively
# R and r are the radii of the body and the earth respectively
# v is the velocity of the body

m = float(input("Enter the mass of the body: "))
r = float(input("Enter the radius of the body: "))
v = float(input("Enter the velocity of the body: "))
G = 6.67 * (10**-11)
M = 5.92 *(10**24)
R = 6.37 *(10**6)


# Compute the forces
C_force = (m * (v**2)) / r
G_force = (G * m * M) / (R**2)

# compare the the forces 
if (C_force == G_force):
    print ("The two forces are equal")
else:
    print("The forces are not equal")
