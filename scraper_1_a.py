from scraper_1 import Bot

with Bot() as scraper:
    link = "https://fsu.campuslabs.com/engage/organizations"
    name = "Florida State University"
    scraper.browser_init(link, name)
    scraper.main()