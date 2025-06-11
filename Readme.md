# Alarm Clock Application

A **Python Tkinter** desktop program that functions as a customizable alarm clock. Users can schedule alarms on specific days and times, select from built‑in sounds, and control alarm playback—all in a lightweight GUI powered by Tkinter and Pygame.

---

## 🚀 Features

* **Schedule Alarms**: Set hour, minute, second and choose a day of the week for each alarm.
* **Customizable Sounds**: Select from `.mp3` sound files (e.g., `beep.mp3`, `chime.mp3`) via a dropdown.
* **Start & Stop Controls**: Use **Set Alarm** to activate and **Stop Alarm** to silence the ringing.
* **Input Validation**: Ensures entered time values are numeric and within valid ranges.
* **Background Scheduling**: Runs alarms without freezing the GUI by leveraging the `after()` method in Tkinter.

---

## 📂 Project Structure

```plaintext
alarm-clock-app/
├── alarm_clock.py        # Main script: GUI layout, scheduling logic, sound playback
├── sounds/               # Folder containing alarm sound files
│   ├── beep.mp3
│   ├── chime.mp3
│   └── ring.mp3
├── requirements.txt      # External dependencies (pygame)
└── README.md             # Project documentation
```

---

## ⚙️ Getting Started

### Prerequisites

* **Python 3.x**
* **Tkinter** (bundled with most Python installations)
* **Pygame** (for audio playback)

### Installation & Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/alarm-clock-app.git
   cd alarm-clock-app
   ```
2. **Install dependencies**

   ```bash
   pip install pygame
   ```
3. **Run the application**

   ```bash
   python alarm_clock.py
   ```

---

## 📡 Usage

1. Launch the app to open the GUI window.
2. Enter the desired **hour**, **minute**, and **second**.
3. Select a **day of the week** (e.g., Monday, Tuesday).
4. Choose an **alarm sound** from the dropdown menu.
5. Click **Set Alarm** to activate. The app will monitor the clock in the background.
6. At the scheduled time, the chosen sound will play.
7. Click **Stop Alarm** to silence it.

---

## 🔑 Skills & Technologies

* **Python 3**: Core application logic and scheduling.
* **Tkinter**: GUI creation, event handling, and background tasks.
* **Pygame**: Loading and playing audio files for alarms.
* **Input Validation**: Ensuring robust user inputs.


