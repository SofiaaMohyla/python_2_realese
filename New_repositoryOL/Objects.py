
class object:
    def __init__(self,x, y, w, h, img,):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))