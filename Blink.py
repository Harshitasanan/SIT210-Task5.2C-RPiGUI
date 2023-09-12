from tkinter import *
import tkinter.font as FONT
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Initialisation of LEDs
led1 = LED(15)
led2 = LED(17)
led3 = LED(27)

# Create a Tkinter window
root = Tk()
root.title("LED Toggler")

# Set the window size
root.geometry("400x200")  # Width x Height

myFont = FONT.Font(family='Helvetica', size=14, weight="bold")

# Function to toggle the LEDs and update button colors
def led_toggle(led, button, other_leds):
    # Turn off all LEDs except the selected one
    for other_led in other_leds:
        other_led.off()
    # Toggle the selected LED
    led.toggle()
    # Update button colors
    for l, b in led_buttons.items():
        if l.is_lit:
            b.config(bg=led_color_map.get(l, 'gray'))
        else:
            b.config(bg='gray')

# Create buttons for Red, Blue, and Green LEDs
led_color_map = {
    led1: 'red',
    led2: 'blue',
    led3: 'green'
}

led_buttons = {
    led1: Radiobutton(root, text="Red", font=myFont, bg='gray', command=lambda: led_toggle(led1, led_buttons[led1], [led2, led3])),
    led2: Radiobutton(root, text="Blue", font=myFont, bg='gray', command=lambda: led_toggle(led2, led_buttons[led2], [led1, led3])),
    led3: Radiobutton(root, text="Green", font=myFont, bg='gray', command=lambda: led_toggle(led3, led_buttons[led3], [led1, led2]))
}

for led, button in led_buttons.items():
    button.grid(row=0, column=list(led_buttons.keys()).index(led), padx=10, pady=10)

# Function to clean up GPIO pins when the window is closed
def close():
    GPIO.cleanup()
    root.destroy()

# Create an Exit button
exit_button = Button(root, text="Exit", command=close)
exit_button.grid(row=1, column=1, pady=20)

# Handle window close event
root.protocol("WM_DELETE_WINDOW", close)

# Start the Tkinter main loop
root.mainloop()
