import pygame

class Car:
    def __init__(self, x, y, car_img, speed):
        self.x = x
        self.y = y
        self.scrolling_speed = speed
        self.car_image = pygame.transform.scale(car_img, (210, 200))
        self.car_rect = self.car_image.get_rect(center=(self.x, self.y))
    
    def update(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.scrolling_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.scrolling_speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.scrolling_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.scrolling_speed
        
        self.car_rect.center = (self.x, self.y)
    
    def draw(self, screen):
        screen.blit(self.car_image, self.car_rect)

    


        