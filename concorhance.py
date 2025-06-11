import matplotlib.pyplot as plt
import pandas as pd

# Simulated concordance data
data = {
    "Agreement Category": ["Exact Match", "Partial Match (1 topic off)", "No Match"],
    "Frequency": [146, 38, 16]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(8, 6))
bars = plt.bar(df["Agreement Category"], df["Frequency"], color="#1f77b4")
plt.title("Topic Assignment Concordance Between Headline and Full-Text Articles", fontsize=14)
plt.ylabel("Number of Articles", fontsize=12)
plt.xlabel("Agreement Category", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=15, fontsize=11)
plt.yticks(fontsize=11)

# Annotate bars with values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, str(yval), ha='center', va='bottom', fontsize=11)

plt.tight_layout()
plt.savefig("headline_vs_fulltext_concordance.png", dpi=300)
plt.show()
