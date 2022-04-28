import os
import sys
import datetime
import requests
#$ python -m pip install requests-html ==0.10.0
from regex import B  #import requests    #import pip._vendor.requests on vscode or any terminal that gives issues with requests installation
from requests_html import HTML
import pandas as pd

BASE_DIR = os.path.dirname (__file__)

url = "https://www.boxofficemojo.com/year/world/"
now = datetime.datetime.now()
year = now.year #brings a date object into it. you can do day, month.. whatever


def url_to_txt(url, filename='world.html', save =False):
    r = requests.get(url)
    if r.status_code ==200:
        html_text= r.text
        if save:
            with open (f'world-{year}.html', 'w') as f:
        #with open(filename, 'w')as f:
                f.write(html_text)
        return html_text
    return None

def parse_and_extract(url, name = '2022'):
    html_text = url_to_txt(url)
    if html_text ==None:
        return False
    r_html = HTML (html=html_text)
    table_class = ".imdb-scroll-table"
#table_class = '#table'
#table_class = "a". a-tag, that will print all the links that is in that weblink
    r_table= r_html.find(table_class)

#print(r_table)
    table_data = []
    table_data_dicts = []
    header_names = []
    if len (r_table) == 0:
        return False
    #print (r_table[0].text)
    #to turn this table into a list of lists, and into a csv at some point
    parsed_table = r_table[0]
    rows = parsed_table.find ('tr') # tr stands for Table Row
    #cmd+shift+p(on web browser) - to enable and disable javascirpt to see more informed developer options
    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [x.text for x in header_cols]  #same as what was done down below,  but this is in 1 line
    for row in rows[1:]:
        #print(row.text)
        cols=row.find('td')
        row_data = [] 
        row_dict_data = {}
        for i,col in enumerate(cols):
            header_name = header_names[i]
            # row_dict_data[header_name] = col.text
            #print(i, col.text, '\n\n' )
            row_data.append(col.text)
        table_data_dicts.append (row_dict_data)
        table_data.append(row_data)
        #i = 0
        #for x in row:  .......> same function as above
         #   i+=1
          #  print (i, x)

    df = pd.DataFrame(table_data, columns = header_names)
    path = os.path.join(BASE_DIR, 'data')
    os.makedirs (path, exist_ok = True)
    filepath = os.path.join('data', f'{name}.csv')
    #df.to_csv(f'data/{name}.csv', index = False)
    df.to_csv(filepath, index=False)
    return True

def run(start_year=None, years_ago=0):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    for i in range(0, years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"Finished {start_year}")
        else:
            print(f"{start_year} not finished")
        start_year -= 1



if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 0
    run(start_year=start, years_ago=count)