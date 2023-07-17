import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2


class EnemyManager:

    ENEMIES = [ENEMY_1, ENEMY_2]

    def __init__(self):
        #Vamos a crear una lista de que se de clase Enemy().
        self.enemies: list[Enemy] = []

    def update(self):

        #Vamos a crear enemigos cuando la lista este vacia 
        if len(self.enemies) == 0:
            self.create_enemies()

        #Ya que creamos el Enemigo, ahora vamos a invocarlo en nuestra clase de Enemy
        for enemy in self.enemies:
            enemy.update(self.enemies)  
        
    def draw(self, screen):
       for enemy in self.enemies:
            enemy.draw(screen)

    def create_enemies(self):
        self.choice = random.choice(self.ENEMIES)
        self.enemies.append(Enemy(self.choice))