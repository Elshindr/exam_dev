"""
IMPORT AND TRANSFORM DATAS
"""
import pandas as pd 


def get_df_nba() :
    """
    Prepare the csv file
    Return pandas DataFrame
    """
    df = pd.read_csv('assets/nba_2013.csv')
    df = df[ df['bref_team_id'] != "TOT" ]
    df = df[ df['pos'] != "G" ]
    df = df.drop(["season", "ft.", "fg.", "efg." ], axis = 1)
    df.rename(columns={"bref_team_id": "Equipe",
                       "pts":"Point",
                       "mp":"Minute joué",
                       #"ft.":"Lancer Francs",
                       "orb":"Rebond Offensif",
                       "drb":"Rebond défensif",
                       "stl":"Interception",
                       "blk":"Contre",
                       "tov":"Perte de Balle",
                       "pf":"Faute",
                       "pos":"Poste",
                       "age":"Age",
                       "player":"Joueur",
    }, inplace=True)
    

    #print(df.head())
    #print("==============================================================================================")
    return df

def get_rookies_seniors():
    """
    Return 2 tuples with pandas DataFrame by player's category
    """
    rookies = df_nba[df_nba["Age"] <= 24 ].sort_values("Joueur")
    seniors = df_nba[df_nba["Age"] > 24 ].sort_values("Joueur")
    
    return rookies, seniors

def get_lst_caracts():
    """
    Get the caracteristics list for the teams dropdown
    """
    lst_caracts = df_nba.columns
    lst_caracts = [c for c in lst_caracts if c not in ["Joueur", "Age", "season", "Equipe", "Poste"]]
    lst_caracts.sort()
    
    return lst_caracts

def get_lst_postes():
    """
    Get the caracteristics list for the teams dropdown
    """
    lst_postes = df_nba['Poste'].unique().tolist()
    lst_postes.append("Aucun")
    lst_postes.sort()

    return lst_postes
   
    

df_nba = get_df_nba()