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
rows, columns = os.popen('stty size', 'r').read().split() #http://goo.gl/cD4CFf
#"pydoc -p 1234" will start a HTTP server on port 1234, allowing you  to  browse
#the documentation at "http://localhost:1234/" in your preferred Web browser.
cwf = os.path.abspath(inspect.getfile(inspect.currentframe())) # Current Working File
cwfd = os.path.dirname(cwf) # Current Working File Path

#_____________________________________________________________________GlobalVars
lock = threading.Lock()
verbose = False
TriesVar = 1
objctives = 1

#______________________________________________________________________Functions

#pfund(1.602176634*(10**-19), (6.62607015*(10**-34)/(2*math.pi)), 299792458, 6.67430*(10**-11))
def pfund(U_Qe, U_hbar, U_c, U_G): #U_Qe, U_hbar, U_c, U_G
    dlesA = 0.0072973525693
    electronmass = (4.018146716484959*(10**-28)) #print(str((9.1093837015*(10**-31)) / 0.002267060997082957))
    TPW = 1.66218078033717e-18 # = 273.16 / 1.6433832181875484e+20
    MF = (1/1.39e+24)
    LF = ((1/1.39e+24)*299792458)
    TF = (1/1.39e+24)
    QF = (1/1.39e+24)
    unitHbar    = ((MF** 1)*(LF** 2)*(TF**-1)*(QF** 0))
    unitc       = ((MF** 0)*(LF** 1)*(TF**-1)*(QF** 0))
    unitkb      = ((MF** 1)*(LF** 1)*(TF** 0)*(QF**-1)) * 2 * math.pi
    unitUf      = (1 / unitkb)
    unitKe      = ((MF** 1)*(LF** 3)*(TF**-2)*(QF**-2)) * dlesA#(unitHbar * unitc * unitdlesA)/(QF**2)
    unitu0      = ((MF** 1)*(LF** 1)*(TF** 0)*(QF**-2)) * (dlesA*4*math.pi)
    unite0      = ((MF**-1)*(LF**-3)*(TF** 2)*(QF** 2)) * (1/(dlesA*4*math.pi))
    unitrydberg = ((MF**-1)*(LF**-1)*(TF** 0)*(QF** 0)) * (((dlesA**2)*electronmass)/(4*math.pi)) ##$R_{\infty }  m−1$
    unitdlesA   = (unitu0 * unitc *(QF ** 2)) / (4*math.pi*unitHbar)
    print("unitHbar    = " + str(unitHbar    ) + "(M^ 1)*(L^ 2)*(T^-1)*(Q^ 0}")
    print("unitc       = " + str(unitc       ) + "(M^ 0)*(L^ 1)*(T^-1)*(Q^ 0}")
    print("unitkb      = " + str(unitkb      ) + "(M^ 1)*(L^ 1)*(T^ 0)*(Q^-1}")
    print("unitUf      = " + str(unitUf      ) + "(M^ 1)*(L^ 2)*(T^-2)*(Q^ 0}")
    print("unitKe      = " + str(unitKe      ) + "(M^ 1)*(L^ 3)*(T^-2)*(Q^-2}")
    print("unitu0      = " + str(unitu0      ) + "(M^ 1)*(L^ 1)*(T^ 0)*(Q^-2}")
    print("unite0      = " + str(unite0      ) + "(M^-1)*(L^-3)*(T^ 2)*(Q^ 2}")
    print("unitrydberg = " + str(unitrydberg ) + "(M^-1)*(L^-1)*(T^ 0)*(Q^ 0}")
    print("unitdlesA   = " + str(unitdlesA   ) + "(M^ 0)*(L^ 0)*(T^ 0)*(Q^ 0}")
    smoothjazz = (((5/3)*(1.39e+24)*unitkb*TPW*unitUf )/(40.671) )**(1/2)
    print(str(smoothjazz)+" smoothjazz\n")
 # v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v
 ##U_Qe, U_hbar, U_c, U_G HAVE NOT BEEN USED BEFORE THIS POINT
 ## NEED TO FIND DEFINITION OF 5.615737772898213e-39 WITHOUT EXPERIMENTAL DATA IN ORDER TO FIX THIS
 ##U_Qe, U_hbar, U_c, U_G HAVE NOT BEEN USED BEFORE THIS POINT
    #MFG=((((p** 1)*(m**2)*(s**-1)*(q** 0))**1)*unitHbar)*(dlesA**2)
    #print(str(MFG)+" MF G\n")
    #unitG       = 5.615737772898214e-39= ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * (dlesA**2) * U_hbar
 # ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
    #unitkb      = 6.283185307179586     (M^ 1)*(L^ 1)*(T^ 0)*(Q^-1}
    #unitUf      = 0.15915494309189535   (M^ 1)*(L^ 2)*(T^-2)*(Q^ 0}
    #unitKe      = 0.0072973525693       (M^ 1)*(L^ 3)*(T^-2)*(Q^-2}
    #unitu0      = 0.09170123688946993   (M^ 1)*(L^ 1)*(T^ 0)*(Q^-2}
    #unite0      = 10.904978317853313    (M^-1)*(L^-3)*(T^ 2)*(Q^ 2}
    #electronmass = 0.0005585216538561247 MF
    #unitrydberg = 2.366795911858418e-09 (M^-1)*(L^-1)*(T^ 0)*(Q^ 0}
    #unitdlesA   = 0.0072973525693       (M^ 0)*(L^ 0)*(T^ 0)*(Q^ 0}
    #smoothjazz  = 1.0263790404029806e-06 speed sound in argon at triple point of water
    U_m = (U_hbar**(  2/2))*(dlesA**(  2/2))*(U_c**(  1/2))*(U_G**(-1/2))
    p = 1.39e+24 * U_m
    m = (1.39e+24/299792458) * (U_G/((U_c**2)))*U_m*(1/((dlesA**2)*U_hbar)) #((U_hbar * dlesA * U_G)/(U_c**3))**(1/2) 
    s = 1.39e+24 * (U_G/((U_c**3)))*U_m*(1/((dlesA**2)*U_hbar)) #((U_hbar * dlesA * U_G)/(U_c**3))**(1/2) 
    q = 1.39e+24 * U_Qe
 # v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v v
    MFG=((((p** 1)*(m**2)*(s**-1)*(q** 0))**1)*unitHbar)*(dlesA**2)#5.615737772898214e-39
    unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * MFG#5.615737772898214e-39
    print(str(MFG)+" MF G\n")#5.615737772898214e-39
    print("unitG       = " + str(unitG       ) + "(M^-1)*(L^ 3)*(T^-2)*(Q^ 0}") #1.5131045212830784e-13=unitG
 # ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
    print(str(p)+" p  per M")
    print(str(m)+" m per L")
    print(str(s)+" s per T")
    print(str(q)+" q per Q\n")

    unitG       = 1.5131045212830784e-13#= ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * (dlesA**2) * U_hbar
    unitG       = 1.5131045212830784e-13#= ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * (dlesA**2) * unitHbar *0.00226706
    #unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * (dlesA**2) * unitHbar
    #unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * unitHbar * (dlesA**2)
    #mHbar = metricH = 6.62607015*(10**-34)/(2*math.pi)
    #unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * (dlesA**2)
    #unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * (dlesA**2)
    #unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * ((MF**-1)*(LF** 0)*(TF**-1)*(QF** 4)) * (10**-14)
    #unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * ((unitHbar*(unitKe**1)*(QF**1))/((unitc**0.5)))
    #unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * ((MF**1)*(1/ unitc** (3/2))*(TF**-1))*((dlesA**2))
    #unitG       = ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * (dlesA**3) * \
    #(MF** 1)*(LF** 2)*(TF**-1) *U_hbar *(U_c**(  1/2))*(U_G**(-1/2)) * 1.39e+24
    #5.615737772898211e-39 = (dlesA**2) * U_hbar
    unitG       = 1.5131045212830784e-13#= ((MF**-1)*(LF** 3)*(TF**-2)*(QF** 0)) * (dlesA**2) * U_hbar
    print("unitG       = " + str(unitG       ) + "(M^-1)*(L^ 3)*(T^-2)*(Q^ 0}")

    sikb = unitkb*(((p**1)*(m**1)*(s**0)*(q**-1))**1)
    siUf = ((((p**1)*(m**2)*(s**-2))**1)) / sikb
    TPW = 273.16/siUf
    print(str(TPW)+" tpw\n")

    SIh    = (((p** 1)*(m**2)*(s**-1)*(q** 0))**1)*unitHbar
    print(str(SIh)+" SI h\n")

#unitHbar*(unitdlesA**2)
#___________________________________________________________________________Jobs
def percent_display():
    global objctives, TriesVar
    i = 0
    while(i<100):
        with lock:
            i = (objctives/TriesVar)*100
        sys.stdout.write("\rloading... %s%%\n" % i)
        time.sleep(0.06)
    print("\n")

#to avoid globalvars use a list https://stackoverflow.com/a/21700609/144020
    #There are no variables in Python. The key to understanding parameter passing is 
    #to stop thinking about "variables". There are names and objects in Python and 
    #together they appear like variables, but it is useful to always distinguish the 
    #three.
        #1. Python has names and objects.
        #2. Assignment binds a name to an object.
        #3. Passing an argument into a function also binds a name (the parameter name of the function) to an object.

#____________________________________________________________________Main Script
#https://youtu.be/IgqwfvODZIE?list=PLUl4u3cNGP60Do91PdN978llIsvjKW0au

def master():
    print ("This program wasn't called by another python")
    global objctives, TriesVar
    with lock:
        objctives=1
        TriesVar=1
    #rngGenerator = rng.Bitstream("2tacos")

    print("pfund\n") #U_Qe, U_hbar, U_c, U_G
    pfund(1.602176634*(10**-19), (6.62607015*(10**-34)/(2*math.pi)), 299792458, 6.67430*(10**-11))

if __name__ == "__main__":
    threads = [threading.Thread(target=master),
               threading.Thread(target=percent_display)]
    for t in threads:
        t.daemon = True
        t.start()
    for t in threads:
        t.join()
else:
    print ("This program was called by another python")
    pass

exit()

##from http://goo.gl/9XO7sa
#SPObject_Unzip = subprocess.Popen( ['gzip', '-dc', './virtualenv-tmp.tar.gz'],
#	stdin=None, stdout=subprocess.PIPE, stderr=None, cwd=cwfd, env=None)
#SPObject_Untar = subprocess.Popen( ['tar', '-xpvf', '-'],
#	stdin=SPObject_Unzip.stdout, stdout=None, stderr=None, cwd=cwfd, env=None)
#SPObject_Unzip.stdout.close()  # Allow SPObject_Unzip to receive a SIGPIPE if p2 exits.
#SPObject_Untar.wait()
#if (SPObject_Untar.returncode == 0):
#	print "\n\'virtualenv-tmp.tar.gz\' has been unzipped.\n"
#else:
#	print "unzip failed\n"
