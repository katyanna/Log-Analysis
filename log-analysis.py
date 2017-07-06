import psycopg2

DBNAME = 'news'

def choose(choice):
    if choice == '1':
        most_popular_articles()
    elif choice == '2':
        most_popular_authors()
    elif choice == '3':
        days_with_more_errors()
    else:
        choice = input('Enter only the number of your question: ')
        choose(choice)

def most_popular_articles():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()

    c.execute("""
    SELECT * FROM articles_popularity
    LIMIT 3;
    """)

    answer = c.fetchall()
    conn.close()

    for i, x in enumerate(answer, start = 1):
        print('{} - {} '.format(i, x[1]))

def most_popular_authors():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()

    c.execute("""
    SELECT SUM(articles_popularity.count) AS views,
            authors.name
    FROM authors
    JOIN articles_popularity
        ON authors.id = articles_popularity.author
    GROUP BY authors.name
    ORDER BY views DESC;
    """)

    answer = c.fetchall()
    conn.close()

    for i, x in enumerate(answer, start = 1):
        print('{} - {} '.format(i, x[1]))

def days_with_more_errors():
    pass

if __name__ == '__main__':
    options = """
    [1] What are the most popular three articles of all time?
    [2] Who are the most popular article authors of all time?
    [3] On which days did more than 1% of requests lead to errors?
    """

    print(options)

    choice = input('Enter the number of your question [1-2-3]: ')

    choose(choice)
