# Input multiple filenames
filename = input(
    "Input multiple file names in a proper format:\n"
    "Eg: xyz.zip,abc.img,demi.god\nInput: "
).strip().lower()

file_list = filename.split(",")

# Dictionary of file types
file_type = {
    "Images": [".jpg", ".gif", ".png"],
    "Text": [".txt", ".pdf", ".doc"]
}

# Loop through each filename
for ext in file_list:
    found = False  # Flag to check if a match is found
    for fn, ft in file_type.items():
        if ext.endswith(tuple(ft)):
            print(ext, "->", fn)
            found = True
            break  # Stop checking other types if matched
    if not found:
        print(ext, "-> Unknown ⚠️")