import string
import time
from pynput.keyboard._win32 import KeyCode
from pynput import keyboard
from math import ceil
import sys

num = int( sys.argv[1] )
# num=int(input("enter the button number(0-9):"))
# if num>9:
#    raise ValueError("enter valid value")
special_keymap = {
    "Key.enter": 'ENTER' , "Key.esc": "ESCAPE" , "Key.backspace": "BACKSPACE" , "Key.tab": "TAB" ,
    "Key.space": "SPACEBAR" ,
    "Key.caps_lock": "CAPSLOCK" , "Key.print_screen": "PRINTSCREEN" , "Key.scroll_lock": "SCROLLLOCK" ,
    "Key.pause": "PAUSE" ,
    "Key.insert": "INSERT" , "Key.home": "HOME" , "Key.page_up": "PAGEUP" , "Key.delete": "DELETE" , "Key.end": "END" ,
    "Key.page_down": "PAGEDOWN" , "Key.right": "RIGHTARROW" , "Key.left": "LEFTARROW" , "Key.down": "DOWNARROW" ,
    "Key.up": "UPARROW" , "Key.num_lock": "NUMLOCK" , "Key.cmd": "GUI" , "Key.alt_l": "ALT" , "Key.alt_gr": "ALT" ,
    "Key.menu": "KEYBOARDAPPLICATION" , "Key.shift": "SHIFT" , "Key.shift_r": "SHIFT"
}
modifier = {"Key.cmd": 0 , "Key.alt_l": 0 , "Key.alt_gr": 0 , "Key.shift": 0 , "Key.shift_r": 0}
time1 = 0
output = open( f"output{num}.txt" , "w" )
output.close()
no_of_modifier = 0
modified = 0
printables = list( string.punctuation + string.ascii_letters + string.digits )
ctrl = 0
ctrl_m = 0
modifier_key = modifier.keys()
key_was_aln = 0
special_keymap_keys = special_keymap.keys()

time_modifier = 0


def key_handeler_pressed(key):
    global time1 , ctrl , time_modifier , modified , ctrl_m , no_of_modifier , key_was_aln
    key = str( key )
    print( len( key ) , key , ctrl )

    delay = ceil( (time.time_ns() - time1) / 1000000 )

    if key in modifier_key or ((key == "Key.ctrl_l") or (key == "Key.ctrl_r")):
        modified = 0
        key_was_aln = 0
        if time1 != 0:
            if (key != "Key.ctrl_l") and (key != "Key.ctrl_r"):
                if not modifier[key]:
                    no_of_modifier += 1
                modifier[key] = 1

        pass
    else:
        if ctrl == 0:
            modifier_active = 0
            modifier_str = ''
            for x in modifier:
                if modifier[x] == 1:
                    modifier_active = 1
                    modifier_str = f"{modifier_str}{special_keymap[x]}|"
                    modified = 1
            modifier_str = modifier_str[:-1]
            print( modifier_str )
            if key in special_keymap_keys:
                key_was_aln = 0

            if time1 != 0 and not key_was_aln:
                print( f'''delay({delay});''' , end=" " )
                with open( f"output{num}.txt" , "a" )as output:
                    output.write( f'''delay({delay}); ''' )

            if (len( key ) == 4) & (key[0] == "'"):
                print( modifier_str[:-1] )
                print( f'''keyboard.tapKey('\\');''' , end=" " )
                with open( f"output{num}.txt" , "a" )as output:
                    output.write( f'''keyboard.tapKey('\\'); ''' )
            if key in special_keymap_keys:
                if key not in modifier_key:
                    if modifier_active == 1:
                        print( f'''keyboard.tapSpecialKey(({modifier_str}),{special_keymap[key]});''' , end=" " )
                        with open( f"output{num}.txt" , "a" )as output:
                            output.write( f'''keyboard.tapSpecialKey(({modifier_str}),{special_keymap[key]}); ''' )
                    else:
                        print( f'''keyboard.tapSpecialKey({special_keymap[key]});''' , end=" " )
                        with open( f"output{num}.txt" , "a" )as output:
                            output.write( f'''keyboard.tapSpecialKey({special_keymap[key]}); ''' )
            if len( key ) == 3:

                if key[1] in printables:
                    if modifier_active and not (
                            (modifier["Key.shift_r"] == 1 or modifier["Key.shift"] == 1) and no_of_modifier == 1):
                        key_was_aln = 0
                        print( f'''keyboard.tapKey(({modifier_str}),{key});''' , end=" " )
                        with open( f"output{num}.txt" , "a" )as output:
                            output.write( f'''keyboard.tapKey(({modifier_str}),{key}); ''' )
                    else:
                        key_was_aln = 1
                        print( f'''keyboard.tapKey({key});''' , end=" " )
                        with open( f"output{num}.txt" , "a" )as output:
                            output.write( f'''keyboard.tapKey({key}); ''' )

            if key[0:5] == "Key.f":
                n = int( key[5:] )
                if modifier_active:
                    print( f'''keyboard.tapSpecialKey(({modifier_str}),F{n});''' , end=" " )
                    with open( f"output{num}.txt" , "a" )as output:
                        output.write( f'''keyboard.tapSpecialKey(({modifier_str}),F{n}); ''' )

            time_modifier = ceil( (time.time_ns() - time1) / 1000000 )
        if (key == "Key.ctrl_l") or (key == "Key.ctrl_r"):
            ctrl = 1
            ctrl_m = 0

        if ctrl == 1:
            modified = 1
            ctrl_m = 1
            modifier_active = 0
            modifier_str = ''
            for x in modifier:
                if modifier[x] == 1:
                    modifier_active = 1
                    modifier_str = f"{modifier_str}{special_keymap[x]}|"
            modifier_str = modifier_str[:-1]
            print( modifier_str[:-1] )

            if time1 != 0:
                print( f'''delay({delay});''' , end=" " )
                with open( f"output{num}.txt" , "a" )as output:
                    output.write( f'''delay({delay}); ''' )
            if len( key ) <= 6:

                if key[2] == 'x':

                    key1 = key[3:5]
                    char = (string.ascii_lowercase + "[\]")[int( key1 , 16 ) - 1]
                    if modifier_active:
                        print( f'''keyboard.tapKey((CTRL|{modifier_str}),'{char}');''' , end=" " )
                        with open( f"output{num}.txt" , "a" )as output:
                            output.write( f'''keyboard.tapKey((CTRL|{modifier_str}),'{char}'); ''' )
                    else:
                        print( f'''keyboard.tapKey(CTRL,'{char}');''' , end=" " )
                        with open( f"output{num}.txt" , "a" )as output:
                            output.write( f'''keyboard.tapKey(CTRL,'{char}'); ''' )
                if (key[0] == '<') & (len( key ) == 4):
                    numb = int( key[1:3] ) - 48
                    if numb < 10 and numb > -1:
                        if modifier_active:
                            print( f'''keyboard.tapKey((CTRL|{modifier_str}),'{numb}');''' , end=" " )
                            with open( f"output{num}.txt" , "a" )as output:
                                output.write( f'''keyboard.tapKey((CTRL|{modifier_str}),'{numb}'); ''' )
                        else:
                            print( f'''keyboard.tapKey(CTRL,'{numb}');''' , end=" " )
                            with open( f"output{num}.txt" , "a" )as output:
                                output.write( f'''keyboard.tapKey(CTRL,'{numb}'); ''' )

                if key[0:5] == "Key.f":
                    n = int( key[5:] )
                    if modifier_active:
                        print( f'''keyboard.tapSpecialKey((CTRL|{modifier_str}),F{n});''' , end=" " )
                        with open( f"output{num}.txt" , "a" )as output:
                            output.write( f'''keyboard.tapSpecialKey((CTRL|{modifier_str}),F{n}); ''' )
            else:
                if modifier_active:
                    print( f'''keyboard.tapSpecialKey((CTRL|{modifier_str}),{special_keymap[key]});''' , end=" " )
                    with open( f"output{num}.txt" , "a" )as output:
                        output.write( f'''keyboard.tapSpecialKey((CTRL|{modifier_str}),{special_keymap[key]}); ''' )
            # ctrl=0

        time1 = time.time_ns()


def key_handeler_relased(key):
    global time1 , ctrl , modified , ctrl_m , no_of_modifier
    print( key , ctrl , ctrl_m , no_of_modifier , modified )
    key = str( key )
    delay = ceil( (time.time_ns() - time1) / 1000000 )
    if not modified or ctrl or ctrl_m:
        if (ctrl == 1) & ((key == 'Key.ctrl_l') | (key == 'Key.ctrl_r')):
            if (ctrl_m == 0):
                if time1 != 0:
                    print( f'''delay({delay});''' , end=" " )
                    with open( f"output{num}.txt" , "a" )as output:
                        output.write( f'''delay({delay}); ''' )
                time1 = time.time_ns()

                print( f'''keyboard.tapSpecialKey(CTRL);''' , end=" " )
                with open( f"output{num}.txt" , "a" )as output:
                    output.write( f'''keyboard.tapSpecialKey(CTRL); ''' )
            ctrl = 0
            ctrl_m = 0
        if key in modifier_key:

            if no_of_modifier == 1:
                if time1 != 0:
                    print( f'''delay({delay});''' , end=" " )
                    with open( f"output{num}.txt" , "a" )as output:
                        output.write( f'''delay({delay}); ''' )
                print()
                print( f'''keyboard.tapSpecialKey({special_keymap[key]});''' , end=" " )
                with open( f"output{num}.txt" , "a" )as output:
                    output.write( f'''keyboard.tapSpecialKey({special_keymap[key]}); ''' )
                modifier[key] = 0
                time1 = time.time_ns()
        modified = 1
    if key in modifier_key:
        no_of_modifier -= 1
        modifier[key] = 0


# print( string.punctuation + string.ascii_letters + string.digits )

# 10
# print( dir( KeyCode ) )
print( "close me when you are done" )
with keyboard.Listener( on_press=key_handeler_pressed , on_release=key_handeler_relased ) as listener:
    listener.join()
