import sqlite3
import requests
from bs4 import BeautifulSoup
from sqlite3 import Error

with open("moneyControlLink.txt", encoding="utf8") as textFile:
    content = textFile.readlines()
textFile.close()

conn = sqlite3.connect('record1.sqlite3')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS stockData(id INTEGER PRIMARY KEY, name TEXT,exch TEXT, time TEXT, price TEXT, chng TEXT, vol TEXT, vol5 TEXT, vol10 TEXT, vol30 TEXT, prevClose TEXT, openPrice TEXT, bidPrice TEXT, offrPrice TEXT, vwap TEXT, buyQty TEXT, sellQty TEXT, low TEXT, high TEXT, low52 TEXT, high52 TEXT, lowPrc TEXT, highPrc TEXT)')

quote = []
for line in range(1):
    
    dataBSE = []
    url = content[5734]
    #print(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    company = soup.find("div", {"class": "b_42 PT5 PR"})
    bse = soup.find("div", {"class": "FL bseStDtl"})
    nse = soup.find("div", {"class": "FR nseStDtl"})
    bseDet = bse.find_all("div")
    nseDet = nse.find_all("div")

    name = company.find("h1").get_text()
    exch = bseDet[0].find("div", {"class": "FR PR3"}).get_text()
    time = bseDet[0].find("div", {"id": "bse_upd_time"}).get_text()
    price = bseDet[0].find("div", {"id": "Bse_Prc_tick_div"}).get_text()
    chng = bseDet[0].find("div", {"id": "b_changetext"}).get_text()
    vol = bseDet[0].find("span", {"id": "bse_volume"}).get_text()
    vol5 = bseDet[0].find("td", {"id": "avgvol5daysB"}).get_text()
    vol10 = bseDet[0].find("td", {"id": "avgvol10daysB"}).get_text()
    vol30 = bseDet[0].find("td", {"id": "avgvol30daysB"}).get_text()

    prevClose = bseDet[19].find("div", {"id": "b_prevclose"}).get_text()
    openPrice = bseDet[19].find("div", {"id": "b_open"}).get_text()
    bidPrice = bseDet[19].find("div", {"id": "b_bidprice_qty"}).get_text()
    offPrice = bseDet[19].find("div", {"id": "b_offerprice_qty"}).get_text()

    vwap = bseDet[33].find("span", {"class": "gD_11 ML3"}).get_text()
    buyQty = bseDet[33].find("p", {"id": "b_total_buy_qty"}).get_text()
    sellQty = bseDet[33].find("p", {"id": "b_total_sell_qty"}).get_text()
    todayLow = bseDet[33].find("span", {"id": "b_low_sh"}).get_text()
    todayHigh = bseDet[33].find("span", {"id": "b_high_sh"}).get_text()
    low52 = bseDet[33].find("span", {"id": "b_52low"}).get_text()
    high52 = bseDet[33].find("span", {"id": "b_52high"}).get_text()
    lowPriceLim = bseDet[33].find("span", {"id": "b_low_price_limit"}).get_text()
    highPriceLim = bseDet[33].find("span", {"id": "b_high_price_limit"}).get_text()


    c.execute('''INSERT INTO stockData(name, exch, time, price, chng, vol, vol5, vol10, vol30, prevClose, openPrice, bidPrice, offrPrice, vwap, buyQty, sellQty, low, high, low52, high52, lowPrc, highPrc)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (name, exch, time, price, chng, vol, vol5, vol10, vol30, prevClose, openPrice, bidPrice, offPrice, vwap, buyQty, sellQty, todayLow, todayHigh, low52, high52, lowPriceLim, highPriceLim)) 
    conn.commit()

conn.close
