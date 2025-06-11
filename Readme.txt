# Alarm Clock Application

A **Python Tkinter** desktop alarm clock that lets you schedule **alarms** on specific days and times with customizable **Pygame** sounds. This project demonstrates building a simple GUI, handling time-based events, and integrating audio playback.

---

## 🚀 Features

* **Schedule Alarms**: Input hour, minute, and second, then choose the day of the week for your alarm to trigger.
* **Customizable Sounds**: Pick from a dropdown of built-in `.mp3` files to personalize your alarm tone.
* **Start & Stop Controls**: Use **Set Alarm** to activate and **Stop Alarm** to silence the alarm once it’s ringing.
* **Input Validation**: Ensures you enter valid numeric values for time fields, preventing impossible settings.

---

## 📂 Project Structure

```plaintext
alarm-clock-app/
├── alarm_clock.py        # Main application script (Tkinter GUI + scheduling logic)
├── sounds/               # Folder containing alarm sound files
│   ├── beep.mp3
│   ├── chime.mp3
│   └── ring.mp3
├── requirements.txt      # Lists external dependencies (pygame)
└── README.md             # This documentation
```

---

## ⚙️ Getting Started

### Prerequisites

* **Python 3.x**
* **Tkinter** (bundled with most Python installs)
* **Pygame** for audio playback

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/alarm-clock-app.git
   cd alarm-clock-app
   ```
2. **Install Dependencies**

   ```bash
   pip install pygame
   ```
3. **Run the Application**

   ```bash
   python alarm_clock.py
   ```

---

## 📡 Usage

1. Launch the app to open the GUI window.
2. Enter the desired **hour**, **minute**, and **second**.
3. Select the **day of the week** for the alarm.
4. Choose an alarm **sound** from the dropdown menu.
5. Click **Set Alarm** to start. When the scheduled time arrives, the selected sound will play.
6. Click **Stop Alarm** to silence it.

---

## 🔑 Skills & Technologies

* **Python 3** – Core application logic
* **Tkinter** – GUI components and event handling
* **Pygame** – Audio playback for alarm sounds

---

## 🎯 Why This Project?

1. **GUI Development**: Learn how to build desktop applications with Tkinter.
2. **Scheduling Logic**: Practice handling time-based triggers in Python.
3. **Multimedia Integration**: See how to incorporate Pygame for sound playback.
