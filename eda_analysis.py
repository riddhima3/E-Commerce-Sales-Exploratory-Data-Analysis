"""
E-Commerce Sales EDA
====================
A complete exploratory data analysis of e-commerce sales data covering:
- Data overview & cleaning
- Sales trends over time
- Category & product performance
- City-wise distribution
- Payment method analysis
- Customer ratings & returns
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Style ──────────────────────────────────────────────────────────────────────
sns.set_theme(style='whitegrid', palette='muted')
plt.rcParams.update({
    'figure.dpi': 150,
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
})
COLORS = sns.color_palette('muted', 10)

# ── Load Data ──────────────────────────────────────────────────────────────────
df = pd.read_csv('data/ecommerce_sales.csv', parse_dates=['order_date'])
df['month'] = df['order_date'].dt.to_period('M')
df['month_name'] = df['order_date'].dt.strftime('%b')
df['month_num'] = df['order_date'].dt.month
df['quarter'] = df['order_date'].dt.to_period('Q').astype(str)

print("=" * 55)
print("  E-COMMERCE SALES — EXPLORATORY DATA ANALYSIS")
print("=" * 55)

# ── 1. Data Overview ───────────────────────────────────────────────────────────
print("\n[1] DATASET OVERVIEW")
print(f"  Rows       : {len(df):,}")
print(f"  Columns    : {df.shape[1]}")
print(f"  Date range : {df['order_date'].min().date()} → {df['order_date'].max().date()}")
print(f"  Missing    : {df.isnull().sum().sum()}")
print(f"  Duplicates : {df.duplicated().sum()}")
print("\nData types:")
print(df.dtypes.to_string())
print("\nBasic stats:")
print(df[['unit_price','quantity','discount','revenue','rating']].describe().round(2).to_string())

# ── 2. Monthly Revenue Trend ───────────────────────────────────────────────────
monthly = df.groupby('month_num').agg(
    revenue=('revenue', 'sum'),
    orders=('order_id', 'count')
).reset_index()
month_labels = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthly['month_label'] = monthly['month_num'].apply(lambda x: month_labels[x-1])

fig, ax1 = plt.subplots(figsize=(12, 4))
ax2 = ax1.twinx()
bars = ax1.bar(monthly['month_label'], monthly['revenue']/1000,
               color=COLORS[0], alpha=0.75, label='Revenue (₹K)')
ax2.plot(monthly['month_label'], monthly['orders'], color=COLORS[3],
         marker='o', linewidth=2, markersize=5, label='Orders')
ax1.set_ylabel('Revenue (₹ Thousands)')
ax2.set_ylabel('Number of Orders')
ax1.set_title('Monthly Revenue & Order Volume — 2023')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
plt.tight_layout()
plt.savefig('images/01_monthly_trend.png')
plt.close()
print("\n[2] Saved: 01_monthly_trend.png")

best_month = monthly.loc[monthly['revenue'].idxmax(), 'month_label']
worst_month = monthly.loc[monthly['revenue'].idxmin(), 'month_label']
print(f"  Best month  : {best_month}")
print(f"  Worst month : {worst_month}")

# ── 3. Revenue by Category ─────────────────────────────────────────────────────
cat_revenue = df.groupby('category')['revenue'].sum().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(cat_revenue.index, cat_revenue.values/1000, color=COLORS[:len(cat_revenue)])
ax.set_xlabel('Revenue (₹ Thousands)')
ax.set_title('Total Revenue by Category')
for bar, val in zip(bars, cat_revenue.values):
    ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2,
            f'₹{val/1000:.0f}K', va='center', fontsize=9)
plt.tight_layout()
plt.savefig('images/02_category_revenue.png')
plt.close()
print("[3] Saved: 02_category_revenue.png")
print(f"  Top category    : {cat_revenue.idxmax()} (₹{cat_revenue.max()/1000:.0f}K)")
print(f"  Bottom category : {cat_revenue.idxmin()} (₹{cat_revenue.min()/1000:.0f}K)")

# ── 4. Top 10 Products by Revenue ─────────────────────────────────────────────
top_products = df.groupby('product')['revenue'].sum().nlargest(10).sort_values()

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(top_products.index, top_products.values/1000, color=COLORS[1])
ax.set_xlabel('Revenue (₹ Thousands)')
ax.set_title('Top 10 Products by Revenue')
for bar, val in zip(bars, top_products.values):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f'₹{val/1000:.0f}K', va='center', fontsize=9)
plt.tight_layout()
plt.savefig('images/03_top_products.png')
plt.close()
print("[4] Saved: 03_top_products.png")

# ── 5. City-wise Orders ────────────────────────────────────────────────────────
city_data = df.groupby('city').agg(
    orders=('order_id', 'count'),
    revenue=('revenue', 'sum')
).sort_values('revenue', ascending=False).reset_index()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].bar(city_data['city'], city_data['orders'], color=COLORS[2])
axes[0].set_title('Orders by City')
axes[0].set_ylabel('Number of Orders')
axes[0].tick_params(axis='x', rotation=30)

axes[1].bar(city_data['city'], city_data['revenue']/1000, color=COLORS[4])
axes[1].set_title('Revenue by City')
axes[1].set_ylabel('Revenue (₹ Thousands)')
axes[1].tick_params(axis='x', rotation=30)

plt.suptitle('City-wise Performance', fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('images/04_city_performance.png', bbox_inches='tight')
plt.close()
print("[5] Saved: 04_city_performance.png")
print(f"  Top city : {city_data.iloc[0]['city']} — ₹{city_data.iloc[0]['revenue']/1000:.0f}K")

# ── 6. Payment Method Distribution ────────────────────────────────────────────
payment_counts = df['payment_method'].value_counts()

fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct='%1.1f%%',
    colors=COLORS[:len(payment_counts)],
    startangle=140,
    pctdistance=0.82
)
for at in autotexts:
    at.set_fontsize(9)
ax.set_title('Payment Method Distribution', pad=20)
plt.tight_layout()
plt.savefig('images/05_payment_methods.png')
plt.close()
print("[6] Saved: 05_payment_methods.png")
print(f"  Most popular : {payment_counts.idxmax()} ({payment_counts.max()/len(df)*100:.1f}%)")

# ── 7. Rating Distribution ─────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].hist(df['rating'], bins=25, color=COLORS[5], edgecolor='white', linewidth=0.5)
axes[0].axvline(df['rating'].mean(), color='red', linestyle='--', linewidth=1.5,
                label=f'Mean: {df["rating"].mean():.2f}')
axes[0].set_title('Customer Rating Distribution')
axes[0].set_xlabel('Rating')
axes[0].set_ylabel('Count')
axes[0].legend()

cat_rating = df.groupby('category')['rating'].mean().sort_values(ascending=False)
axes[1].bar(cat_rating.index, cat_rating.values, color=COLORS[6])
axes[1].set_ylim(0, 5.5)
axes[1].axhline(3.75, color='red', linestyle='--', linewidth=1, label='Avg 3.75')
axes[1].set_title('Average Rating by Category')
axes[1].set_ylabel('Average Rating')
axes[1].tick_params(axis='x', rotation=25)
axes[1].legend()
for i, (cat, val) in enumerate(cat_rating.items()):
    axes[1].text(i, val + 0.05, f'{val:.2f}', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('images/06_ratings.png')
plt.close()
print("[7] Saved: 06_ratings.png")

# ── 8. Return Rate by Category ─────────────────────────────────────────────────
return_rate = df.groupby('category')['returned'].mean().sort_values(ascending=False) * 100

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(return_rate.index, return_rate.values, color=[
    COLORS[3] if v > return_rate.mean() else COLORS[0] for v in return_rate.values
])
ax.axhline(return_rate.mean(), color='red', linestyle='--', linewidth=1.5,
           label=f'Avg return rate: {return_rate.mean():.1f}%')
ax.set_ylabel('Return Rate (%)')
ax.set_title('Return Rate by Category')
ax.tick_params(axis='x', rotation=20)
ax.legend()
for bar, val in zip(bars, return_rate.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            f'{val:.1f}%', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('images/07_return_rate.png')
plt.close()
print("[8] Saved: 07_return_rate.png")
print(f"  Highest returns : {return_rate.idxmax()} ({return_rate.max():.1f}%)")

# ── 9. Discount vs Revenue Heatmap ────────────────────────────────────────────
df['discount_pct'] = (df['discount'] * 100).astype(int).astype(str) + '%'
pivot = df.groupby(['category', 'discount_pct'])['revenue'].sum().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(pivot/1000, annot=True, fmt='.0f', cmap='YlOrRd', ax=ax,
            cbar_kws={'label': 'Revenue (₹K)'})
ax.set_title('Revenue Heatmap — Category vs Discount Level')
ax.set_xlabel('Discount %')
ax.set_ylabel('Category')
plt.tight_layout()
plt.savefig('images/08_discount_heatmap.png')
plt.close()
print("[9] Saved: 08_discount_heatmap.png")

# ── 10. Quarterly Revenue ──────────────────────────────────────────────────────
quarterly = df.groupby('quarter')['revenue'].sum().reset_index()

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(quarterly['quarter'], quarterly['revenue']/1000, color=COLORS[:4])
ax.set_ylabel('Revenue (₹ Thousands)')
ax.set_title('Quarterly Revenue — 2023')
for i, row in quarterly.iterrows():
    ax.text(i, row['revenue']/1000 + 10, f'₹{row["revenue"]/1000:.0f}K',
            ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('images/09_quarterly_revenue.png')
plt.close()
print("[10] Saved: 09_quarterly_revenue.png")

# ── Summary ────────────────────────────────────────────────────────────────────
total_rev = df['revenue'].sum()
total_orders = len(df)
avg_order = df['revenue'].mean()
total_returned = df['returned'].sum()

print("\n" + "=" * 55)
print("  SUMMARY STATS")
print("=" * 55)
print(f"  Total Revenue  : ₹{total_rev:,.0f}")
print(f"  Total Orders   : {total_orders:,}")
print(f"  Avg Order Value: ₹{avg_order:,.2f}")
print(f"  Total Returns  : {total_returned} ({total_returned/total_orders*100:.1f}%)")
print(f"  Avg Rating     : {df['rating'].mean():.2f} / 5.0")
print("=" * 55)
print("\nAll charts saved to images/ folder.")
