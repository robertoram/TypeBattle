import pygame

# Mapa de teclas con acento para Windows
accent_keys_windows = {
    pygame.K_QUOTE: {"char": "´", "mod": pygame.KMOD_LSHIFT},
    pygame.K_BACKQUOTE: {"char": "`", "mod": pygame.KMOD_LSHIFT},
    pygame.K_QUOTE: {"char": "´", "mod": pygame.KMOD_LCTRL},
    pygame.K_BACKQUOTE: {"char": "`", "mod": pygame.KMOD_LCTRL},
}

# Mapa de teclas con acento para macOS
accent_keys_macos = {
    pygame.K_e: {"char": "é", "mod": pygame.KMOD_LALT},
    pygame.K_u: {"char": "ú", "mod": pygame.KMOD_LALT},
    pygame.K_i: {"char": "í", "mod": pygame.KMOD_LALT},
    pygame.K_o: {"char": "ó", "mod": pygame.KMOD_LALT},
    pygame.K_a: {"char": "á", "mod": pygame.KMOD_LALT},
}

# Diccionario de teclas con acento
accent_keys = {}
accent_keys.update(accent_keys_windows)
accent_keys.update(accent_keys_macos)

# Inicializar Pygame
pygame.init()

# Crear ventana
window = pygame.display.set_mode((640, 480))

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            # Verificar si se presionó una tecla con acento
            if event.key in accent_keys:
                accent_key = accent_keys[event.key]
                # Verificar si se presionó el modificador de acento correspondiente
                if (event.mod & accent_key["mod"]) or event.key == pygame.K_QUOTE :
                    # Agregar la letra con acento a la entrada de texto
                    print(accent_key["char"])
            # Verificar si se presionó una tecla normal
            elif event.unicode.isalpha():
                # Agregar la letra a la entrada de texto
                print(event.key)

    # Actualizar la ventana
    pygame.display.update()
