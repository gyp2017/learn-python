# -*- coding: utf-8 -*-
# 52 웹 게임 시작

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.path = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
페르칼 25번 행성의 고전족은 여러분의 우주선에 침략하고 모든 승무원을
죽였습니다. 당신은 마지막 생존자이며 마지막 임무로 무기고에서 중성자탄을
가져와 다리에 설치하고 구명정에 타기 전에 우주선을 폭파해야 합니다.

붉은 비늘 피부, 시커먼 때가 낀 이빨, 증오로 가득 찬 몸에서 물 흐르듯
이어지는 사악한 광대 복장의 고던인이 뛰쳐 나오는 동안 당신은 중앙
복도에서 무기고로 내달리고 있습니다.고던인은 무기고로 가는 문을 가로막고
당신을 날려버리려 무기를 겨누는 참입니다.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
운 좋게도 당신은 학교에서 고던어 욕설을 배웠습니다. 이는 고던 농담을
하나 합니다.
Lbhe zbgure vf fb sng, jura fur fvbf nebhaq gur ubhfr, fur fvg nebhaq gur ubhfr.
고던인이 멈춰서 웃지 않으려 하지만, 결국 웃음이 터지자 움직이지 못합니다.
당신은 고던인이 웃는 동안 뛰쳐나가 머리를 정통으로 맞춰 쓰러뜨리고 무기고
문으로 뛰어듭니다.

당신은 무기고로 뛰어 구러 들어가 쪼그려 앉고 방을 살피며 숨어 있을지도
모르는 고던인을 찾습니다. 쥐죽은 듯이, 지나치게 조용합니다.
일어서서는 문 건너편으로 달려가 컨테이너에서 중선자탄을 찾습니다.
상장는 비밀번호로 잠겨 있고 폭탄을 꺼내려면 비밀번호를 알아내야만
합니다. 비밀번호를 10번 틀리면 자물쇠는 영원히 잠기고 폭탄을 꺼낼 수
없습니다. 비밀번호는 3자리수입니다.
""")

the_bridge = Room("The Bridge",
"""
철컥하며 컨테이너가 열리고 틈새로 공기가 새어나옵니다.
중성자탄을 움켜쥐고 설치해야 할 장소인 다리를 향해 할 수 있는 한
가장 빠른 속도로 달립니다.

당신은 팔에 중성자탄을 끼고 다리로 뛰어들어 우주선 조종권을
빼앗으려던 고던인 5며을 놀라게 합니다. 그 모두가 방금 전에 본
고던인보다 더 못생긴 광대 복장을 하고 있습니다. 아직 무기를 뽑지는
않았지만 당신이 팔에 낀 활성화된 폭탄을 보고 터뜨리고 않고 싶어
합니다.
""")

escape_pod = Room("Escape Pod",
"""
팔에 낀 폭탄을 광선총으로 겨누자 고던인들은 팔을 들고 땀을 흘리기
시작합니다. 당신은 문 뒤에 바짝 붙어 열고 광선총을 겨눈 채로
조심스럽게 폭탄을 바닥에 설치합니다.
다음으로 문 밖으로 뛰쳐나와 닫기 버튼을 두드리고 잠금장치를
쐬버려 고던인들이 나올 수 없게 만들어버립니다.
이제 폭탄은 설치되었고 당신은 이 깡통에서 벗어나기 위해 구명정으로
달려갑니다.

우주선이 통째로 폭발하기 전에 구명정에 닿기 위해 우주선을 가로질러
필사적으로 달립니다. 우주선에는 고던인이 거의 없어 방해받지 않고
질주합니다. 당신은 구명정이 있는 방에 도달하고 이제 하나를 골라야
합니다. 이 중 몇개는 손상되었을 수 있지만 살펴볼 시간이 없습니다.
구명정이 5대 있습니다. 몇 번을 타겠습니까?
""")

the_end_winner = Room("The End",
"""
2번 구명정으로 뛰어들어 탈출 단추를 누릅니다.
구명정은 가볍게 우주로 미끄러져 나가며 아래의 행성으로 향합니다.
행성으로 날아가는 동안 뒤돌아보니 우주선이 파괴되면서 밝은 별처럼
폭발하고 고던 우주선가지 없애버리는 것을 확인합니다.
당신이 이겼습니다!
""")

the_end_loser = Room("The End",
"""
아무 구명정으로 뛰어들어 탈출 단추를 누릅니다.
구명정은 우주의 진공으로 빠져나가고, 콩깍지가 터지듯 안으로
무너지며 당신을 곤약처럼 으스러뜨립니다.
""")

escape_pod.add(paths{
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    '폭탄 던지기': generic_death
    '천천히 폭탄 설치하기': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    '발사!': generic_death,
    '회피!': generic_death,
    '농담하기': laser_weapon_armory,
})

START = central_corridor
