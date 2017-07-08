### Log Analysis
A project for the Udacity Full Stack Nanodegree. The project is to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like

#### What you'll need:
1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
4. Download this repository.
5. Copy the `log-analysis.py` and the `newsdata.sql` files into the Vagrant sub-directory.

#### Get in the VM:
1. Go to Vagrant sub-directory of the fullstack-nanodegree-vm repository and run:

```
$ vagrant up
```
2. Log in:

```
$ vagrant ssh
```
3. Change directory to /vagrant.

#### Setup the databade:

1. To load the data locally, run:

```
psql -d news -f newsdata.sql
```
2. Connect to database:

```
psql -d news
```

3. Create view articles_popularity:
```
CREATE VIEW articles_popularity AS SELECT count(log.path) AS count, articles.title, articles.author, articles.slug FROM articles JOIN log ON log.path LIKE concat('%',articles.slug,'%') GROUP BY articles.slug, articles.title, articles.author ORDER BY count DESC;
```

4. Create view errors:
```
CREATE VIEW errors AS SELECT date(time), ROUND(100.0 * SUM(CASE log.status WHEN '200 OK' THEN 0 ELSE 1 END)/COUNT(log.status), 2) AS errors_percentage FROM log GROUP BY date(time) ORDER BY errors_percentage DESC;
```

#### Run the queries:
1. From the vagrant directory inside the virtual machine, run:
```
$ python3 log-analysis.py
```
