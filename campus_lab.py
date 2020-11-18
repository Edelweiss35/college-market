from scraper_1 import Bot

with Bot() as scraper:
    link = ""
    name = ""
    scraper.browser_init(link, name)
    scraper.main()