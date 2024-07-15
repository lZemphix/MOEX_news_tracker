import requests, logging
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")

def get_main_url_data(url: str, title: str = None) -> str:
    
    handlers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
    }

    response = requests.get(url, headers=handlers)
    logging.debug(f"request url: {url}, status: {response.status_code}") #debug
    if title != None:
        with open(f"/home/zemphix/Рабочий стол/pythonina/invest_news_parser/htmls/{title}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
    return response.text
    
def get_last_news_base_data():
    response = get_main_url_data("https://www.moex.com/ru/news/")
    soup = BeautifulSoup(response, "lxml")
    last_new_date = soup.find("div", class_="new-moex-news-list__date").text.strip()
    last_new_time = soup.find("div", class_="new-moex-news-list__time").text.strip()
    last_new_title = soup.find("a", class_="new-moex-news-list__link").text.strip()
    link = soup.find("a", class_="new-moex-news-list__link").get("href")
    logging.debug(f"get last_new_date: {last_new_date}, get last_new_time: {last_new_time},get last_new_title: {last_new_title}, get link: {link}") #debug
    return last_new_date, last_new_time, link, last_new_title
    
def get_full_information():

    response = get_main_url_data(f"https://www.moex.com/{get_last_news_base_data()[2]}")
    soup = BeautifulSoup(response, "lxml")

    text_html = soup.find("div", class_="news_text")
    filtered = []

    for el in text_html.text.split('\n\n\n'):
        if el != '':
            filtered.append(el)
    return ":".join(filtered)
    


if __name__ == "__main__":
    # print(get_last_news_full_data())
    print(get_full_information())
    # get_full_information()
    try:
        ...
        # get_main_url_data('https://www.moex.com/n71218?nt=0', 'table')
    except Exception as e:
        print(f"something went wrong: {e}")
        logging.error(f"something went wrong: {e}")
    