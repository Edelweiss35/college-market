from scraper_1 import Bot

with Bot() as scraper:
    link = "https://maizepages.umich.edu/organizations"
    name = "University of Michigan"
    scraper.browser_init(link, name)
    scraper.main()