class mazo:
    def __init__(self):
        self.cartas=['As de Trebol','2 de Trebol','3 de Trebol','4 de Trebol','5 de Trebol','6 de Trebol','7 de Trebol','8 de Trebol','9 de Trebol','10 de Trebol','J de Trebol','Q de Trebol','K de Trebol',
        'As de Espadas','2 de Espadas','3 de Espadas','4 de Espadas','5 de Espadas','6 de Espadas','7 de Espadas','8 de Espadas','9 de Espadas','10 de Espadas','J de Espadas','Q de Espadas','K de Espadas',
        'As de Corazones','2 de Corazones','3 de Corazones','4 de Corazones','5 de Corazones','6 de Corazones','7 de Corazones','8 de Corazones','9 de Corazones','10 de Corazones','J de Corazones','Q de Corazones','K de Corazones',
        'As de Rombos','2 de Rombos','3 de Rombos','4 de Rombos','5 de Rombos','6 de Rombos','7 de Rombos','8 de Rombos','9 de Rombos','10 de Rombos','J de Rombos','Q de Rombos','K de Rombos']
        self.elegidas=[]
        self.casa_plantada=False
        for i in range(52):
            self.elegidas.append(False)
