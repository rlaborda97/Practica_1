import webtech

web_tech = webtech.WebTech()
technologies = web_tech.start_from_url('https://www.habitaclia.com/', timeout=1)
print(technologies)