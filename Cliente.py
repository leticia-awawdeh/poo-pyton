class Cliente:
    def __init__(self, n, tel):

        self._nome = n
        self._telefone = tel
    #get
    def get_nome(self):
        return self._nome
    #set
    def set_nome(self, nome):
        self._nome = nome