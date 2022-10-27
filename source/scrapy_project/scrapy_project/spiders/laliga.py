import scrapy


class LaligaSpider(scrapy.Spider):
    name = 'laliga'
    allowed_domains = ['www.laliga.com/']
    start_urls = ['https://www.laliga.com/estadisticas/']
    # Para probar ejecutar: scrapy crawl laliga
    def parse(self, response):
        rows = response.xpath("//tr")

        for row in rows:
            position = row.xpath("./td[1]/a/text()").get()
            players = row.xpath("./td[1]//text()").get()
            teams = row.xpath("./td[2]//text()").get()
            goals = row.xpath("./td[3]//text()").get()
            matchs = row.xpath("./td[4]//text()").get()
            goals_by_match = row.xpath("./td[5]//text()").get()
            yield{
               "position": position,
               "players": players,
               "teams": teams,
               "goals": goals,
               "matchs": matchs,
               "goals_by_match": goals_by_match,
            }