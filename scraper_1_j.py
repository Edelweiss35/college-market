from scraper_1 import Bot

with Bot() as scraper:
    link = "https://utk.campuslabs.com/engage/organizations"
    name = "University of Tennessee, Knoxville"
    scraper.browser_init(link, name)
    scraper.main()