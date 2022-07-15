#~para iniciar un entorno virtual en python en con "python -m venv nombre del entorno"
#para activar un entorno virtual se hace de la siguiente manera  en powershell "nombreDelEntorno\Scripts\Activate.ps1"
import re





def dibujar_salida(listaDeEntrada):
    import pygame, sys
    pygame.init()
    GRAY =  (0, 255, 255)
    AZURE = (240, 255, 255)

    size= (500, 600)
    screen = pygame.display.set_mode(size)

    miFuente = pygame.font.Font(None, 30)
    miTextoInicio = miFuente.render(listaDeEntrada[3], 0,(200,60,80))
    miVariableEntrada = miFuente.render(listaDeEntrada[4], 0,(200,60,80))
    

    numeros = re.compile("(^([0-9]+))")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                

        screen.fill(AZURE)

        #dibujamos el elipse
        inicio = pygame.draw.ellipse(screen, GRAY,[180, 10, 150, 40], 2)

        #dibujamos la linea
        pygame.draw.line(screen, GRAY, [255, 50], [255,100], 2)

        #texto
        screen.blit(miTextoInicio,(180+(inicio.width-miTextoInicio.get_width())/2,
                                10+(inicio.height-miTextoInicio.get_height())/2))
        #entrada
        entrada = pygame.draw.polygon(screen, GRAY, [(100, 150),(130,100),(400,100),(365,150)],2)

        screen.blit(miVariableEntrada,(100+(entrada.width-miVariableEntrada.get_width())/2,
                                100+(entrada.height-miVariableEntrada.get_height())/2))
        
        pygame.draw.line(screen, GRAY, [255, 150], [255,200], 2)
        if listaDeEntrada[6]== '=':
            resultadoNumero = re.fullmatch(numeros, listaDeEntrada[9])
            if listaDeEntrada[7] == listaDeEntrada[5] or listaDeEntrada[7] == listaDeEntrada[4]:
                if resultadoNumero != None or listaDeEntrada[9] == listaDeEntrada[5] or listaDeEntrada[9] == listaDeEntrada[4]:

                
               
                
                    textoProceso= ''
                    textoProceso= listaDeEntrada[5] + listaDeEntrada[6] + listaDeEntrada[7] + listaDeEntrada[8] + listaDeEntrada[9]
                    miTextoProceso = miFuente.render(textoProceso, 0, (200,60,80))
                    miTextoFinal = miFuente.render(listaDeEntrada[11], 0,(200,60,80))

                    #dibujamos el rectangulo
                    proceso = pygame.draw.rect(screen, GRAY, (50,200,400,53),2)
                    screen.blit(miTextoProceso,(50+(proceso.width-miTextoProceso.get_width())/2,
                                            200+(proceso.height-miTextoProceso.get_height())/2))

                    pygame.draw.line(screen, GRAY, [255, 252], [255,300], 2)

                    miTextoSalida = miFuente.render(listaDeEntrada[10], 0, (200,60,80))

                    if listaDeEntrada[10] == listaDeEntrada[4] or listaDeEntrada[10] == listaDeEntrada[5]:

                        #impresion
                        impresion = pygame.draw.polygon(screen, GRAY, [(100, 350),(130,300),(400,300),(365,350)],2)
                        screen.blit(miTextoSalida,(100+(impresion.width-miTextoSalida.get_width())/2,
                                                300+(impresion.height-miTextoSalida.get_height())/2))

                        pygame.draw.line(screen, GRAY, [255, 350], [255,400], 2)

                        #dibujamos el elipse
                        final = pygame.draw.ellipse(screen, GRAY,[180, 400, 150, 40], 2)
                        #texto
                        screen.blit(miTextoFinal,(180+(final.width-miTextoFinal.get_width())/2,
                                                400+(final.height-miTextoFinal.get_height())/2))

                        pygame.display.flip()
                    else:
                        print("HAY VARIABLES QUE NO SE UTLIZAN")
                        pygame.quit()
                        break

        else:
            miTextoFinal = miFuente.render(listaDeEntrada[6], 0,(200,60,80))
            miTextoSalida = miFuente.render(listaDeEntrada[5], 0, (200,60,80))
            
            if listaDeEntrada[5] == listaDeEntrada[4]:

                #impresion
                impresion = pygame.draw.polygon(screen, GRAY, [(100, 250),(130,200),(400,200),(365,250)],2)
                screen.blit(miTextoSalida,(100+(impresion.width-miTextoSalida.get_width())/2,
                                        200+(impresion.height-miTextoSalida.get_height())/2))

                pygame.draw.line(screen, GRAY, [255, 250], [255,300], 2)

                #dibujamos el elipse
                final = pygame.draw.ellipse(screen, GRAY,[180, 300, 150, 40], 2)
                #texto
                screen.blit(miTextoFinal,(180+(final.width-miTextoFinal.get_width())/2,
                                        300+(final.height-miTextoFinal.get_height())/2))



                pygame.display.flip()
            else:
                print("LA VARIABLE QUE INTENTA IMPRIMIR NO ESTA DECLARADO")
                pygame.quit()
                break
                

