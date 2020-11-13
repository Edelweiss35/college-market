from scraper_1 import Bot

with Bot() as scraper:
    link = "https://missouri.campuslabs.com/engage/organizations"
    name = "University of Missouri"
    scraper.browser_init(link, name)
    scraper.main()