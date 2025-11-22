# Student Attendance System

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.0+-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A modern, lightweight Flask web application for managing student attendance records. Users can easily add, view, and delete student information through an intuitive interface with a clean, responsive design.

## ✨ Features

- **Add Student Details** – Submit student information via an easy-to-use form
- **View Records** – Display all saved students in a responsive, sortable table
- **Delete Records** – Remove student entries with a single click
- **Modern UI** – Clean, professional interface with custom CSS styling
- **Cloud Deployed** – Publicly accessible via Render hosting
- **Lightweight Database** – SQLite backend for fast, efficient data storage

## 🚀 Live Demo

The application is deployed and accessible at: **https://student-attendance-gt2w.onrender.com/**

## 📸 Screenshots

### Home Page
*[Screenshot placeholder: Add form interface image here]*

### Students List
*[Screenshot placeholder: Add students table view image here]*

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS (Jinja2 Templates)
- **Deployment:** Render
- **Styling:** Custom CSS

## 📁 Project Structure

```
student-attendance-system/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── students.db              # SQLite database (auto-generated)
│
├── templates/
│   ├── base.html            # Base template with navigation
│   ├── form.html            # Student registration form
│   └── students.html        # Students list view
│
└── static/
    ├── css/
    │   └── styles.css       # Custom styling
    └── img/
        └── logo.png         # Application logo
```

## 🔧 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-attendance-system.git
   cd student-attendance-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the app**
   - Open your browser and navigate to `http://localhost:5000`

## 📦 Dependencies

```
Flask==2.3.0
```

All dependencies are listed in `requirements.txt` and can be installed using pip.

## 🌐 Deployment on Render

### Step-by-Step Guide

1. **Create a Render Account**
   - Sign up at [render.com](https://render.com)

2. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Build Settings**
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`

4. **Set Environment Variables** (if needed)
   - Add any required environment variables in the Render dashboard

5. **Deploy**
   - Click "Create Web Service"
   - Wait for the deployment to complete
   - Access your app via the provided Render URL

## 📖 Usage Guide

### Adding a New Student

1. Navigate to the home page or click "Add Student" in the navigation
2. Fill in the student details:
   - **Name:** Student's full name
   - **Department:** Academic department (e.g., Computer Science)
   - **Roll Number:** Unique student identifier
   - **College:** Institution name
3. Click "Submit" to save the record

### Viewing Student Records

1. Click "View Students" in the navigation menu
2. Browse the responsive table showing all student records
3. Records display: Name, Department, Roll Number, and College

### Deleting a Record

1. Navigate to the "View Students" page
2. Click the "Delete" button next to the student record you wish to remove
3. The record will be permanently removed from the database

## 🔮 Future Enhancements

- **User Authentication** – Implement login/logout functionality with role-based access
- **Firebase Integration** – Add Firebase authentication for secure user management
- **Cloud Database** – Migrate from SQLite to cloud-based MySQL for scalability
- **Export Functionality** – Download student records as CSV or PDF
- **Search & Filter** – Advanced filtering options for large datasets
- **Attendance Tracking** – Add date-wise attendance marking features
- **Email Notifications** – Automated alerts for low attendance
- **Dashboard Analytics** – Visual charts and statistics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

