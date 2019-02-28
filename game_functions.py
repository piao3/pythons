import pygame
import sys
from bullet import  Bullet

def key_down(event, ai_setting, screen, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  if event.key == pygame.K_LEFT:
    ship.moving_left = True
  if event.key == pygame.K_SPACE:
    new_bullet = Bullet(ai_setting, screen, ship)
    bullets.add(new_bullet)
    
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

def update_screen(ai_settings, screen, ship, bullets):
  screen.fill(ai_settings.bg_color)
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()
  pygame.display.flip()