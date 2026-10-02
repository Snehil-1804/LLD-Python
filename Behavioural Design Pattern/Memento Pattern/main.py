from history import History
from text_memento import TextMemento
from text_editor import TextEditor

text_editor=TextEditor()
history = History()

text_editor.write("Hello")
text_editor.write(" World")
# print(text_editor.get_text())
history.save_state(text_editor.save())


text_editor.write(" Good")
text_editor.write(" Bye")
history.save_state(text_editor.save())

print(text_editor.get_text())
history.get_history()

print("--------------------------------------------")

# print(history.undo().get_saved_text())

print("---------------------------------------------")
text_editor.restore(history.undo())
print(text_editor.get_text())
text_editor.restore(history.undo())
print(text_editor.get_text())