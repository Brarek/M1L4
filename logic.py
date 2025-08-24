from random import randint
from datetime import datetime,timedelta
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.last_heal_time = datetime(year=2000, month=1, day=1)
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.attack = self.get_attack()
        self.type = 'common'

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]['base_stat'])
        else:
            return "0"
        
    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][1]['base_stat'])
        else:
            return "0"
        
    def heal(self, heal_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=heal_interval)  
        if (current_time - self.last_heal_time) > delta_time:
            self.hp += hp_increase
            self.last_heal_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время лечения покемона: {current_time+delta_time}"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}; У него {self.hp} хп и {self.attack} урона Класс: {self.type}"
    
    def fight(self, enemy):
        if enemy.hp > self.attack:
            enemy.hp -= self.attack
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer} осталось {enemy.hp} хп"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


class Fighter(Pokemon):

    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.type = 'figher'

    def fight(self, enemy):
        power = randint(1, 25)
        self.attack += power
        if enemy.hp > self.attack:
            enemy.hp -= self.attack
            self.attack -= power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer} осталось {enemy.hp} хп"
        else:
            enemy.hp = 0
            self.attack -= power
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "



