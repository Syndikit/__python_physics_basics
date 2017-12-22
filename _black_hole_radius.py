# A program to find how much you have shrink to become a black hole.
# This also finds required black hole radius for any object.

from math import sqrt


c=299792458.00000#velcity of light
G=6.67e-11#Universal Gravital Constant
rad_of_H=5.29e-11#Radius of Hydrogen Atom
rad_of_electron=2.8179e-15#Raius of Electron
rad_of_Down_quark=4.3e-20#Radius of Down Quark

def escape_velcity(M, R): #Checks the escape velcity with schwartzhild radius
    _escape_velcity=sqrt((2*G*M)/R)
    return _escape_velcity


def s_radius(M): #Finds the required Schwartzchilds radius
    _radius=((2*M*G)/(c*c))
    return _radius


def atom_compare(radius):#this checks the ratio of schwartzhildradius with radius of Hydrogen atom
    size=rad_of_H/radius
    return size

def quark_compare(radius): # This checks the ratio of Black hole radius of mass with quark.
    size=rad_of_Down_quark/radius
    return size

def electron_compare(radius): #This checks the ratio of Black hole radius with electron.
    size = rad_of_electron/radius
    return size



def planet_check(Mass):#This checks if the user entered planet or custom mass
    if (Mass.lower() == "earth"):
        new_Mass = 5.97219e24
    elif (Mass.lower() == "mars"):
        new_Mass = 0.64171e24
    elif (Mass.lower == "moon"):
        new_Mass = 7.3476739e22
    else:
        new_Mass = float(Mass)

    return new_Mass



def main():

    Mass=input("Enter the mass for the object(Enter Earth or name of planet for planets)")
    new_Mass=planet_check(Mass)


    _s_rad=s_radius(new_Mass)#Finding Black hole radius.


    light_scape=escape_velcity(new_Mass,_s_rad)


    print("The radius required to be black hole is : " + str(_s_rad))

    if (Mass.lower() != "earth" and Mass.lower() != "mars" and Mass.lower != "moon"):
        comp1 = atom_compare(_s_rad)
        comp2=electron_compare(_s_rad)
        comp3=quark_compare(_s_rad)

        print("You are " + str(comp1) + " times smaller than hydrogen atom. ")
        print("You are " + str(comp2) + " times smaller than electron. ")
        print("You are " + str(comp3) + " times smaller than Down Quark. ")

    print("The escape velcity must be"+str(light_scape))
    if(light_scape==c):
        print("Light can not escape.")
    else:
        print("Calculation error.")

main()
