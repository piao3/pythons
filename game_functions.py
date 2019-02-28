import pygame
import sys
from bullet import  Bullet
from alien import Alien

def key_down(event, ai_setting, screen, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  if event.key == pygame.K_LEFT:
    ship.moving_left = True
  if event.key == pygame.K_SPACE:
    fire_bullet(ai_setting, screen, ship, bullets)
  if event.key == pygame.K_q:
    sys.exit()
    
def key_up(event, ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  if event.key == pygame.K_LEFT:
    ship.moving_left = False
  
def check_events(ai_setting, screen, ship, bullets):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      key_down(event, ai_setting, screen, ship, bullets)
    elif event.type == pygame.KEYUP:
      key_up(event, ship)

def update_bullets(bullets):
  bullets.update()
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)

def fire_bullet(ai_setting, screen, ship, bullets):
  if len(bullets) < ai_setting.bullets_allowed:
    new_bullet = Bullet(ai_setting, screen, ship)
    bullets.add(new_bullet)

def create_fleet(ai_setting, screen, aliens):
  alien = Alien(ai_setting, screen);
  alien_width = alien.rect.width
  available_space_x = ai_setting.screen_width -2 * alien_width
  number_aliens_x = int(available_space_x / (2 * alien_width))
  for alien_number in range(number_aliens_x):
    alien = Alien(ai_setting, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def update_screen(ai_settings, screen, ship, aliens, bullets):
  screen.fill(ai_settings.bg_color)
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  aliens.draw(screen)
  ship.blitme()
  # aliens.blitme()
  pygame.display.flip()