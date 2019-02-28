import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
  ai_setting = Setting()
  pygame.init()
  screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
  pygame.display.set_caption("ET Fighting")
  ship = Ship(ai_setting, screen)
  alien = Alien(ai_setting, screen)
  bullets = Group()
  aliens = Group()
  
  gf.create_fleet(ai_setting, screen, aliens)
  
  while True:
    gf.check_events(ai_setting, screen, ship, bullets)
    ship.update()
    gf.update_bullets(bullets)
    gf.update_screen(ai_setting, screen, ship, aliens, bullets)
    
run_game()