def solution():
    def draw_line(length, tick=''):
        s=('-'*length)
        if tick:
            s+=' '+tick
        print(s)
    def draw_interval(centerlength):
        if centerlength>0:
            draw_interval(centerlength-1)
            draw_line(centerlength)
            draw_interval(centerlength-1)
    def english_ruler(length, tick):
        draw_line(tick, str(0))
        for i in range(1, length+1):
            draw_interval(tick-1)
            draw_line(tick,str(i))
    english_ruler(4,3)
def my_ver():
    def draw_tick(length, num=''):
        if num:
            print('-' * length, f' {num}')
        else:
            print('-' * length)

    def recursive_draw(length):
        if length == 0:
            return 0
        recursive_draw(length - 1)
        draw_tick(length)
        recursive_draw(length - 1)

    def draw_ruler(tick, length):
        draw_tick(tick, '0')
        for j in range(1, length + 1):
            recursive_draw(tick - 1)
            draw_tick(tick, str(j))
    draw_ruler(3, 5)

my_ver()

