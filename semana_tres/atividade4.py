import os
import cv2
from matplotlib import pyplot as plt


IMG = 'Lena.png'
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def calculate_show_bin():
    # Importando a imagem em escala de cinza
    lena = cv2.imread(IMG, cv2.IMREAD_GRAYSCALE)
    
    # valor de binarização
    bin = 127
    
    ret, thresh = cv2.threshold(lena, bin, 255, cv2.THRESH_BINARY)

    cv2.imshow("Lena binary", thresh)

    # Espera qualquer tecla ser pressionada para destruir a janela
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    calculate_show_bin()