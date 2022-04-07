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
'''
I know how to count to schfiftyfive
'''
#________________________________________________________________Library Imports
import time, subprocess, threading, re, os, sys, inspect, shutil, argparse, random, math

electronmass = (9.1093837015*(10**-31))
mc = 299792458
dlesA = 0.0072973525693
p=0.002267060997082957
q=222702.25716748508
TPW=1.6621807803371769e-18 # = 273.16 / 1.6433832181875484e+20

def sound(M, L, T, Q, convolved=1):
    unitHbar=(mc**2)*((1.39e+24)**-2)*(((M**1)*(L**2)*(T**-1)*(Q**0))**convolved)
    unitenergy = (mc**2)*((1.39e+24)**0)*(((M**1)*(L**2)*(T**-2))**convolved)
    unitkb=2*math.pi*(mc**1)*((1.39e+24)**-1)*(((M**1)*(L**1)*(T**0)*(Q**-1))**convolved)
    unitUf= ((((M**1)*(L**2)*(T**-2))**convolved)) / unitkb
    unitc = (mc**1)*((1.39e+24)**0)*(((M**0)*(L**1)*(T**-1)*(Q**0))**1)
    unitKe = (mc**3)*((1.39e+24)**0)*dlesA*(((M**1)*(L**3)*(T**-2)*(Q**-2))**convolved)
    unitu0 = (mc**1)*((1.39e+24)**0)*(dlesA*4*math.pi)*(((M**1)*(L**1)*(T**0)*(Q**-2))**convolved)
    unite0 = (mc**-3)*((1.39e+24)**0)*(1/(dlesA*4*math.pi))*(((M**-1)*(L**-3)*(T**2)*(Q**2))**convolved)
    unitqe = ((1.39e+24)**-1)*((Q**1)**convolved)
    unitG=(((M**-1)*(L**3)*(T**-2)*(Q**0))**convolved)*(mc**3)*((1.39e+24)**0)*unitHbar*(dlesA**2)
    unitdlesA = (unitu0 * unitc *(unitqe ** 2)) / (4*math.pi*unitHbar)
    unitrydberg = (mc**-1)*((1.39e+24)**2)*((dlesA**2)/(4*math.pi))*electronmass*(((L**-1)*(T**0)*(Q**0))**convolved)#*(M**-1)#unitrydberg
    smoothjazz = (mc**0)*(((5/3)*((1.39e+24)**1)*unitkb*TPW*unitUf )/(40.671*(M**convolved)) )**(1/2)

    print( str(unitqe)+"?=?"+"qe\n")
    print( str(unitKe)+"?=?"+"ke\n")
    print( str(unitu0)+"?=?"+"u0\n")
    print( str(unite0)+"?=?"+"e0\n")
    print( str(unitrydberg)+"?=?"+"rydberg\n")
    print( str(unitenergy)+"?=?energy"+" kg⋅m2⋅s−2⋅C0\n") #(8.987551787368176e+16)×(0.00226701)
    print( str(unitkb)+"?=?"+"kg⋅m2⋅s−1⋅C0=kb\n")
    print( str(unitHbar)+"?=?"+"kg⋅m2⋅s−1⋅C0=hbar\n")
    print( str(unitc)+"?=?"+str(mc)+"kg0⋅m1⋅s−1⋅C0\n")
    print( str(unitdlesA)+"?=?"+"unitdlesA\n")
    print( str(unitG)+"?=?"+"G \n")
    print( str((1.39e+24))+"?=?"+"N_A \n")
    print( str(unitUf)+"?=?"+"Uf \n")
    print(str(smoothjazz)+" smoothjazz\n")

    #https://sciencenotes.org/coulombs-law-example-problem/
    print( str(unitKe * (((0.000001 / q)**2) / (0.01**2)))+"?=?"+"force 39644×0.002267061 = 90N \n")
    print( str(273.16/unitUf)+"?=?"+"3xwater\n")

    print(str(M)+" M per ?\n")
    print(str(L)+" Meters per L\n")
    print(str(T)+" Seconds per T\n")
    print(str(Q)+" Q per ?\n")

sound(0.002267060997082957, 1, 1, 222702.25716748508)
electronmass = (4.018146716484959*(10**-28)) #print(str((9.1093837015*(10**-31)) / 0.002267060997082957))
sound((1/0.002267060997082957), 1, 1, (1/222702.25716748508), convolved=-1)
sound(1, 1, 1, 1)


    #mp = (((unitHbar * unitc) / unitG)**0.5)
    #lp = mp * (unitG / unitc**2)
    #tp = mp * (unitG / unitc*3)
    #TP = (unitqe*lp)/(2*math.pi*(tp**2))
