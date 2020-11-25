import sys

def recorrerParticipantes():
    #Nombre del Participante. args[1] pasado en ejecucion
    participante = str(sys.argv[1]).lower()
    ticketsMaximosEvento=20
    ticketsGanados=int(sys.argv[2])

    #Fichero de participantes
    nombreFichero='participantes.txt'
    participantesFile = open(nombreFichero,'r')
    #Lista con todos los participantes y sus tickets obtenidos
    Participantes=participantesFile.readlines()
    participantesFile.close()
    totalParticipantes=len(Participantes)
    print(Participantes)
    if totalParticipantes>0:
        #Iteramos las lineas del fichero participante a paticipante
        for linea in Participantes: 
            print('linea: '+linea)

            #Obtenemos el nombre de usuario del participante
            usuario=linea.split(':')[0]
            #Obtenemos los tickets del usuario. Eliminamos saltos de linea
            totalTickets=linea.split(':')[1]
            tickets=int(totalTickets.split('\n')[0])

            #Si el participante ya estaba registrado 
            if str(participante) == usuario:
                #Si este participante tiene menos del maximo de tickets
                if tickets<ticketsMaximosEvento:
                    print(usuario)
                    print('antes: '+str(tickets))
                    #Actualizamos sus tickets
                    participantes=open(nombreFichero,'w')
                    print('actual linea: '+linea)
                    remplazo=str(usuario+':'+str(tickets+ticketsGanados)+'\n')
                    print('remplazo linea: '+remplazo)
                    participantes.write(linea.replace(linea,remplazo))
                    participantes.close()
                    print('Puntos actualizados: '+str(tickets+ticketsGanados))
            else:
                print(usuario)
                print('antes: '+str(tickets))
                participantes = open(nombreFichero,'a')
                participantes.write(str(participante)+':'+str(ticketsGanados)+'\n')
                participantes.close()
    else:
        participantes = open('participantes.txt','a')
        participantes.write(str(participante)+':'+str(ticketsGanados)+'\n')
        participantes.close()


recorrerParticipantes()



#def guardarParticipante(participante):
#    participantesFile = open('participantes.txt','a')
#    recorrerParticipantes(participante)

#    participantesFile.write(str(participante))