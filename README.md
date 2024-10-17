---

# AetherCare_ChatBot Project

## Overview

This project implements a custom healthcare-focused question-answering system using **Pinecone Vector Search**, **Hugging Face Embeddings**, and a **LLM model**. The system retrieves relevant documents and generates answers based on user queries, using advanced machine-learning techniques.

## Project Structure

<!-- - `environment.yml`: Contains the dependencies for setting up the Conda environment.-->

<!-- - `src/`: The source code for the project with scripts to handle document retrieval and QA. --><!-- - `README.md`: Project documentation (this file). -->
- `testing.ipynb`: A Jupyter notebook to run initial checks and tests for the project.
- `models/`: Stores local models like Llama used in the project.
- `data/`: Placeholder for any input or processed data files.
  
## Requirements

Before running the project, you need to set up the environment with the necessary dependencies. The following instructions detail the steps to do this.

## Installation

### Step 1: Create a Conda Environment

To ensure that all dependencies are correctly installed, start by creating a Conda environment using the provided `requirements.txt` file.

```bash
# Clone the repository
git clone https://github.com/your-username/AetherCare_ChatBott.git
cd AetherCare_ChatBot

# Create the environment
conda create -n health-bot python=3.8 -y

# Activate the environment
conda activate health-bot

# Download the Dependencies
pip install -r requirements.txt
```

### Step 2: Set up API Keys

Make sure you have your **Pinecone API key** and any other necessary keys configured in your environment:

```bash
# Set Pinecone API key
PINECONE_API_KEY=your_pinecone_api_key
```

## Usage

### Initial Testing

Before exploring the full project structure, run the initial test notebook to ensure everything is working as expected.

1. Open the `testing.ipynb` Jupyter notebook:

    ```bash
    jupyter notebook testing.ipynb
    ```

2. Run the notebook cells to test:
   - Setting up Pinecone.
   - Creating embeddings using the Hugging Face model.
   - Perform a similarity search and generate answers using the LLM model.


## Testing

For testing, utilize the Jupyter Notebook to ensure that:
- Embeddings are created correctly.
- The vector store is properly initialized.
- QA retrieval returns valid results.

Once satisfied with the initial tests, move the code to the organized repository structure and refine the functionality.

---

This README file outlines how to:
- Create the environment with Conda.
- Download dependencies.
- Test the project using the notebook.
- Transition to a more structured codebase for further development.

Make sure to replace placeholders (e.g., API keys, repository URLs) with the actual project details.