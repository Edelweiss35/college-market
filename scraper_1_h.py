from scraper_1 import Bot

with Bot() as scraper:
    link = "https://usf.campuslabs.com/engage/organizations"
    name = "University of South Florida"
    scraper.browser_init(link, name)
    scraper.main()