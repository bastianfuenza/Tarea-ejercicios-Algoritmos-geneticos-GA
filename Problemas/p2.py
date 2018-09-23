from pyevolve import G1DBinaryString #Se importa el objeto genoma de tipo binario
from pyevolve import GSimpleGA
from pyevolve import Initializators
from pyevolve import Selectors
from pyevolve import Mutators
from pyevolve import Crossovers
from pyevolve import Statistics
import pyevolve

#Se recomienda usar el archivo ex1.py como referencia.

#En el caso de muchas librerias como pyevolve, el fitness real es una transformacion (lineal, gaussiana, etc) del 
#score entregado por la funcion de evaluacion, por lo que en la pantalla de comando sale un Score o Raw, que corresponde
#al valor entregado por la funcion, y ademas un Fitness, que viene siendo el escalado del Score.

# Defina la funcion de evaluacion del problema
#En este caso tiene que transformar el individuo binario al valor entero que representa, luego aplicarle
#una transformacion lineal para ajustarlo al rango de [0.50], y finalmente aplicarle la funcion del enunciado.
def eval_func(chromosome): #recibe un cromosoma, en este caso una lista de 1s y 0s
   score = 0.0


   return score

# Defina el tipo de genoma, en este caso G1DBinaryString.G1DBinaryString(numero de genes)
genome = G1DBinaryString.G1DBinaryString( )

#Muchos parametros tienen una opcion predefinida, numero de generaciones, probabilidades de mutacion y cruzamiento,
#metodos de mutacion, crossover, inicializacion, etc; pero se recomienda especificarlos en caso de ser relevantes 

# Defina que funcion evaluadora, initializator, mutator y crossover utilizara. Busque los ultimos 3 en el Anexo
genome.evaluator.set(eval_func)
genome.initializator.set()
genome.mutator.set()
genome.crossover.set()

# Creacion del algoritmo genetico usando el "genome" definido
ga = GSimpleGA.GSimpleGA(genome)

# Defina el tipo de seleccion del algoritmo. Busquelo en el anexo
ga.selector.set()

# Numero de generaciones
ga.setGenerations(500)

#Ejecuta la evolucion
ga.evolve()

#Arroja el mejor individuo
print ga.bestIndividual()