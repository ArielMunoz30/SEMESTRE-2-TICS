import os
import subprocess

# ================================
# CONFIGURACIÓN BASE DEL DASHBOARD
# ================================

def obtener_ruta_base():
    """
    Obtiene la ruta raíz del proyecto de forma segura,
    independientemente desde dónde se ejecute el script.
    """
    return os.path.dirname(os.path.abspath(__file__))


def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux / Mac
            subprocess.Popen(['python3', ruta_script])
    except Exception as e:
        print(f"❌ Error al ejecutar el código: {e}")


def mostrar_menu():
    ruta_base = obtener_ruta_base()

    unidades = {
        '1': 'UNIDAD 1',
        '2': 'UNIDAD 2'
    }

    while True:
        print("\n====================================")
        print(" DASHBOARD DE PROGRAMACIÓN POO ")
        print(" Autor: Francis Ariel Muñoz Puetate ")
        print("====================================")
        print("\nMenú Principal")

        for key, value in unidades.items():
            print(f"{key} - {value}")

        print("0 - Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            print("👋 Saliendo del programa.")
            break

        if opcion in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[opcion])

            if not os.path.exists(ruta_unidad):
                print(f"⚠️ No se encontró la carpeta: {ruta_unidad}")
                input("Presiona Enter para continuar...")
            else:
                mostrar_sub_menu(ruta_unidad)
        else:
            print("❌ Opción inválida.")


def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [
        f.name for f in os.scandir(ruta_unidad) if f.is_dir()
    ]

    while True:
        print(f"\n📂 Contenido de {os.path.basename(ruta_unidad)}")

        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")

        print("0 - Regresar al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            break

        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(sub_carpetas):
                ruta_sub = os.path.join(ruta_unidad, sub_carpetas[indice])
                mostrar_scripts(ruta_sub)
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Ingrese un número válido.")


def mostrar_scripts(ruta_sub_carpeta):
    scripts = [
        f.name for f in os.scandir(ruta_sub_carpeta)
        if f.is_file() and f.name.endswith('.py')
    ]

    while True:
        print(f"\n📄 Scripts en {os.path.basename(ruta_sub_carpeta)}")

        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")

        print("0 - Regresar")

        opcion = input("Seleccione un script: ")

        if opcion == '0':
            break

        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                codigo = mostrar_codigo(ruta_script)

                if codigo:
                    ejecutar = input("\n¿Desea ejecutar el script? (1 = Sí | 0 = No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)

                input("\nPresiona Enter para continuar...")
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Ingrese un número válido.")


# ====================
# EJECUCIÓN PRINCIPAL
# ====================
if __name__ == "__main__":
    mostrar_menu()

