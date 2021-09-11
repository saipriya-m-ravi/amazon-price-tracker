import pandas
from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd

HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept-Language":"en-US,en;q=0.5"
}

data_dict = {
    "url" : ["https://www.amazon.in/Climate-Trekking-Travel-compar-Rucksack/dp/B09BJTQ1J6?ref_=Oct_d_onr_d_1984997031&pd_rd_w=rThBT&pf_rd_p=4599172e-6201-4ea0-865b-8d658f9bdd69&pf_rd_r=CD2H1TFM9BGVYT3Q5KPV&pd_rd_r=b0a26a04-275c-41f3-a456-dbb57a6b71aa&pd_rd_wg=ILOor&pd_rd_i=B09BJXXPLQ&th=1", "https://www.amazon.in/HP-21-5-inch-Desktop-Keyboard-22-df0444in/dp/B098BKMSG7?ref_=Oct_d_orecs_d_10384420031&pd_rd_w=SBMta&pf_rd_p=b03e4d5d-30a1-4b98-9fee-e5c8fa7446f9&pf_rd_r=JRX6BRR8YFENWE3XZCQ2&pd_rd_r=48ca2b5d-eeed-4aad-b20b-b720ea69e7e9&pd_rd_wg=kW6ah&pd_rd_i=B098BKMSG7", "https://www.amazon.in/Ray-Ban-protected-Sunglasses-0RB3129IW022658-millimeters/dp/B00JZ48QT4/ref=sr_1_7?dchild=1&pf_rd_i=1968036031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=a1c959b9-2121-4b12-af5c-30067f7b2857&pf_rd_r=639AT1T58F27VZPZ356V&pf_rd_s=merchandised-search-6&qid=1631343297&refinements=p_n_feature_fifteen_browse-bin%3A4296235031%2Cp_36%3A100-&s=apparel&sr=1-7","https://www.amazon.in/Bizanne-Fashion-Backpack-College-Stylish/dp/B09C22LXTH/ref=sr_1_5?dchild=1&pf_rd_i=17939238031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=0122df46-1bfc-4588-9b9a-4f1f9a86b8b6&pf_rd_r=2KERHMK1CAAXK4NMXND5&pf_rd_s=merchandised-search-6&qid=1631343485&refinements=p_n_pct-off-with-tax%3A00-%2Cp_85%3A10440599031&rnid=10440598031&rps=1&s=shoes&sr=1-5","https://www.amazon.in/Love-out-Stock-Guan-Yuxi/dp/7530672347/ref=sr_1_4?dchild=1&keywords=out+of+stock&qid=1631348267&sr=8-4"],
    "buy_below" : [2000,30000,3000,150,100]
}

data=pandas.DataFrame(data_dict)
data.to_csv("tracker.csv")
prod_tracker = pd.read_csv("tracker.csv")
prod_tracker_URLS = prod_tracker.url

for x,url in enumerate(prod_tracker_URLS):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")

    # Scraping product name
    title = soup.find(id='productTitle').get_text().strip()

    # Checking if out of stock
    stock = soup.find(name="span", class_="a-size-medium a-color-price").get_text()

    if stock != "Currently unavailable.":
        # Scraping price details
        price = float(soup.find(id='priceblock_ourprice').get_text().replace(",","")[1:])

        if price and price < prod_tracker.buy_below[x]:
            # Sending email alert
            print(f"Price for - {title} - has gone below {prod_tracker.buy_below[x]}. Go and get it soon !")







