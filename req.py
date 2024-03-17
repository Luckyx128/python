import requests


class RequestClass:
        
        
    def ReqClass():
            session = requests.session()


            cep = '81490053'
            return (session.get(f"https://viacep.com.br/ws/{cep}/json/").text)



