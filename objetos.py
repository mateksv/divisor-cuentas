class Persona:
    # Inicializo la clase padre con __init__
    def __init__(self, nombre, inversion, diferencia):
        self.nombre = nombre
        self.inversion = inversion
        self.diferencia = diferencia

    
    # get()
    def getNombre(self):
        return self.nombre
    def getInversion(self):
        return self.inversion
    def getDiferencia(self):
        return self.diferencia # si 'diferencia < 0', el valor es negativo, por lo tanto tiene el modulo de ese valor a favor

    
    # imprimirDatos()
    def getAll(self):
        print("Nombre:", self.getNombre())
        print("Inversion: $", self.getInversion())
        if self.getDiferencia() < 0:
            print("Debe: $", round(self.getDiferencia() * -1, 2))
        if self.getDiferencia() >= 0:
            print("Se le debe: $", round(self.getDiferencia(), 2))

    def getAllVar(self):
        reg = [self.getNombre(), self.getInversion(), self.getDiferencia()]
        return reg
        
    # modDato()
    def modNombre(self, nNombre):
        self.nombre = nNombre
    def modInversion(self, nInversion):
        self.inversion = nInversion
    def modDiferencia(self, nDiferencia):
        self.diferencia = nDiferencia


