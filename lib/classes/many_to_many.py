class Game:
    '''Game property title
Returns the game's title
Titles must be of type str
Titles must be longer than 0 characters
Should not be able to change after the game is instantiated
hint: hasattr()'''
    def __init__(self, title):
        self.title = title

    @property
    def game_title(self):
        return self._title
    

    @game_title.setter
    def game_title(self, new_title):
        if not hasattr(self, 'title') and type(new_title) == str and len(new_title) > 0:
            self._title = new_title
        else:
            raise Exception("title is a string and cannot be mutated")
        
    @property
    def results(self):
        return self._result
    
    @results.setter
    def results(self, new_result):
        if type(new_result) == Result:
            self._result = new_result

    def players(self):
        pass

    def average_score(self, player):
        pass

'''Player property username
Returns the player's username
Usernames must be of type str
Usernames must be between 2 and 16 characters, inclusive.
Should be able to change after the player is instantiated'''
class Player:
    def __init__(self, username):
        self.username = username


    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if type(new_username) == str and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception("username should be a string between 2 and 16 characters")

    @property
    def results(self):
        return self._results
    
    @results.setter
    def result(self, new_result):
        if type(new_result) == Result:
            self._result == new_result
        pass
    
    @property
    def games_played(self):
        return self._game
        
    @games_played.setter
    def played_game(self, game):
        if type(game) == Game:
            self._game = game
        pass

    def num_times_played(self, game):
        pass

class Result:
    '''Result property score
Returns the result's score
Scores must be of type int
Scores must be between 1 and 5000, inclusive
Should not be able to change after the result is instantiated
hint: hasattr()'''
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if not hasattr(self, 'score') and type(new_score) == int and 1 <= new_score <= 5000:
            self._score = new_score
        else:
            raise Exception("score must be an int between 1 and 5000")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if type(new_player) == Player:
            self._player = new_player
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if type(new_game) == Game:
            self._game = new_game


farcry = Game("FarCry")
print(farcry.title)

# farcry.title = "FarCry6"
# print(farcry.title)


ninja = Player("Ninja")
print(ninja.username)

# ninja.username = "Ninjago"
# print(ninja.username)

FCR = Result(ninja, farcry, 1000)

print(FCR)

print(FCR.player.username)
print(FCR.game.title)
print(FCR.score)
