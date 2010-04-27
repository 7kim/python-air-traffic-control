#	File: waypoint.py

import pygame;

class Waypoint:

    def __init__(self, location):
        self.setLocation(location)

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        if(location[0] > 791):
            self.location = (791, location[1])
        else:
            self.location = location

        self.way_rect = pygame.Rect(self.location, (7, 7))
        self.way_rect.center = self.location

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.way_rect, 0)

    def clickedOn(self, clickpos):
        return (self.way_rect.collidepoint(clickpos))
