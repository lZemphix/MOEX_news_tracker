import parser, time,logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    date, time_, link, title = parser.get_last_news_base_data()
    # text = parser.get_last_news_full_data()
    text = parser.get_full_information()

    while True:
        with open(f"/home/zemphix/Рабочий стол/pythonina/invest_news_parser/news/{date}_{time_}.md", "w") as f:
            f.write(f"""# {title} 

{text}

{date} {time_}

Ссылка: https://www.moex.com{link}""")
        time.sleep(15)  



if __name__ == "__main__":
    main()
    try:
        main()
    except Exception as e:
        print(f"something went wrong: {e}")
        logging.error(f"something went wrong: {e}")