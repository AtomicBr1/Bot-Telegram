import pyautogui
import time


time.sleep(5)

# Obter a posição atual do mouse
posicao = pyautogui.position()

# Exibir as coordenadas x e y
print("Posição do mouse:")
print(f"X: {posicao.x}, {posicao.y}")
