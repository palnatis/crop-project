1. Create Database Scema 
	create database <db_name>;
2. Change Directoy to project
    cd project
3. Run DDL Commands to create tables
	mysql -h "localhost" -u "root" -p -D "<db_name>" < "DDL_scripts/ddl.sql"
4. Update exports.txt with DB details
5. Download text data files into text_data folder
6. Add environment variables
    source exports.txt
7. Run Corn yield migration
    python corn_yield_migration.py -f "text_data/yld_data/US_corn_grain_yield.txt"
8. Run Weather data migration
    python weather_data_migration.py -f "text_data/wx_data/USC00120177.txt"
    use `python models/weather_data_migration.py -h` for help
9. Run data analysis file to generate statistics
    python data_analysis.py
10. Run Flask application
    python application.py
11. Run pep8
    pe8 project
12. Run unit tests/nonsetest tests/
