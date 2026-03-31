# Notes-Generator 📚

An intelligent autonomous documentation generation system that automatically creates comprehensive, well-structured technical documentation for any topic using AI agents and web research.

## Overview

Notes-Generator is a multi-agent system that orchestrates the creation of professional technical documentation. It leverages AI models, web search capabilities, and a specialized agent architecture to produce cohesive, well-researched documentation similar to platforms like GeeksforGeeks.

## Features ✨

- **Multi-Agent Architecture**: Four specialized agents working together:
  - 🎯 **Orchestrator Agent**: Plans logical topic breakdowns and creates curriculum structure
  - 🔍 **Researcher Agent**: Conducts web research using DuckDuckGo to gather relevant information
  - ✍️ **Writer Agent**: Generates well-structured content based on research data
  - ✓ **Reviewer Agent**: Validates and refines content for quality and accuracy

- **Comprehensive Documentation**: Automatically generates documentation with:
  - Introduction and conceptual overview
  - Core concepts and syntax
  - Practical use cases and examples
  - Best practices and performance optimization
  - Advanced patterns and troubleshooting

- **Smart Resource Management**: 
  - Organized file structure with topic-based directories
  - Automatic index page generation
  - Reference section with source links and citations

- **Flexible AI Backend**: Uses OpenRouter API for model flexibility and cost optimization

## Project Structure

```
Notes-Generator/
├── main.py                  # Entry point and DocumentationSystem class
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── .gitignore              # Git configuration
├── .env                    # Environment variables (create this locally)
├── agents/                 # Multi-agent system
│   ├── __init__.py
│   ├── orchestrator.py     # Topic planning and curriculum design
│   ├── researcher.py       # Web research functionality
│   ├── writer.py           # Content generation
│   └── reviewer.py         # Content validation and refinement
├── utils/                  # Utility modules
│   ├── __init__.py
│   ├── openrouter_client.py        # AI API integration
│   ├── search_tool.py              # Web search wrapper
│   └── file_manager.py             # File I/O operations
├── templates/              # Content templates and formatting
├── docs/                   # Generated documentation output
│   └── Nginx/             # Example: Nginx documentation
└── env/                    # Virtual environment (auto-generated)
```

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenRouter API key ([Get one here](https://openrouter.ai))

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/vijay-narasimha/Notes-Generator.git
   cd Notes-Generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```bash
   OPENROUTER_API_KEY=your_api_key_here
   ```

## Usage

### Basic Usage

```python
from main import DocumentationSystem

# Initialize the system
system = DocumentationSystem(topic="Your Topic", model="gpt-4-mini")

# Generate documentation
system.run("Your Technical Topic")
```

### Command Line Usage

```bash
python main.py --topic "Nginx" --model "gpt-4-mini"
```

### Example: Generating Nginx Documentation

```python
from main import DocumentationSystem

# Create system for Nginx documentation
doc_system = DocumentationSystem(topic="Nginx", model="gpt-4-mini")

# Run the pipeline
doc_system.run("Nginx - Web Server and Reverse Proxy")
```

The system will:
1. Break down the topic into logical subtopics
2. Research each subtopic using web search
3. Generate comprehensive content for each section
4. Review and refine the content
5. Save everything to `docs/Nginx/` directory
6. Generate an index page and references

## How It Works

### Documentation Generation Pipeline

```
Topic Input
    ↓
[Orchestrator Agent]
    Plan subtopics and structure
    ↓
For each subtopic:
    ↓
[Researcher Agent]
    Gather information from web
    ↓
[Writer Agent]
    Generate content
    ↓
[Reviewer Agent]
    Validate and refine
    ↓
[File Manager]
    Save to organized structure
    ↓
Generate Index & References
    ↓
Documentation Ready! 📚
```

### Agent Responsibilities

| Agent | Role |
|-------|------|
| **Orchestrator** | Analyzes the main topic and creates a logical curriculum structure (introduction → basics → advanced) |
| **Researcher** | Searches the web for relevant information and gathers data for each subtopic |
| **Writer** | Transforms research data into clear, well-formatted documentation |
| **Reviewer** | Reviews content for accuracy, clarity, and consistency; generates references |

## Configuration

### Environment Variables

- `OPENROUTER_API_KEY`: Your OpenRouter API key (required)

