def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def visualize_data(data, title="Data Visualization"):
    """Visualizes the given data using matplotlib."""
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid()
    plt.show()

def save_to_csv(dataframe, file_path):
    """Saves a DataFrame to a CSV file."""
    dataframe.write.csv(file_path, header=True, mode='overwrite')