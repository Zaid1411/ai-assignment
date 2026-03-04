# Rayeeva AI Systems Internship Assignment

## Overview

This project implements AI-powered backend modules using **FastAPI**.
The system analyzes product descriptions and generates structured outputs for catalog automation and sustainability impact reporting.

Implemented Modules:

* AI Auto Category & Tag Generator
* AI Impact Reporting Generator

The API returns structured JSON responses and includes logging, validation, and modular business logic.

---

## Architecture Overview

The system follows a simple API architecture.

Flow:

Client Request → FastAPI API → AI Logic / Business Logic → JSON Response

Components:

1. **FastAPI Server**
   Handles HTTP requests and routes.

2. **Product Input Model (Pydantic)**
   Validates incoming product data.

3. **AI Category Generator**
   Analyzes product descriptions and generates:

   * category
   * sub-category
   * SEO tags
   * sustainability filters

4. **Impact Reporting Module**
   Calculates environmental impact such as:

   * plastic saved
   * carbon avoided
   * impact statement

5. **Logging System**
   Logs prompts and responses for debugging and monitoring.

---

## AI Prompt Design

The AI logic analyzes product descriptions to determine product category and sustainability attributes.

Example Input:

{
"description": "Reusable bamboo water bottle",
"quantity": 5
}

Processing Steps:

1. Convert product description to lowercase.
2. Detect sustainability-related keywords such as:

   * bamboo
   * reusable
   * eco
3. Based on detected keywords, assign:

   * category
   * sub-category
   * SEO tags
   * sustainability filters

Example Output:

{
"category": "Eco Products",
"sub_category": "Reusable Items",
"seo_tags": ["eco friendly", "plastic free"],
"filters": ["recyclable", "eco-friendly"]
}

This approach simulates AI-driven classification logic while ensuring structured JSON outputs.

---

## API Endpoints

### Generate Category

POST /generate-category

Input:

{
"description": "Reusable bamboo water bottle",
"quantity": 5
}

Output:
Returns category, sub-category, SEO tags, and filters.

---

### Impact Report

POST /impact-report

Input:

{
"description": "Reusable bamboo water bottle",
"quantity": 5
}

Output:

{
"plastic_saved_kg": 1.0,
"carbon_avoided_kg": 1.5,
"impact_statement": "This order reduces plastic waste and carbon emissions."
}

---

## Technology Used

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## How to Run the Project

Install dependencies:

python3 -m pip install -r requirements.txt

Run the API server:

python3 -m uvicorn main:app --reload

Open API documentation:

http://127.0.0.1:8000/docs
