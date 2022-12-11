import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

WIDTH, HEIGHT = 800,800
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,1000)
draw_options = pymunk.pygame_util.DrawOptions(window)
FPS = 60

elasticidade_quadrados = float(input(f'Qual elasticidade voce deseja aos quadrados?\n'))
massa_quadrado_1 = float(input(f'Qual sera a massa do quadrado 1?\n'))
massa_quadrado_2 = float(input(f'Qual sera a massa do quadrado 2?\n'))
velocidade_x_quadrado_1 = float(input(f'Qual sera a velocidade inicial do quadrado 1?(lembrando que o sentido positivo eh a direita)\n'))
velocidade_x_quadrado_2 = float(input(f'Qual sera a velocidade inicial do quadrado 2?(lembrando que o sentido positivo eh a direita)\n'))



    # Converte coordenadas do self.body.position para formar vertices que se movem
    # O objeto é formado no ponto (0,0) e admite crescimento em Y para negativo e em X para positivo, assim:
    # odd = impar = ->
    # even = par = <-

def conversor_coordenadas_q1_odd_vertice1(coordenada):
    return 40+int(coordenada[0]), int(coordenada[1])-80

def conversor_coordenadas_q1_odd_vertice2(coordenada):
    return 55+int(coordenada[0]), int(coordenada[1])-85

def conversor_coordenadas_q1_odd_vertice3(coordenada):
    return 40+int(coordenada[0]), int(coordenada[1])-90


def conversor_coordenadas_q1_even_vertice1(coordenada):
    return 20+int(coordenada[0]), int(coordenada[1])-80

def conversor_coordenadas_q1_even_vertice2(coordenada):
    return 5+int(coordenada[0]), int(coordenada[1])-85

def conversor_coordenadas_q1_even_vertice3(coordenada):
    return 20+int(coordenada[0]), int(coordenada[1])-90


class Chao:
    def __init__(self):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, (50,750),(750,750),4)
        self.shape.color = (0,0,0,100)
        space.add(self.body,self.shape)

class Parede:
    def __init__(self,x = 50):

        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body,(x,500),(x,750),5)        
        self.shape.color = (0,0,0,100)
        self.shape.elasticity = 1
        space.add(self.body,self.shape)

class QuadradoeVetor:

    def __init__(self, x_pos = 70, velocidade = (0,0), massa = 1 ):

        #   Referente ao quadrado principal

        self.body = pymunk.Body()
        self.shape = pymunk.Poly(self.body,[(0,0),(0,-60),(60,-60),(60,0)])
        self.shape.color = (255,0,0,100)
        self.shape.density = 1
        self.shape.elasticity = elasticidade_quadrados
        self.shape.mass = massa
        self.body.position = x_pos,750 # 50 + (grossura parede)/2 e 750 - (lado quadrado) - grossura chao
        self.body.velocity = velocidade

        #   Referente ao quadrado do vetor   

        quadradovetor = pymunk.Poly(self.body,[(20,-80),(20,-90),(40,-90),(40,-80)])
        quadradovetor.color = (0,0,0,100)


        space.add(self.body,self.shape,quadradovetor)

    def seta_vetor(self):


        # desenha uma imgaem pelo pygame que representa o ponteiro do vetor velocidade dependendo da direção
        # da velocidade do objeto


        if (self.body.velocity) > (0,0):

            pygame.draw.polygon(window,(0,0,0),(conversor_coordenadas_q1_odd_vertice1(self.body.position),conversor_coordenadas_q1_odd_vertice2(self.body.position),conversor_coordenadas_q1_odd_vertice3(self.body.position)))
        
        elif (self.body.velocity) < (0,0):

                pygame.draw.polygon(window,(0,0,0),(conversor_coordenadas_q1_even_vertice1(self.body.position),conversor_coordenadas_q1_even_vertice2(self.body.position),conversor_coordenadas_q1_even_vertice3(self.body.position)))
        
        elif (self.body.velocity) == (0,0):

            pass

def jogo():

    chao = Chao()
    arede = Parede()
    parede = Parede(750)
    corpoteste1 = QuadradoeVetor(70,(velocidade_x_quadrado_1,0),massa_quadrado_1)
    corpoteste2 = QuadradoeVetor(670,(velocidade_x_quadrado_2,0), massa_quadrado_2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        window.fill("white")
        corpoteste1.seta_vetor()
        corpoteste2.seta_vetor()
        space.debug_draw(draw_options)


        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

jogo()
pygame.quit()