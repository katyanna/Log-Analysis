import psycopg2
import pdb

DBNAME = 'news'

most_popular_articles = "SELECT * FROM articles_popularity LIMIT 3;"

most_popular_authors = """
                        SELECT SUM(articles_popularity.count) AS views,
                                authors.name
                        FROM authors
                        JOIN articles_popularity
                            ON authors.id = articles_popularity.author
                        GROUP BY authors.name
                        ORDER BY views DESC;
                        """

days_with_more_errors = "SELECT * FROM errors WHERE errors_percentage > 1"

def answer(query):
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()

    c.execute(query)

    answer = c.fetchall()
    conn.close()

    for x in answer:
        print(x[0], ' - ',x[1])

if __name__ == '__main__':
    print("\n[1] What are the most popular three articles of all time?")
    answer(most_popular_articles)

    print("\n[2] Who are the most popular article authors of all time?")
    answer(most_popular_authors)

    print("\n[3] On which days did more than 1% of requests lead to errors?")
    answer(days_with_more_errors)
