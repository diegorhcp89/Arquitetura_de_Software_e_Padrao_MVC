"""
exc type: 0 tipo da exceção que ocorreu, se houver.  
Se não ocorreu nenhuma exceção, este parâmetro será None.

exc val: 0 valor da exceção que ocorreu, se houver.  
Se não ocorreu nenhuma exceção, este parâmetro será None.

exc tb: 0 traceback (rastreamento de pilha) associado à exceção que ocorreu,  
Se não ocorreu nenhuma exceção, este parâmetro será None.

"""
class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo")

with AlgumaCoisa() as something:
    print("estou no meio")
