# ✈️ Flight Fare Prediction Using Machine Learning

## 📝 Objective
The goal of this project is to predict flight ticket prices based on various factors such as airline, source city, destination, departure time, number of stops, class, and days left until departure. This helps travelers estimate flight costs and plan accordingly.

## 📂 Dataset
The dataset includes the following features:
- 🏢 **Airline** - The airline operating the flight
- 🔢 **Flight** - The flight number
- 🌍 **Source City** - Departure city
- ⏰ **Departure Time** - Time when the flight departs
- ✈️ **Stops** - Number of stops during the flight
- ⏳ **Arrival Time** - Time when the flight arrives
- 📍 **Destination City** - Arrival city
- 💺 **Class** - Flight class (Economy, Business, etc.)
- 🕒 **Duration** - Total flight duration
- 📅 **Days Left** - Days left until departure
- 💰 **Price** - Target variable (flight fare)

## 🚀 Steps Involved
1️⃣ **Data Loading & Preprocessing:**
   - Load the dataset and explore it
   - Handle missing values and encode categorical features
   - Standardize numerical features

2️⃣ **Data Splitting:**
   - Split the dataset into training and testing sets
   - Save test data for manual testing

3️⃣ **Model Building & Training:**
   - Train multiple models (Linear Regression, Decision Tree, Random Forest, etc.)
   - Evaluate models using R² Score, MAE, MSE, RMSE

4️⃣ **Model Selection:**
   - Choose the best-performing model based on evaluation metrics
   - Save the best model and scaler as `.pkl` files

5️⃣ **Manual Testing:**
   - Load the saved model and scaler
   - Preprocess and scale test data
   - Predict fares and compare with actual values

6️⃣ **API Integration (Flask Web App):**
   - Build a user-friendly web interface using Flask
   - Users can input flight details and get fare predictions
   - Display predicted fares using an interactive UI

## 🛠️ Technologies Used
- 🐍 **Python**
- 📊 **Scikit-learn**
- 🔢 **Pandas & NumPy**
- 📈 **Matplotlib & Seaborn**
- 🌐 **Flask (for API and UI integration)**
- 🏗️ **Machine Learning Algorithms**

## ⚙️ Installation & Setup
### Prerequisites
Ensure you have Python installed and install the required libraries using:
```sh
pip install -r requirements.txt
```

### ▶️ Running the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Flight-Fare-Prediction.git
   cd Flight-Fare-Prediction
   ```
2. Run the Jupyter Notebook for model training:
   ```sh
   jupyter notebook Flight_Fare_Prediction.ipynb
   ```
3. Run the Flask web app (if integrated):
   ```sh
   python app.py
   ```



