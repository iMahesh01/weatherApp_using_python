from tkinter import *
from tkinter import messagebox


def tell_weather():
    import requests
    api_key = "e57ac6a3ce57c0e6706f2c7992908696"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        # Clear fields before inserting new data
        temp_field.delete(0, END)
        atm_field.delete(0, END)
        humid_field.delete(0, END)
        desc_field.delete(0, END)

        temp_field.insert(0, str(current_temperature) + " Kelvin")
        atm_field.insert(0, str(current_pressure) + " hPa")
        humid_field.insert(0, str(current_humidiy) + " %")
        desc_field.insert(0, str(weather_description))
    else:
        messagebox.showerror("Error", "City Not Found \nPlease enter a valid city name")
        city_field.delete(0, END)

def clear_all():
    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
    city_field.focus_set()

if __name__ == "__main__":
    root = Tk()
    root.title("Weather Application")

    # Set the background color of GUI window
    root.configure(background="light blue")

    # Set the configuration of GUI window
    root.geometry("450x300");

    # Create a Weather GUI Application label
    headlabel = Label(root, text="Weather GUI Application", fg='white', bg='black', font=('Helvetica', 16, 'bold'))
    headlabel.pack(pady=10)

    # Create a frame for input and labels
    input_frame = Frame(root, bg='light blue')
    input_frame.pack(pady=10, padx=10)

    # Create labels and entry fields
    label1 = Label(input_frame, text="City name:", fg='white', bg='dark gray', font=('Helvetica', 12, 'bold'))
    label1.grid(row=0, column=0, padx=10, pady=5, sticky="E")
    city_field = Entry(input_frame, font=('Helvetica', 12))
    city_field.grid(row=0, column=1, ipadx="50", pady=5)

    label2 = Label(input_frame, text="Temperature:", fg='white', bg='dark gray', font=('Helvetica', 12, 'bold'))
    label2.grid(row=1, column=0, padx=10, pady=5, sticky="E")
    temp_field = Entry(input_frame, font=('Helvetica', 12))
    temp_field.grid(row=1, column=1, ipadx="50", pady=5)

    label3 = Label(input_frame, text="Atm pressure:", fg='white', bg='dark gray', font=('Helvetica', 12, 'bold'))
    label3.grid(row=2, column=0, padx=10, pady=5, sticky="E")
    atm_field = Entry(input_frame, font=('Helvetica', 12))
    atm_field.grid(row=2, column=1, ipadx="50", pady=5)

    label4 = Label(input_frame, text="Humidity:", fg='white', bg='dark gray', font=('Helvetica', 12, 'bold'))
    label4.grid(row=3, column=0, padx=10, pady=5, sticky="E")
    humid_field = Entry(input_frame, font=('Helvetica', 12))
    humid_field.grid(row=3, column=1, ipadx="50", pady=5)

    label5 = Label(input_frame, text="Description:", fg='white', bg='dark gray', font=('Helvetica', 12, 'bold'))
    label5.grid(row=4, column=0, padx=10, pady=5, sticky="E")
    desc_field = Entry(input_frame, font=('Helvetica', 12))
    desc_field.grid(row=4, column=1, ipadx="50", pady=5)

    # Create a frame for buttons
    button_frame = Frame(root, bg='light blue')
    button_frame.pack(pady=10)

    # Create buttons
    button1 = Button(button_frame, text="Submit", bg="pink", fg="black", font=('Helvetica', 12, 'bold'), command=tell_weather)
    button2 = Button(button_frame, text="Clear", bg="pink", fg="black", font=('Helvetica', 12, 'bold'), command=clear_all)

    button1.grid(row=0, column=0, padx=10)
    button2.grid(row=0, column=1, padx=10)

    # Start the GUI
    root.mainloop()
