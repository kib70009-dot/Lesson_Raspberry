import pygame

# 初始化 Pygame
pygame.init()

# 遊戲視窗設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("俄羅斯方塊")

# 方塊大小
BLOCK_SIZE = 30

# 顏色定義 (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# 俄羅斯方塊形狀定義 (以 4x4 網格表示)
# 0 表示空，1 表示方塊實體
SHAPES = {
    'I': [
        [[0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0]]
    ],
    'O': [
        [[0, 0, 0, 0],
         [0, 1, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]]
    ],
    'T': [
        [[0, 0, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]],

        [[0, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]],

        [[0, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]
    ],
    'S': [
        [[0, 0, 0, 0],
         [0, 1, 1, 0],
         [1, 1, 0, 0],
         [0, 0, 0, 0]],

        [[0, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 0]]
    ],
    'Z': [
        [[0, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]],

        [[0, 0, 1, 0],
         [0, 1, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]
    ],
    'J': [
        [[0, 0, 0, 0],
         [1, 1, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 0]],

        [[0, 1, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 0, 0, 0]],

        [[1, 0, 0, 0],
         [1, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 1, 1, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]
    ],
    'L': [
        [[0, 0, 0, 0],
         [1, 1, 1, 0],
         [1, 0, 0, 0],
         [0, 0, 0, 0]],

        [[1, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]],

        [[0, 0, 1, 0],
         [1, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],

        [[0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]]
    ]
}

# 方塊顏色對應
COLORS = {
    'I': CYAN,
    'O': YELLOW,
    'T': PURPLE,
    'S': GREEN,
    'Z': RED,
    'J': BLUE,
    'L': ORANGE
}

# 遊戲板設定
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
# 遊戲板的左上角在螢幕上的位置
BOARD_OFFSET_X = (SCREEN_WIDTH - BOARD_WIDTH * BLOCK_SIZE) // 2
BOARD_OFFSET_Y = (SCREEN_HEIGHT - BOARD_HEIGHT * BLOCK_SIZE) // 2

# 字體設定
font = pygame.font.Font(None, 36) # 預設字體，大小 36

# 音樂和音效

# 初始化遊戲板 (用黑色代表空)
board = [[BLACK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# 繪製單一方塊
def draw_block(surface, color, row, col):
    pygame.draw.rect(surface, color, (BOARD_OFFSET_X + col * BLOCK_SIZE, BOARD_OFFSET_Y + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    pygame.draw.rect(surface, WHITE, (BOARD_OFFSET_X + col * BLOCK_SIZE, BOARD_OFFSET_Y + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1) # 邊框

# 繪製整個遊戲板
def draw_board(surface, board):
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if board[r][c] != BLACK:
                draw_block(surface, board[r][c], r, c)

import random

# 建立新的方塊
def create_new_block():
    shape_name = random.choice(list(SHAPES.keys()))
    shape = SHAPES[shape_name][0]  # 初始旋轉狀態
    color = COLORS[shape_name]
    # 初始位置 (頂部中央)
    x = BOARD_WIDTH // 2 - len(shape[0]) // 2
    y = 0
    return {'shape': shape, 'color': color, 'x': x, 'y': y, 'rotation_index': 0, 'shape_name': shape_name}

# 檢查碰撞 (偵測方塊是否到達底部或碰撞到其他方塊)
def check_collision(block, board, dx=0, dy=0):
    shape = block['shape']
    for r_offset, row in enumerate(shape):
        for c_offset, cell in enumerate(row):
            if cell == 1:
                board_x = block['x'] + c_offset + dx
                board_y = block['y'] + r_offset + dy

                # 檢查是否超出邊界
                if not (0 <= board_x < BOARD_WIDTH and 0 <= board_y < BOARD_HEIGHT):
                    return True
                # 檢查是否與已固定的方塊碰撞
                if board_y >= 0 and board[board_y][board_x] != BLACK:
                    return True
    return False

# 固定方塊到遊戲板上
def lock_block(block, board):
    shape = block['shape']
    for r_offset, row in enumerate(shape):
        for c_offset, cell in enumerate(row):
            if cell == 1:
                board_x = block['x'] + c_offset
                board_y = block['y'] + r_offset
                if 0 <= board_x < BOARD_WIDTH and 0 <= board_y < BOARD_HEIGHT:
                    board[board_y][board_x] = block['color']

# 消除滿行
def clear_lines(board):
    lines_cleared = 0
    r = BOARD_HEIGHT - 1
    while r >= 0:
        if BLACK not in board[r]: # 如果這一行是滿的
            lines_cleared += 1
            # 移除這一行並在頂部插入一個新行
            del board[r]
            board.insert(0, [BLACK for _ in range(BOARD_WIDTH)])
        else:
            r -= 1 # 檢查下一行
    return lines_cleared

# 遊戲狀態
game_state = 'start' # 'start', 'playing', 'game_over'

# 重置遊戲狀態
def reset_game():
    global board, current_block, next_block, score, level, fall_time, fall_speed, game_state
    board = [[BLACK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    current_block = create_new_block()
    next_block = create_new_block()
    score = 0
    level = 1 # 初始化等級
    fall_time = 0
    fall_speed = 500 # 毫秒

# 當前方塊
current_block = create_new_block()
next_block = create_new_block()

# 遊戲分數
score = 0
# 遊戲等級
level = 1

# 遊戲時鐘
clock = pygame.time.Clock()

# 掉落時間控制
fall_time = 0
fall_speed = 500 # 毫秒

# 遊戲迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == 'start':
            if event.type == pygame.KEYDOWN:
                game_state = 'playing'
                reset_game()
        elif game_state == 'game_over':
            if event.type == pygame.KEYDOWN:
                game_state = 'start' # 或 'playing' 直接開始新遊戲
                reset_game()
        elif game_state == 'playing':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(current_block, board, dx=-1):
                        current_block['x'] -= 1
                if event.key == pygame.K_RIGHT:
                    if not check_collision(current_block, board, dx=1):
                        current_block['x'] += 1
                if event.key == pygame.K_UP: # 旋轉方塊
                    original_rotation_index = current_block['rotation_index']
                    new_rotation_index = (original_rotation_index + 1) % len(SHAPES[current_block['shape_name']])
                    original_shape = current_block['shape']
                    current_block['shape'] = SHAPES[current_block['shape_name']][new_rotation_index]

                    if check_collision(current_block, board):
                        current_block['shape'] = original_shape # 恢復原狀
                        current_block['rotation_index'] = original_rotation_index
                    else:
                        current_block['rotation_index'] = new_rotation_index
                if event.key == pygame.K_DOWN: # 快速下降
                    while not check_collision(current_block, board, dy=1):
                        current_block['y'] += 1
                    lock_block(current_block, board)
                    lines_cleared = clear_lines(board) # 消除行
                    if lines_cleared == 1:
                        score += 100
                    elif lines_cleared == 2:
                        score += 300
                    elif lines_cleared == 3:
                        score += 500
                    elif lines_cleared == 4:
                        score += 800
                        pass  # 處理清除行數的邏輯
                    if lines_cleared > 0:

                    # 檢查升級
                        pass  # 清除行數大於0時的處理邏輯
                    if score >= level * 1000:
                        level += 1
                        fall_speed = max(100, 500 - (level - 1) * 50) # 速度加快

                    current_block = next_block
                    next_block = create_new_block()
                    if check_collision(current_block, board):
                        game_state = 'game_over' # 遊戲結束
                    fall_time = 0 # 重置掉落時間，避免立即再次掉落

    if game_state == 'playing':
        clock.tick() # 控制幀率
        fall_time += clock.get_rawtime()

        # 自動掉落
        if fall_time >= fall_speed:
            fall_time = 0
            if not check_collision(current_block, board, dy=1):
                current_block['y'] += 1
            else:
                lock_block(current_block, board)
                lines_cleared = clear_lines(board) # 消除行
                if lines_cleared == 1:
                    score += 100
                elif lines_cleared == 2:
                    score += 300
                elif lines_cleared == 3:
                    score += 500
                elif lines_cleared == 4:
                    score += 800
                if lines_cleared > 0:
                    pass  # 清除行數大於0時的處理邏輯

                # 檢查升級
                if score >= level * 1000:
                    level += 1
                    fall_speed = max(100, 500 - (level - 1) * 50) # 速度加快

                current_block = next_block
                next_block = create_new_block()
                if check_collision(current_block, board):
                    game_state = 'game_over' # 遊戲結束

    # 填充背景顏色
    screen.fill(BLACK)  # 黑色背景

    if game_state == 'start':
        title_text = font.render("俄羅斯方塊", True, WHITE)
        start_text = font.render("按任意鍵開始", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
    elif game_state == 'playing':
        # 繪製遊戲板
        draw_board(screen, board)

        # 繪製當前方塊
        for r_offset, row in enumerate(current_block['shape']):
            for c_offset, cell in enumerate(row):
                if cell == 1:
                    draw_block(screen, current_block['color'], current_block['y'] + r_offset, current_block['x'] + c_offset)

        # 顯示分數
        score_text = font.render(f"分數: {score}", True, WHITE)
        screen.blit(score_text, (BOARD_OFFSET_X + BOARD_WIDTH * BLOCK_SIZE + 50, BOARD_OFFSET_Y + 50))

        # 顯示等級
        level_text = font.render(f"等級: {level}", True, WHITE)
        screen.blit(level_text, (BOARD_OFFSET_X + BOARD_WIDTH * BLOCK_SIZE + 50, BOARD_OFFSET_Y + 80))

        # 顯示下一個方塊
        next_block_text = font.render("下一個", True, WHITE)
        screen.blit(next_block_text, (BOARD_OFFSET_X + BOARD_WIDTH * BLOCK_SIZE + 50, BOARD_OFFSET_Y + 130))
        for r_offset, row in enumerate(next_block['shape']):
            for c_offset, cell in enumerate(row):
                if cell == 1:
                    # 調整繪製位置，使其顯示在遊戲板右側的預覽區
                    draw_block(screen, next_block['color'], r_offset + (BOARD_OFFSET_Y + 180) // BLOCK_SIZE, c_offset + (BOARD_OFFSET_X + BOARD_WIDTH * BLOCK_SIZE + 50) // BLOCK_SIZE)
    elif game_state == 'game_over':
        game_over_title = font.render("遊戲結束", True, WHITE)
        final_score_text = font.render(f"最終分數: {score}", True, WHITE)
        restart_text = font.render("按任意鍵重新開始", True, WHITE)
        screen.blit(game_over_title, (SCREEN_WIDTH // 2 - game_over_title.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    # 更新顯示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
