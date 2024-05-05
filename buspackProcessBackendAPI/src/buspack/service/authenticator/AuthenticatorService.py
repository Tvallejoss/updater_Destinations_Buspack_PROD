class AuthenticatorService:

    def __init__(self,response):
        self.statusCode = response.status_code
        self.message = response.json().get('mensaje')
        self.url = 'https://rest.empresar-sys.com.ar:1433/auth'

    def runCheckAuthentication(self):
        if not (self.statusCode  == 200 and self.message == 'Autorizado'):
            print("Authentication Fail --> " + "Code: ",  self.statusCode,", Mensaje: ", self.message)
            exit()
        else:
            print("Authentication completed successfully")







