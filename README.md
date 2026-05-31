# Retro Snake Game (PyQt5)

A classic **Snake Game** built from scratch in Python using the **PyQt5** framework. 

The goal of this project was to create a fully functional game using pure code, without relying on external game engines (like Pygame). This required writing all the movement and rendering logic from the ground up.

## Key Features & Logic:

* **Movement Logic (Arrays):** The snake's body is stored as a list of coordinates. With every step, a new block is added to the front (the head) and the last block is removed from the end (the tail), creating smooth movement.
* **Game Loop (QTimer):** A PyQt5 timer ticks every 150 milliseconds to refresh the game, move the snake, and check if the game has ended.
* **Custom Graphics (QPainter):** Instead of using external image files, everything on the screen (the snake and the food) is drawn directly through code using geometric shapes and colors.
* **Controls & Collisions:** The game detects arrow key presses in real time and automatically triggers a "Game Over" window if the snake hits the wall or itself.

## How to Run

1. **Install PyQt5** (if you haven't already):
```bash
   pip install PyQt5
