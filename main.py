from pyscript import document, display

ICT_CLUB = ["Matthew Matthias","Kaleb Balibog","Brixen Rabacca", "Naguit Natahaniel"]

def show_list():
    output = document.getElementById("output")  
    output.innerHTML = ""

    for item in ICT_CLUB:
        display(item, target="output")

def append_value(e):
    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()
    user_input = first_name + " " + last_name
    message = document.getElementById("message")

    if user_input in ICT_CLUB:
        message.innerHTML = f"Congratulations! {user_input} you are part of the ICT Club."
        show_list()
    else:
        message.innerHTML = f"Sorry {user_input}, your name is not on the list"
    document.getElementById("firstname").value = ""
    document.getElementById("lastname").value = ""
