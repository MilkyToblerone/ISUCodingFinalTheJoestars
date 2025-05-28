# JOJO: The AI Chronicles

**JOJO: The AI Chronicles** is a command-line, story-driven game inspired by the JoJo's Bizarre Adventure universe. Built using Python and OpenAI's API, this project blends user interaction with generative storytelling to deliver a personalized, stylized narrative experience.

---

## 🎯 Overview

In this game, players:

* Create a custom character and receive a randomly assigned Stand or alternative power (Hamon or Spin)
* Are given a motivation and a unique main plotline
* Engage in a series of four AI-narrated battles
* Save and load their journey at any point
* Receive episodic summaries after each encounter, written in the tone and style of classic JoJo anime

The experience is enhanced by a dynamic prompt system, a custom stand designer, and structured save/load capabilities.

---

## 📁 Project Structure

### `main.py`

Central control of the game loop and menu interface.

* Menu options include: Play Game, Create/View Custom Stands, Load Game, Exit
* Easter egg triggers for specific character names (e.g., "DIO", "Gustave")
* Character setup includes power, motivation, and plotline assignment

### `characters.py`

Defines core game entities:

* `Character`: includes HP, name, progress, stand or alternative power
* `Stand`: includes name, ability, and weakness

### `custom.py`

Tools for creating and managing user-defined stands.

* Custom stands are stored as JSON and can be used exclusively in custom mode

### `plotline.py`

Randomizes both motivations and narrative paths.

* Includes several thematic plotlines and character motivations

### `battle.py`

Handles all combat logic:

* Four enemy battles with AI-generated narrative per round
* Damage is estimated by the AI and parsed for accuracy
* Enemies can be defeated early or automatically at round 3
* Ensures fair and immersive fight resolution

### `savegame.py`

Save/load infrastructure:

* Game progress saved as structured JSON
* Includes character state, progress, and battle number

### `episodes.py`

Creates a summarized JoJo-style episode recap after each fight:

* Includes an AI-generated episode title and three-part summary
* Stored as `.txt` files for future reference

---

## ✅ Stability and Logic Handling

* Game exit is cleanly handled to prevent infinite loops or repeated sessions
* Input validation prevents unexpected behavior during game mode selection
* Battle outcomes prioritize player status, ensuring the game ends immediately if the player is defeated
* Damage calculation is AI-controlled and includes fallback parsing logic for robustness

---

## 📌 Design Philosophy

This game is designed for replayability and narrative engagement. Every session is unique:

* Different combinations of powers and motivations
* Randomly selected plotlines and battle scenarios
* AI-driven scenes ensure variety and character

Whether you're a fan of JoJo or narrative games in general, JOJO: The AI Chronicles offers a compact but creative twist on interactive storytelling.

---

Made with precision, creativity, and a deep love for bizarre adventures.
