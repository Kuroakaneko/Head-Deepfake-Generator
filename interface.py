import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import shutil
import subprocess
from PIL import Image, ImageTk
import cv2  # OpenCV to handle video playback

NAME_TO_FOLDER = {
    "Elon Musk": "elon", "Vladimir Putin": "putin", 
    "Donald Trump": "trump", "Emmanuel Macron": "macron"
}

target_video_path = None

def on_drop(event, video_type):
    """Handles file drop for target video."""
    video_file = event.data.strip('{}')
    if video_file:
        if video_type == "target":
            update_video_path(video_file)

def update_video_path(video_file):
    """Updates video path and UI elements."""
    global target_video_path
    target_video_path = video_file
    label_target_video.config(text=f"Selected: {os.path.basename(video_file)}")
    button_remove_target_video.pack(pady=5)

def save_videos():
    """Saves the videos and runs batch files."""
    selected_name = selected_name_var.get()
    folder_name = NAME_TO_FOLDER[selected_name]
    folder_path = folder_name
    os.makedirs(folder_path, exist_ok=True)

    try:
        save_video(target_video_path, folder_path, "data_dst.mp4")

        run_batch_files(folder_name)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to save videos: {e}")

def save_video(video_path, folder_path, filename):
    """Helper function to save a video."""
    if video_path:
        shutil.copy(video_path, os.path.join(folder_path, filename))

def run_batch_files(folder_name):
    """Runs batch files for the selected name."""
    uppercase_name = folder_name.upper()
    batch_files = [f"{uppercase_name}_0_CLEAR.bat", f"{uppercase_name}_1_SPLIT_DST.bat", f"{uppercase_name}_2_EXTRACT_FACES_DST.bat"]
    
    for batch in batch_files:
        batch_path = os.path.join(batch)
        if os.path.exists(batch_path):
            subprocess.run(batch_path, shell=True, check=True)
        else:
            messagebox.showwarning("Warning", f"Batch file not found: {batch}")

def run_merge_batch_files_and_play():
    """Runs the merge batch files for the selected name and plays the result video."""
    selected_name = selected_name_var.get()
    folder_name = NAME_TO_FOLDER[selected_name]
    uppercase_name = folder_name.upper()

    batch_files = [
        f"{uppercase_name}_7_MERGE.bat", 
        f"{uppercase_name}_8_MERGED_TO_MP4.bat"
    ]

    # Run merge batch files
    for batch in batch_files:
        batch_path = os.path.join(batch)
        if os.path.exists(batch_path):
            subprocess.run(batch_path, shell=True, check=True)
        else:
            messagebox.showwarning("Warning", f"Batch file not found: {batch}")
    
    # Play the result video after merge is complete
    play_result_video(folder_name)

def play_result_video(folder_name):
    """Plays the resulting video (result.mp4) using ffplay (which supports audio)."""
    result_video_path = os.path.join(folder_name, "result.mp4")

    if not os.path.exists(result_video_path):
        messagebox.showerror("Error", "Result video not found.")
        return
    
    # Use ffplay to play the video with audio
    subprocess.run(["ffplay", "-autoexit", result_video_path], shell=True)


    
    def update_frame():
        """Displays frames from the video in the Tkinter window."""
        ret, frame = cap.read()
        if ret:
            # Convert the frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(img)
            
            # Update the image in the label
            video_label.config(image=img_tk)
            video_label.image = img_tk
            
            # Call update_frame every 20ms to keep the video playing
            video_window.after(20, update_frame)
        else:
            cap.release()
            video_window.destroy()  # Close the window when video ends
    
    video_label = tk.Label(video_window)
    video_label.pack()
    
    # Start playing the video
    update_frame()

def remove_video():
    """Removes the selected target video."""
    global target_video_path
    target_video_path = None
    label_target_video.config(text="Drop a target video here")
    button_remove_target_video.pack_forget()

def copy_image_to_face_to_keep(image_path):
    """Copies the clicked image to the 'face_to_keep' folder and runs the batch file."""
    selected_name = selected_name_var.get()
    folder_name = NAME_TO_FOLDER[selected_name]
    aligned_path = os.path.join(folder_name, "data_dst", "aligned")
    face_to_keep_path = os.path.join(folder_name, "face_to_keep")

    # Create the 'face_to_keep' folder if it doesn't exist
    os.makedirs(face_to_keep_path, exist_ok=True)

    try:
        # Copy the image to the 'face_to_keep' folder
        shutil.copy(image_path, face_to_keep_path)

        # Run the corresponding batch file
        uppercase_name = folder_name.upper()
        batch_file = f"{uppercase_name}_3_CLEAR_UNWANTED_FACES.bat"
        batch_path = os.path.join(batch_file)
        
        if os.path.exists(batch_path):
            subprocess.run(batch_path, shell=True, check=True)
        else:
            messagebox.showwarning("Warning", f"Batch file not found: {batch_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy image: {e}")

def show_first_occurrences():
    """Opens a new window showing the first appearance of each subject."""
    selected_name = selected_name_var.get()
    folder_name = NAME_TO_FOLDER[selected_name]
    aligned_path = os.path.join(folder_name, "data_dst", "aligned")
    
    if not os.path.exists(aligned_path):
        messagebox.showerror("Error", f"No 'aligned' folder found for {selected_name}.")
        return

    first_occurrences = {}
    for file in sorted(os.listdir(aligned_path)):
        if file.endswith(".jpg"):
            subject_id = file.split("_")[1].split(".")[0]
            if subject_id not in first_occurrences:
                first_occurrences[subject_id] = os.path.join(aligned_path, file)

    if not first_occurrences:
        messagebox.showerror("Error", "No subject images found.")
        return

    # Display images in a new window
    viewer_window = Toplevel(root)
    viewer_window.title(f"First Appearances - {selected_name}")
    
    for subject_id, image_path in first_occurrences.items():
        img = Image.open(image_path).resize((150, 150))
        img_tk = ImageTk.PhotoImage(img)
        frame = tk.Frame(viewer_window)
        frame.pack(pady=5)

        tk.Label(frame, text=f"Subject {subject_id}").pack()
        
        # Make the image clickable
        img_label = tk.Label(frame, image=img_tk)
        img_label.image = img_tk  # Keep reference to avoid garbage collection
        img_label.pack()
        
        # Bind the image click event to copy the image
        img_label.bind("<Button-1>", lambda event, path=image_path: copy_image_to_face_to_keep(path))

root = TkinterDnD.Tk()
root.title("Deepfake Generator")

# UI Elements
label_name = tk.Label(root, text="Selected Name: ")
label_name.pack(pady=5)
selected_name_var = tk.StringVar(value="Emmanuel Macron")
dropdown = tk.OptionMenu(root, selected_name_var, *NAME_TO_FOLDER.keys())
dropdown.pack(pady=5)

# Target video section
def create_video_section(label_text):
    """Helper function to create video drop section."""
    frame = tk.Frame(root, width=400, height=150, bg="lightgray", relief="solid", bd=2)
    frame.pack_propagate(False)
    frame.pack(pady=5)
    label = tk.Label(frame, text=label_text, bg="lightgray")
    label.pack(expand=True)
    button_remove = tk.Button(root, text="X", command=remove_video, fg="red", font=("Arial", 12), relief="solid", width=3)
    button_remove.pack_forget()
    return frame, label, button_remove

target_frame, label_target_video, button_remove_target_video = create_video_section("Drop a target video here")

# Buttons
save_button = tk.Button(root, text="Extract Faces", command=save_videos, font=("Arial", 12), bg="green", fg="white")
save_button.pack(pady=10)

view_images_button = tk.Button(root, text="Select Target", command=show_first_occurrences, font=("Arial", 12), bg="blue", fg="white")
view_images_button.pack(pady=10)

merge_button = tk.Button(root, text="Merge Faces", command=run_merge_batch_files_and_play, font=("Arial", 12), bg="purple", fg="white")
merge_button.pack(pady=10)

# Register drop areas
target_frame.drop_target_register(DND_FILES)
target_frame.dnd_bind('<<Drop>>', lambda event: on_drop(event, "target"))

root.mainloop()
