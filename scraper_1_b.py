from scraper_1 import Bot

with Bot() as scraper:
    if scraper.readGoogleSheet(1):
        scraper.browser_init()
        scraper.main()
        scraper.updateGoogleSheet()