#➡️ File Opening Modes:
# When you open a file, you must specify a mode — it tells Python what you want to do with the file (read, write, append, etc.).

# Character / Meaning
# 'r' → Read (default) - Open for reading. The file must exist.
# 'w' → Write - Open for writing. Creates a new file or truncates an existing one.
# 'a' → Append - Open for writing. Creates a new file or appends to
# an existing one.
# 'x' → Exclusive Creation - Open for writing. Creates a new file, but fails if the file already exists.
# 'b' → Binary Mode - Open in binary mode (e.g., for images,
# audio). Can be combined with other modes (e.g., 'rb', 'wb').
# t → Text Mode (default) - Open in text mode. Can be combined with other modes (e.g., 'rt', 'wt').



# Examples:
# Open a file for reading (default)
file = open("myfile.txt", "r")
# Open a file for writing (creates or truncates)
file = open("myfile.txt", "w")
# Open a file for appending (creates or appends)
file = open("myfile.txt", "a")
# Open a file for exclusive creation (fails if exists)
file = open("myfile.txt", "x")
# Open a file in binary mode for reading
file = open("image.png", "rb")
# Open a file in text mode for writing
file = open("notes.txt", "wt")



#🎯 Pro tip:
# In real projects, 'w' mode is risky — it silently deletes all existing content! Use 'a' when you want to add to a file, or 'x' when you want to create a new file and not overwrite an old one.