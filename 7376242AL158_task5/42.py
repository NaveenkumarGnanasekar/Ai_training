import os
path = "/some/directory"
if os.path.exists(path):
    print("Directory exists")
else:
    print("Directory does NOT exist")