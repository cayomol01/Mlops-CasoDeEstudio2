import argparse

def main():
    parser = argparse.ArgumentParser(description="Procesar argumentos en Docker")
    parser.add_argument("--nombre", type=str, help="Nombre del usuario", required=True)
    parser.add_argument("--edad", type=int, help="Edad del usuario", required=True)
    args = parser.parse_args()

    print(f"Hola {args.nombre}, tienes {args.edad} años.")

if __name__ == "__main__":
    main()
