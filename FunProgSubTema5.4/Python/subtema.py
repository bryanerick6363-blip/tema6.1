import modulo_venta

def main():#principal
    opcion = 0

    while opcion != 6:
        print("\n=== MINIMARKET - INVENTARIO CON PIPE ===")
        print("1. Registrar producto")
        print("2. Buscar por codigo")
        print("3. Listar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Salir")
        opcion = int(input("Opcion: ").strip())

        if opcion == 1:
            modulo_venta.registrar_producto()
        elif opcion == 2:
            modulo_venta.buscar_por_codigo()
        elif opcion == 3:
            modulo_venta.listar()
        elif opcion == 4:
            modulo_venta.modificar_producto()
        elif opcion == 5:
            modulo_venta.eliminar_producto()
        elif opcion == 6:
            modulo_venta.print("Saliendo del inventario...")
        else:
            print("Opcion no valida.")


main()