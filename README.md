# AI Food Demand Forecasting & Inventory Planning

## Introduction
Accurately predicting customer demand is a major challenge for restaurants and food outlets. Underestimating demand can cause shortages and dissatisfied customers, while overestimating often results in food wastage. Many small and medium-sized restaurants still rely on manual estimates, which can be inefficient.

This project implements an **AI-enabled system** that predicts daily and weekly customer counts and their food demand using historical data. By providing accurate forecasts, the system helps optimize inventory, reduce waste, and improve overall food supply chain management.

---

## Functional Requirements

### Data Collection
- Collect historical daily and weekly customer counts.
- Record food items sold, quantities, and time of purchase.
- Allow manual data entry for outlets without POS systems.

### Data Pre-processing
- Clean raw data by removing duplicates, handling missing values, and normalizing entries.
- Support transformations such as grouping by day, week, or food category.
- Allow users to upload CSV/Excel datasets.

### Prediction
- Predict the number of customers for the next day and upcoming week.
- Forecast demand for specific food items based on historical consumption.
- Support multiple prediction models (Linear Regression, ARIMA, LSTM).

### Visualization & Reporting
- Generate charts (line, bar, pie) showing past trends and predicted demand.
- Provide downloadable reports in PDF/Excel.
- Display daily and weekly prediction dashboards.

### Inventory Planning Support
- Suggest approximate quantities of raw materials required based on predicted demand.
- Generate alerts if demand is significantly higher or lower than average.

### User Management
- Support multiple user types (admin/manager, staff).
- Secure login and authentication.
- Maintain a history of predictions.

### System Maintenance & Updates
- Allow retraining of the model when new data is added.
- Automatically update predictions when the dataset is refreshed.

---

## Tools and Techniques
- **Programming:** Python, Django, Flask
- **ML & Data:** Pandas, Scikit-learn, XGBoost, TensorFlow / Keras
- **Databases:** SQLite, MySQL, PostgreSQL
- **Visualization:** Matplotlib, Seaborn, Plotly / Dash
- **Web Frontend:** HTML, CSS, Chart.js
- **Web Deployment:** Streamlit, Django, Flask

---

## Features
- Interactive dashboard with actual vs predicted orders.
- Sales data input and CSV dataset upload.
- Predict daily and weekly food demand.
- Inventory planning support with raw material calculations.
- User authentication and role-based access.
- Modern, responsive UI with charts and tables.

---

## Installation & Setup

1. **Clone repository:**
```bash
git clone https://github.com/yourusername/ai-food-demand-forecasting.git
cd ai-food-demand-forecasting

Create & activate virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Create superuser (optional for admin):

python manage.py createsuperuser

Run the server:

python manage.py runserver

Access in browser:

http://127.0.0.1:8000/dashboard/
Project Structure
ai-food-demand-forecasting/
│
├── accounts/          # User authentication app
├── demand/            # Prediction & dashboard app
├── inventory/         # Inventory planning app
├── food_forecast/     # Django project folder
├── templates/         # HTML templates
├── static/            # CSS, JS
├── db.sqlite3         # Database
├── manage.py
└── requirements.txt
