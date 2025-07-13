# 🏏 Cricket Match Dashboard

A simple and interactive **Streamlit dashboard** that shows **recent cricket matches** from Cricbuzz (via RapidAPI) or your own `.csv` file.  
The data is stored in a **MySQL database** and displayed in a clean, responsive dashboard UI.

---

## 🚀 Features

- 🏆 Import real match data from Cricbuzz or CSV
- 💾 Store matches in a local MySQL database
- 📊 View recent cricket match results with Streamlit
- 🔒 Secure credentials using `.env` file
- 🛠 Easily customizable for future stats like scores, venues, players, etc.

---

## 🖼 Preview

![App Screenshot](https://github.com/user-attachments/assets/97934877-2321-4e43-ac2d-61fc12f50305) 

---

## 📦 Tech Stack

| Tool                                              | Purpose                        |
| ------------------------------------------------- | ------------------------------ |
| [Streamlit](https://streamlit.io)                 | Frontend dashboard             |
| [RapidAPI](https://rapidapi.com)                  | API access to Cricbuzz         |
| [MySQL](https://www.mysql.com/)                   | Relational database            |
| [Python](https://python.org)                      | Core backend logic             |
| [dotenv](https://pypi.org/project/python-dotenv/) | Load environment variables     |
| [Pandas](https://pandas.pydata.org/)              | Data manipulation & analysis   |
| [SQLAlchemy](https://www.sqlalchemy.org/)         | SQL connection with Pandas     |

---

## 📁 Project Structure

📁 Cricket-Match-Dashboard
├── 📄 app.py                    # Streamlit frontend
├── 📄 fetch_cricket_data.py     # API fetch + MySQL insert
├── 📄 insert_csv_to_db.py       # CSV insert alternative
├── 📄 recent_matches.csv        # Sample data (optional)
├── 📄 requirements.txt          # Dependencies
├── 📄 .env                      # Secrets (ignored)
├── 📄 .env.template             # Template for .env
├── 📄 README.md                 # Project docs


---

## ⚙️ Setup Instructions

# ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-username/Cricket-Match-Dashboard.git
cd Cricket-Match-Dashboard
```
# 🔐 2. Create a .env File

- Copy the example file:

```bash
cp .env.template .env
```

- Update the .env file with your own:

```env
# .env

API_KEY=your_rapidapi_key
API_HOST=cricbuzz-cricket.p.rapidapi.com

DB_NAME=cricket_dashboard
DB_USERNAME=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306

```

# 🐬 3. Set Up MySQL
- Install MySQL & create a database named cricket_dashboard.
- Start your MySQL server (via Workbench or command line).

# 📦 4. Install Dependencies
- Use pip to install required libraries:

```bash
pip install -r requirements.txt
```

# 🏗️ 5. Fetch Live Data (optional):

- If you're using the Cricbuzz API:

```bash
python fetch_cricket_data.py
```

- Or use sample CSV:

```bash
python insert_csv_to_db.py
```

# ▶️ 6. Run the App:

```bash
streamlit run app.py
```

