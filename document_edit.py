import tkinter as tk
from tkinter import filedialog

# ---------------- FUNCTIONS ----------------

def new_file():
    text_box.delete("1.0", tk.END)

def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        with open(file, "w") as f:
            f.write(text_box.get("1.0", tk.END))

def load_file():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        with open(file, "r") as f:
            content = f.read()

        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, content)

# ---------------- HEADING FUNCTIONS ----------------

def apply_tag(tag_name):
    try:
        start = text_box.index(tk.SEL_FIRST)
        end = text_box.index(tk.SEL_LAST)

        text_box.tag_add(tag_name, start, end)

    except:
        pass

def apply_h1():
    apply_tag("h1")

def apply_h2():
    apply_tag("h2")

def apply_h3():
    apply_tag("h3")

# ---------------- WINDOW ----------------

root = tk.Tk()
root.title("Z4 Editor")
root.geometry("800x500")

# ---------------- TOOLBAR ----------------

toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x")

# File buttons
new_btn = tk.Button(toolbar, text="New", command=new_file)
new_btn.pack(side="left")

load_btn = tk.Button(toolbar, text="Load", command=load_file)
load_btn.pack(side="left")

save_btn = tk.Button(toolbar, text="Save", command=save_file)
save_btn.pack(side="left")

# Space
space = tk.Label(toolbar, text="   ")
space.pack(side="left")

# Heading buttons
h1_btn = tk.Button(toolbar, text="H1", command=apply_h1)
h1_btn.pack(side="left")

h2_btn = tk.Button(toolbar, text="H2", command=apply_h2)
h2_btn.pack(side="left")

h3_btn = tk.Button(toolbar, text="H3", command=apply_h3)
h3_btn.pack(side="left")

p_btn = tk.Button(toolbar, text="P", command=lambda: apply_tag("P"))
p_btn.pack(side="left")
# ---------------- TEXT AREA ----------------

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

text_box = tk.Text(
    root,
    wrap="word",
    font=("Arial", 12),
    yscrollcommand=scrollbar.set
)

text_box.pack(expand=True, fill="both")

scrollbar.config(command=text_box.yview)

# ---------------- TAG STYLES ----------------

text_box.tag_configure(
    "h1",
    font=("Arial", 24, "bold")
)

text_box.tag_configure(
    "h2",
    font=("Arial", 18, "bold")
)

text_box.tag_configure(
    "h3",
    font=("Arial", 14, "bold")
)

text_box.tag_configure(
    "P",
    font=("Arial", 12)
)

# ---------------- START ----------------

root.mainloop()