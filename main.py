"""
main.py
-------------------
This script creates a compressed version of a selected directory, excluding certain files and folders based on .gitignore rules.
It then optimizes HTML, JS, CSS, and JSON files within the compressed directory using functions from the optimisation_def module.
"""

import os
import shutil
import minify_html
import requests
from tkinter import filedialog
from html_optimiser import optimisation_def as optimisation
from html_optimiser import gitignore_logic_v2 as gitignore

class MessagePrinter:
    """ Utility class for printing messages with temporary and final states.
    """
    def __init__(self):
        self.msg_length = 0

    def print_final(self, msg):
        """ Print a final message, clearing any temporary message first. """
        self.remove_tmp()
        print(msg)

    def print_tmp(self, msg):
        """ Print a temporary message that can be cleared later. """
        self.msg_length = len(msg)
        print(msg, end="", flush=True)

    def remove_tmp(self):
        """ Clear the last printed temporary message. """
        print("\b" * self.msg_length + " " * self.msg_length + "\b" * self.msg_length, end="")
        self.msg_length = 0

# Directory to be compressed

def main():
    """
    Main function to execute the directory compression and file optimization.
    """
    printer = MessagePrinter()

    source_folder_path = filedialog.askdirectory()
    if not source_folder_path:
        printer.print_final("No folder selected.")
        return

    compressed_folder_name = "compressed"
    compressed_folder_path = os.path.join(source_folder_path, compressed_folder_name)

    printer.print_tmp("Setting up compressed folder...")
    if os.path.exists(compressed_folder_path):
        printer.remove_tmp()
        printer.print_tmp("Deleting old compressed folder...")
        shutil.rmtree(compressed_folder_path)
        printer.print_final("Old compressed folder deleted.")
    os.makedirs(compressed_folder_path, exist_ok=True)
    printer.print_final("New compressed folder created.")

    printer.print_tmp("Copying files...")
    ignore_function = gitignore.create_ignore_function(source_folder_path, compressed_folder_name)
    shutil.copytree(source_folder_path, compressed_folder_path, ignore=ignore_function, dirs_exist_ok=True)
    printer.print_final("Files copied.")

    printer.print_tmp("Optimizing files...")
    for root, _, files in os.walk(compressed_folder_path):
        for file_name in files:
            printer.remove_tmp()
            printer.print_tmp(f"Optimizing {file_name}...")
            file_path = os.path.join(root, file_name)
            file_extension = os.path.splitext(file_path)[1]
            optimisation.mapping.get(file_extension, lambda x: None)(file_path)
    printer.print_final("Files optimized.")

if __name__ == "__main__":
    main()
