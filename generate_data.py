
#Import de module
import random
import pandas as pd
import matplotlib.pyplot as plt

random.seed(2023)

def complete_0(value, nb_char = 3):
    """Take an positive integer and make a string that represent that integer
       in completing it with zero in front
    """
    val = str(value)
    return '0' * ( nb_char - len(val) ) + val

def random_date():
    """Generate random data in iso format
    """
    
    y = random.choice(['2023', '2022', '2021'])
    m = str( random.randint(1,12) )
    if (m == '2' and (int(y) % 4 == 0) and not (int(y) % 100 == 0) ):
        d = str( random.randint(1, 29) )
    elif m == '2' :
        d = str( random.randint(1, 28) )
    else :
        d = str( random.randint(1, 30) )

    if len(m) < 2 :
        m = '0' + m
    if len(d) < 2 :
        d = '0' + d

    return y + '/' + m + '/' + d

def dataframe2sql(df, tab_name, dir = "./sql/"):
    """Save a dataframe in a .sql insert tab
    """
    with open(dir + tab_name + ".sql", 'w') as data :
        data.write( f"INSERT INTO {tab_name}({', '.join(df.columns)}) \n")
        data.write("VALUES \n")
        values = [str(v) for v in df.itertuples(index=False, name=None)]
        data.writelines( ',\n'.join( values ) )

if __name__ == '__main__' :

    nb_prod = 800
    nb_bat = 6
    nb_conso = 600
    enr = ['Hydraulique', 'Eolienne', 'Solaire', 'Biomasse', 'Geothermie']
    energie = ['Gaz naturel', 'Electricité']

    batiment = pd.DataFrame({
        'id_batiment' : ['B' + complete_0(i) for i in range(nb_bat)],
        'nom_batiment' : ['Bâtiment ' + chr(65 + i) for i in range(nb_bat)],
        'surface' : [10 * int( random.uniform(5, 16) * 10 ) for i in range(nb_bat)],
        'annee_construction' : [random.randint(1980, 2001) for i in range(nb_bat)]
        })
    
    ids_batiment = batiment['id_batiment'].to_list()
    ids_batiment.extend( random.choices(batiment['id_batiment'], k = (nb_prod - nb_bat)) )
    random.shuffle(ids_batiment)

    type_enr = list(enr)
    type_enr.extend( random.choices(enr, k= (nb_prod -len(enr)) ) )
    random.shuffle(type_enr)

    production = pd.DataFrame({
        'id_production' : ['P' + complete_0(i) for i in range(nb_prod)],
        'id_batiment' : ids_batiment,
        'quantite_produite' : [10 * int( random.uniform(0.1, 7) * 10 ) for i in range(nb_prod)],
        'type_energie_renouvelable' : type_enr,
        'date_production' : [random_date() for i in range(nb_prod)]
    })

    ids_batiment_conso = batiment['id_batiment'].to_list()
    ids_batiment_conso.extend(random.choices(batiment['id_batiment'], k = (nb_conso - nb_bat)))
    random.shuffle( ids_batiment_conso )

    col_enrergie = list(energie)
    col_enrergie.extend( random.choices(enr, k= (nb_conso -len(energie)) ) )
    random.shuffle(type_enr)

    consommation = pd.DataFrame({
        'id_consommation' : ['C' + complete_0(i) for i in range(nb_conso)],
        'id_batiment' : ids_batiment_conso,
        'consommation_kwh' : [10 * int( random.uniform(0.1, 5) * 10 ) for i in range(nb_conso)],
        'type_energie' : col_enrergie,
        'date_consommation' : [random_date() for i in range(nb_conso)]
    })

    #Write dataFrame in sql format
    dataframe2sql(batiment, 'batiments')
    dataframe2sql(consommation, 'consommation_energetique')
    dataframe2sql(production, 'production_energies_renouvelables')