from scraper_1 import Bot

with Bot() as scraper:
    link = "https://ramlink.campuslabs.com/engage/organizations"
    name = "Colorado State University"
    scraper.browser_init(link, name)
    scraper.main()