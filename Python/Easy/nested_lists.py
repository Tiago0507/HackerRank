if __name__ == '__main__':
    def getting_names_of_second_lowest_score(records):
        # Encuentra el puntaje mas bajo
        # Esto es una comprensiÃ³n de generador, es como si usÃ¡ramos yield internamente
        # A diferencia de los list comprehension, la comprensiÃ³n de generadores se escribe con parÃ©ntesis. Si estÃ¡ dentro de una funciÃ³n
        # como min(), no es necesario escribirlos
        lowest_score = min(record[1] for record in records)
        # Filtra los registros con el puntaje mas bajo
        filtered_records = [record for record in records if record[1] != lowest_score]
        # Encuentra el segundo puntaje mas bajo entre los registros filtrados
        second_lowest_score = min(record[1] for record in filtered_records)
        # Encuentra los nombres de los registros con el segundo puntaje mas bajo
        names = sorted(record[0] for record in filtered_records if record[1] == second_lowest_score)
        return names
            
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    names = getting_names_of_second_lowest_score(records)
    for name in names:
        print(name)
    
    
    
            
                
            
