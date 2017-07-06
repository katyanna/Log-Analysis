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
    SELECT articles.slug,
           articles.title,
           count(log.path) AS count
    FROM   articles
    JOIN log
      ON log.path LIKE concat('%',articles.slug,'%')
    GROUP BY articles.slug, articles.title
    order BY count DESC
    LIMIT 3;
    """)

    answer = c.fetchall()
    conn.close()

    for i, x in enumerate(answer, start = 1):
        print('{} - {} '.format(i, x[1]))

def most_popular_authors():
    pass

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
