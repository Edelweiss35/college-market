from scraper_1 import Bot

with Bot() as scraper:
    link = "https://k-state.campuslabs.com/engage/organizations"
    scraper.browser_init(link)
    scraper.main()