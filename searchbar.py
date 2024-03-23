# import tkinter as tk
# from tkinter import messagebox

# def on_search_button_clicked():
#     search_term = search_entry.get()
#     if search_term:
#         highlight_and_search(search_term)
#     else:
#         messagebox.showwarning('Warning', 'Search term is empty')

# def highlight_and_search(search_term):
#     current_tags = list_box.tag_names()
#     for tag in current_tags:
#         list_box.tag_remove(tag, 1.0, tk.END)

#     search_start_index = 1.0
#     while True:
#         search_start_index = list_box.search(search_term, search_start_index, nocase=1)
#         if not search_start_index:
#             break
#         end_search_start_index = f"{search_start_index}+{len(search_term)}c"
#         list_box.tag_add(search_term, search_start_index, end_search_start_index)
#         search_start_index = end_search_start_index

#         # We can break after a certain number of matches if needed
#         # if number_of_matches >= 5:
#         #     break

# root = tk.Tk()
# root.geometry("300x400")

# search_entry = tk.Entry(root)
# search_entry.pack(pady=10)

# search_button = tk.Button(root, text="Search", command=on_search_button_clicked)
# search_button.pack(pady=5)

# list_box = tk.Listbox(root)
# list_box.pack(pady=10, fill=tk.BOTH, expand=True)

# for i in range(100):
#     list_box.insert(tk.END, f"Item {i + 1}")

# root.mainloop()

