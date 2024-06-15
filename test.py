class Musica:
    var = 0
    # dunder = double underlines
    def __init__(self, file_music):
        Musica.var += 1
        self.__file_music = file_music
        
        
path = 'xabinga'
sound_one = Musica(path)
sound_two = Musica(path)


print(sound_one._Musica__file_music)
