import tkinter as tk
from PIL import ImageTk, Image
import whisper
import os
import sys
import time

model = whisper.load_model('tiny.en')
#function to run whisper ai on each .wav file within the current directory

def whisper_Now():
    output_text = ''
    for file_name in os.listdir():
        if file_name.endswith('.wav'):
            audio = whisper.load_audio(file_name)
            result = model.transcribe(audio)
            output_text += file_name + '\n' + result['text'] + '\n' +'\n'
    return output_text

#function to count the number of .wav files in the current directory

def button_click1():
    count = 0
    for wav in os.listdir():
        if wav.endswith('.wav'):
            count += 1
    label.configure(text=str(count))

#Function defining button2 to display the results of whisper_Now in a new window

def button_click2():
    new_window = tk.Toplevel(window)
    new_window.title('Human! All done!')

    text_widget = tk.Text(new_window)
    text_widget.pack()

    text_output = whisper_Now()

    text_widget.insert(tk.END, text_output)


#main window

window = tk.Tk()
window.title("Voice Mail Analyzer")
image = ImageTk.PhotoImage(Image.open('robot.png'))
image_label = tk.Label(window, image=image)
image_label.place(x=100, y=100)
window.geometry("750x500")


label = tk.Label(window, text="Greetings Human!")
label.pack()

label2 = tk.Label(window, text = 'Human! Do you want to know how many voicemails are in the folder?')
label2.pack()

button1 = tk.Button(window, text="Click Me!", command=button_click1)
button1.pack()

label3 = tk.Label(window, text = 'Or do you want me to analyze the voicemails?')
label3.pack()

button2 = tk.Button(window, text="Or...Click Me!", command=button_click2)
button2.pack()




window.mainloop()
