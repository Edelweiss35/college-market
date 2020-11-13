from scraper_1 import Bot

with Bot() as scraper:
    link = "https://unl.campuslabs.com/engage/organizations"
    name = "University of Nebraska"
    scraper.browser_init(link, name)
    scraper.main()