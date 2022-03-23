from tkinter import *
import json


def save_data():
    message = message_entry.get("1.0", "end-1c")
    orcs = orcs_entry.get("1.0", "end-1c")
    orc_list = orcs.split("\n")

    dictionary = {
        "api_id": api_id.get(),
        "api_hash": api_hash.get(),
        "orcs": orc_list,
        "message": message,

    }

    json_object = json.dumps(dictionary, indent=4)

    with open("api_config.json", "w") as outfile:
        outfile.write(json_object)

    root.destroy()
    import main


root = Tk()
root.title("Report the orcs")

try:
    f = open('api_config.json')
    data = json.load(f)
    default_api_id = data['api_id']
    default_api_hash = data['api_hash']
except:
    default_api_id = ""
    default_api_hash = ""


api_id = StringVar(value=default_api_id)
api_hash = StringVar(value=default_api_hash)
orcs = StringVar()
message = StringVar()


api_id_label = Label(text="api_id:")
api_hash_label = Label(text="api_hash:")
message_label = Label(text="message:")
orcs_label = Label(text="orcs:")

api_id_label.grid(row=0, column=0, sticky="w")
api_hash_label.grid(row=1, column=0, sticky="w")
orcs_label.grid(row=2, column=0, sticky="w")
message_label.grid(row=3, column=0, sticky="w")

api_id_entry = Entry(textvariable=api_id, width=33)
api_hash_entry = Entry(textvariable=api_hash, width=33)
orcs_entry = Text(root, height=5, width=33)
message_entry = Text(root, height=5, width=33)

api_id_entry.grid(row=0, column=1, padx=5, pady=5)
api_hash_entry.grid(row=1, column=1, padx=5, pady=5)
orcs_entry.grid(row=2, column=1, padx=5, pady=5)
message_entry.grid(row=3, column=1, padx=5, pady=5)

message_button = Button(text="REPORT", command=save_data)
message_button.grid(row=4, column=1, padx=5, pady=5, sticky="e")

root.mainloop()