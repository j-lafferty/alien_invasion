import pygame

class Background():
    def __init__(self, screen):
        """Initialize the background and set its starting position."""
        self.screen = screen

        # Load the background image and get its rect.
        self.bg_image = pygame.image.load('images/background.bmp')

    def blitme(self):
        """Draw the background starting in the top left corner."""
        self.screen.blit(self.bg_image, (0, 0))