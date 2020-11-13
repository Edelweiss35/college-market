from scraper_1 import Bot

with Bot() as scraper:
    link = "https://involvement.und.edu/organizations"
    scraper.browser_init(link)
    scraper.main()