import pygame


def load_image(image_path: str, colorkey: tuple = None) -> pygame.Surface:
    """
    Carga una imagen desde un archivo y la convierte en una Surface de Pygame.

    :param image_path: ruta del archivo de la imagen.
    :param colorkey: color transparente de la imagen (opcional).
    :return: la Surface de Pygame con la imagen cargada.
    """
    try:
        image = pygame.image.load(image_path)
    except pygame.error as e:
        print(f"No se pudo cargar la imagen {image_path}: {e}")
        raise SystemExit(e)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def draw_text(surface: pygame.Surface, text: str, font: pygame.font.Font, color: tuple,
              x: int, y: int, align: str = "left"):
    """
    Dibuja un texto en una Surface de Pygame.

    :param surface: la Surface donde se dibujará el texto.
    :param text: el texto a dibujar.
    :param font: la fuente de Pygame para el texto.
    :param color: el color del texto.
    :param x: la posición x del texto.
    :param y: la posición y del texto.
    :param align: la alineación del texto (izquierda, centro o derecha).
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == "left":
        text_rect.x = x
    elif align == "center":
        text_rect.centerx = x
    elif align == "right":
        text_rect.right = x
    text_rect.y = y
    surface.blit(text_surface, text_rect)
