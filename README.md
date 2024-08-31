# 🌍 LLM-Based Text Adventure: Amazing Race (Backend Server)

Welcome to the **LLM-Based Text Adventure: Amazing Race** project! This is an interactive, location-based text adventure game inspired by "The Amazing Race." The game challenges players to solve riddles and navigate through various cities and points of interest, using an AI-powered system to deliver a unique and engaging experience.

**NOTE**: This repository only holds the backend LLM + data code for this project

### Complementary Repository: https://github.com/astronights/llm-amazing-race-ui

## 🎯 Project Overview

This module is built primarily with Python, leveraging the power of large language models (LLMs) to create dynamic and immersive gameplay. Players will embark on a virtual adventure where they must solve riddles to discover and travel to various landmarks around the world.

## 🛠️ Tech Stack

This repository encompasses the server-side operations of the project, utilizing various technologies to deliver a seamless experience.

### Backend Technology

- **Python**: The backbone of the backend is Python, which is used for implementing the game's logic, interfacing with the LLM, and processing data from location services.
- **Flask**: Flask serves as the web framework for the server, providing configurations for Cross-Origin Resource Sharing (CORS) and handling request parameters.
- **Gemini LLM**: The Gemini LLM is leveraged to generate riddles, offer hints, and facilitate interactive communication with players in natural language.
- **MongoDB**: MongoDB is used as the database to store and manage the project's data.

### Deployment

- **Vercel**: The backend is deployed on Vercel, providing a scalable and reliable platform for hosting serverless functions and managing deployments.

### Data

- **World City Data**: This dataset includes information on major cities worldwide, which is queried and stored in MongoDB for use in the application.
- **Real-Time Open Source Location Data**: The game utilizes real-time, open-source location datasets to query cities and points of interest, enabling the creation of accurate and engaging challenges based on real-world locations.


## 🌟 Features

- **Global City Database**: Access a comprehensive list of cities from around the world, ensuring a broad and diverse range of locations.
- **Custom Coordinate Search**: Enable players to discover cities based on custom coordinates, adding flexibility and personalization to the gameplay.
- **Advanced LLM Integration**: Utilize sophisticated chain-based prompting techniques (similar to Langchain and LlamaIndex) to harness the full potential of the LLM, delivering well-formatted and insightful responses.

## 🚀 Getting Started

### **Prerequisites**

Before you begin, ensure you have the following installed:

- **Python 3.12** (for the backend)
- **Vercel CLI** (for deployment)
- **Git** (for version control)

### **Installation**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/astronights/llm-amazing-race-ai.git
   cd llm-amazing-race-ai
   ```

2. **Install the Requirements:**

   ```bash
   # Create an environment if you need to
   conda create -n flask python=3.12
   pip install -r requirements.txt
   ```

3. **Start the Flask Server:**

   ```bash
   flask --app api/index run -p 5328
   ```