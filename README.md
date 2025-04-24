# Python Shop

A simple e-commerce web application built with Flask that allows users to browse products and add them to a shopping cart.

## Features
- Product listing
- Add products to cart
- Remove products from cart
- View cart and total
- Responsive design using Tailwind CSS

## Setup and Installation

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your web browser and visit: `http://127.0.0.1:5000`

## Project Structure
- `app.py`: Main application file with routes and logic
- `templates/`: HTML templates
  - `base.html`: Base template with common layout
  - `index.html`: Product listing page
  - `cart.html`: Shopping cart page
- `requirements.txt`: Python package dependencies 