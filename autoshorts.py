from pygame_gui.core import ObjectID
from file_pick import FilePicker
import pygame_gui
import pygame
import sys
import os

import pygame_gui.ui_manager

SCREEN_DIMS = (900, 700)
CTRL_PANEL_DIMS = (500, 670)

class Autoshorts:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("AutoShorts")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_DIMS)
        self.display = pygame.Surface(SCREEN_DIMS)
        
        self.control_panel = pygame.Surface(CTRL_PANEL_DIMS)
        self.controls_bground = pygame.Surface(CTRL_PANEL_DIMS)
        self.controls_bground.fill(pygame.Color('#5C7285'))
        self.controls_pos = ((SCREEN_DIMS[1] - CTRL_PANEL_DIMS[1]) / 2, (SCREEN_DIMS[1] - CTRL_PANEL_DIMS[1]) / 2)
        self.controls_manager = pygame_gui.UIManager(CTRL_PANEL_DIMS, 'theme.json')
        
        self.file_picker = FilePicker()
        self.file_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(((CTRL_PANEL_DIMS[0] / 2 - 200), self.controls_pos[0] + 10, 400, 50)),
            text='Video Input',
            manager=self.controls_manager,
            object_id=ObjectID(class_id='@input_button', object_id='#file_button'))
    
    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.file_button:
                        filepath = self.file_picker.run()
                        print("file button pressed")
                        
                self.controls_manager.process_events(event)
                    
            self.controls_manager.update(self.clock.tick(60)/1000.0)
            self.control_panel.blit(self.controls_bground)
            self.controls_manager.draw_ui(self.control_panel)
            
            self.display.blit(self.control_panel, self.controls_pos)
            self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Autoshorts().run()