# Os modules
import os

# current working directory
print("Current working directory:", os.getcwd())

# list files in the current directory
print("Files in current directory:", os.listdir('.'))

# create a new directory
os.makedirs('new_directory', exist_ok= True)
print("Directory 'new_directory' created.")

# remove the directory
os.rmdir('new_directory')
print("Directory 'new_directory' removed.")
