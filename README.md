# DRF API Project

This project is a Django-based API built using Django Rest Framework (DRF). It provides endpoints for managing books and categories, including filtering, searching, and pagination.

## Features

- **Books Management**: Create, read, update, and delete books.
- **Categories Management**: Create, read, update, and delete categories.
- **Filtering**: Filter books by category, published date, availability, and title.
- **Searching**: Search books by title.
- **Ordering**: Order books by published date.
- **Pagination**: Paginate results with a default page size of 5.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shreif92/DRF_API.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DRF_API/project
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Endpoints

The API provides the following endpoints:

### Books

- `GET /books/`: List all books.
- `POST /books/`: Create a new book.
- `GET /books/{id}/`: Retrieve a specific book.
- `PUT /books/{id}/`: Update a specific book.
- `DELETE /books/{id}/`: Delete a specific book.

### Categories

- `GET /categorys/`: List all categories.
- `POST /categorys/`: Create a new category.
- `GET /categorys/{id}/`: Retrieve a specific category.
- `PUT /categorys/{id}/`: Update a specific category.
- `DELETE /categorys/{id}/`: Delete a specific category.

## Configuration

### Installed Apps

The following apps are included in the `INSTALLED_APPS` section of `settings.py`:

- `rest_framework`
- `django_filters`
- `api`

### REST Framework Settings

Pagination is enabled with a default page size of 5:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}
```

## Models

### Book

- `title`: CharField
- `author`: CharField
- `category`: ForeignKey to `Category`
- `published_date`: DateField
- `available`: BooleanField
- `created_at`: DateTimeField (auto-added)

### Category

- `name`: CharField
- `description`: TextField

## Filters

The `Booksviewset` supports filtering by:

- `category`
- `published_date`
- `available`
- `title`

## License

This project is licensed under the MIT License.
