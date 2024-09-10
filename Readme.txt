
# Alarm Clock Application

This is a basic alarm clock app built with Python’s Tkinter library. It’s a simple, straightforward tool for setting alarms on specific days and times, with a few built-in sounds to choose from. The goal is to provide an easy-to-use, customizable alarm that you can control right from your desktop.

## Purpose

This app was created to offer a basic alarm clock that you can set for specific times on chosen days of the week. Whether you need a reminder or just a gentle nudge at a certain hour, this app provides an intuitive way to manage alarms. It's also a great little project to demonstrate the use of Tkinter for building GUIs and Pygame for handling sound.

## Major Features

- **Set Alarm Time and Day:** You can enter the hour, minute, and second for your alarm, and pick which day of the week it should go off.
- **Choose Your Alarm Sound:** There’s a simple dropdown that lets you select from a few included sounds, so you can customize what you hear when the alarm goes off.
- **Control Your Alarm:** Use the "Set alarm" button to activate the alarm and the "Stop alarm" button if you want to turn it off once it starts.
- **Input Validation:** The app checks to make sure you’re entering valid numbers for the time, so you won’t accidentally set something impossible like 99 minutes.

## Dependencies

Here’s what you’ll need to run the app:

- **Python 3.x**: Make sure Python is installed on your system. You can get it from [python.org](https://www.python.org/).
- **Tkinter**: This is usually included with Python, but on some systems, you might need to install it separately.
- **Pygame**: This library is used to play the alarm sounds. If you don’t have it, you can install it easily:
  ```bash
  pip install pygame
  ```

## How to Build and Run

To get the alarm clock up and running on your computer, follow these steps:

1. **Clone the Project:**
   First, grab the code from the repository and navigate into the project folder:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Required Libraries:**
   Make sure you have Python and then install Pygame using pip:
   ```bash
   pip install pygame
   ```

3. **Run the Application:**
   Start the app by running the Python script:
   ```bash
   python alarm_clock.py
   ```

4. **Using the App:**
   - Open the app and enter the time for your alarm in the provided fields.
   - Select the day of the week and the sound you want.
   - Click “Set alarm” to start it up. When it’s time, the alarm will sound, and you can stop it by clicking the “Stop alarm” button.

