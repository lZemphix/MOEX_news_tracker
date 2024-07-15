import parcer, time,logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")

def get_last_news():
    """return date, time, title, text every 20 seconds"""
    time.sleep(15)
    last_new_date, last_new_time, link, last_new_title = parcer.get_last_news_base_data()
    news_text = parcer.get_last_news_full_data()
    return last_new_date, last_new_time, link, last_new_title, news_text

def main():
    previous_new_title = []
    while True:
        date, time, link, title, text = get_last_news()
        if title not in previous_new_title:
            with open(f"invest_news_parcer/news{date}_{time}.md", "w") as f:
                f.write(f"""# {title} 

{text}

{date} {time}

Ссылка: https://www.moex.com{link}""")
            previous_new_title.clear()
        else:
            previous_new_title.append(title)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"something went wrong: {e}")
        logging.error(f"something went wrong: {e}")