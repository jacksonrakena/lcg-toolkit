"""
    'utils.py' - Jackson Rakena, 2021 - AS91906 Digital Technologies

    This file contains several reusable utility functions, removed
    from the main file for brevity.
"""

from tkinter import *

def delete_text_in_entry(entry):
    """
    This utility function deletes all text in a Tkinter Entry.
    """
    entry.delete(0, END)

def replace_text_in_entry(entry, text):
    """
    This utility function replaces all text in a Tkinter Entry widget with the
    provided text.
    """
    delete_text_in_entry(entry)
    entry.insert(0, text)

def compute_and_replace(widgets):
    """
    This utility function takes in a list of Tkinter Entry widgets, and attempts to check if the
    content of each widget is a valid number. If it is not, it attempts to calculate it (if it is a function,
    or mathematical formula) and replaces the contents with the result. Otherwise, it will
    replace it with 'Invalid'.
    """
    return_status = True

    for widget in widgets:
        try:
            int(widget.get())
        except ValueError: # contents are not a valid integer
            try:
                # Replace text with the evaluated result
                replace_text_in_entry(widget, int(eval(widget.get())))
            except:
                # Replace text with error message
                replace_text_in_entry(widget, 'Invalid')
                return_status = False
    return return_status

# Deprecated
def build(type):
    """
        (shorthand) Builds and packs a widget of 'type', and passes the provided kwargs
        to the widget's constructor.
    """
    type.pack()
    return type