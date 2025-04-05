import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
import threading
import os

# TTS engine setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Use female voice if available
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150)

# Global states
sentences = []
current_index = 0
is_paused = False
is_playing = False
play_thread = None


def load_pdf():
    global sentences, current_index, is_paused, is_playing
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        try:
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                # Split into sentences
                sentences = [s.strip() for s in text.split('.') if s.strip()]
                current_index = 0
                is_paused = False
                is_playing = False
                messagebox.showinfo("Success", "PDF Loaded Successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def threaded_play():
    global current_index, is_paused, is_playing
    if not sentences:
        messagebox.showwarning("No PDF", "Load a PDF first.")
        return

    if is_playing:
        return  # already playing

    is_playing = True
    while current_index < len(sentences):
        if is_paused:
            break
        engine.say(sentences[current_index])
        engine.runAndWait()
        current_index += 1
    is_playing = False


def play_speech():
    global play_thread
    if not is_playing:
        play_thread = threading.Thread(target=threaded_play, daemon=True)
        play_thread.start()


def pause_speech():
    global is_paused
    if is_playing:
        engine.stop()
        is_paused = True


def resume_speech():
    global is_paused
    if sentences and is_paused:
        is_paused = False
        play_speech()


def stop_speech():
    global is_paused, is_playing, current_index
    engine.stop()
    is_paused = False
    is_playing = False
    current_index = 0


def save_as_mp3():
    if not sentences:
        messagebox.showwarning("No PDF", "Load a PDF first.")
        return

    text = ". ".join(sentences)
    try:
        tts = gTTS(text)
        save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 File", "*.mp3")])
        if save_path:
            tts.save(save_path)
            messagebox.showinfo("Saved", f"Audio saved to: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Setup
root = tk.Tk()
root.title("PDF to Audio Reader")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="📘 PDF to Audio Reader", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(root, text="Load PDF", command=load_pdf, width=30).pack(pady=5)
tk.Button(root, text="▶ Play", command=play_speech, width=30).pack(pady=5)
tk.Button(root, text="⏸ Pause", command=pause_speech, width=30).pack(pady=5)
tk.Button(root, text="🔁 Resume", command=resume_speech, width=30).pack(pady=5)
tk.Button(root, text="⏹ Stop", command=stop_speech, width=30).pack(pady=5)
tk.Button(root, text="💾 Save as MP3", command=save_as_mp3, width=30).pack(pady=5)

tk.Label(root, text="Made by Ranveer ✨", font=("Arial", 10)).pack(side="bottom", pady=10)

root.mainloop()
