import sys
sys.path.append('../src')
sys.path.append('src')

from scraper import ED_scraper


# Get a free token at https://www.ensembledata.com/register
TOKEN = "XXXXXXXXXXXX"

#Initialize sender class 
scraper = ED_scraper(token_ED_API=TOKEN)

#Send the request to the ED server
print("sending the request..")
res, success = scraper.yt.get_search("magic",2)


if success:
    print("Success!")
else:
    print("Something went wrong, check the response for more information. \n(Did you insert a valid token?)")
