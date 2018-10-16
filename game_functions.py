import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_KP6:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_KP4:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create new bullet and add it to bullets group
        new_bullet = Bullet(ai_settings, screen, bullets)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_KP6:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_KP4:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)

            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)                

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
