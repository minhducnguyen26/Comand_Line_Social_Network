# Refresh Database
new:
	rm database.db
	sqlite3 database.db < schema.sql
	sqlite3 database.db < mockdata.sql

interesting_queries:
	sqlite3 database.db < interesting_queries.sql