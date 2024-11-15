from model import *

def menu():
    print(" ")
    print("***** MENU *****")
    print("- pred")
    print("- changes")
    pass

def pred(model):
    import numpy as np
    km4 =   input("Ingrese km4week: ")
    sp4 =   input("Ingrese sp4week: ")
    wall =  input("Ingrese Wall21: ")

    try:
        km4 = float(km4)
        sp4 = float(sp4)
        wall = float(wall)
        score = km4*sp4
        data = np.array([[km4, sp4, wall, score]])
        

    except:
        print("Ingrese datos numéricos!")

    pred = model.predict(data)

    print(f"Con los datos proporcionados, se tendría un tiempo de: {pred[0]:.2f} horas")

    pass

def changes(df, model, model_path):
    id = input("Ingrese el id del concursante: ")
    
    try:
        id = int(id)
        if id <= len(df) and id > 0:  # Verifica que el id sea válido
            columna = input("Ingrese el dato que desea cambiar: ")
            columnas = df.columns
            
            if columna in columnas:
                dato = input("Ingrese el nuevo dato: ")
                
                if columna in ['sp4week', 'km4week', 'Wall21', 'MarathonTime']:
                    try:
                        dato = float(dato)  # Asegúrate de convertir el dato a float
                        df.loc[id - 1, columna] = dato  # Actualiza el valor en el DataFrame
                        df.to_csv('MarathonData.csv', index=False)

                        df['Score'] = df['km4week']*df['sp4week']
                        print(f"El campo '{columna}' ha sido actualizado a {dato}.")

                        # Reentrenar el modelo con los datos actualizados
                        print("Actualizando el modelo con los nuevos datos...")
                        df = preprocess_data(df)
                        model = train_model(df)
                        save_model(model, model_path)
                        print("El modelo ha sido actualizado con éxito.")
                        return model
                    except ValueError:
                        print("Esta columna necesita un dato numérico válido.")
                        return model
                else:
                    # Si la columna no es numérica, actualiza el dato como texto
                    df.loc[id - 1, columna] = dato
                    print(f"El campo '{columna}' ha sido actualizado a {dato}.")
                    return model
            else:
                print(f"Campo no encontrado. Por favor, ingrese alguno de los siguientes: {list(columnas)}")
                return model
        else:
            print("ID no encontrado. Regresando al menú...")
            return model
    except ValueError:
        print("Por favor, ingrese un ID válido.")
        return model

    

def main():
    data_path = "MarathonData.csv"
    df = load_data(data_path)
    model_path = 'Models/modelV1.pkl'
    model = load_model(model_path)

    command = ""
    while command !="exit()":
        menu()
        command = input("  > ")
        if command == "pred":
            pred(model)
        elif command == "changes":
            changes(df, model, model_path)
        else:
            print("Escoja una opción disponible")


if __name__ == "__main__":
    main()
