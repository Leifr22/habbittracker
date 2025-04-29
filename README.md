```markdown
# Habit Tracker

📌 **Description**  
Habit Tracker is a project designed to track daily habits.  
The application helps users stay motivated and maintain consistency in completing their habits.

---

## 🚀 **Features**  
- ✔️ **Registration/Authentication** — secure user authentication  
- ✔️ **Habit Management** — add, update, and delete habits  
- ✔️ **Daily Tracking** — mark completed habits and monitor progress  
- ✔️ **Simple Interface** — user-friendly and intuitive design  

---

## 🛠 **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Leifr22/habbittracker.git
   cd habbittracker
   ```

2. **Ensure Docker is installed.**

3. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the project using Docker:**
   ```bash
   docker-compose up --build
   ```

   Or start the local development server:
   ```bash
   python manage.py runserver
   ```

6. **Open the application in your browser:**  
   [http://127.0.0.1:8000](http://127.0.0.1:8000)


