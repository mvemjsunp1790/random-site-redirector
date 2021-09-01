Required environment variables:

* SITES=[comma separated list of redirection URLs. Protocol required]


Example docker-compose.yml:

    version: '2'
    services:
      random-site-redirector:
        image: mvemjsunp/random-site-redirector:latest
        restart: always
        ports:
          - "8000:8000"
        environment:
         - SITES=https://www.bbc.co.uk/news,https://www.theguardian.com/uk,https://apnews.com,https://www.reuters.com
