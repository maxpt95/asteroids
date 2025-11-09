# Asteroids

A classic Asteroids game implementation built with Python and Pygame.

## Description

This is a recreation of the classic arcade game Asteroids. Control a spaceship, shoot asteroids, and survive as long as possible! The game features collision detection, asteroid splitting mechanics, and game state logging for analysis.

## Features

- **Classic Gameplay**: Control a triangular spaceship in space
- **Asteroid Mechanics**: Asteroids split into smaller pieces when shot
- **Smooth Controls**: Rotate, move forward/backward, and shoot
- **Game State Logging**: Automatic logging of game events and states for analysis
- **60 FPS**: Smooth gameplay at 60 frames per second

## Requirements

- Python >= 3.12
- Pygame 2.6.1

## Installation

1. Clone the repository:
```bash
git clone https://github.com/maxpt95/asteroids.git
cd asteroids
```

2. Install dependencies using uv:
```bash
uv sync
```

## How to Play

Run the game with:
```bash
uv run main.py
```

### Controls

- **W**: Move forward
- **S**: Move backward
- **A**: Rotate left
- **D**: Rotate right
- **SPACE**: Shoot

### Objective

Survive as long as possible by shooting asteroids before they hit your ship. When you shoot an asteroid, it splits into two smaller asteroids (unless it's already at minimum size). The game ends when an asteroid collides with your spaceship.

## Game Configuration

You can modify game parameters in `constants.py`:

- `SCREEN_WIDTH` / `SCREEN_HEIGHT`: Window dimensions (default: 1280x720)
- `PLAYER_SPEED`: Player movement speed (default: 300)
- `PLAYER_TURN_SPEED`: Player rotation speed (default: 300)
- `PLAYER_SHOOT_COOLDOWN_SECONDS`: Time between shots (default: 0.3s)
- `ASTEROID_SPAWN_RATE`: Asteroid spawn interval (default: 0.8s)
- `ASTEROID_MIN_RADIUS`: Smallest asteroid size (default: 20)

## Possible new features
- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped