#!/usr/bin/env/python3
#-*- coding: utf-8 -*-
import os
import subprocess
from termcolor import *

banner = """
 ▄▄▄· ·▄▄▄▄  ▄▄▄▄· ▄• ▄▌.▄▄ ·  ▄▄▄· ·▄▄▄▄        ▄▄▄  
▐█ ▀█ ██▪ ██ ▐█ ▀█▪█▪██▌▐█ ▀. ▐█ ▀█ ██▪ ██ ▪     ▀▄ █·
▄█▀▀█ ▐█· ▐█▌▐█▀▀█▄█▌▐█▌▄▀▀▀█▄▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄ 
▐█ ▪▐▌██. ██ ██▄▪▐█▐█▄█▌▐█▄▪▐█▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█•█▌
 ▀  ▀ ▀▀▀▀▀• ·▀▀▀▀  ▀▀▀  ▀▀▀▀  ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀
                               Krypton Security
"""
print(banner)

modulos = """[1] Mostrar Dispositivos\n
[2] Instalar una apk \n
[3] Tomar ScreenShot\n
[4] Abrir una shell\n
[5] Salir\n
Selecciona una opcion: """ 

dispositivo = """
WMMNkc;oXMMMMMM
WKdl;. .cKMMMMMM
O, .',.  ;0WWMMMM
o.   ';. .oKNMMMMM
x.   .cxxONWMMMMMMM
K;   'kMMMMMMMMMMMMM
Wk'  .kWMMMMMMMMMMMMM
MWx.  ;0MMMMMMMMMMMMMM
MMNx.  ,kNMMMMNOodKMMMM
MMMWk,  .:dkkOo'  ,OWMM
MMMMWKc.    ..';.  'kWM
MMMMMMNk;.     .;.  'OW
MMMMMMMMNk:,..  'cccxXW
kXWMMMMMMMWNKkdxOXWWXkc
"""
apk = """
         +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm/WMM[0MMMWFMM
      hMMMMMMMMMMMMMMMMMMh
   WMMW[92m..  yyyyyyyyyyyyyy           
 WWM[92m.mMMm`MMMMMMMMMMMMMMMMM            
 MMW[92m:MMMM-MMMMMMMMMMMMMMMMM
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs'''
"""
shell = """
MMXkooooooooooooooooooooooooooooooloxXMM
MNl..................................oNM
MX:..................................:XM
MXc..................................:XM
MXc....':c,..........................cXM
MXc....'o000xl:,.....................cXM
MX:......':oONWXx,...................cXM
MX:.....;ldO00Oxc'...................cXM
MXc....'dOxo:'.......................cXW
MXc.....'............................:XM
MX:..................................:XM
MXc..................................cXM
MWk:'''''''''''''''''''''''''''''''':kWM
MMWNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKNWMW
"""
