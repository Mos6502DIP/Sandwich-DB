
# Sandwich-DB (WIP)

The **Sandwich-DB** project is a web-based platform where users can upload and share sandwich-related blog posts. Users can submit blogs with descriptions, thumbnails, and more. The platform dynamically displays a random selection of sandwich blogs on the main dashboard and allows for easy exploration of sandwich-related content.

## Features

- **Dynamic Dashboard**
  - Displays a random selection of sandwich blogs on the main page.
  
- **Blog Submission**
  - Users can upload new sandwich blogs, including a title, description, blog content, author name, and a thumbnail image.

- **Blog Display**
  - View detailed sandwich blogs with thumbnail images and blog content.

## Tech Stack

- **Backend**: Python (Flask)
- **Database**: SQLite
- **Frontend**: HTML, Jinja2 templates
- **File Storage**: Local directory for thumbnails

## Installation

Follow the steps below to set up the project locally.

### Prerequisites

- Python 3.x
- Flask

### Clone the Repository

```bash
git clone https://github.com/MOS6502DIP/Sandwich-DB.git
cd Sandwich-DB
```

### Database Setup

The project uses SQLite for database management. You need to create the database and tables for the project to work correctly.

Run the following commands in Python to set up the database:

```python
import sqlite3

conn = sqlite3.connect('sandwich.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sandwiches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        blog TEXT,
        author TEXT,
        thumbnail TEXT,
        date TEXT,
        title TEXT
    )
''')

conn.commit()
conn.close()
```

### Folder Setup

Ensure that you have a folder for thumbnail images where uploaded images will be stored:

```bash
mkdir -p static/thumbnails
```

### Run the Application

To run the application locally:

```bash
python app.py
```

The app will be accessible on `http://127.0.0.1:5000`.

## Usage

### Main Dashboard

- Visit the main page at `/` to see a random selection of 12 sandwich blogs.
- Each blog card displays the title and a short description, along with a thumbnail.

### View All Blogs

- Go to `/sandwiches` to see all sandwich blogs.
- Each blog is listed with its title, description, author, and thumbnail.

### Blog Submission

- Visit `/upload` to submit a new blog.
- Fill in the form with a blog title, description, content, and author. Upload a thumbnail image, and click **Submit**.
- After submission, the blog will be visible on the site.

### View Specific Blog

- Visit `/blog/<blog_title>` to view a specific blog. If the blog exists, you'll see the detailed content, thumbnail image, and author.

## Folder Structure

```
sandwich-db/
│
├── app.py                   # Main application
├── sandwich.db               # SQLite database
├── static/                   # Static assets (images)
│   └── thumbnails/           # Uploaded thumbnails
├── templates/                # HTML templates for the web pages
│   ├── landing.html
│   ├── upload_form.html
│   ├── blog.html
│   ├── sandwiches.html
│   └── about.html
└── README.md                 # Project README file
```

## Contributing

As this project is in its early stages, contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Disclaimer
This is a **work-in-progress** project. Additional features such as comment sections, blog categorization, and enhanced search functionality will be added in future updates.
