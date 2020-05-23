import tkinter as tk
from tkinter import ttk
from tkinter import font,filedialog,colorchooser,messagebox
import os
main_application=tk.Tk()
main_application.geometry("1200x800")
main_application.title("Vpad Text Editor")
main_application.wm_iconbitmap("icon.ico")
# -------------------------------------------- main menu -----------------------------------------------
main_menu=tk.Menu()
# file icons
new_icon=tk.PhotoImage(file="icons2/new.png")
open_icon=tk.PhotoImage(file="icons2/open.png")
save_icon=tk.PhotoImage(file="icons2/save.png")
save_as_icon=tk.PhotoImage(file="icons2/save_as.png")
exit_icon=tk.PhotoImage(file="icons2/exit.png")
# file menu
file_menu=tk.Menu(main_menu,tearoff=False)
########Edit icons
copy_icon=tk.PhotoImage(file="icons2/copy.png")
paste_icon=tk.PhotoImage(file="icons2/paste.png")
cut_icon=tk.PhotoImage(file="icons2/cut.png")
clear_all_icon=tk.PhotoImage(file="icons2/clear_all.png")
find_icon=tk.PhotoImage(file="icons2/find.png")
# edit menu
edit_menu=tk.Menu(main_menu,tearoff=False)
############view icons
toolbar_icon=tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon=tk.PhotoImage(file="icons2/status_bar.png")
# view menu
view_menu=tk.Menu(main_menu,tearoff=False)

########color theme icons
light_default_theme=tk.PhotoImage(file="icons2/light_default.png")
light_plus_theme=tk.PhotoImage(file="icons2/light_plus.png")
dark_theme=tk.PhotoImage(file="icons2/dark.png")
red_theme=tk.PhotoImage(file="icons2/red.png")
monokai_theme=tk.PhotoImage(file="icons2/monokai.png")
night_blue_theme=tk.PhotoImage(file="icons2/night_blue.png")
color_theme=tk.Menu(main_menu,tearoff=False)
theme_choice=tk.StringVar()
color_icons=(light_default_theme,light_plus_theme,dark_theme,red_theme,monokai_theme,night_blue_theme)

color_dict={
    "light default":("#000000","#ffffff"),
    "light plus":("#474747","#e0e0e0"),
    "dark":("#c4c4c4","#2d2d2d"),
    "red":("#d3b774","#474747"),
    "monokai":("#2d2d2d","#ffe8e8"),
    "night blue":("#000000","#ffffff")
}
# cascade
main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)
main_menu.add_cascade(label="View",menu=view_menu)
main_menu.add_cascade(label="Color Theme",menu=color_theme)

###################################################### main menu end #################################################
# -------------------------------------------- tool bar -----------------------------------------------

tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# font box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_box["values"]=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)
# size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state="readonly")
font_size["values"]=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)
# toolbar buttons
# bold button
bold_icon=tk.PhotoImage(file="icons2/bold.png")
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
#italic button
italic_icon=tk.PhotoImage(file="icons2/italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
#----underline button
underline_icon=tk.PhotoImage(file="icons2/underline.png")
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
#---font color button
font_color_icon=tk.PhotoImage(file="icons2/font_color.png")
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)
#left allignment button
align_left_icon=tk.PhotoImage(file="icons2/align_left.png")
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)
# centre alignment button
align_center_icon=tk.PhotoImage(file="icons2/align_center.png")
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)
#right alignment button
align_right_icon=tk.PhotoImage(file="icons2/align_right.png")
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)
###################################################### tool bar end #################################################
# -------------------------------------------- text editor -----------------------------------------------
text_editor=tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
scroll_bar.focus_set()
scroll_bar.pack(fill=tk.Y,side=tk.RIGHT)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
# font family and font size functionality
current_font_family="Arial"
current_font_size=12
def change_font(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_fontsize)

############buttons functionality
# bold button
def change_bold():
    text_property=tk.font.Font(font=text_editor["font"])
    if text_property.actual()["weight"]=="normal":
        text_editor.configure(font=(current_font_family,current_font_size,"bold"))
    if text_property.actual()["weight"]=="bold":
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
bold_btn.configure(command=change_bold)
###italic button
def change_italic():
    text_property=tk.font.Font(font=text_editor["font"])
    if text_property.actual()["slant"]=="roman":
        text_editor.configure(font=(current_font_family,current_font_size,"italic"))
    if text_property.actual()["slant"]=="italic":
        text_editor.configure(font=(current_font_family,current_font_size,"roman"))
italic_btn.configure(command=change_italic)
# under_line_button
def change_underline():
    text_property=tk.font.Font(font=text_editor["font"])
    if text_property.actual()["underline"]==0:
        text_editor.configure(font=(current_font_family,current_font_size,"underline"))
    if text_property.actual()["underline"]==1:
        text_editor.configure(font=(current_font_family,current_font_size,"normal"))
underline_btn.configure(command=change_underline)
# change color of text
def chnage_color_font():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=chnage_color_font)
######ALIGNMENT left
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

## center 
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

## right 
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)
text_editor.configure(font=("Arial",12))
###################################################### text editor end #################################################
# -------------------------------------------- main status bar -----------------------------------------------
status_bar=ttk.Label(main_application,text="Develop by Shehroz Kapoor")
status_bar.pack(side=tk.BOTTOM)
text_change=False
def changed(event=None):
    if text_editor.edit_modified():
        words = len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Character:{characters} words:{words}                       developed by:SHEHROZ KAPOOR')
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",changed)
###################################################### main status bar end ##########################################main status bar
# -------------------------------------------- main menu functionality -----------------------------------------------
# ------file menu commands
# new main menu functionality
url=''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)
file_menu.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+n",command=new_file)
# open main menu functionality
def open_file(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_application.title(os.path.basename(url))
file_menu.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="ctrl+o",command=open_file)
# save main menu functionality
def save_file(event=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return 
file_menu.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="ctrl+s",command=save_file)
def save_as(event=None):
    global url 
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return 
file_menu.add_command(label="Save As",image=save_as_icon,compound=tk.LEFT,accelerator="ctrl+alt+s",command=save_as)
# exit functionality
def exit_func(event=None):
    global url, text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        elif mbox is False:
            main_application.destroy()
    except:
        return 
file_menu.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="ctrl+q",command=exit_func)
# find functionality 
def find_func():
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()
# ----edit menu commands
edit_menu.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="ctrl+c",command=lambda:text_editor.event_generate("<Control c>"))
edit_menu.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
edit_menu.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="ctrlL+x",command=lambda:text_editor.event_generate("<Control x>"))
edit_menu.add_command(label="Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator="ctrl+alt+c",command=lambda:text_editor.delete(1.0,tk.END))
edit_menu.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator="ctrl+f",command=find_func)
# ------ view menu checkbuttons
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_toolbar.set(True)
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTTOM)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
       status_bar.pack(side=tk.BOTTOM)
       show_statusbar = True
view_menu.add_checkbutton(label="Tool Bar",onvalue=1,offvalue=0,variable=show_toolbar,image=toolbar_icon,compound=tk.LEFT,command=hide_toolbar)

view_menu.add_checkbutton(label="Status Bar",onvalue=1,offvalue=0,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)


#-------- color theme loop
def change_theme():
    choosen_theme = theme_choice.get()
    color_tuple= color_dict.get(choosen_theme)
    fg_color,bg_color= color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1 
###################################################### main menu functionality end #################################################



main_application.config(menu=main_menu)
#### bind shortcut keys 
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)

main_application.mainloop()