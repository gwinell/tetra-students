import pygame

CELL = 80
OUTLINE = (30, 30, 30)


def draw_king(surf, cell_x, cell_y, color):
    temp = pygame.Surface((400, 400), pygame.SRCALPHA)
    cx, cy = 200, 200

    # большое основание
    w, h = 100, 30
    x, y = cx - w // 2, cy - h + 40
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # среднее основание
    w, h = 80, 20
    x, y = cx - w // 2, cy - h + 40 - 30
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # тело
    w, h = 50, 110
    x, y = cx - w // 2, cy - h + 40 - 30 - 20
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # голова
    w, h = 90, 25
    x, y = cx - w // 2, cy - h + 40 - 30 - 20 - 110
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # крест вертикальный
    w, h = 14, 50
    x, y = cx - w // 2, y - h
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # крест горизонтальный
    w, h = 44, 14
    x, y = cx - w // 2, y + 18
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    scaled = pygame.transform.scale(temp, (CELL, CELL))
    surf.blit(scaled, (cell_x, cell_y))


def draw_queen(surf, cell_x, cell_y, color):
    temp = pygame.Surface((400, 400), pygame.SRCALPHA)
    cx, cy = 200, 200

    # большое основание
    baseb_w = 100
    baseb_h = 30
    baseb_x = cx - baseb_w // 2
    baseb_y = cy - baseb_h + 40
    pygame.draw.rect(temp, OUTLINE, (baseb_x - 2, baseb_y - 2, baseb_w + 4, baseb_h + 4))
    pygame.draw.rect(temp, color, (baseb_x, baseb_y, baseb_w, baseb_h))

    # среднее основание
    baseb_w1 = 80
    baseb_h1 = 20
    baseb_x1 = cx - baseb_w1 // 2
    baseb_y1 = cy - baseb_h1 + 40 - baseb_h
    pygame.draw.rect(temp, OUTLINE, (baseb_x1 - 2, baseb_y1 - 2, baseb_w1 + 4, baseb_h1 + 4))
    pygame.draw.rect(temp, color, (baseb_x1, baseb_y1, baseb_w1, baseb_h1))

    # тело
    baseb_w2 = 50
    baseb_h2 = 120
    baseb_x2 = cx - baseb_w2 // 2
    baseb_y2 = cy - baseb_h2 + 40 - baseb_h1
    pygame.draw.rect(temp, OUTLINE, (baseb_x2 - 2, baseb_y2 - 2, baseb_w2 + 4, baseb_h2 + 4))
    pygame.draw.rect(temp, color, (baseb_x2, baseb_y2, baseb_w2, baseb_h2))

    # переход к голове
    baseb_w3 = 80
    baseb_h3 = 20
    baseb_x3 = cx - baseb_w3 // 2
    baseb_y3 = cy - baseb_h3 + 40 - baseb_h2
    pygame.draw.rect(temp, OUTLINE, (baseb_x3 - 2, baseb_y3 - 2, baseb_w3 + 4, baseb_h3 + 4))
    pygame.draw.rect(temp, color, (baseb_x3, baseb_y3, baseb_w3, baseb_h3))

    # голова
    baseb_w4 = 110
    baseb_h4 = 30
    baseb_x4 = cx - baseb_w4 // 2
    baseb_y4 = cy - baseb_h4 + 40 - baseb_h2
    pygame.draw.rect(temp, OUTLINE, (baseb_x4 - 2, baseb_y4 - 2, baseb_w4 + 4, baseb_h4 + 4))
    pygame.draw.rect(temp, color, (baseb_x4, baseb_y4, baseb_w4, baseb_h4))

    # пики
    baseb_w5 = baseb_w4 // 5
    baseb_h5 = 40
    baseb_x5 = baseb_x4
    baseb_y5 = baseb_y4 - baseb_h5
    pygame.draw.rect(temp, OUTLINE, (baseb_x5 - 2, baseb_y5 - 2, baseb_w5 + 4, baseb_h5 + 4))
    pygame.draw.rect(temp, color, (baseb_x5, baseb_y5, baseb_w5, baseb_h5))

    baseb_w6 = baseb_w5
    baseb_h6 = baseb_h5
    baseb_x6 = baseb_x5 + baseb_w6 * 2
    baseb_y6 = baseb_y5
    pygame.draw.rect(temp, OUTLINE, (baseb_x6 - 2, baseb_y6 - 2, baseb_w6 + 4, baseb_h6 + 4))
    pygame.draw.rect(temp, color, (baseb_x6, baseb_y6, baseb_w6, baseb_h6))

    baseb_w7 = baseb_w6
    baseb_h7 = baseb_h6
    baseb_x7 = baseb_x6 + baseb_w6 * 2
    baseb_y7 = baseb_y6
    pygame.draw.rect(temp, OUTLINE, (baseb_x7 - 2, baseb_y7 - 2, baseb_w7 + 4, baseb_h7 + 4))
    pygame.draw.rect(temp, color, (baseb_x7, baseb_y7, baseb_w7, baseb_h7))

    scaled = pygame.transform.scale(temp, (CELL, CELL))
    surf.blit(scaled, (cell_x, cell_y))


def draw_rook(surf, cell_x, cell_y, color):
    temp = pygame.Surface((400, 400), pygame.SRCALPHA)
    cx, cy = 200, 200

    # основание
    base_x = cx - 40
    base_y = cy + 20
    base_w = 80
    base_h = 25
    pygame.draw.rect(temp, OUTLINE, (base_x - 2, base_y - 2, base_w + 4, base_h + 4))
    pygame.draw.rect(temp, color, (base_x, base_y, base_w, base_h))

    # ствол
    body_x = cx - 20
    body_y = cy - 20
    body_w = 40
    body_h = 45
    pygame.draw.rect(temp, OUTLINE, (body_x - 2, body_y - 2, body_w + 4, body_h + 4))
    pygame.draw.rect(temp, color, (body_x, body_y, body_w, body_h))

    # голова с зубцами
    head_x = body_x - 10
    head_y = body_y - 20
    head_w = 60
    head_h = 20
    pygame.draw.rect(temp, OUTLINE, (head_x - 2, head_y - 2, head_w + 4, head_h + 4))
    pygame.draw.rect(temp, color, (head_x, head_y, head_w, head_h))

    # зубцы
    tooth_w = head_w // 5
    tooth_h = 12
    for i in range(5):
        tx = head_x + i * tooth_w
        ty = head_y - tooth_h
        pygame.draw.rect(temp, OUTLINE, (tx - 2, ty - 2, tooth_w + 4, tooth_h + 4))
        pygame.draw.rect(temp, color, (tx, ty, tooth_w, tooth_h))

    # центральная пика
    pygame.draw.rect(temp, OUTLINE, (cx - 12, body_y - 47, 24, 29))
    pygame.draw.rect(temp, color, (cx - 10, body_y - 45, 20, 25))

    scaled = pygame.transform.scale(temp, (CELL, CELL))
    surf.blit(scaled, (cell_x, cell_y))


def draw_bishop(surf, cell_x, cell_y, color):
    temp = pygame.Surface((400, 400), pygame.SRCALPHA)
    cx, cy = 200, 200

    # большое основание
    w, h = 100, 30
    x, y = cx - w // 2, cy - h + 40
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # среднее основание
    w, h = 80, 20
    x, y = cx - w // 2, cy - h + 40 - 30
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # тело
    w, h = 45, 100
    x, y = cx - w // 2, cy - h + 40 - 30 - 20
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # шапка (широкая)
    w, h = 70, 25
    x, y = cx - w // 2, y - h
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # верхушка шапки
    w, h = 40, 20
    x, y = cx - w // 2, y - h
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # шарик наверху
    w, h = 18, 18
    x, y = cx - w // 2, y - h
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # срез (ступенька справа)
    w, h = 10, 28
    x, y = cx + 18, cy - 90
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    scaled = pygame.transform.scale(temp, (CELL, CELL))
    surf.blit(scaled, (cell_x, cell_y))


def draw_knight(surf, cell_x, cell_y, color):
    temp = pygame.Surface((400, 400), pygame.SRCALPHA)
    cx, cy = 200, 200

    # основание
    w, h = 90, 25
    x, y = cx - w // 2, cy + 45
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # ноги
    leg_w, leg_h = 10, 40
    for lx in [cx - 28, cx - 10, cx + 10, cx + 28]:
        pygame.draw.rect(temp, OUTLINE, (lx - 2, cy + 5 - 2, leg_w + 4, leg_h + 4))
        pygame.draw.rect(temp, color, (lx, cy + 5, leg_w, leg_h))
        # копыта
        pygame.draw.rect(temp, OUTLINE, (lx - 2, cy + 40 - 2, leg_w + 4, 10 + 4))
        pygame.draw.rect(temp, (20, 20, 20), (lx, cy + 40, leg_w, 10))

    # тело
    w, h = 55, 35
    x, y = cx - w // 2, cy - 5
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # шея
    pygame.draw.rect(temp, OUTLINE, (cx + 15 - 2, cy - 35 - 2, 12 + 4, 35 + 4))
    pygame.draw.rect(temp, color, (cx + 15, cy - 35, 12, 35))
    pygame.draw.rect(temp, OUTLINE, (cx + 22 - 2, cy - 58 - 2, 12 + 4, 28 + 4))
    pygame.draw.rect(temp, color, (cx + 22, cy - 58, 12, 28))

    # голова
    w, h = 38, 24
    x, y = cx + 22, cy - 82
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # морда
    w, h = 20, 14
    x, y = cx + 55, cy - 74
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # ухо
    w, h = 8, 18
    x, y = cx + 28, cy - 100
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # грива
    for i, gx in enumerate([cx + 18, cx + 22, cx + 26]):
        gy = cy - 48 + i * 5
        pygame.draw.rect(temp, OUTLINE, (gx - 2, gy - 2, 5 + 4, 12 + 4))
        pygame.draw.rect(temp, color, (gx, gy, 5, 12))

    # хвост
    pygame.draw.rect(temp, OUTLINE, (cx - 42, cy - 7, 10 + 4, 6 + 4))
    pygame.draw.rect(temp, color, (cx - 40, cy - 5, 10, 6))
    pygame.draw.rect(temp, OUTLINE, (cx - 47, cy - 20, 6 + 4, 16 + 4))
    pygame.draw.rect(temp, color, (cx - 45, cy - 18, 6, 16))

    # глаз
    pygame.draw.rect(temp, OUTLINE, (cx + 44, cy - 78, 5, 5))

    scaled = pygame.transform.scale(temp, (CELL, CELL))
    surf.blit(scaled, (cell_x, cell_y))


def draw_pawn(surf, cell_x, cell_y, color):
    temp = pygame.Surface((400, 400), pygame.SRCALPHA)
    cx, cy = 200, 200

    # основание
    w, h = 80, 22
    x, y = cx - w // 2, cy + 45
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # среднее основание
    w, h = 55, 15
    x, y = cx - w // 2, cy + 30
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # тело
    w, h = 35, 60
    x, y = cx - w // 2, cy - 30
    pygame.draw.rect(temp, OUTLINE, (x - 2, y - 2, w + 4, h + 4))
    pygame.draw.rect(temp, color, (x, y, w, h))

    # голова (круг через ellipse)
    pygame.draw.ellipse(temp, OUTLINE, (cx - 27, cy - 77, 54, 54))
    pygame.draw.ellipse(temp, color, (cx - 25, cy - 75, 50, 50))

    scaled = pygame.transform.scale(temp, (CELL, CELL))
    surf.blit(scaled, (cell_x, cell_y))
