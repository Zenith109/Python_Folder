# Graph Analytics Project

This project implements various graph algorithms using PySpark to analyze complex networks and relationships. It aims to uncover insights in areas such as social networks, transportation systems, and fraud detection.

## Project Structure

```
graph-analytics
├── src
│   ├── main.py                # Entry point of the application
│   ├── algorithms             # Contains graph algorithm implementations
│   │   └── graph_algorithms.py
│   ├── data                   # Sample data for testing
│   │   └── sample_data.csv
│   └── utils                  # Utility functions for data processing
│       └── helpers.py
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to be ignored by Git
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd graph-analytics
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have Apache Spark installed and properly configured.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Algorithms Implemented

- **PageRank**: Calculates the importance of nodes in a graph.
- **Connected Components**: Identifies connected subgraphs within a larger graph.
- **Shortest Path**: Finds the shortest path between two nodes in a graph.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.