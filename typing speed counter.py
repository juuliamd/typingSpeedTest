import pygame as pg
import sys
import random
import time

pg.init()
width, height = 1440, 940
win = pg.display.set_mode((width, height))
pg.display.set_caption("TYPING SPEED")

# themes

theme_list = [
    [(50, 52, 55), (208, 209, 197), (226, 183, 20)],
    [(241, 250, 238), (29, 53, 87), (230, 57, 70)]
]
theme = 2
# fonts
text_font = pg.font.Font('LTBinaryNeue.ttf', 25)
time_font = pg.font.Font('LTBinaryNeue.ttf', 45)

###

'''
count = 0
line = 0
correct_char = 0
correct_st = ''
x_cur, y_cur = width / 5-6, height / 2
'''


###

def draw_board(x, st, start=0, end=0):
    win.fill(bg) #wypelnianie kolorem

    theme_info = text_font.render('TAB-refresh/theme change', 1, timer_colour)
    win.blit(theme_info, (10, 10))
    x_t, y_t = width / 5, height / 2

    words_per_row = 8  # slowa na row
    for i in range(line, min(line + words_per_row, len(x))):
        word = x[i]
        text = text_font.render(word, 1, text_colour)
        text.set_alpha(125)
        win.blit(text, (x_t, y_t))
        x_t += text.get_width() + 10  # odstepy miedzy slowami

    x_st, y_st = width / 5, height / 2

    for j in st:
        text_c = text_font.render(j, 1, text_colour)
        win.blit(text_c, (x_st, y_st))
        x_st += text_c.get_width()
        if count == 0:
            x_st = width / 5

    cursor = text_font.render('|', 1, timer_colour)
    win.blit(cursor, (x_cur, y_cur))
    if end - start <= 30:
        time = time_font.render(str(30 - int(end - start)), 1, timer_colour)
        win.blit(time, (width / 5, height / 2 - 50))
    pg.display.update()


def change_theme():
    global theme
    if theme == 1:
        theme = 2
    else:
        theme = 1
    start_val()


def main():
    global line, correct_st, cur_move, x_cur, theme
    global correct_char, smooth, stop_cur, cur_move, start, end
    run = True
    line = 0
    start = 0
    end = 0
    correct_char = 0
    clock = pg.time.Clock()

    type_list = []
    for i in range(20):
        type_list.append(word_seq(sequence()))

    start_val()

    while run:

        clock.tick(120) #fps
        if count == len(type_list[line]):
            start_val()
            line += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if start == 0:
                    start = time.time()
                if event.key == pg.K_TAB:
                    change_theme()
                    main()

                verify(event.key, type_list)

            if cur_move:
                x_cur += 4.7
                smooth += 4.7
                if smooth == stop_cur:
                    cur_move = False

            if int(end - start) == 30:
                run = False
                wpm_page(correct_char)
        end = time.time()
        draw_board(type_list, correct_st, start, end)
    main()


def start_val():
    global count, line, correct_st, x_cur, y_cur, cur_move, smooth, stop_cur
    global bg, text_colour, timer_colour
    count = 0
    correct_st = ''
    x_cur, y_cur = width / 5 - 6, height / 2
    cur_move = False
    smooth = 0
    stop_cur = 0

    # colours
    bg = theme_list[theme - 1][0]
    text_colour = theme_list[theme - 1][1]
    timer_colour = theme_list[theme - 1][2]


def sequence():  #sekwencja długości słów
    li = []
    while sum(li) < 50:
        li.append(random.randint(1, 11))
        if sum(li) > 50:
            li.pop()

        return li


def word_seq(li):  #sekwencję słów o określonej długości
    st = ''
    with open('words.txt') as file:
        rec = file.readlines()
    rec_words = [i.rstrip('\n') for i in rec]
    for i in li:
        word_list = [x for x in rec_words if len(x) == i]
        st += random.choice(word_list).lower()
        st += ' '

    return st


def verify(a, l): #sprawdzanie poprawności pwrowadzanych liter
    global count, correct_char, line, correct_st, cur_move, stop_cur

    if alphabet(a) == l[line][count]:
        correct_st += l[line][count]
        correct_char += 1
        stop_cur += text_font.render(l[line][count], 1, (0, 0, 0)).get_width()
        count += 1
        cur_move = True
    else:
        #
        cur_move = False

    # print(count)


def alphabet(a):
    if a == pg.K_a:
        return 'a'
    if a == pg.K_b:
        return 'b'
    if a == pg.K_c:
        return 'c'
    if a == pg.K_d:
        return 'd'
    if a == pg.K_e:
        return 'e'
    if a == pg.K_f:
        return 'f'
    if a == pg.K_g:
        return 'g'
    if a == pg.K_h:
        return 'h'
    if a == pg.K_i:
        return 'i'
    if a == pg.K_j:
        return 'j'
    if a == pg.K_k:
        return 'k'
    if a == pg.K_l:
        return 'l'
    if a == pg.K_m:
        return 'm'
    if a == pg.K_n:
        return 'n'
    if a == pg.K_o:
        return 'o'
    if a == pg.K_p:
        return 'p'
    if a == pg.K_q:
        return 'q'
    if a == pg.K_r:
        return 'r'
    if a == pg.K_s:
        return 's'
    if a == pg.K_t:
        return 't'
    if a == pg.K_u:
        return 'u'
    if a == pg.K_v:
        return 'v'
    if a == pg.K_w:
        return 'w'
    if a == pg.K_x:
        return 'x'
    if a == pg.K_y:
        return 'y'
    if a == pg.K_z:
        return 'z'
    if a == pg.K_MINUS:
        return '-'
    if a == pg.K_SPACE:
        return ' '
    if a == pg.K_QUOTE:
        return "'"


def wpm_page(correct_char):
    run = True

    while run:

        win.fill(bg)
        wpm = time_font.render('WPM: ' + str(correct_char / 2.5), 1, timer_colour)
        wid = wpm.get_width()
        win.blit(wpm, ((width // 2) - (wid // 2), height / 2.5))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    run = False
                    main()

        pg.display.update()


if __name__ == '__main__':
    main()