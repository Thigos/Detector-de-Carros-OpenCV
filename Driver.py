import os
import cv2
import pyautogui
import mahotas


#Local do video
video_original = cv2.VideoCapture('teste.wmv')
#O local aonde os arquivos estão
diret = os.path.dirname(os.path.abspath(__file__))


while True:
    #Frame do video
    ret, frame = video_original.read()
    #Converte para escalas de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Suaviza a imagem
    suavizador = cv2.GaussianBlur(gray, (7, 7), 0)
    #Utiliza o método otsu para transformar a imagem em binário 0,1 (preto ou branco)
    otsu = mahotas.thresholding.otsu(suavizador)
    #Copia a imagem em escalas de cinza
    binar = gray.copy()
    #Calcula áreas em que há um pico de intensidade e transforma em branco (255) ou preto (0)
    binar[binar > otsu] = 255
    binar[binar < 255] = 0
    binar = cv2.bitwise_not(binar)


    #Pega todos os arquivos que estão na pasta ML_RECORT
    for nome in os.listdir(diret + '\\ML_RECORT'):
            #Lê o arquivo
            carro = cv2.imread(diret + '\\ML_RECORT\\' + str(nome))
            #Converte a imagem para escalas de cinza
            carroGray = cv2.cvtColor(carro, cv2.COLOR_BGR2GRAY)
            #Pega o w (largura) e h (altura) da imagem
            w, h = carroGray.shape[::-1]

            #Compara a imagem modelo (carroGray) com a imagem de entrada (binar)
            res = cv2.matchTemplate(binar, carroGray, cv2.TM_CCOEFF)
            limit = 200000000
            #Recebe as informações da comparação
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            #Verificar se o valor da comparação é maior ou igual a 200000000
            if (max_val >= limit):
                #Forma um retângulo e uma palavra para identificar o carro
                cv2.rectangle(frame, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)
                fonte = cv2.FONT_HERSHEY_SIMPLEX
                texto = "CARRO"
                #Os frames 136 e 236 são os pontos em que o carro está mais perto do outro
                #Então, o programa avisará para frear o carro e apertará o 's' que é o freio do carro no jogo
                if(nome == "frame136.png" or nome == "frame236.png"):
                    texto = "FREAR"
                    #pyautogui.press('s')
                cv2.putText(frame, texto, (max_loc[0], max_loc[1] - 5), fonte,
                            0.5, (0, 0, 255), 1, cv2.LINE_AA)
                #É preciso que o for pare, assim não terá conflitos de frames
                break


    #Mostra o video
    cv2.imshow("Driver", frame)

    #Aperte 'q' para sair
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    


cv2.destroyAllWindows()


