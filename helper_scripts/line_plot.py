import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Model": ["EfficientNetB6", "EfficientNetB6","EfficientNetB6","EfficientNetB6",
               "ViT-base-patch16-224", "ViT-base-patch16-224", "ViT-base-patch16-224", "ViT-base-patch16-224"],
    "Images Count": [150, 500, 750, 1000, 150, 500, 750, 1000],
    "Accuracy": [81, 89, 95, 94, 84, 93, 96, 96]
}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))

# Iterate through models and plot each
for model in df["Model"].unique():
    subset = df[df["Model"] == model]
    plt.plot(
        subset["Images Count"], 
        subset["Accuracy"], 
        marker="o", 
        label=model
    )
    # Add annotations for each point
    for i in range(len(subset)):
        x = subset["Images Count"].iloc[i]
        y = subset["Accuracy"].iloc[i]
        plt.annotate(
            f"{y}%",  # Add the accuracy value as text
            (x, y),  # Position of the annotation
            textcoords="offset points", 
            xytext=(0, 10),  # Offset to avoid overlapping the point
            ha="center",
            fontsize=10,
            color="black"
        )

# Formatting
plt.title("Model Accuracy vs. Number of Images", fontsize=14)
plt.xlabel("Number of Images", fontsize=12)
plt.ylabel("Accuracy (%)", fontsize=12)
plt.legend(title="Model")
plt.grid(True)

# Save or Show
plt.savefig("line_plot_with_labels.png", dpi=300)  # Save the figure