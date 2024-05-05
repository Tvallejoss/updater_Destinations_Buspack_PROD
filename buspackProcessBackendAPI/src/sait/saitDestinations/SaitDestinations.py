
class SaitDestinations:
    def __init__(self, token):
        self.activos = 1
        self.url = 'https://rest.empresar-sys.com.ar:1433/sait/destinosHabilitados'
        self.token = token.json().get('token')

    def parametersFormData(self):
        return {"activos" : self.activos}
    
    def headerToken(self):
        return {"token" : self.token}
