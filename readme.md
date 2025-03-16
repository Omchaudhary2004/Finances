# Stock Market Live Prices & Prediction App

This is a **Django-based web application** that fetches real-time stock market index prices (both **Indian & Global**) using **Yahoo Finance (`yfinance`)** and integrates **machine learning models (LSTM) for stock price predictions**.

## 📌 Features
✅ **Live Stock Market Prices** (NIFTY, SENSEX, NASDAQ, DOW JONES, etc.)  
✅ **Global Market Support** (NASDAQ, S&P 500, FTSE 100, etc.)  
✅ **Stock Market Predictions** using **LSTM Neural Networks**  
✅ **Historical Data Processing** with `pandas`, `sqlite3`, and `numpy`  
✅ **Visualization with `matplotlib`**  

---

## 📂 Project Structure
📦 stock-market-app │-- 📂 finances/ # App Directory │ ├── 📂 templates/ # HTML Templates │ ├── 📂 static/ # CSS, JS, Images │ ├── 📜 views.py # Backend logic for fetching live prices & ML │ ├── 📜 urls.py # API Routes │-- 📂 data/ # Data Processing & Storage │-- 📂 models/ # ML Models (LSTM) │-- 📜 manage.py # Django Main File │-- 📜 requirements.txt # Dependencies │-- 📜 README.md # Project Documentation

yaml
Copy
Edit

---

## 🚀 Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/stock-market-app.git
```
cd stock-market-app
2️⃣ Install Dependencies
```sh
Copy
Edit
pip install -r requirements.txt
```
3️⃣ Apply Migrations
```sh
Copy
Edit
python manage.py migrate
```
4️⃣ Run the Django Server
```sh
Copy
Edit
python manage.py runserver
The app will be available at http://127.0.0.1:8000/ 🚀
```
🔗 API Endpoints
Method	Endpoint	Description
```
GET	/api/live-prices/	Fetches real-time stock market prices
GET	/api/historical/	Retrieves historical stock data
POST	/api/predict/	Predicts future stock prices using LSTM
```
📌 Example: Fetch Live Stock Prices
Request
```sh
Copy
Edit
GET http://127.0.0.1:8000/api/live-prices/
Response
json
Copy
Edit
{
  "NIFTY": 22150.25,
  "SENSEX": 73700.15,
  "BANK_NIFTY": 48200.45,
  "NIFTY_IT": 36500.50,
  "NASDAQ": 14250.60,
  "DOW_JONES": 34000.75,
  "SP500": 4900.85,
  "FTSE100": 7300.45
}
```
📊 Stock Market Prediction (LSTM Model)
The project includes an LSTM (Long Short-Term Memory) neural network for stock price predictions.

Model Architecture
python
Copy
Edit
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
📈 Technologies Used
Backend: Django, Python
Data Handling: Pandas, SQLite, NumPy
Finance API: Yahoo Finance (yfinance)
Machine Learning: TensorFlow, LSTM
Visualization: Matplotlib
Frontend: HTML, Bootstrap, JavaScript
🤝 Contributing
Feel free to contribute by creating a pull request or reporting issues.

📄 License
This project is open-source under the MIT License.

⭐ Star the Repository!
If you found this useful, consider giving it a ⭐ on GitHub!
