import os
import cv2


IMG = 'Lena.png'
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def negative():
    """
    Mostra a imagem de lena negativada
    """
    # Importar imagem em escala de cinza
    lena = cv2.imread(IMG, cv2.IMREAD_GRAYSCALE)

    # Transforma em negativo
    negative_lena = 255 - lena
    cv2.imshow("Lena", negative_lena)

    # Espera qualquer tecla ser pressionada para destruir a janela
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    negative()
