# 🛒 E-Commerce Sales — Exploratory Data Analysis

An end-to-end EDA project on a synthetic e-commerce sales dataset covering **5,000 orders across 2023**. The goal is to extract meaningful business insights from raw sales data using Python.

---

## 📊 What's Inside

| File | Description |
|------|-------------|
| `data/ecommerce_sales.csv` | Sales dataset (5,000 rows, 12 columns) |
| `data/generate_data.py` | Script used to generate the dataset |
| `notebooks/ecommerce_eda.ipynb` | Main Jupyter notebook with full analysis |
| `eda_analysis.py` | Standalone Python script (no Jupyter needed) |
| `images/` | All generated charts |

---

## 📁 Dataset Columns

| Column | Description |
|--------|-------------|
| `order_id` | Unique order identifier |
| `order_date` | Date of purchase |
| `category` | Product category (Electronics, Clothing, etc.) |
| `product` | Product name |
| `unit_price` | Price per unit (₹) |
| `quantity` | Number of units ordered |
| `discount` | Discount applied (0 to 0.20) |
| `revenue` | Final revenue after discount |
| `city` | Customer city |
| `payment_method` | Payment used |
| `rating` | Customer rating (2.5–5.0) |
| `returned` | Whether the order was returned (0/1) |

---

## 🔍 Key Insights

1. **Electronics dominates revenue** — highest revenue despite moderate order volume
2. **December is the peak month** — holiday season drives a clear sales spike
3. **UPI + Credit Card = 60% of payments** — strong digital payment adoption
4. **Sports has the highest return rate** (~12.7%) — potential quality or sizing issue
5. **10% discount is the sweet spot** — maximises revenue across most categories
6. **Hyderabad leads all cities** in total revenue
7. **Average rating is 3.74/5** — consistent across all categories

---

## 📈 Charts Generated

| Chart | Description |
|-------|-------------|
| `01_monthly_trend.png` | Revenue and orders by month |
| `02_category_revenue.png` | Total revenue per category |
| `03_top_products.png` | Top 10 products by revenue |
| `04_city_performance.png` | Orders and revenue by city |
| `05_payment_methods.png` | Pie chart of payment methods |
| `06_ratings.png` | Rating distribution + avg by category |
| `07_return_rate.png` | Return rate per category |
| `08_discount_heatmap.png` | Revenue heatmap: category vs discount |
| `09_quarterly_revenue.png` | Q1–Q4 revenue breakdown |

---

## 🚀 How to Run

### Option 1 — Jupyter Notebook (recommended)
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/ecommerce-eda.git
cd ecommerce-eda

# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook notebooks/ecommerce_eda.ipynb
```

### Option 2 — Python script
```bash
pip install -r requirements.txt
python eda_analysis.py
```

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Pandas** — data manipulation
- **Matplotlib** — plotting
- **Seaborn** — statistical visualisations
- **Jupyter Notebook** — interactive analysis

---

## 📌 Project Structure

```
ecommerce-eda/
├── data/
│   ├── ecommerce_sales.csv
│   └── generate_data.py
├── notebooks/
│   └── ecommerce_eda.ipynb
├── images/
│   ├── 01_monthly_trend.png
│   ├── 02_category_revenue.png
│   └── ...
├── eda_analysis.py
├── requirements.txt
└── README.md
```

---

## 👤 Author

Made as part of a data analyst portfolio project.  
Feel free to fork, use, and build on this!
