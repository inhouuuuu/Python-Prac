from random import *

#일반 유닛
class unit:
    def __init__(self,name,hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다.".format(name))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛
class attackunit(unit):
    def __init__(self,name,hp,speed, damage):
        unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#마린
class marine(attackunit):
    def __init__(self):
        attackunit.__init__(self, "마린", 40, 1, 5)

    def stimpact(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소).".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
#탱크
class tank(attackunit):
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        attackunit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if tank.seize_developed == False:
            return
        # 현재 시즈모드가 아닐때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            if self.seize_mode == True:
                print("{0} : 시즈모드를 해제합니다.".format(self.name))
                self.damage /= 2
                self.seize_mode = False

#공중 유닛 클래스
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class flyableattackunit(attackunit,flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, 0, damage) #지상 스피드는 0
        flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


#레이스
class wraith(flyableattackunit):
    def __init__(self):
        flyableattackunit.__init__(self,"레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제상태)

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else: #클로킹 모드 해제 - > 설정
            if self.clocked == False:
                print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
                self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장 하셨습니다.")


#실제 게임 시작
game_start()
#마린 3기 생성
m1 = marine()
m2 = marine()
m3 = marine()

#탱크 2기 생성
t1 = tank()
t2 = tank()

#레이스 1기 생성
w1 = wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료 되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, marine):
        unit.stimpact()
    elif isinstance(unit, tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음

# 게임 종료
game_over()

