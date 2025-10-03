from pyscript import display, document

def total_order():
    total_price = 0
    if document.getElementById("d1").checked:  # Water
        total_price += 10
    if document.getElementById("d2").checked:  # Iced Tea
        total_price += 18
    if document.getElementById("d3").checked:  # Milktea
        total_price += 18
    if document.getElementById("d4").checked:  # Brewed Coffee
        total_price += 25
    if document.getElementById("d5").checked:  # Sprite
        total_price += 20
    if document.getElementById("d6").checked:  # Pepsi
        total_price += 20
    if document.getElementById("d7").checked:  # Coca-Cola
        total_price += 20
    if document.getElementById("d8").checked:  # C2
        total_price += 20
    return total_price


def show_info(e):  
    name = str(document.getElementById("name").value)
    contact = str(document.getElementById("contact").value)

    total_price = total_order()   # call the right function

    info = f"Name: {name}\nContact: {contact}"
    notes = f"Thank you {name} for ordering at our brewery. We will contact you at {contact}."
    summary = f"{info}\n\n{notes}\n\nTotal: ₱{total_price}"

    display(summary, target="output")   # your HTML div is id="output"