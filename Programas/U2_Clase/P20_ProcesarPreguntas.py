import P19_LeerPreguntas as p
import random as rnd

def procesar_preguntas():
    preguntas = p.cargar_preguntas()
    # print("Preguntas Cargadas:")
    # for i in preguntas:
    #     print(i)

    #print("Preguntas Desordenadas Con Opciones Desordenadas: ")
    rnd.shuffle(preguntas) #desordena las preguntas
    for pregunta in preguntas: #desordena las opciones
        rnd.shuffle(pregunta[2])
        #print(pregunta)
    return preguntas

if __name__ == '__main__':
    preguntas = procesar_preguntas()
    for i in preguntas:
        print(i)