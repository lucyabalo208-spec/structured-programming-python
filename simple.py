from stanfordkarel import *
print('Karel library imported succesfull!')

def  main():
    move()
    put_beeper()
    move()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper() 
    move()
    turn_right()
    move()
    put_beeper()
    move()
    turn_right()
    move()
    put_beeper()
    move()
    move()
    turn_right()
    finish()

def turn_right():
    for i in range(3):
        turn_left()
        

def move_twice():
        move()
        move()
        move()
def move_down():
    for i in range(3):
        move()

def finish():
    for i in range(3):
        move()
        
    pick_beeper()
def move_down():
    for i in range():
        move()

if __name__ == '__main__':
    run_karel_program()  


           