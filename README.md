# stockx-web-scraper-app-thingy
this is a stockx web scraper app thingy. I don't really have a vision for it but i'm just hacking around

## curr functionality
- this goes to stockx.com and get the top trending sneakers/streetwear
- i also cache in an apache cassandra db cause i noticed it was taking a while to query the stockx page

## initial setup
- install apache cassandra and beautiful soup
- then setup cassandra(instructions later) and create a keyspace, table, etc


## running
- go to root dir and run `export FLASK_APP=main`
- then run the command `flask run`
- now you can go to `http://127.0.0.1:5000/` to see the running app. 
- try hitting the endpoint `/top-sneaker-brand` to see the top trending brand on stockx
- 

.... more to come soon





