import requests
import json

def consult(Movie_Title):
    API_key = '7657f2bb'
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=%s&t=%s' % (API_key, Movie_Title))
        dict = json.loads(req.text)  # transforma o arquivo em .json
        return dict
    except:
        return None



def create_txt(json_do_filme):
    # Cria o arquivo .txt

    file = open(json_do_filme['Title'] +".txt", 'w')

    for value in json_do_filme:
        file.write("%s: %s\n"% (value, json_do_filme[value]))

    file.close()


def main():
    while True:
            filme = input('digite o nome do filme a consultar ou digite SAIR para fechar: ')
            if filme.upper() == 'SAIR':
                print("Saindo...")
                exit()
            else:
                dict_movie = consult(filme)
                if dict_movie['Response'] == 'False':
                    print("filme não encontrado")
                else:
                    create_txt(dict_movie)


main()