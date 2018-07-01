# coding:utf-8
import random
import time


class Kicker:
    def shoot(self, direction):
        return direction


class Keeper:
    def jump(self, direction):
        return direction


class Team:
    def __init__(self):
        self.point = 0

    def get_point(self):
        self.point += 1


class OpponentTeam(Team):
    pass


class PlayerTeam(Team):

    def __init__(self, name):
        Team.__init__(self)
        self.name = name

    def win(self):
        print(self.name + "さんの勝ちです")

    def lose(self):
        print(self.name + "さんの負けです")


class Round:
    count = 1

    def __init__(self, first):
        self.first = first

    def play_both_sides(self):
        print("\n\nあなたのキック成功：%s 相手のキック成功：%s" % (player.point, opponent.point))
        print("第%sラウンド" % Round.count)
        side = 0
        while side < 2:
            self._play_pk()
            self.first = opponent if self.first == player else player
            side += 1
        Round.count += 1

    def _decide_direction(self):
        while 1:
            try:
                return int(input("0:左上, 1:左下, 2:正面, 3:右上, 4:右下"))
            except Exception:
                print("正しく入力してください")

    def _play_pk(self):
        kicker = Kicker()
        keeper = Keeper()

        if self.first == player:
            print("\nキッカーです。どこに蹴りますか?")
            direction = self._decide_direction()
            if kicker.shoot(direction) == keeper.jump(random.randint(1, 5)):
                print("キーパーに止められました")
            else:
                print("シュートが決まりました")
                player.point += 1

        else:
            print("\nキーパーです。どこに飛びますか？")
            direction = self._decide_direction()
            if kicker.shoot(random.randint(1, 5)) == keeper.jump(direction):
                print("シュートを止めました")
            else:
                print("シュートを決められました")
                opponent.point += 1


class PkGame:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def match_five_rounds(self):
        while Round.count <= 5:
            round =Round(first=player if self._deside_side() == 0 else opponent)
            round.play_both_sides()
        self._announce_result()

    def _deside_side(self):
        while 1:
            try:
                turn = int(input("先攻か後攻か選んでください\n0:先攻  1:後攻"))
                break
            except Exception:
                print("正しく入力してください")
        return turn

    def _announce_result(self):
        print("\n\n結果発表")
        time.sleep(3)
        print("\n\nあなたのキック成功：%s 相手のキック成功：%s\n" % (player.point, opponent.point))

        if player.point == opponent.point:
            print("引き分けです")
        elif player.point > opponent.point:
            player.win()
        else:
            opponent.win()


if __name__ == "__main__":
    player = PlayerTeam(name=raw_input("あなたの名前を入力してください"))
    opponent = OpponentTeam()
    pk_game = PkGame(player, opponent)
    pk_game.match_five_rounds()
