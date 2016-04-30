from collections import OrderedDict

from engine.game.dungeon.dungeon import Dungeon
from engine.game.player.player import Player
from engine.game.party.party import Party
from engine.ui.core.manager import Manager
import engine.ui.manager as manager

import engine.game.move.built_moves as mv

class GameManager(Manager):
    """GameManager is responsible for rendering and updating
    all the various gameplay related elements in the game
    it also controls pseudorandom ordering of menu systems
    in the form of the manager list. It is also in charge of macro
    level logic of the rendering of the menus."""

    def __init__(self):
        super(GameManager, self).__init__()
        self.hover = manager.MouseHoverManager()
        self.party = manager.PartyManager()
        self.sidebar = manager.SidebarManager()
        self.encounter = manager.EncounterManager()
        self.castbar = manager.CastBarManager(440)
        self.loot = manager.LootManager(450, 20, 300, 400)
        self.scenario = manager.ScenarioManager(20, 60)
        self.travel = manager.TravelManager(800, 300, 1280//2-800//2, 100)
        self.battle = manager.BattleManager()
        self.level = manager.LevelUpManager(1280, 720)
        self.shop = None
        self.character = manager.CharacterCardManager(20, 20)
        self.item = None

    def init(self, game, difficulty):
        # May need to shift this functionality
        game.difficulty = difficulty
        game.current_dungeon = Dungeon("catacombs", game.difficulty)
        game.floor_type = game.current_dungeon.level
        game.current_location = game.current_dungeon.start
        game.current_location.generate()
        game.current_dialog = game.current_location.get_event()
        game.focus_window = "scenario"
        game.party = Party([Player("Player "+str(i)) for i in range(3)])
        game.loot = None
        for player in game.party.players:
            player.add_move(mv.PLAYER_MOVES["attack"])
            player.add_move(mv.PLAYER_MOVES["magic bolt"])
            player.add_move(mv.PLAYER_MOVES["stunning blow"])
            player.add_move(mv.PLAYER_MOVES["blessing"])
            player.add_move(mv.PLAYER_MOVES["firebolt"])
            player.add_move(mv.PLAYER_MOVES["arcane blast"])
            player.add_move(mv.PLAYER_MOVES["backstab"])
            player.castbar[0] = player.moves[0] # temp
            player.castbar[1] = player.moves[1] # temp
            player.castbar[2] = player.moves[2] # temp
            player.castbar[3] = player.moves[3] # temp
            player.castbar[4] = player.moves[4] # temp
            player.castbar[5] = player.moves[5] # temp
            player.castbar[6] = player.moves[6] # temp


    def render(self, surface, game):
        super().render(surface, game)
        self.sidebar.render(surface, game)
        self.encounter.render(surface, game)
        self.party.render(surface, game)
        self.character.render(surface, game)
        self.loot.render(surface, game)
        self.castbar.render(surface, game)
        self.level.render(surface, game)
        if game.focus_window == "travel":
            self.travel.render(surface, game)
        elif game.focus_window == "shop":
            pass
        elif game.focus_window == "loot":
            pass
        elif game.focus_window == "scenario":
            self.scenario.render(surface, game)
        self.hover.render(surface, game)
        # self.item.render(surface, game)

    def update(self, game):
        if game.focus_window != "level": # if level up not occurring
            super().update(game)
            self.battle.update(game)
            self.sidebar.update(game)
            self.party.update(game)
            self.character.update(game)
            self.castbar.update(game)
            self.encounter.update(game)
            self.loot.update(game)
            if game.focus_window == "travel":
                self.travel.update(game)
            if game.focus_window == "shop":
                pass
            if game.focus_window == "loot":
                pass
            if game.focus_window == "scenario":
                self.scenario.update(game)
            self.hover.update(game)
            # self.item.update(game)
        else:
            self.level.update(game)