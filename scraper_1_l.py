from scraper_1 import Bot

with Bot() as scraper:
    link = "https://involvement.und.edu/organizations"
    name = "University of North Dakota"
    scraper.browser_init(link, name)
    scraper.main()