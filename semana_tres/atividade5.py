import os
import cv2
from matplotlib import pyplot as plt


IMG = 'Lena.png'
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def alargamento():
    lena = cv2.imread(IMG, cv2.IMREAD_GRAYSCALE)

    # dados
    limiar = [100, 200]
    k = [0.6, 1.2, 0.95]

    # Altura e largura
    height, width = lena.shape

    # Alargamento:
    for i in range(height):
        for j in range(width):
            for kj in range(len(limiar)):
                if lena[i, j] <= limiar[kj]:
                    lena[i, j] *= k[kj]
                    break
                else:
                    lena[i, j] *= k[-1]

    cv2.imshow("Alargamento", lena)

    # Espera qualquer tecla ser pressionada para destruir a janela
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    alargamento()
