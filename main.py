import string
import time
from pynput import keyboard
from math import ceil
import sys
import tkinter as tk



def key_handeler_pressed(key) :
    global time1 , time_modifier , modified , no_of_modifier , key_was_aln , delay , op
    s_key = str( key )
    print( len( s_key ) , key )
    delay = ceil( (time.time_ns() - time1) / 1000000 )
    if s_key in modifier_key :
        modified = 0
        key_was_aln = 0
        if not modifier[s_key] :
            no_of_modifier += 1
        modifier[s_key] = 1
        # print( s_key , no_of_modifier , modified ,modifier )

    else :
        text.config( state='normal' )
        modifier_active = 0
        modifier_str = ''
        for x in modifier :
            if modifier[x] == 1 :
                modifier_active = 1
                modifier_str = f"{modifier_str}{special_keymap[x]}|"
                modified = 1
        modifier_str = modifier_str[:-1]
        # print( modifier_str )
        # print(s_key)
        if s_key in special_keymap_keys :
            key_was_aln = 0
        if time1 != 0 and not key_was_aln :
            co = f'''delay({delay});'''
            op += co
            text.insert(tk.INSERT,co+'\n')
        if (len( s_key ) == 4) & (s_key[0] == "'") :
            # print( modifier_str[:-1] )
            co = f'''keyboard.tapKey('\\\\');'''
            op += co
            text.insert( tk.INSERT , co + '\n' )
        elif s_key in special_keymap_keys :
            if s_key not in modifier_key :
                if modifier_active == 1 :
                    co = f'''keyboard.tapSpecialKey(({modifier_str}),{special_keymap[s_key]});'''
                    op += co
                    text.insert( tk.INSERT , co + '\n' )
                else :
                    co = f'''keyboard.tapSpecialKey({special_keymap[s_key]});'''
                    op += co
                    text.insert( tk.INSERT , co + '\n' )
        elif len( s_key ) == 3 and not (modifier["Key.ctrl_r"] == 1 or modifier["Key.ctrl_l"] == 1) :
            if s_key[1] in printables :
                if modifier_active and not (
                        (modifier["Key.shift_r"] == 1 or modifier["Key.shift"] == 1) and no_of_modifier == 1) :
                    key_was_aln = 0
                    co = f'''keyboard.tapKey(({modifier_str}),{s_key});'''
                    op += co
                    text.insert( tk.INSERT , co + '\n' )
                else :
                    key_was_aln = 1
                    co = f'''keyboard.tapKey({s_key});'''
                    op += co
                    text.insert( tk.INSERT , co + '\n' )
        elif s_key[0 :5] == "Key.f" :
            n = int( s_key[5 :] )
            if modifier_active :
                co = f'''keyboard.tapSpecialKey(({modifier_str}),F{n});'''
                op += co
                text.insert( tk.INSERT , co + '\n' )
            else :
                co = f'''keyboard.tapSpecialKey(F{n});'''
                op += co
                text.insert( tk.INSERT , co + '\n' )
        elif modifier["Key.ctrl_r"] == 1 or modifier["Key.ctrl_l"] == 1 :
            O_key = listner.canonical( key )
            O_key = str( O_key )
            if O_key[1] in printables :
                key_was_aln = 0
                co = f'''keyboard.tapKey(({modifier_str}),{O_key});'''
                op += co
                text.insert( tk.INSERT , co + '\n' )
        time_modifier = ceil( (time.time_ns() - time1) / 1000000 )
        time1 = time.time_ns()
        text.see( tk.END )
        text.config( state='disable' )
        # print( key , no_of_modifier , modified )


def key_handeler_relased(key) :
    global time1 , modified , no_of_modifier , delay , op
    text.config(state='normal')
    key = str( key )
    # delay = ceil( (time.time_ns() - time1) / 1000000 )
    if not modified :
        if key in modifier_key :
            if no_of_modifier == 1 :
                if time1 != 0 :
                    co = f'''delay({delay});'''
                    op += co
                    text.insert( tk.INSERT , co + '\n' )
                # print()
                co = f'''keyboard.tapSpecialKey({special_keymap[key]});'''
                op += co
                text.insert( tk.INSERT , co + '\n' )
                modifier[key] = 0
                time1 = time.time_ns()
        modified = 1
    if key in modifier_key :
        no_of_modifier -= 1
        modifier[key] = 0
    text.see(tk.END)
    text.config( state='disable' )
def button_start():
    global listner
    listner= keyboard.Listener( on_press=key_handeler_pressed , on_release=key_handeler_relased )
    listner.start()
    button['bg'] = 'green'
def on_exit() :
    with open( f"output{num}.txt" , "w" )as output :
        output.write( op )
    try:
        listner.stop()
    except:
        pass
    w.destroy()

    # print( key , no_of_modifier , modified )


if __name__ == '__main__' :
    num = int( sys.argv[1] )
    # num=int(input())
    special_keymap = {
        "Key.enter" : 'ENTER' ,
        "Key.esc" : "ESCAPE" ,
        "Key.backspace" : "BACKSPACE" ,
        "Key.tab" : "TAB" ,
        "Key.space" : "SPACEBAR",
        "Key.caps_lock" : "CAPSLOCK" ,
        "Key.print_screen" : "PRINTSCREEN" ,
        "Key.scroll_lock" : "SCROLLLOCK" ,
        "Key.pause" : "PAUSE" ,
        "Key.insert" : "INSERT" ,
        "Key.home" : "HOME" ,
        "Key.page_up" : "PAGEUP" ,
        "Key.delete" : "DELETE" ,
        "Key.end" : "END" ,
        "Key.page_down" : "PAGEDOWN" ,
        "Key.right" : "RIGHTARROW" ,
        "Key.left" : "LEFTARROW" ,
        "Key.down" : "DOWNARROW" ,
        "Key.up" : "UPARROW" ,
        "Key.num_lock" : "NUMLOCK" ,
        "Key.cmd" : "GUI" ,
        "Key.alt_l" : "ALT_L" ,
        "Key.alt_gr" : "ALT_R" ,
        "Key.menu" : "KEYBOARDAPPLICATION" ,
        "Key.shift" : "SHIFT_L" ,
        "Key.shift_r" : "SHIFT_R" ,
        "Key.ctrl_l" : "CTRL_L" ,
        "Key.ctrl_r" : "CTRL_R",
        "Key.media_volume_down" : "VOLUMEDOWN",
        "Key.media_volume_up" : "VOLUMEUP"
    }
    modifier = {
        "Key.cmd" : 0 ,
        "Key.alt_l" : 0 ,
        "Key.alt_gr" : 0 ,
        "Key.shift" : 0 ,
        "Key.shift_r" : 0 ,
        "Key.ctrl_l" : 0 ,
        "Key.ctrl_r" : 0
    }
    w=tk.Tk()
    w.geometry('500x400')
    w.title(f'programming for {num}')
    font=("Helvetica", "11")
    button=tk.Button(w,text='start',height=2, width=8,command=button_start)
    button.place(x=410,y=355)
    text=tk.Text(w,height=20, width=58,font=font)
    text.place(x=10,y=10)
    scroll = tk.Scrollbar( w )
    scroll.pack( side=tk.RIGHT , fill=tk.Y )
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    time1 = 0
    op = ''
    no_of_modifier = 0
    delay = 00
    modified = 0
    printables = string.punctuation + string.ascii_letters + string.digits
    modifier_key = modifier.keys()
    key_was_aln = 0
    special_keymap_keys = special_keymap.keys()
    time_modifier = 0
    w.protocol("WM_DELETE_WINDOW",on_exit)
    w.mainloop()
    print( "close me when you are done" )

