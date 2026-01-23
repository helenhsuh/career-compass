# Career Compass: AI-Assisted Career Pivot Reasoning Tool

Career Compass is a human-centered AI project designed to help individuals navigate complex career transitions with clarity and structure. The tool blends counseling-informed reasoning with foundational machine learning concepts to help users understand role alignment, transferable skills, and long-term career fit.

This repository reflects the full design and architecture of the project, including data preparation planning, feature engineering reasoning, baseline modeling approaches, evaluation strategies, and iterative experimentation. While no real dataset was used, the project is structured to support real development in the future.

---

## 🌟 Project Purpose

Career transitions are overwhelming. Job descriptions are inconsistent, skills are hard to compare, and people often lack access to personalized guidance. Career Compass aims to:

- Provide structured, accessible support for career pivots  
- Identify alignment between user backgrounds and potential roles  
- Surface transferable skills and realistic next-step pathways  
- Model trade-offs across skills, salary, location, and constraints  
- Demonstrate foundational ML reasoning and problem-solving  

---

## 🧠 Problem Definition

People need a way to understand which roles align with their skills, values, constraints, and long-term goals. Career Compass is designed to:

- Standardize role information  
- Represent user profiles and job descriptions in comparable formats  
- Rank roles based on alignment and user-defined priorities  
- Provide interpretable, human-centered recommendations  

---

## 🏗️ Repository Structure

career-compass/
│
├── data/
│   ├── raw/                  # Unprocessed job descriptions, skills, taxonomies
│   ├── interim/              # Cleaned but not yet structured
│   └── processed/            # Final structured data ready for modeling
│
├── notebooks/
│   ├── 01_data_design.ipynb
│   ├── 02_feature_engineering_baselines.ipynb
│   ├── 03_embeddings_exploration.ipynb
│   ├── 04_similarity_and_ranking.ipynb
│   └── 05_evaluation_strategy.ipynb
│
├── src/
│   ├── data/
│   │   ├── data_design.py            # Schema definition and data planning
│   │   └── preprocessing.py          # Text normalization and cleaning utilities
│   │
│   ├── features/
│   │   ├── tfidf_features.py         # Baseline TF‑IDF vectorization
│   │   └── embedding_features.py     # Embedding feature scaffolding
│   │
│   ├── models/
│   │   ├── baseline_similarity.py    # Cosine similarity ranking
│   │   └── embedding_similarity.py   # Embedding‑based similarity design
│   │
│   ├── evaluation/
│   │   ├── metrics.py                # Semantic similarity and clustering metrics
│   │   └── human_review.py           # Human‑in‑the‑loop evaluation design
│   │
│   └── utils/
│       ├── helpers.py                # Shared helper functions
│       └── config.py                 # Configuration settings
│
├── docs/
│   ├── project_overview.md
│   ├── data_design.md
│   ├── feature_engineering.md
│   ├── modeling_approach.md
│   ├── evaluation_plan.md
│   ├── limitations_and_future_work.md
│   └── ethical_considerations.md
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_similarity.py
│   └── test_embeddings.py
│
├── requirements.txt
├── CONTRIBUTING.md
└── README.md


## How to Navigate This Repo

Career Compass is organized to reflect the full reasoning and architecture behind the project, even without a real dataset. If you're exploring the repository, here’s the best way to understand how everything fits together:

### 1. Start with the `docs/` folder  
This is the conceptual foundation of the project. It includes:
- project_overview.md – purpose and vision  
- data_design.md – schema planning and data assumptions  
- feature_engineering.md – baseline and embedding reasoning  
- modeling_approach.md – similarity and ranking design  
- evaluation_plan.md – hybrid evaluation strategy  
- limitations_and_future_work.md – constraints and next steps  
- ethical_considerations.md – fairness, transparency, and user agency  

### 2. Explore the `notebooks/` directory  
These notebooks walk through the reasoning process step by step:
- data design  
- baseline feature engineering  
- embedding exploration  
- similarity scoring  
- evaluation planning  

### 3. Review the `src/` directory  
This is the code scaffolding for future development:
- data/ – preprocessing and schema logic  
- features/ – TF‑IDF and embedding feature modules  
- models/ – baseline and embedding similarity modules  
- evaluation/ – metrics and human‑review design  
- utils/ – shared helpers and configuration  

### 4. Check the `tests/` folder  
These starter tests reflect engineering best practices.

### 5. Look at `requirements.txt` and `CONTRIBUTING.md`  
These outline dependencies and collaboration guidelines.

This structure is designed to demonstrate engineering thinking, ML reasoning, and human‑centered design, while keeping the project ready for future development.
---

## 🔧 Technical Foundations Demonstrated

### **Data Thinking**
- Schema design  
- Planning for normalization, deduplication, labeling  
- Understanding what “clean data” means in ML contexts  

### **Feature Engineering**
- TF‑IDF baseline  
- Cosine similarity  
- Transformer-based embedding design  
- Trade-offs between interpretability and performance  

### **Modeling Reasoning**
- Why baselines matter  
- When embeddings are appropriate  
- How to compare models  
- How to evaluate without labels  

### **Evaluation Strategy**
- Hybrid metrics + human review  
- Clustering coherence  
- Counseling-informed interpretability  

---

## 🧪 Challenges & How They Were Overcome

- **No dataset available** → Designed full pipeline with synthetic examples  
- **Knowledge gaps in embeddings** → Used documentation, small experiments, and AI assistants  
- **Unclear evaluation without labels** → Designed hybrid evaluation strategy  
- **AI assistants giving incorrect code** → Verified, discarded, and corrected through reasoning  

---

## 🤖 Use of AI Coding Assistants

AI tools were used to:
- Scaffold code structure  
- Debug syntax issues  
- Visualize vector similarity concepts  

AI tools were *not* blindly trusted.  
Incorrect outputs were discarded and replaced with documented reasoning.

---

## 🚀 Future Work

- Collect real datasets  
- Build an API for role matching  
- Add user feedback loops  
- Integrate salary/location trade-off modeling  
- Create a dashboard for skill-gap analysis  

---

## 🧭 Why This Project Matters

Career Compass reflects:
- Human-centered design  
- Ethical reasoning  
- Data-driven thinking  
- ML conceptual understanding  
- Problem decomposition  
- Responsible use of AI  

It is intentionally designed to grow into a real product while demonstrating the engineering mindset required for the REACH apprenticeship.
