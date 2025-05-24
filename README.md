# Asteroids

**Asteroids** is a simple, Pygame-based clone of the classic arcade game, built as part of the Boot.dev curriculum.

## Features

* **Player Ship**: Rotate, thrust, and shoot projectiles with smooth acceleration and inertia (WASD)
* **Asteroid Field**: Randomly generated asteroids in multiple sizes, breaking into smaller pieces.
* **Collision Detection**: Circle-based collision checks between ship, asteroids, and shots.
* **Scoring**: Earn points for destroying asteroids; track and display high score.
* **3 Lives**: Game ends when player is hit by 3 asteroids.
* **Game States**: Active play, Pause (P), and Game Over in the CLI terminal.

## Demo

## Getting Started

### Prerequisites

* Python 3.7 or higher
* [Pygame](https://www.pygame.org/) (installed via `requirements.txt`)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/LyricalEcho/asteroids.git
   cd asteroids
   ```
2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the game with:

```bash
python main.py
```

Controls:

* **Rotate**: A / D keys
* **Thrust**: W / S arrow key
* **Shoot**: Spacebar
* **Pause**: P key

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is for educational purposes and follows open-source best practices. No license file is included—please contact the author for reuse permissions.
