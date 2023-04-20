from kanren import Relation, facts, run, conde, var, eq
#  x es abuelo de y
def abuelo(x, y):
    temp = var()
    return conde((padres(x, temp), padres(temp, y)))

#  x es tio de y
def tio(x, y):
    temp = var()
    return conde((padre(temp, x), abuelo(temp, y)))  

#  x es padre de y
def padres(x, y):
    return conde([padre(x, y)], [madre(x, y)])

#  x, y y son hermanos
def hermano(x, y):
    temp = var()
    return conde((padres(temp, x), padres(temp, y)))

if __name__ == '__main__':

    padre = Relation()
    madre = Relation()

    facts(madre, ("Cecilia", "Gregoria"),
          ("Cecilia", "Julian"),
          ("Maria", "Walter"),
          ("Maria", "Fransico"),
          ("Gregoria", "Freddy"),
          ("Gregoria", "Crispin"),
          ("Gregoria", "Monica"),
          ("Gregoria", "Efrain"),
          ("Gregoria", "Maritza"),
          ("Gregoria", "Limberth"),
          ("Gregoria", "Yenny"),
          ("Gregoria", "Beatriz"),
          ("Gregoria", "Wilson"),
          ("Gregoria", "Karen"),
          ("Melania", "Camila"),
          ("Melania", "Alejandro"),
          ("Melania", "Melisa"),
          ("Lidia", "Lupe"),
          ("Lidia", "Ivan")
          )
    facts(padre, ("Pascual", "Walter"),
          ("Juan", "Gregoria"),          
          ("Juan", "Julian"),
          ("Walter", "Freddy"),
          ("Walter", "Crispin"),
          ("Walter", "Monica"),
          ("Walter", "Efrain"),
          ("Walter", "Maritza"),
          ("Walter", "Limberth"),
          ("Walter", "Yenny"),
          ("Walter", "Beatriz"),
          ("Walter", "Wilson"),
          ("Walter", "Karen"),
          ("Julio", "Camila"),
          ("Julio", "Alejandro"),
          ("Julio", "Melisa")
          )
    x = var()

    # Los hijos de Juan
    nombre = 'Walter'
    salida = run(0, x, padre(nombre, x))
    print("\nLista de hijos de " + nombre)
    for item in salida:
        print(item)

    # La madre de Carlos
    nombre = 'Gregoria'
    salida = run(0, x, madre(x, nombre))[0]
    print("\nMadre de " + nombre + "\n" + salida)

    # Los padres de Andres
    nombre = 'Limbert'
    salida = run(0, x, padres(x, nombre))
    print("\nLos padres de " + nombre)
    for item in salida:
        print(item)

    # Los abules de Maritza
    nombre = 'Maritza'
    salida = run(0, x, abuelo(x, nombre))
    print("\nLos abulelos de  " + nombre)
    for item in salida:
        print(item)

    # Los nietos de Cecilia
    nombre = 'Cecilia'
    salida = run(0, x, abuelo(nombre, x))
    print("\nLos nietos de " + nombre)
    for item in salida:
        print(item)

    # Los hermanos de Efrain
    nombre = 'Efrain'
    salida = run(0, x, hermano(x, nombre))
    hermano = [x for x in salida if x != nombre]
    print("\nLos hermanos de " + nombre)
    for item in hermano:
        print(item)

    #Los tios de Vanesa
    nombre = 'Vanesa'
    nombre_padre = run(0, x, padre(x, nombre))[0]
    salida = run(0, x, tio(x, nombre))
    salida = [x for x in salida if x != nombre_padre]
    print("\nLos tios de " + nombre)
    for item in salida:
        print(item)