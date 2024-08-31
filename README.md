# 🌍 LLM-Based Text Adventure: Amazing Race (Backend Server)

Welcome to the **GenAI Text Adventure: Amazing Race** project! This is an interactive, location-based text adventure game inspired by "The Amazing Race." The game challenges players to solve riddles and navigate through various cities and points of interest, using an AI-powered system to deliver a unique and engaging experience.

**NOTE**: This repository only holds the backend LLM + data code for this project.

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

### Demo

A sample of the puzzle created leveraging Open Source Geo data and LLM:

   ```yaml
[
    {
        "answer": "Eiffel Tower",
        "congratulatory_message": "You've reached the iconic Eiffel Tower, a must-see in Paris!",
        "hint": "A famous tower.",
        "riddle": "I stand tall, a symbol of France, my iron lady, a beacon of romance.",
        "task": {
            "answer": "324",
            "question": "What is the height of the Eiffel Tower in meters?"
        }
    },
    {
        "answer": "Louvre Museum",
        "congratulatory_message": "Welcome to the Louvre Museum, a treasure trove of art!",
        "hint": "A world-renowned museum.",
        "riddle": "I house masterpieces, from Mona Lisa's smile, to Venus de Milo's style.",
        "task": {
            "answer": "9.6 million",
            "question": "How many visitors does the Louvre Museum receive annually?"
        }
    },
    {
        "answer": "Champs-Élysées",
        "congratulatory_message": "You've arrived at the Champs-Élysées, a Parisian paradise!",
        "hint": "A famous shopping street.",
        "riddle": "I am a grand avenue, lined with shops, a haven for fashion, where luxury drops.",
        "task": {
            "answer": "1.9",
            "question": "What is the length of the Champs-Élysées in kilometers?"
        }
    },
    {
        "answer": "Pont Alexandre III",
        "congratulatory_message": "Congratulations on reaching the beautiful Pont Alexandre III!",
        "hint": "A bridge over the Seine.",
        "riddle": "I am a bridge of love, a romantic sight, a symbol of Paris, bathed in golden light.",
        "task": {
            "answer": "1900",
            "question": "What year was the Pont Alexandre III bridge inaugurated?"
        }
    },
    {
        "answer": "Palace of Versailles",
        "congratulatory_message": "You've reached the grand Palace of Versailles, a symbol of French history!",
        "hint": "A former royal residence.",
        "riddle": "I am a palace of history, where kings once reigned, a testament to grandeur, my beauty unfeigned.",
        "task": {
            "answer": "800",
            "question": "How many acres does the Palace of Versailles encompass?"
        }
    },
    {
        "answer": "Notre Dame Cathedral",
        "congratulatory_message": "Welcome to Notre Dame Cathedral, a breathtaking architectural wonder!",
        "hint": "A famous cathedral.",
        "riddle": "I am a cathedral of dreams, a Gothic masterpiece, a testament to faith, where history finds its peace.",
        "task": {
            "answer": "1163",
            "question": "What year was the Notre Dame Cathedral built?"
        }
    },
    {
        "answer": "Luxembourg Gardens",
        "congratulatory_message": "You've arrived at the serene Luxembourg Gardens, a haven of peace!",
        "hint": "A famous park in Paris.",
        "riddle": "I am a park of peace, a green oasis in the city, where nature's beauty finds its purity.",
        "task": {
            "answer": "Luxembourg Palace",
            "question": "What is the name of the palace located in the Luxembourg Gardens?"
        }
    },
    {
        "answer": "Montmartre",
        "congratulatory_message": "Welcome to Montmartre, a vibrant hub of artistic expression!",
        "hint": "A bohemian district in Paris.",
        "riddle": "I am a hidden gem, a charming neighborhood, with cobblestone streets, where artistry is bred.",
        "task": {
            "answer": "Sacré-Cœur Basilica",
            "question": "What is the name of the famous basilica located in Montmartre?"
        }
    },
    {
        "answer": "Pont Neuf",
        "congratulatory_message": "You've reached the Pont Neuf, a bridge blending artistry and functionality!",
        "hint": "A bridge with a unique design.",
        "riddle": "I am a bridge of art, a modern masterpiece, a symbol of Paris, where creativity finds its release.",
        "task": {
            "answer": "238",
            "question": "What is the length of the Pont Neuf in meters?"
        }
    },
    {
        "answer": "Arc de Triomphe",
        "congratulatory_message": "Congratulations on reaching the Arc de Triomphe, a monument to victory!",
        "hint": "A triumphal arch.",
        "riddle": "I am a symbol of freedom, a soaring archway, a testament to unity, where history finds its sway.",
        "task": {
            "answer": "660",
            "question": "How many names of soldiers are inscribed on the Arc de Triomphe?"
        }
    },
    {
        "answer": "Finish",
        "congratulatory_message": "Congratulations on completing your Amazing Race through Paris!",
        "hint": "The ending of the race.",
        "riddle": "The journey is complete, your adventure's end, Paris's wonders, memories you'll lend.",
        "task": {}
    }
]
   ```
