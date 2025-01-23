import pygame
from colors import WHITE, BLACK
from road import Road
from car import Car
from hole import Hole
from forest import Forest

class Game:

    def __init__(self):
        self.speed = 1
        self.WIDTH, self.HEIGHT = 1100, 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        hole_path = "data/images/hole.png"
        car_path = "data/images/car.png"
        forest_path = "data/images/forest.jpg"
        road_path = "data/images/road.png"

        pygame.mixer.init()
        pygame.mixer.music.load("data/music/car_movement.mp3")
        pygame.mixer.music.play(-1)
        crash_sound = "data/music/crash.mp3"
        self.crash_sound = pygame.mixer.Sound(crash_sound)
        self.road_img = pygame.image.load(road_path).convert_alpha()
        self.hole_img = pygame.image.load(hole_path)
        self.car_img = pygame.image.load(car_path)
        self.forest_img = pygame.image.load(forest_path)


        pygame.display.set_caption("Retro Racer")
        self.clock = pygame.time.Clock()

    def draw_text(self, text, x, y, font, color):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def game_loop(self):
        running = True
        car = Car(self.WIDTH // 2, self.HEIGHT // 2 + 150, self.car_img, self.speed)
        road = Road(self.HEIGHT, self.WIDTH, self.road_img, self.speed)
        hole = Hole(self.HEIGHT, self.hole_img, self.speed)
        forest = Forest(self.HEIGHT, self.forest_img, self.speed)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            car.update(keys)
            forest.draw(self.screen)
            road.draw(self.screen)
            hole.draw(self.screen)
            car.draw(self.screen)
            road.update()
            hole.update()
            forest.update()

            if car.car_rect.colliderect(hole.hole_rect):
                self.crash_sound.play()
                self.draw_text("Игра окончена", 64, BLACK, self.WIDTH//3, self.HEIGHT//3)
                pygame.display.update()
                pygame.time.delay(2000)  # Подождите 2 секунды перед выходом
                running = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()

