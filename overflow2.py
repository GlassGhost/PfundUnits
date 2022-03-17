#!/usr/bin/env python3
# coding=utf-8
#________________________________________________________________________LICENSE
#	Copyright © 2022 Roy Pfund. All rights reserved.
#
#	Licensed under the Apache License, Version 2.0 (the  "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable  law  or  agreed  to  in  writing,
#	software distributed under the License is distributed on an  "AS
#	IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,  either
#	express or implied. See the License for  the  specific  language
#	governing permissions and limitations under the License.
#__________________________________________________________________DOCUMENTATION
'''overflow.py
I know how to count to schfiftyfive
'''#_____________________________________________________________Library Imports
import time, subprocess, threading, re, os, sys, inspect, shutil, argparse, random, math
rows, columns = os.popen('stty size', 'r').read().split() #http://goo.gl/cD4CFf
#"pydoc -p 1234" will start a HTTP server on port 1234, allowing you  to  browse
#the documentation at "http://localhost:1234/" in your preferred Web browser.
cwf = os.path.abspath(inspect.getfile(inspect.currentframe())) # Current Working File
cwfd = os.path.dirname(cwf) # Current Working File Path

#_____________________________________________________________________GlobalVars

G = 6.67430*(10**-11)
Qe = 1.602176634*(10**-19)
c = 299792458.0
h = 6.62607015*(10**-34)
hbar = h/(2*math.pi)
dlesA = 0.0072973525693
#dlesA = (c*(mQe**2)*(10**-7))/mHbar
#dlesA = (Qe**(   2))*(hbar**(  -1))*(mc**(   1))*(10**-7)
avogadro = (6.02214076*(10**26))
u0 = (1.256637*(10**-6))
e0 = (8.854187*(10**-12))

metricKe = (hbar * c * dlesA)/(Qe**2)
neutronmass= (1.67493*(10**-27))
protonmass= (1.67262*(10**-27))
electronmass= (9.1093837015*(10**-31))
#rydberg = 10973731.568160 ##$R_{\infty }  m−1$
rydberg = (((dlesA**2)*electronmass*c)/(4*math.pi*hbar)) ##$R_{\infty }  m−1$

#MF approx.= 1.6309812938532615e-27 Kg
MF = (Qe**( 4/2))*(c**( 3/2))*(G**(-1/2))*((10**-7)**(   1))
LF = hbar/(   c  *  MF)
TF = hbar/((c**2) * MF)

#______________________________________________________________________Functions
def constant(M, L, T, Q):
    unitHbar=((M**1)*(L**2)*(T**-1)*(Q**0))
    unitkb=((M**1)*(L**1)*(T**0)*(Q**-1))*2*math.pi
    unitUf=((M**1)*(L**2)*(T**-2)*(Q**0))/unitkb
    unitc=((M**0)*(L**1)*(T**-1)*(Q**0))
    unitG=((M**-1)*(L**3)*(T**-2)*(Q**0))
    #unitdlesA = ((unitc*(Q**2))/unitHbar)*(10**-7)
    unitdlesA = (((Q**2)*(10**-7))/((M**1)*(L**1)))
    unitKe = (unitHbar * unitc * unitdlesA)/(Q**2)
    unitGX = unitHbar*(unitdlesA**2)
    unitrydberg = (((unitdlesA**2)*electronmass*((M**-1)*(L**-1)*(T**0)*(Q**0)))/(4*math.pi)) ##$R_{\infty }  m−1$
    #unit2rydberg = (((unitdlesA**2)*electronmass*unitc)/(4*math.pi*unitHbar)) ##$R_{\infty }  m−1$
    #((M**1)*(L**3)*(T**-2)*(Q**-2))
    print(str(M)+" Kg per M\n")
    print(str(L)+" Meters per L\n")
    print(str(T)+" Seconds per T\n")
    print(str(Q)+" Coulumbs per Q\n")
    print( str(unitHbar)+"?=?"+str(hbar)+"kg⋅m2⋅s−1⋅C0\n")
    print( str(unitkb)+"?=?"+str(55)+"kg⋅m2⋅s−1⋅C0\n")
    print( str(unitc)+"?=?"+str(c)+"kg0⋅m1⋅s−1⋅C0\n")
    print( str(unitG)+"?=?"+str(G)+"kg0⋅m1⋅s−1⋅C0\n")
    united = (Q**(   4))*(unitHbar**(  -1))*(unitc**(   2))*((10**-7)**(   2))
    unitR = unitHbar*unitc#(Q**(   4))*(M**(  -1))*(T**(  -1))*((10**-7)**(   2))
    print( str(unitG * unitGX)+"?=?"+str(G)+"extrakg0⋅m1⋅s−1⋅C0\n")
    #print( str(unitG * ((M**2)/(mc*mHbar)))+"?=?"+str(mG)+"extrakg0⋅m1⋅s−1⋅C0\n")
    testKe = ((L**2)*(T**-2)*(10**-7))
    #print(str(testKe)+" TestKe per Q\n")
    print( str((M**1)*(L**2)*(T**-2)*(Q**0))+"?=?energy"+" kg⋅m2⋅s−2⋅C0\n")
    print( str((M**1)*(L**2)*(T**-2)*(Q**-1))+"?=?eV"+" kg⋅m2⋅s−2⋅C-1\n")
    print( str((M**1)*(L**3)*(T**-2)*(Q**-2))+"?=?"+str(metricKe)+" kg⋅m3⋅s−2⋅C−2\n")
    print( str((M**1)*(L**1)*(T** 0)*(Q**-2))+"?=?"+str(u0)+" kg⋅m⋅s0⋅C−2\n")
    print( str((M**1)*(L**1)*(T** 0)*(Q**-2)*unitdlesA*4*math.pi)+"?=?"+str(u0)+" kg⋅m⋅s0⋅C−2\n")
    print( str((M**-1)*(L**-3)*(T** 2)*(Q**2)*(1/(4*math.pi*dlesA)))+"?=?"+str(e0)+" x10-12 kg⋅m⋅s0⋅C−2\n")
    print( str(unitrydberg)+"?=?"+str(rydberg)+"rydberg kg⋅m-1⋅s0⋅C−2\n")
    temper = (L*Q)/((T**2)*2*math.pi)
    #temp = ((273.16/(M*39.946))*((avogadro * M)/(temper))*(((L**2)*M)/(T**2))*(5/3))**(1/2)
    temp = ((273.16/(M*39.946*(1/avogadro)))*((1 * M)/(temper))*(((L**2)*M)/(T**2))*(5/3))**(1/2)
    print(str(temp)+" test\n")
    smoothjazz = (((5/3)*1*unitkb*(273.16/unitUf)*unitUf )/(40.671*M) )**(1/2)
    print(str(smoothjazz)+" smoothjazz\n")
    print( str((unitdlesA)**1)+"?=?"+str((dlesA)**1)+" dlesA\n")
    #print( str(Q*((unitc*(10**-7))/unitHbar)**0.5)+"?=?"+str(mQe*((mc*(10**-7))/mHbar)**0.5)+" sqrtdlesA\n")
    print(str(avogadro * M)+" avogadro\n")
    #dlesA^0.5=Q*((unitc*(10**-7))/unitHbar)^0.5
    #print(str(dlesA )+" dlesA\n")
    devil = c / L
    print(str(devil)+" Devil\n")
    print(str(M*devil)+" Kg per M\n")
    print(str(L*devil)+" Meters per L\n")
    print(str(T*devil)+" Seconds per T\n")
    print(str(Q*devil)+" Coulumbs per Q\n")


#____________________________________________________________________Main Script
if __name__ == "__main__":
    constant(MF, LF, TF, Qe)
else:
    print ("This program was called by another python")
    pass
