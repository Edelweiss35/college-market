# import os


# def start():
    # os.system(  '/usr/bin/python3.6 /root/college-market/scraper_1_a.py &'
    #             '/usr/bin/python3.6 /root/college-market/scraper_1_b.py &'
    #             '/usr/bin/python3.6 /root/college-market/scraper_1_c.py &'
    #             '/usr/bin/python3.6 /root/college-market/scraper_1_d.py &'
    #             '/usr/bin/python3.6 /root/college-market/scraper_1_e.py &')
    # os.system('~/Desktop/workspace/emScraper_v2/venv/bin/python3.6 ~/Desktop/workspace/emScraper_v2/college-market/scraper_1_a.py &'
    #           '~/Desktop/workspace/emScraper_v2/venv/bin/python3.6 ~/Desktop/workspace/emScraper_v2/college-market/scraper_1_b.py &'
    #           '~/Desktop/workspace/emScraper_v2/venv/bin/python3.6 ~/Desktop/workspace/emScraper_v2/college-market/scraper_1_c.py &')
              # '~/Desktop/workspace/emScraper_v2/venv/bin/python3.6 ~/Desktop/workspace/emScraper_v2/college-market/scraper_1_d.py &'
              # '~/Desktop/workspace/emScraper_v2/venv/bin/python3.6 ~/Desktop/workspace/emScraper_v2/college-market/scraper_1_e.py &')

# start()

import applescript
import os
path = os.path.abspath(os.getcwd())
print(path)

cmd = 'cd {}; python3 scraper_1_a.py'
applescript.tell.app('Terminal', 'do script "' + cmd + '"', background=True )
cmd = 'cd {}; python3 scraper_1_b.py'
applescript.tell.app('Terminal', 'do script "' + cmd + '"', background=True )
cmd = 'cd {}; python3 scraper_1_c.py'
applescript.tell.app('Terminal', 'do script "' + cmd + '"', background=True )
cmd = 'cd {}; python3 scraper_1_d.py'
applescript.tell.app('Terminal', 'do script "' + cmd + '"', background=True )
cmd = 'cd {}; python3 scraper_1_e.py'
applescript.tell.app('Terminal', 'do script "' + cmd + '"', background=True )