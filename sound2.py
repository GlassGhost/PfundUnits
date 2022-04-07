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

electronmass= (9.1093837015*(10**-31))
mc = 299792458
dlesA = 0.0072973525693
def sound(M, L, T, Q):
    unitHbar=((M**1)*(L**2)*(T**-1)*(Q**0))*(mc**2)*((1.39e+24)**-2)
    unitenergy = (M**1)*(L**2)*(T**-2)*(mc**2)*((1.39e+24)**0)
    unitkb=((M**1)*(L**1)*(T**0)*(Q**-1))*2*math.pi*(mc**1)*((1.39e+24)**-1)
    unitUf=((M**1)*(L**2)*(T**-2)*(Q**0))/unitkb
    unitc=((M**0)*(L**1)*(T**-1)*(Q**0))*(mc**1)*((1.39e+24)**0)
    unitdlesA = (((Q**2)*(10**-7))/((M**1)*(L**1)))
    unitKe = ((M**1)*(L**3)*(T**-2)*(Q**-2))*(mc**3)*((1.39e+24)**0)*dlesA
    unitu0 = ((M**1)*(L**1)*(T**0)*(Q**-2))*(mc**1)*((1.39e+24)**0)*(dlesA*4*math.pi)
    unite0 = ((M**-1)*(L**-3)*(T**2)*(Q**2))*(mc**-3)*((1.39e+24)**0)*(1/(dlesA*4*math.pi))
    unitrydberg = ((electronmass*(M**-1))*(L**-1)*(T**0)*(Q**0))*(mc**-1)*((1.39e+24)**2)*((dlesA**2)/(4*math.pi))
    smoothjazz = (((5/3)*(1.39e+24)*unitkb*(273.16/unitUf)*unitUf )/(40.671*M) )**(1/2)
    unitG=((M**-1)*(L**3)*(T**-2)*(Q**0))*(mc**3)*((1.39e+24)**0)
    unitGX = unitHbar*(dlesA**2)

    print(str(M)+" Kg per M\n")
    print(str(L)+" Meters per L\n")
    print(str(T)+" Seconds per T\n")
    print(str(Q)+" Coulumbs per Q\n")
    print( str(unitKe)+"?=?"+"ke\n")
    print( str(unitu0)+"?=?"+"u0\n")
    print( str(unite0)+"?=?"+"e0\n")
    print( str(unitrydberg)+"?=?"+"rydberg\n")

    print( str(unitenergy)+"?=?energy"+" kg⋅m2⋅s−2⋅C0\n")
    print( str(unitkb)+"?=?"+"kg⋅m2⋅s−1⋅C0=kb\n")
    print( str(unitHbar)+"?=?"+"kg⋅m2⋅s−1⋅C0=hbar\n")
    print( str(unitc)+"?=?"+str(mc)+"kg0⋅m1⋅s−1⋅C0\n")
    print( str((1.39e+24))+"?=?"+"N_A\n")
    print(str(smoothjazz)+" smoothjazz\n")
    print(str((unitUf))+" temp\n")
    print( str(unitG * unitGX)+"?=?"+"extrakg0⋅m1⋅s−1⋅C0\n")

sound(0.002267060997082957, 1, 1, 222702.25716748508)
