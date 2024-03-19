import pygame 
import os
import random

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((640,480))
playlist=["music\\1.mp3","music\\2.mp3","music\\3.mp3","music\\4.mp3","music\\5.mp3","music\\6.mp3"]  
current_index=0
current_song=playlist[current_index]
font = pygame.font.SysFont("Arial", 60)
text=font.render("Player", True, (0, 128, 0))
text2=font.render("Next: D", True, (0, 128, 0))
text3=font.render("Previous: A", True, (0, 128, 0))
text4=font.render("Stop: S", True, (0, 128, 0))
text5=font.render("Pause|Unpause: Space", True, (0, 128, 0))

def Next():
  global current_index, playlist, current_song
  next_song_index=(current_index+1) % len(current_song)
  current_song=playlist[next_song_index]
  pygame.mixer.music.load(current_song)
  pygame.mixer.music.play()
  current_index=next_song_index

def Prev():
  global current_song, current_index, playlist
  prev_song_index=(current_index-1)%len(current_song)
  current_song=playlist[prev_song_index]
  pygame.mixer.music.load(current_song)
  pygame.mixer.music.play()
  current_index=prev_song_index

def Pause_Unpause():
  if pygame.mixer.music.get_busy():
    pygame.mixer.music.pause()
  else:
    pygame.mixer.music.unpause()

def Stop():
  pygame.mixer.music.stop()

while True:
  for event in pygame.event.get():
    if event.type ==pygame.QUIT:
      pygame.quit()
    elif event.type==pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        Pause_Unpause()
      elif event.key == pygame.K_d:
        Next()
      elif event.key == pygame.K_a:
        Prev()
      elif event.key == pygame.K_s:
        Stop()
  screen.fill ((255,255,255))
  screen.blit(text, (120 - text.get_width() // 2, 40 - text.get_height() // 2))
  screen.blit(text2, (140 - text2.get_width() // 2, 120 - text2.get_height() // 2))
  screen.blit(text3, (140 - text2.get_width() // 2, 200 - text2.get_height() // 2))
  screen.blit(text4, (140 - text2.get_width() // 2, 280 - text2.get_height() // 2))
  screen.blit(text5, (140 - text2.get_width() // 2, 360 - text2.get_height() // 2))

  pygame.display.flip()




  