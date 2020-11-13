from scraper_1 import Bot

with Bot() as scraper:
    link = "https://msu.campuslabs.com/engage/organizations"
    name = "Michigan State University"
    scraper.browser_init(link, name)
    scraper.main()