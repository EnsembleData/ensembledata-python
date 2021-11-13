import sys
sys.path.append('../src')
sys.path.append('src')

from scraper import IH_scraper


# Get a free token at www.influencerhunters.com
TOKEN = "XXXXXXXXXXXX"

#Initialize sender class 
scraper = IH_scraper(token_IH_API=TOKEN)

#Send the request to the IH server
print("sending the request..")
res, success = scraper.tt.get_post_from_keyword("maigc", period = 1, sorting = 0, cursor = 0)


if success:
    print("Success!")
else:
    print("Something went wrong, check the response for more information. \n(Did you insert a valid token?)")
