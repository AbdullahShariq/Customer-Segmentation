# Customer Segmentation Using Graph Clustering

## Overview
This project segments e-commerce customers using graph-based clustering with `NetworkX`. It constructs a bipartite graph linking customers to product categories based on purchase quantities. The greedy modularity communities algorithm identifies clusters of similar purchasing behaviors. The graph is visualized with nodes colored by community, and metrics like modularity, average degree, and clustering coefficient are computed. Results are saved to `clusters.json` for further analysis.

---

## Files
- **main.py**: Processes data, builds the graph, performs clustering, visualizes results, and calculates metrics.
- **clusters.json**: Stores customer IDs grouped into clusters.
- **ecommerce_customer_data_custom_ratios.csv**: Input dataset with `Customer ID`, `Product Category`, and `Quantity`.

---

## Technologies Used

- **Python**: Core programming language.
- **NetworkX**: For graph construction and community detection.
- **Pandas**: For data preprocessing and manipulation.
- **Matplotlib**: For graph visualization.
- **NumPy**: For numerical computations.

---

## Prerequisites
Install required libraries:
```bash
pip install pandas networkx matplotlib numpy
```
Place `ecommerce_customer_data_custom_ratios.csv` in the project directory.

---

## How It Works
1. **Data Preprocessing**: Loads dataset, samples 0.5% of records, groups by `Customer ID` and `Product Category`, maps categories to numbers (Books: 1, Electronics: 2, Home: 3, Clothing: 4).
2. **Graph Construction**: Creates a bipartite graph with customers and categories as nodes, edges weighted by purchase quantity.
3. **Clustering**: Uses `greedy_modularity_communities` to detect clusters, saved to `clusters.json`.
4. **Visualization**: Plots the graph with nodes colored by community.
5. **Metrics**: Computes modularity, average degree, diameter, average path length, clustering coefficient, and density.

---

## Running the Project
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbdullahShariq/Customer-Segmentation.git
   cd Customer-Segmentation
   ```
2. **Ensure dependencies and dataset are ready.**
3. **Run:**
   ```bash
   python main.py
   ```
4. **Outputs:** `clusters.json`, graph visualization, and metrics printed to console.

---

## Notes
- Dataset must include `Customer ID`, `Product Category`, and `Quantity`.
- Disconnected graphs report "Inf" for diameter and path length.
- Random seed (`random_state=42`) ensures reproducibility.
