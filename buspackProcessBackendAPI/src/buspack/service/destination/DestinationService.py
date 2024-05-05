
class DestinationService:

    def __init__(self,response):
        self.statusCode = response.status_code
        self.message = response.json().get('mensaje')
        self.url = 'https://rest.empresar-sys.com.ar:1433/sait/destinosHabilitados'

    def runCheckAvailableDestinations(self):
        if not ( ( self.statusCode  == 200 or self.statusCode  == 201 ) and self.message == 'Correcto'):
            print("Destinations Request Fails --> " + "Code: ", self.statusCode,", Mensaje: ", self.message)
            exit()
        else:
            print("Available Destinations Achieve  successfully")