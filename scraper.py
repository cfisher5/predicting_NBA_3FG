from urllib.request import urlopen
from bs4 import BeautifulSoup


def real_gm_scrape(url_input, filename, last_page, league):

    file = open(filename, 'a')
    for i in range(1, last_page):
        if league == "nba":
            url = url_input + str(i) + "/Regular_Season"
        else:
            url = url_input + str(i)
        page = urlopen(url)
        soup = BeautifulSoup(page, "html.parser")

        r_table = soup.find('table', {"class": "tablesaw compact"})

        if r_table is None:
            print("end of data")
            break

        print("Scraping page " + str(i))
        for row in r_table.findAll("tr"):

            cells = row.findAll("td")

            for cell in cells:
                if cell.string is None:
                    if cell.find("a") is not None:
                        value = cell.find("a").string.replace(",", "")
                        file.write(value + ",")
                    else:
                        file.write(',')
                else:
                    value = cell.string.replace(",", "")
                    file.write(value + ',')

            file.write('\n')
    file.close()


def sports_ref_scrape(url, filename):

    file = open(filename, 'a')
    for i in range(0, 6000, 100):
        url2 = url + str(i)
        page = urlopen(url2)
        soup = BeautifulSoup(page, "html.parser")
        r_table = soup.find('table', {"id": "stats"})

        if r_table is None:
            print("end of data")
            break

        print("Scraping page " + str(i))
        for row in r_table.find("tbody").findAll("tr"):

            player_name_col = row.find("td")
            print(player_name_col.a.string)
            if player_name_col is not None:
                player_id = player_name_col.a['href']
                file.write(player_id + ',')
            cells = row.findAll("td")
            for cell in cells:
                if cell.string is not None:
                    file.write(str(cell.string) + ',')
                else:
                    file.write(',')

            file.write('\n')

    file.close()


def get_draft_class_ids(url, filename):

    file = open(filename, 'a')
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    r_table = soup.find('table', {"id": "stats"})

    for row in r_table.find("tbody").findAll("tr"):

        cells = row.findAll("td")
        for cell in cells:
            if cell.a is not None:
                file.write(cell.a.string + ",")
                file.write(cell.a['href'] + ",")

        file.write('\n')

    file.close()