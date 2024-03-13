import psycopg2

class cp:
    def psyco():
        conect = psycopg2.connect(
            host="localhost",
            database="dankibanco",
            user="postgres", password="postgres")
        

        cursor = conect.cursor()
        cur = cursor.execute("""SELECT id, ativo, created, motivoinativacao, updated, descricao, nome, valor FROM public.produto;""")
        result = cursor.fetchall()
        return result