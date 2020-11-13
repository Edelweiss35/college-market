from scraper_1 import Bot

with Bot() as scraper:
    link = "https://k-state.campuslabs.com/engage/organizations"
    name = "Kansas State University"
    scraper.browser_init(link, name)
    scraper.main()