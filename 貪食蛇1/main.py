import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 視窗尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("貪食蛇")

# 顏色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 蛇的設定
snake_block = 20

clock = pygame.time.Clock()

# 字型設定
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_score(score):
    """顯示分數"""
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def our_level(level):
    """顯示等級"""
    value = score_font.render("Level: " + str(level), True, yellow)
    screen.blit(value, [screen_width - 150, 0])

def draw_snake(snake_block, snake_list):
    """繪製蛇的身體"""
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """在螢幕上顯示訊息"""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def game_loop():
    """
    遊戲主迴圈
    返回 True 表示要徹底退出遊戲，返回 False 表示僅結束本局。
    """
    game_over = False
    game_close = False

    # 蛇的初始位置
    x1 = screen_width / 2
    y1 = screen_height / 2

    # 蛇的位置變化量
    x1_change = 0
    y1_change = 0

    # 蛇的身體
    snake_list = []
    length_of_snake = 1

    # 食物的位置
    foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0

    # 等級和速度
    level = 1
    snake_speed = 10
    food_eaten_in_level = 0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            our_score(length_of_snake - 1)
            our_level(level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        # 返回 True，通知 main 函式退出
                        return True
                    if event.key == pygame.K_c:
                        # 不要遞迴呼叫，直接返回，讓主迴圈重新開始
                        return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 返回 True，通知 main 函式退出
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        our_score(length_of_snake - 1)
        our_level(level)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            food_eaten_in_level += 1

            if food_eaten_in_level >= 5:
                level += 1
                snake_speed += 2
                food_eaten_in_level = 0


        clock.tick(snake_speed)

    # 如果是因為撞牆或關閉視窗導致 game_over，也返回 True
    return True

def main():
    """遊戲進入點，控制遊戲是否要不斷重玩"""
    # 如果 game_loop 返回 False (重玩)，迴圈繼續
    while not game_loop():
        pass # 繼續下一局

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
