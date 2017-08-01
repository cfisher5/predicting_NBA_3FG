import csv
import mysql.connector

# This method does the grunt work - it iterates through the NBA stats DB
# and finds a match in the NCAA DB. Then it writes a row in a new csv with
# college shooting stats and NBA 3PT%

def filter_data(file1, file1_id_pos, file2, file2_id_pos, newfile):

    test_data = open(newfile, 'w')
    w = csv.writer(test_data, delimiter=",")
    header_row = "sports_ref_ID,Player,From,To,School,Conf,G,MP,3P,3PA,threeP_percent," \
                 "FT,FTA,FT_percent,PTS,3PG,threePAG,basketball_ref_ID,Player,G,MPG,3P," \
                 "3PA,NBA_3P_percent"
    w.writerow([header_row])

    with open(file1, 'r') as nba_file:
        nba = csv.reader(nba_file, delimiter=",")

        for row_nba in nba:
            if row_nba:
                nba_id = row_nba[file1_id_pos]
                ncaa_id = get_ncaa_id(nba_id)

                with open(file2, "r") as ncaa_file:
                    ncaa = csv.reader(ncaa_file, delimiter=",")

                    for row_ncaa in ncaa:
                        if row_ncaa:
                            id = row_ncaa[file2_id_pos]

                            if ncaa_id == id:

                                print("MATCH: " + row_nba[1])
                                row_to_add = row_ncaa + row_nba
                                w.writerow(row_to_add)

                ncaa_file.close()
    nba_file.close()


def get_ncaa_id(nba):

    cnx = mysql.connector.connect(host='localhost', user='root', database="players_db")
    cursor = cnx.cursor()
    get_ncaa = (
        "SELECT sports_ref_ID from players "
        "WHERE basketball_ref_ID = %s"
    )

    cursor.execute(get_ncaa, (str(nba),))
    ncaa_db = cursor.fetchone()
    if ncaa_db is None:
        return None
    return ncaa_db[0]

