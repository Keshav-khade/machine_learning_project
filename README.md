# 🎬 Prime_Flix – Movie Recommender System

Welcome to **Prime_Flix**, a personalized movie recommender system built using **machine learning** and deployed with **Streamlit** on the cloud.

This project uses content-based filtering to suggest similar movies based on a user's selected choice. It uses a precomputed similarity matrix to deliver fast recommendations with poster previews via the TMDB API.

---

## 🚀 Features

- 🎯 Content-based movie recommendation
- 📦 Pre-trained model using `scikit-learn` and `pandas`
- 🖼️ Movie posters using the TMDB API
- 🌐 Deployed with **Streamlit** and **Render**
- ⚡ Fast recommendations using a similarity matrix

---

## 📁 Project Structure

Prime_Flix/
│
├── app.py # Main Streamlit app
├── model.py # Recommendation logic
├── setup.sh # Shell script for setup on Render
├── requirements.txt # All dependencies
├── Procfile # Render startup instructions
├── .gitignore # Files/folders to ignore in Git
├── README.md # This file
│
├── movie_dict.pkl # (ignored) Dictionary of movies
├── similarity.pkl # (ignored) Similarity matrix (~176MB)


---

## 🧠 Recommender System Overview

This project uses a **content-based recommendation system** where:

- Movie metadata is vectorized using NLP techniques
- Cosine similarity is computed between movie vectors
- Top N similar movies are retrieved for a selected movie

Poster images are retrieved live using **TMDB’s public API**.

---

## 🛠️ Mandatory Files for Deployment

| File         | Description                                      |
|--------------|--------------------------------------------------|
| `app.py`     | Main Streamlit app, connects frontend & backend |
| `model.py`   | Recommender logic + data loading                |
| `setup.sh`   | Installs dependencies on Render                 |
| `requirements.txt` | Python packages required                    |
| `Procfile`   | Tells Render how to start the app               |
| `.gitignore` | Prevents large or sensitive files from tracking |

> 🔒 `.pkl` and `.csv` files are **ignored** in Git, but downloaded automatically at runtime using Google Drive links.

---

## ☁️ Deployment on Render

### ➤ Render Setup Steps

1. Push code to GitHub
2. Go to [Render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set:
   - Runtime: **Python 3**
   - Start command:
     ```bash
     sh setup.sh && streamlit run app.py
     ```
5. Deploy and enjoy 🎉

---

## 🔗 External Dependencies

- [Streamlit](https://streamlit.io)
- [TMDb API](https://developer.themoviedb.org)
- [gdown](https://github.com/wkentaro/gdown) for downloading `.pkl` files from Google Drive
- [pandas](https://pandas.pydata.org)
- [scikit-learn](https://scikit-learn.org)

---

## 💡 Future Improvements

- Add user-based collaborative filtering
- Include movie genres and cast in filtering
- Add search functionality
- Deploy with Docker for even more control

---

## 🙌 Acknowledgements

Thanks to:
- [TMDb](https://www.themoviedb.org/) for movie data & posters
- Open-source Python community
- You, for using this tool 💙

---

## 📸 Example Output

| 🎥 Movie Selected | 🔍 Recommendations |
|------------------|--------------------|
| Inception        | Interstellar, The Prestige, Tenet, etc. |

---

## 👨‍💻 Author

**Keshav Khade**  
➡ [GitHub](https://github.com/Keshav-khade)

---

> ⭐ _Don’t forget to star the repo if you found this helpful!_
