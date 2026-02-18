# AurumBit: Where Economic Cybernetics Meets Luxury Design
[![AurumBit Quality Check](https://github.com/Puiutmic/AurumBit-Generative-Engine/actions/workflows/ci_pipeline.yml/badge.svg)](https://github.com/Puiutmic/AurumBit-Generative-Engine/actions/workflows/ci_pipeline.yml)

### Hi, I'm David

AurumBit is my attempt to bridge the gap between abstract mathematical bits and the physical world of luxury goods. Coming from a background in **Economic Cybernetics**, I’ve always been fascinated by how data and algorithms can optimize traditional, labor-intensive industries.

### The Problem with Luxury
Traditional jewelry design is often stuck in a binary choice: either mass-produced via static molds or handcrafted at an unscalable pace. There is a missing middle—a way to create unique, complex, and organic forms that are driven by data rather than manual labor.

### The Solution: An Algorithmic Engine
Instead of modeling shapes by hand, I am building an engine in Python that "calculates" jewelry. By using the Blender API, I treat 3D space as a mathematical canvas. My current prototypes use parametric equations to generate geometries like twisted Mobius bands and cellular structures that would be nearly impossible to design traditionally.

### Current Status: Work in Progress 
Right now, AurumBit is in its **Engine Foundation** phase. 
- **What works:** The core Python logic can already generate complex meshes based on mathematical constants. 
- **The Bridge:** I have successfully decoupled the design intent from the geometry. The engine now listens to a `config.json` file, meaning I can change the entire look of a piece by simply adjusting data points, without touching the source code.

![AurumBit Gen1](renders/aurumbit_gen1.png)

---

## The Roadmap: From Code to Gold

I don't just want to make "cool shapes." I am building a full-cycle generative pipeline.

#### Phase 1: Geometric Synthesis (Current)
Developing the library of algorithms (Voronoi, Fibonacci spirals, and L-systems) that define the "AurumBit style."

#### Phase 2: The AI Interpreter (Next Step)
This is where the "Bit" truly meets "Aurum." I am working on integrating an LLM bridge to translate natural language prompts into the JSON parameters my engine requires. The goal is to let a user describe a feeling or an inspiration and have the engine calculate the perfect geometric response.

#### Phase 3: Physical Validation & Export
Optimizing the generated meshes specifically for high-precision 3D printing and lost-wax casting. A design is only successful if it can actually be held in one's hand :)

### Technical Stack
- **Core Logic:** Python (Blender API / bpy).
- **Data Structure:** JSON-based parameter mapping.
- **Mathematics:** Vector calculus and parametric geometry.

---
*AurumBit is a Work in Progress. It represents my journey into Deep Tech—proving that with enough code, we can turn a bit of information into a piece of gold.*
