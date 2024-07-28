def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    # Calcular el nivel basado en el número de pregunta y preguntas por nivel
    if p_level == 1:
        # Cada pregunta tiene su propio nivel
        if n_pregunta == 1:
            return "basicas"
        elif n_pregunta == 2:
            return "intermedias"
        elif n_pregunta == 3:
            return "avanzadas"
        else:
            raise ValueError("Número de pregunta inválido.")
    
    elif p_level == 2:
        # Nivel cambia cada 2 preguntas
        if 1 <= n_pregunta <= 2:
            return "basicas"
        elif 3 <= n_pregunta <= 4:
            return "intermedias"
        elif 5 <= n_pregunta:
            return "avanzadas"
        else:
            raise ValueError("Número de pregunta inválido.")
    
    elif p_level == 3:
        # Nivel cambia cada 3 preguntas
        if 1 <= n_pregunta <= 3:
            return "basicas"
        elif 4 <= n_pregunta <= 6:
            return "intermedias"
        elif 7 <= n_pregunta <= 9:
            return "avanzadas"
        else:
            raise ValueError("Número de pregunta inválido.")
        
    
    
    ##################################################

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias