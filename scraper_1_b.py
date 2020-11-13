from scraper_1 import Bot

with Bot() as scraper:
    link = "https://asu.campuslabs.com/engage/organizations"
    name = "Arizona State University"
    scraper.browser_init(link, name)
    scraper.main()