#➡️ Files exist on disk, Python opens them into memory
# When you open a file, Python creates a connection (called a file object or file handle) between your program and that file. You then read/write through this handle. When done, you must close it to free up system resources.


# The basic pattern of File I/O in Python
file = open("myfile.txt", "r")   # open → get a file handle
content = file.read()             # read → do something with it
file.close()   

# Pro tip:
# Always close a file after you're done! Forgetting to close can cause data loss or file corruption. Python has a better way using 'with' — we'll cover that soon.