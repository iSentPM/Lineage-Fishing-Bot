
import random


def randomFirstPanel(verib):
    if (verib == 1):
        Typelist = [DIK_6, DIK_7, DIK_8, DIK_9, DIK_0]
    elif verib == 2:
        Typelist = [DIK_1, DIK_2, DIK_3, DIK_4, DIK_5]
    elif verib == 3:
        Typelist = [DIK_Q, DIK_E, DIK_R, DIK_T]
    elif verib == 4:
        Typelist = [DIK_Y, DIK_U, DIK_I]
    elif verib == 5:
        Typelist = [DIK_O, DIK_P]
    keytup = random.choice(Typelist)
    return keytup




DIK_1 = 0x02
DIK_2 = 0x03
DIK_3 = 0x04
DIK_4 = 0x05
DIK_5 = 0x06
DIK_6 = 0x07
DIK_7 = 0x08
DIK_8 = 0x09
DIK_9 = 0x0A
DIK_0 = 0x0B

DIK_Q = 0x10
DIK_E = 0x12
DIK_R = 0x13
DIK_T = 0x14
DIK_Y = 0x15
DIK_U = 0x16
DIK_I = 0x17
DIK_O = 0x18
DIK_P = 0x19

DIK_F1 = 0x3B
DIK_F2 = 0x3C
DIK_F3 = 0x3D
DIK_F4 = 0x3E
DIK_F5 = 0x3F
DIK_F6 = 0x40
DIK_F7 = 0x41
DIK_F8 = 0x42
DIK_F9 = 0x43
DIK_F10 = 0x44