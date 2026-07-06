# autoUiGame

`autoUiGame` is a Python-based UI automation tool designed for automating repetitive tasks in games via image recognition. It provides a graphical interface to select and run various automation "Use Cases" such as endless battles or dungeon farming.

## Features

- **Image Recognition**: Uses `pyautogui` and `OpenCV` to find UI elements on screen based on template images.
- **Graphical User Interface**: Built with `PySide6`, allowing users to configure and monitor automation tasks easily.
- **Multithreaded Execution**: Automation runs in a background thread to keep the UI responsive.
- **Configurable Use Cases**: Supports different scenarios like "Endless Battle" and "Endless Dungeon" with specific settings (e.g., dungeon level selection, result handling).
- **Robustness**: Includes retry logic, confidence-based matching, and automatic pop-up clearing.

## Project Structure

- `main_app.py`: The entry point that launches the GUI application.
- `AppState.py`: Manages the application state and orchestrates the execution of different Use Cases.
- `ClickObject.py`: The core engine for finding and interacting with UI elements. It encapsulates the `pyautogui` logic for image matching and clicking.
- `app/`: Contains UI components and the main application window (`AppWidget.py`).
- `usecase/`: Contains the logic for specific automation scenarios.
    - `BaseUsecase.py`: Abstract base class providing common functionality like logging and retries.
    - `BattleDungeon.py`: Logic for entering dungeons, selecting levels, and handling results.
    - `BattleUseCase.py`: Logic for general battle automation.
    - `MaxDimondUseCase.py`: Logic for specific diamond-related tasks.
- `utils/`: Utility functions and constants.
    - `ImageConstants.py`: Centralized management of image paths for UI elements.
    - `Utils.py`: Helper methods for threading, logging, and delays.
- `images/`: Stores the `.png` templates used for image recognition.

## How It Works (Flow of Logic)

1. **Initialization**: Running `python main_app.py` initializes the `AppWidget` GUI.
2. **Configuration**: The user selects a Use Case (e.g., "Endless Dungeon") and configures parameters like the dungeon level or what to do with rewards.
3. **Task Start**: Clicking the "Start" button triggers `_onClickStart` in `AppWidget`, which initializes `AppState` and spawns a background thread.
4. **Automation Loop**:
    - The thread executes the corresponding method in `AppState` (e.g., `performDungeon`).
    - The `AppState` repeatedly calls `start_use_case()` on the active `UseCase` object.
    - The `UseCase` uses `ClickObject` instances to look for specific images on the screen.
    - When a match is found (with a specified `confidence` level), `ClickObject` performs a mouse click at that location.
5. **Monitoring & Logs**: The GUI displays real-time logs of what the automation is doing (found images, clicks, retries).
6. **Stopping**: Clicking "Stop" sets a threading event that signals the background thread to exit its loop gracefully. It then prints a summary of actions performed (e.g., total items received).

## Prerequisites

- Python 3.11+
- Virtual environment (recommended)

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main_app.py
```
Select the desired task and configuration, then click **Start**. Make sure the game window is visible on your screen.

## Important Notes

- **Screen Resolution**: The automation relies on exact image matches. Ensure your game resolution and UI scale match the images in the `images/` directory.
- **Permissions**: On macOS/Linux, `pyautogui` may require Accessibility permissions to control the mouse.
