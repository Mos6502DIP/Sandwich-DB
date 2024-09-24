import json
import sqlite3

conn = sqlite3.connect('sandwich.db')
cursor = conn.cursor()


with open('blogs.json', 'r') as file:
    data = json.load(file)

for sandwich_name, sandwich_data in data.items():
    title = sandwich_data['Title']
    description = sandwich_data['Description']
    date = sandwich_data['Date']
    thumbnail = sandwich_data['thumbnail']
    blog = sandwich_data['Blog']

    author = "Chat GTP"
    print(f'Sandwich Name: {sandwich_name}, Title: {title}, Description: {description}, Date: {date}, Thumbnail: {thumbnail}')
    # Insert into the database
    cursor.execute('''
        INSERT OR IGNORE INTO sandwiches (name, description, blog, author, thumbnail, date, title)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (sandwich_name, description, blog, author, thumbnail, date, title))


conn.commit()
conn.close()