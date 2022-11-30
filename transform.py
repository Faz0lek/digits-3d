import pandas
import matplotlib; matplotlib.use('agg'); import matplotlib.pyplot as plt
import os

DATA_FOLDER = r"data"
OUTPUT_FOLDER= r"images"

if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(r"data"):
        if not filename.endswith(".csv"):
            continue

        print(f"Working {filename}")

        label = filename.split("_")[1]
        os.makedirs(os.path.join(OUTPUT_FOLDER, label), exist_ok=True)

        df = pandas.read_csv(os.path.join(DATA_FOLDER, filename), sep=",", header=None, usecols=[0, 1], names=["x", "y"])
        print(f"{filename} data read.")

        fig = plt.figure(figsize=(1, 1))

        plt.plot(df["x"], df["y"], "-", color="black", linewidth=4.0)
        print(f"{filename} plot done.\n")

        plt.axis("off")

        fig.savefig(os.path.join(OUTPUT_FOLDER, label, f"{filename.split('.')[0]}.png"), dpi=32)
        plt.close()
