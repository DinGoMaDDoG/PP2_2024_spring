import pygame
from datetime import datetime 

pygame.init()
width= height=800
screen=pygame.display.set_mode((width, height))
done=False
sec_pic=pygame.image.load("images\leftarm.png")
min_pic=pygame.image.load("images\\rightarm.png")
body_pic=pygame.image.load("images\mainclock.png")
mickey_rect = body_pic.get_rect(center=(width // 2, height // 2))

while True:
  for event in pygame.event.get():
    if event.type ==pygame.QUIT:
      pygame.quit()
  now=datetime.now()
  min_ang=now.minute*6+60
  sec_ang=now.second*6+7
  screen.fill((255,255,255))
  screen.blit(body_pic, mickey_rect)

  rotate_sec=pygame.transform.rotate(sec_pic, -sec_ang)
  rotate_sec_rect=rotate_sec.get_rect(center=mickey_rect.center)
  screen.blit(rotate_sec,rotate_sec_rect)

  rotate_min=pygame.transform.rotate(min_pic, -min_ang)
  rotate_min_rect=rotate_min.get_rect(center=mickey_rect.center)
  screen.blit(rotate_min, rotate_min_rect)

  pygame.display.flip()
  pygame.time.Clock().tick(30)


  