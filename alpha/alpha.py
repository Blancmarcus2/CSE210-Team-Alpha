import random
import pygame

# Owamamwen Ogunniyi


def get_project():

    BLACK = (0,   0,   0)
    WHITE = (255, 255, 255)
    RED = (255,   0,   0)

    class Block(pygame.sprite.Sprite):

        def __init__(self, color, width, height):
            super().__init__()

            self.image = pygame.Surface([width, height])
            self.image.fill(color)

            self.rect = self.image.get_rect()
# End Owamamwen Ogunniyi

# Taylor Paxman
    # Initialize the  Pygame
    pygame.init()
    pygame.display.set_caption("Block Game")

    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 400
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    block_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    for i in range(10):

        block = Block(BLACK, 20, 15)

        block.rect.x = random.randrange(SCREEN_WIDTH)
        block.rect.y = random.randrange(SCREEN_HEIGHT)

        block_list.add(block)
        all_sprites_list.add(block)

# End Taylor Paxman

# Marcus Blanc
    player = Block(RED, 20, 15)
    all_sprites_list.add(player)

    done = False

    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)

    score = 0

    level = 1

# End Marcus Blanc

# Noah Blevins
    # -------- Main Program Loop -----------
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pos = pygame.mouse.get_pos()

        player.rect.x = pos[0]
        player.rect.y = pos[1]

        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        for block in blocks_hit_list:
            score += 1
            print(score)

        if len(block_list) == 0:

            level += 1

            for i in range(level * 10):

                block = Block(BLACK, 20, 15)

                block.rect.x = random.randrange(SCREEN_WIDTH)
                block.rect.y = random.randrange(SCREEN_HEIGHT)

                block_list.add(block)
                all_sprites_list.add(block)
# End Noah Blevins

# Josh
        screen.fill(WHITE)

        all_sprites_list.draw(screen)

        text = font.render("Score: "+str(score), True, BLACK)
        screen.blit(text, [10, 10])

        text = font.render("Level: "+str(level), True, BLACK)
        screen.blit(text, [10, 40])

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

    # End Josh
