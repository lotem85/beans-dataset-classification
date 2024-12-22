import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Model": ["EfficientNetB6", "EfficientNetB6","EfficientNetB6","EfficientNetB6",
               "ViT-base-patch16-224", "ViT-base-patch16-224", "ViT-base-patch16-224", "ViT-base-patch16-224"],
    "Images_Count": [150, 500, 750, 1000, 150, 500, 750, 1000],
    "Number_Of_Eppochs": [46, 29, 25, 25, 7, 4, 6, 18]
}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))

# Iterate through models and plot each
for model in df["Model"].unique():
    subset = df[df["Model"] == model]
    plt.plot(
        subset["Images_Count"], 
        subset["Number_Of_Eppochs"], 
        marker="o", 
        label=model
    )
    # Add annotations for each point
    for i in range(len(subset)):
        x = subset["Images_Count"].iloc[i]
        y = subset["Number_Of_Eppochs"].iloc[i]
        plt.annotate(
            y,  # Add the accuracy value as text
            (x, y),  # Position of the annotation
            textcoords="offset points", 
            xytext=(0, 10),  # Offset to avoid overlapping the point
            ha="center",
            fontsize=10,
            color="black"
        )

# Formatting
plt.title("Number of Epochs Vs Number of Image", fontsize=14)
plt.xlabel("Number of Images", fontsize=12)
plt.ylabel("Number of Epochs", fontsize=12)
plt.legend(title="Model")
plt.grid(True)

# Save or Show
plt.savefig("number_of_epochs.png", dpi=300)  # Save the figure