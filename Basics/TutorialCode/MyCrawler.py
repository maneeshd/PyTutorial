from bs4 import BeautifulSoup
from requests import get


def forum_scraper(max_pages=50):
    page = 1
    while page <= max_pages:
        url = "https://thenewboston.com/forum/recent_activity.php?page=" + str(page)
        src_code = get(url).text
        crawler = BeautifulSoup(src_code, "html.parser")
        for link in crawler.find_all("a", {"class": "title text-semibold"}):
            title = link.string.replace(" ", "")
            print(title)
            print(link.get("href"))
        page += 1


def main():
    forum_scraper(5)

if __name__ == '__main__':
    main()
