# Indeed scraper

from jobs_scraper import JobsScraper

class Job:
  def __init__(self, country=None, position=None, location=None, salary=None, 
  company=None):
    self.country = country
    self.position = position
    self.location = location
    self.salary = salary
    self.company = company


def Scrape():
  scraper = JobsScraper(country="US", position="Helpdesk Support", location="Kalamazoo", pages=3, max_delay=5)
  df = scraper.scrape()
  return df


def main():
  results = Scrape()
  print(results)


if __name__ == '__main__':
  main()
