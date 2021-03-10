# Detector-de-Carros-OpenCV

#### Bibliotecas necessárias:
``` css
opencv-python
mahotas
pyautogui (Opcional)
```

A partir do reconhecimento de imagens usando o Template Matching do OpenCV foi possível reconhecer carros do jogo Driver San Francisco.

Para reconhecer foram usadas imagens de modelo (pasta ML_RECORT) e uma imagem de entrada (binar)
``` python
cv2.matchTemplate(binar, carroGray, cv2.TM_CCOEFF)
```

#### Construção dos modelos:
1. Cada frame do video foi convertido em binário utilizando o método otsu.
2. Foi retirada uma foto de cada frame
3. Foi feito um reconhecimento utilizando 4 imagens que foram cortadas.
4. Depois foi salvo cada reconhecimento
5. Como a imagem dentro do carro do jogo é dividida em 2 partes, a inferior fica o volante e as mãos do personagem, e a superior fica a rua foi feito um corte no meio da imagem para que seja utilizada apenas a parte superior.
6. Foram retiradas imagens que eram de frames muito próximas, assim diminuiu o tempo de processamento mas fez com que alguns reconhecimentos falhem.

#### Imagens:
Etapa 3 do modelo:

![frame1](https://user-images.githubusercontent.com/67590378/106367282-2d986f00-6320-11eb-8a82-57b6814f7476.png)
![frame2](https://user-images.githubusercontent.com/67590378/106367283-2ec99c00-6320-11eb-8636-04c3485c2679.png)
![frame3](https://user-images.githubusercontent.com/67590378/106367284-2ec99c00-6320-11eb-89b1-b00f1adad05b.png)
![frame4](https://user-images.githubusercontent.com/67590378/106367285-2f623280-6320-11eb-9b2a-c941d30d6211.png)


Etapa 5 do modelo:

![image](https://user-images.githubusercontent.com/67590378/106367322-823bea00-6320-11eb-94fc-cbc62016fb46.png)



Quando são detectados os frames 136 e 236 os carros estão muito próximos, para evitar uma colisão aparecerá FREAR, e se estiver habilitado o `pyautogui` pressionará a tecla S para frear o carro.

#### Resultado
![Gif ACELERADO](https://user-images.githubusercontent.com/67590378/106366646-0344b280-631c-11eb-8021-75b5e88eb997.gif)
###### OBS: GIF ACELERADO POR CAUSA DO TEMPO DE PROCESSAMENTO.
