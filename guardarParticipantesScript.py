#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, shutil, os
from datetime import datetime

saltoDeLinea = '\n'
ticketsMaximosEvento=20
#Nombre del Participante. args[1] pasado en ejecucion
participante = str(sys.argv[1]).lower()

#Tickets que gana. args[2] pasado en ejecucion
ticketsGanados=int(sys.argv[2])

#Ruta Directorio Backups
nombreDirectorio='BackupParticipantes'
directorioBkp=nombreDirectorio+'/'

#Fichero de participantes
nombreFichero='participantes'
extension='.txt'
fichero=nombreFichero+extension

def gestionarParticipantes():
    #Comprobamos que ya exista un fichero de Participantes, sino lo creamos
    if not os.path.isfile(fichero):
        open(fichero, "w").close()

    #Lista con todos los participantes y sus tickets obtenidos
    participantesFile = open(fichero,'r')
    participantesList=participantesFile.readlines()
    totalParticipantes=len(participantesList)
    participantesFile.close()

    participantesList=actualizarListadoParticipantes(participantesList)

    if totalParticipantes>0:
        hoy=datetime.now()
        fecha=str(hoy.day)+str(hoy.month)+str(hoy.year)
        hora=str(hoy.hour)+str(hoy.minute)+str(hoy.second)
        fechaHoraActual=fecha+hora
        if not os.path.isdir(nombreDirectorio):
            os.mkdir(nombreDirectorio)

        shutil.copy(fichero, directorioBkp)
        nuevoNombre=directorioBkp+nombreFichero+"_"+fechaHoraActual+extension
        archivo=directorioBkp+fichero
        os.rename(archivo, nuevoNombre)

    actualizarFicheroParticipantes(participantesList)

def actualizarListadoParticipantes(participantesList):
    participantesListTemporal=[]
    if participantesList==[]:
        #La variable op.linesep te permitirá obtener los caracteres necesarios para crear el salto de línea de acuerdo al sistema operativo donde estés ejecutando esta rutina.
        participanteNuevo=str(participante)+':'+str(ticketsGanados)
        participantesListTemporal.append(participanteNuevo)
    else:
        print('tengo Participantes')
        for idx, participanteLinea in enumerate(participantesList): 
            print('index: '+str(idx))
            if not participanteLinea == '' and not participanteLinea == '\n':
                print('participanteLinea: '+participanteLinea)
                #Obtenemos el nombre de usuario del participante
                usuario=participanteLinea.split(':')[0]
                print('usuario: '+usuario)
                #Obtenemos los tickets del usuario. Eliminamos saltos de linea
                totalTickets=participanteLinea.split(':')[1]
                tickets=int(totalTickets.split(saltoDeLinea)[0])
                if participante in usuario:
                    print('usuario2: '+usuario)
                    print('participante: '+participante)
                    ticketsActualizados=tickets+ticketsGanados
                    #Comprobamos que no supera el máximo de tickets para el sorteo
                    if tickets<ticketsMaximosEvento and ticketsActualizados<=ticketsMaximosEvento:
                        print('es un parguela')
                        participanteActualizado=str(participante)+':'+str(ticketsActualizados)
                        print('participanteActualizado: '+participanteActualizado)
                        #participantesListTemporal.append(participanteActualizado)
                        if len(participantesListTemporal) == 0:
                            participantesListTemporal.append(participanteActualizado)
                        else:
                            participantesListTemporal[idx] = participanteActualizado
                        print('despues de ser un parguela:')
                        print(participantesListTemporal)
                    else:
                        print('supera el maximo')
                        #Si ya tiene 20 tickets o supera el máximo, se le mantienen sus 20 
                        participanteActualizado=str(participante)+':'+str(ticketsMaximosEvento) 
                        if len(participantesListTemporal) == 0:
                            participantesListTemporal.append(participanteActualizado)
                        else:
                            participantesListTemporal[idx] = participanteActualizado

                        print('despues de superar el maximo:')
                        print(participantesListTemporal)
                else:
                    if not participanteLinea == '\n':
                        participantesListTemporal.append(participanteLinea)
                        #Verificamos que no se ha incluido ya el participante
                        if not verificarDuplicados(participantesListTemporal,str(participante)):
                            nuevoParticipante=str(participante)+':'+str(ticketsGanados)
                            participantesListTemporal.append(nuevoParticipante)

    print('despues de Actualizar:')
    print(participantesListTemporal)
    return participantesListTemporal

def actualizarFicheroParticipantes(participantesList):
    with open(fichero,'w+') as participantesFile:
        for lineaParticipante in participantesList: 
            participanteSinSalto=lineaParticipante.split(saltoDeLinea)[0]
            print >> participantesFile, participanteSinSalto

def verificarDuplicados(participantesListTemporal,usuarioActual):
    for participanteNuevos in participantesListTemporal:
        participanteNuevo=participanteNuevos.split(':')[0]
        if participanteNuevo==usuarioActual:
            return True
    return False

gestionarParticipantes()