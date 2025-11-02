import pygame

WIDTH = 800
HEIGHT = 600

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PARTICLE SIMULATOR")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        window.fill((0, 0, 0))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()