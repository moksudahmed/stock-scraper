from pickle import TRUE
import requests
import sys
import json
import stockurl
import threading
from bs4 import BeautifulSoup
from csv import writer
import save_data
def connection():
    try:    
        response= requests.get(stockurl.top_20_share_url).text    
    except:
        sys.exit("Failed to connect!")

    soup = BeautifulSoup(response, "html.parser")
    tabl = soup.find("table", class_="table")    
    return tabl

def remove_character(line):
    line = line.replace('\r', '')
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    return line

def scrap():
    
    tabl = connection()

    try:
            ls_dict = []
            # Extract data from html table 
            for row in tabl.find_all('tr')[1:]:
                ds = {"SL":"",
                    "TRADING_CODE":"",
                    "LTP":"",
                    "HIGH":"",
                    "LOW":"",
                    "YCP":"",
                    "CLOSE":"",
                    "TRADE":"",
                    "VALUE":"",
                    "VOLUME":""
                    }
                td = row.find_all('td')            
                # Update data to a dictonary
                ds.update({ "SL":td[0].text,
                            "TRADING_CODE":remove_character(td[1].text), 
                            "LTP" : remove_character(td[2].text), 
                            "HIGH" : remove_character(td[3].text),
                            "LOW" : remove_character(td[4].text),
                            "YCP" : remove_character(td[5].text),
                            "CLOSE" : remove_character(td[6].text),                           
                            "TRADE" : remove_character(td[7].text),
                            "VALUE" : remove_character(td[8].text),
                            "VOLUME": remove_character(td[9].text)
                        })
                #Generate a list of dictonary
                ls_dict.append(ds)
            # Write a list to a JSON file
           # json_object = json.dumps(ls_dict, indent=4)                    
            save_data.save(ls_dict, 'top20stock')
            print("Sucessfully saved top 20 stock data")
    except:
        sys.exit("Faild to extract data")
    return ls_dict

