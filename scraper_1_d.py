from scraper_1 import Bot

with Bot() as scraper:
    link = "https://ttu.campuslabs.com/engage/organizations"
    name = "Texas Tech University"
    scraper.browser_init(link, name)
    scraper.main()