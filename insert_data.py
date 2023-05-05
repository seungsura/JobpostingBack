import json
import pymysql
import pprint

# Load JSON data
with open('data.json', 'r') as f:
    data = json.load(f)

# Connect to the MariaDB database
connection = pymysql.connect(
    host='<db 엔드포인트>',
    port=3306,
    user='<이름>',
    password='<비밀번호>',
    db='content',
    charset='utf8mb4'
)

# Prepare the SQL statement
sql = '''
INSERT INTO content_feed (
    company_name, company_image_url, <컬럼명>
) VALUES (
    %s, %s, %s
)
'''

try:
    # Create a cursor
    with connection.cursor() as cursor:
        # Iterate over JSON data and insert into the database
        for item in data:
            pprint.pprint(item)
            cursor.execute(sql, (
                item['company_name'], item['company_image_url'], item['컬럼명']
            ))
        # Commit the changes
        connection.commit()
finally:
    # Close the connection
    connection.close()
