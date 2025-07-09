class Leitura:
    """Classe para descrever o que é enviado pelos Sensores IoT
    
    ...
    Attributes
    ----------
    timestamp : float 
        instante da leitura
    sensor : int
        codigo do sensor responsável pela leitura
    dados : str
        dados da leitura
    
    Methods
    -------
    getCod()
        retorna do codigo da leitura
    getSensorCod()
        retorna o codigo do sensor que obteve a leitura
    getDados()
        retorna os valores da leitura
     
    """
    def __init__(self,timestamp,sensor,dados):
        """Classe para descrever o que é enviado pelos Sensores IoT

        Args:
            timestamp (_type_): _description_
            sensor (_type_): _description_
            dados (_type_): _description_
        """
        self.timestamp = timestamp
        self.sensor = sensor
        self.dados = dados

    def getTimestamp(self) -> float:
        return self.timestamp
    
    def getSensor(self) -> int:
        return self.sensor

    def getDados(self) -> str:
        return self.dados