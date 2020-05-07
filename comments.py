import os

try:
    from bs4 import BeautifulSoup

except ImportError as err:
    raise err


def collect_comments():
    comments = []

    comments_dir = 'comments/'
    all_files = os.listdir(comments_dir)

    for file in all_files:
        with open(comments_dir + file, 'r') as comments_file:
            source = comments_file.read()

        soup = BeautifulSoup(source, "html.parser")

        hrefs = soup.find_all('a')

        for i in hrefs:
            href = i.get('href')

            if 'wall' in href:
                source_id = href.split('wall')[1].split('_')[0]
                comment_id = href.split('reply=')[-1].split('&')[0] if '&' in href else href.split('reply=')[-1]

                comment = (source_id, comment_id)
                
                if comment not in comments:
                    source_and_comment_ids.append(comment)

    return comments
