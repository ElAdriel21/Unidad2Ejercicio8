class Conjunto:
    __conjunto = []

    def __init__(self, v1, v2, v3, v4, v5):
        self.__conjunto = [v1,v2,v3,v4,v5]
        print(self.__conjunto)

    def __add__(self, other):
        union = self.__conjunto
        if type(other) == type(self):
            i = 0
            while i < 5:
                coinciden = False
                j = 0
                while j < 5:
                    if other[i] == self.__conjunto[j]:
                        coinciden = True
                    j += 1
                if coinciden == False:
                    union.append(other[i])
                i += 1
        return union

    def __sub__(self, other):
        diferencia = []
        if type(other) == type(self):
            i = 0
            while i < 5:
                coinciden = False
                j = 0
                while j < 5:
                    if other[j] == self.__conjunto[i]:
                        coinciden = True
                    j += 1
                if coinciden == False:
                    diferencia.append(self.__conjunto[i])
                i += 1
        return diferencia

    def __eq__(self, other):
        coinciden = True
        if type(other) == type(self):
            i = 0
            while i < 5:
                Encontrado = False
                j = 0
                while j < 5:
                    if other[j] == self.__conjunto[i]:
                        Encontrado = True
                        if Encontrado == True:
                            j = 5
                    j += 1
                i += 1
                if Encontrado == False:
                    coinciden = Encontrado
        return coinciden

    def __getitem__(self, item):
        return self.__conjunto[item]

    def __len__(self):
        unaLista = list()
        unaLista.append(self)
        print(unaLista)
        return len(unaLista)