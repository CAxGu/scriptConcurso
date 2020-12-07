#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import shutil
import json
#point at lib folder for classes / references
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from Settings_Module import MySettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Evento Script"
Website = "https://www.twitch.tv/exomaru"
Description = "Usa !ticket para participar"
Creator = "Exomaru"
Version = "1.0.0.0"

from datetime import datetime

#---------------------------
#   Define Global Variables
#---------------------------
global SettingsFile
SettingsFile = ""
global ScriptSettings
ScriptSettings = MySettings()

global saltoDeLinea
saltoDeLinea = ""
global ticketsMaximosEvento
ticketsMaximosEvento = 0

#Nombre del Participante. args[1] pasado en ejecucion
global participante
participante = ""

#Tickets que gana. args[2] pasado en ejecucion
global ticketsGanados
ticketsGanados = 0

#Ruta Directorio Backups
global nombreDirectorio
nombreDirectorio = ""
global directorioBkp
directorioBkp = ""

#Fichero de participantes
global nombreFichero
nombreFichero = ""
global extension
extension = ""
global fichero
fichero = ""

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    #   Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)

    #   Load settings
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
    ScriptSettings = MySettings(SettingsFile)
    ScriptSettings.Response = "Overwritten ticket event settings! ^_^"

    saltoDeLinea = '\n'
    ticketsMaximosEvento = 20

    #Tickets que gana el participante
    ticketsGanados = 1

    #Ruta Directorio Backups
    nombreDirectorio='BackupParticipantes'
    directorioBkp=nombreDirectorio+'/'

    #Fichero de participantes
    nombreFichero='participantes'
    extension='.txt'
    fichero=nombreFichero+extension

    return


#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    #Nombre del Participante. Usuario que ha utilizado el comando
    participante = str(data.User) 

    if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and Parent.IsOnUserCooldown(ScriptName,ScriptSettings.Command,data.User):
        Parent.SendStreamMessage("Time Remaining " + str(Parent.GetUserCooldownDuration(ScriptName,ScriptSettings.Command,data.User)))

    #   Check if the propper command is used, the command is not on cooldown and the user has permission to use the command
    if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and not Parent.IsOnUserCooldown(ScriptName,ScriptSettings.Command,data.User) and Parent.HasPermission(data.User,ScriptSettings.Permission,ScriptSettings.Info):
        Parent.BroadcastWsEvent("EVENT_MINE","{'show':false}")
        Parent.SendStreamMessage(str(data.User) +" "+ ScriptSettings.Response)    # Send your message to chat
        Parent.AddUserCooldown(ScriptName,ScriptSettings.Command,data.User,ScriptSettings.Cooldown)  # Put the command on cooldown

    return


#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return


#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    
    if "$myparameter" in parseString:
        return parseString.replace("$myparameter","I am a cat!")
    
    return parseString


#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return


#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return


#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return