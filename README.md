# Topnotch Online Bookshop Backend

Welcome to the Topnotch Online Bookshop Backend repository! This backend system is designed to facilitate the operations of an online bookshop, specifically tailored for Topnotch, a publisher of educational materials for Kenyan high school students. With this backend, retailers can easily access, order, and purchase books from the Topnotch platform.

## Features

- **User Authentication**: Secure user authentication system allowing both retailers and administrators to log in and access the platform.
- **Book Management**: Comprehensive functionalities for managing books, including adding new books, updating existing ones, and removing outdated titles.
- **Order Management**: Efficient order management system enabling retailers to place orders, track order statuses, and manage their purchase history.
- **Shopping Cart**: Seamless shopping cart functionality for users to add books, review their selections, and proceed to checkout.
- **Search and Filtering**: Advanced search and filtering options to help users quickly find the books they need based on various criteria such as subject, category, or title.
- **Payment Integration**: Integration with payment gateways to facilitate secure online transactions for book purchases.
- **Admin Panel**: Administrative panel for managing users, orders, books, and other essential aspects of the platform.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **PostgreSQL**: A powerful, open-source relational database management system used for storing and retrieving data efficiently.
- **Django REST Framework**: A powerful toolkit for building Web APIs in Django, providing tools for serialization, authentication, and more.
- **Django Channels**: Enables handling WebSockets, HTTP2, and background tasks in Django.
- **JWT Authentication**: JSON Web Token-based authentication for securing API endpoints.
- **Celery**: Distributed task queue for background job processing.
- **Redis**: In-memory data structure store used as a broker for Celery and for caching.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/topnotch-online-bookshop-backend.git
    ```

2. Navigate to the project directory:

    ```bash
    cd topnotch-online-bookshop-backend
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up PostgreSQL and configure the database settings in `settings.py`.

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Register as a new user or log in if you already have an account.
2. Browse through the available books using the search and filtering options.
3. Add desired books to your shopping cart.
4. Proceed to checkout and complete the payment process.
5. Track your orders and manage your account settings as needed.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the developers and contributors of Django, PostgreSQL, and other open-source technologies used in this project.
- Inspiration and guidance from various online tutorials, documentation, and community forums.

Thank you for choosing Topnotch Online Bookshop Backend! Happy reading and happy coding! 📚💻
