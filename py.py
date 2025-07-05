import os
import shutil
import tkinter as tk
from tkinter import filedialog,messagebox


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Executables": [".exe", ".msi"],
    "Others": []
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"





def organize_folder(source):
    print(source)
    if not os.path.exists(source):
        messagebox.showerror("Folder Does not Exit")
        return

    moved_files=0
    for i in os.listdir(source):
        i_path = os.path.join(source,i)

        if os.path.isfile(i_path):
            file_container = get_category(i)
            file_container_folder = os.path.join(source,file_container)
            os.makedirs(file_container_folder,exist_ok=True)

            destination = os.path.join(file_container_folder,i)
            shutil.move(i_path,destination)
            moved_files+=1
    messagebox.showinfo("Successfull !",f"Moved {moved_files} files")
            




def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        organize_folder(folder)



root = tk.Tk()
root.title("File Organizer using Python : ")

frame = tk.Frame(root,padx=20,pady=20)
frame.pack()

label = tk.Label(frame,text="Click below to choose a folder to organize : ")
label.pack()

button = tk.Button(frame,text="Click Here to select Folder ",command=select_folder)
button.pack()

root.mainloop()