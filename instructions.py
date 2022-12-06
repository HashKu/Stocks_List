import csv, os
from os.path import exists




def create(name, value, buy_date):
    id_last=0
    if not exists('informations.csv'):

        with open('informations.csv', 'wt', newline='') as file_out:
            reader = csv.DictWriter(file_out, ['id', 'name', 'value', 'buy_date'])
            reader.writeheader()
            reader.writerow({'id': id_last, 'name': name, 'value': value, 'buy_date': buy_date})
    else:
        with open('informations.csv', 'rt') as file_in:
            
            reader = csv.DictReader(file_in)

            for row in reader:
                stocks = dict(row)
            
                id_last=int(stocks['id'])+1
            file_in.close()
        
        with open('informations.csv', 'at') as file_in:
            
            registro=csv.DictWriter(file_in, ['id', 'name', 'value', 'buy_date'])

            registro.writerow({'id': id_last, 
                                'name': name, 
                                'value': value, 
                                'buy_date': buy_date})
            file_in.close()

def delete(id):
    resultado=[]
    with open('informations.csv', 'rt') as file_in:
        reader = csv.DictReader(file_in)

        for row in reader:

            stocks = dict(row)

            if id!=stocks['id']:
                evento={'id': stocks['id'], 
                        "name": stocks['name'], 
                        "value": stocks['value'], 
                        "buy_date": stocks['buy_date']}
                resultado.append(evento)
        file_in.close()

    with open("informations.csv", "wt", encoding='utf-8') as file_out:

        reader = csv.DictWriter(file_out, ['id', 'name', 'value', 'buy_date'])
        reader.writeheader()
        reader.writerows(resultado)
        file_in.close()

    return 'ok'


def update(id, name, value, buy_date):
    resultado =[]
    with open("informations.csv", "rt") as file_in:

        reader = csv.DictReader(file_in)

        for row in reader:

            stocks = dict(row)

            if id==stocks['id']:

                 evento={'id': stocks['id'], "name": name, "value": value, "buy_date": buy_date}

            else:

                evento={'id': stocks['id'], "name": stocks['name'], "value": stocks['value'], "buy_date": stocks['buy_date']}

            resultado.append(evento)
        file_in.close()

    

    with open("informations.csv", "wt", encoding='utf-8') as file_out:

        reader = csv.DictWriter(file_out, ['id', 'name', 'value', 'buy_date'])
        reader.writeheader()
        reader.writerows(resultado)
        file_in.close()
        
    return 'ok'


def load():
    tasks=[]
    if exists('informations.csv'):

        with open("informations.csv", "rt", encoding='utf-8') as file_in:
            reader = csv.DictReader(file_in)

            for row in reader:
                stocks = dict(row)
                eventos={'id': stocks['id'],
                         'name': stocks['name'], 
                         'value': stocks['value'],
                         'buy_date': stocks['buy_date']}
                tasks.append(eventos)
    return tasks
