stock_url="https://www.dse.com.bd/latest_share_price_scroll_l.php"
individual_stock_url = "https://www.dse.com.bd/displayCompany.php?name=AAMRATECH"
news_url = "https://www.amarstock.com/dse-news"
top_ten_gainer_url = "https://www.dse.com.bd/top_ten_gainer.php"
top_ten_looser_url = "https://www.dse.com.bd/top_ten_loser.php"
top_20_share_url = "https://www.dse.com.bd/top_20_share.php"


cse_stock_url = "https://www.cse.com.bd"

def get_url():
    return stock_url

def get_individual_stock_url(stockid):
    return "https://www.dse.com.bd/displayCompany.php?name="+stockid

def get_news_url():
    return news_url

def get_top_ten_gainer_url():
    return top_ten_gainer_url

def get_top_ten_looser_url():
    return top_ten_looser_url

def get_20_share_url():
    return top_20_share_url

def get_cse_stock_url():
    return cse_stock_url