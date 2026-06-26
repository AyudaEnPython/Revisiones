"""AyudaEnPython: https://www.facebook.com/groups/ayudapython"""

Invoice = dict[str, float | int]
Invoices = list[Invoice]

REPLACE = 9999
MIN = -2.0


def calculate_average(invoices: Invoices) -> float | None:
    if not invoices:
        return None
    return sum(inv["amount"] for inv in invoices) / len(invoices)


def add_invoice(invoices: Invoices, number: int | float, amount: float) -> None:
    if number <= 0:
        raise ValueError("El número de factura debe ser positivo.")
    if amount < 0:
        raise ValueError("El importe no puede ser negativo.")
    invoices.append({"number": number, "amount": amount})


def remove_above_average(invoices: Invoices, fixed_avg: float) -> None:
    invoices[:] = [inv for inv in invoices if inv["amount"] <= fixed_avg]


def replace_even_below_average(
    invoices: Invoices, fixed_avg: float, replace_value: int = REPLACE
) -> None:
    for invoice in invoices:
        if invoice["amount"] >= fixed_avg:
            continue
        if invoice["number"] % 2 == 0:
            invoice["number"] = replace_value
        elif invoice["amount"].is_integer() and int(invoice["amount"]) % 2 == 0:
            invoice["amount"] = float(replace_value)


def replace_min_amount_with(
    invoices: Invoices, target: float, value: float = MIN
) -> None:
    if not invoices:
        return
    for invoice in invoices:
        if invoice["amount"] == target:
            invoice["amount"] = value


def get_input(prompt: str, is_float: bool = False) -> int | float:
    while True:
        try:
            value = float(input(prompt)) if is_float else int(input(prompt))
            if is_float and value < 0:
                print("Ingrese un importe mayor o igual a 0.")
                continue
            return value
        except ValueError:
            print("Ingrese un número válido.")


def load_invoices_interactively() -> Invoices:
    invoices: Invoices = []
    print("Ingrese facturas. Use número de factura 0 para terminar.")
    while True:
        number = get_input("Número de factura (0 para terminar): ")
        if number == 0:
            break
        if number < 0:
            print("No puede ser negativo.")
            continue
        amount = get_input("Importe: ", is_float=True)
        try:
            add_invoice(invoices, number, amount)
        except ValueError as e:
            print(f"Entrada inválida: {e}")
    return invoices


def show(invoices: Invoices, message) -> None:
    print(f"\n--- {message} ---")
    for inv in invoices:
        print(f"Factura N° {int(inv['number'])} - Importe: {inv['amount']}")


def main() -> None:
    invoices = load_invoices_interactively()
    if not invoices:
        print("NO HAY NINGUN REGISTRO REALIZADO")
        return
    orig_avg = calculate_average(invoices) or 0.0
    min_invoice = min(invoices, key=lambda x: x["amount"])
    orig_min_amount = min_invoice["amount"]
    print(f"\nEl importe mínimo facturado es: {orig_min_amount}")
    print(f"Pertenece a la factura N° {min_invoice['number']}")
    show(invoices, "Facturas e importes iniciales")
    replace_even_below_average(invoices, fixed_avg=orig_avg)
    show(invoices, f"Tras reemplazar pares menores al promedio ({orig_avg})")
    remove_above_average(invoices, fixed_avg=orig_avg)
    show(invoices, "Tras eliminar importes mayores al promedio")
    replace_min_amount_with(invoices, target=orig_min_amount, value=MIN)
    show(invoices, f"Lista Final: Tras reemplazar importe mínimo por {MIN}")


if __name__ == "__main__":
    main()
