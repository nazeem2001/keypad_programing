import tkinter as tk

w=0
def main() :
    global w
    with open( "template.txt" , "r" ) as template :
        sorce = template.readlines()
    code = []
    for i in range( 0 , 10 ) :
        try :
            with open( f'output{i}.txt' ) as line :
                code.append( line.readline() )
        except :
            code.append( ' ' )
    print( sorce )
    for i in range( 1 , 10 ) :
        sorce[
            i + 50] = f"case '{i}': digitalWrite(LED_BUILTIN, HIGH); {code[i]}  digitalWrite(LED_BUILTIN, LOW); break; \n"
    sorce[90] = f'digitalWrite(LED_BUILTIN, HIGH); {code[0]}digitalWrite(LED_BUILTIN, LOW); '

    print( code )
    with open( "code_final/code_final.ino" , "w" ) as output :
        output.writelines( sorce )
    w = tk.Tk()
    w.geometry( '400x60' )
    w.title( "done" )
    message = tk.Label( w , text="code generation was succesfull" )
    button = tk.Button( w , text='Done' , height=2 , width=8 , command=button_done )
    message.pack()
    button.place(x=320,y=17)
    w.mainloop()


def button_done() :
    global w
    w.destroy()

if __name__ == '__main__':
    main()
