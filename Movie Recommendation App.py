import tkinter as tk
from tkinter import messagebox
import random

# Extended movie data categorized by genre
movies_by_genre = {
    'Action': [
        'Mad Max: Fury Road', 'Die Hard', 'John Wick', 'The Dark Knight', 'Gladiator', 'Terminator 2',
        'The Avengers', 'Casino Royale', 'The Bourne Identity', 'Mission: Impossible', '300',
        'The Raid: Redemption', 'Black Panther', 'The Equalizer', 'Fury'
    ],
    'Comedy': [
        'Superbad', 'The Hangover', 'Step Brothers', 'Anchorman', 'Bridesmaids', 'Dumb and Dumber',
        'Mean Girls', 'The Big Lebowski', 'Hot Fuzz', 'Borat', 'Ghostbusters', 'Napoleon Dynamite',
        'Shaun of the Dead', 'Zoolander', 'Crazy Rich Asians'
    ],
    'Drama': [
        'The Shawshank Redemption', 'Forrest Gump', 'The Godfather', '12 Angry Men', 'Schindler’s List',
        'The Green Mile', 'A Beautiful Mind', 'Fight Club', 'American Beauty', 'The Pursuit of Happyness',
        'Good Will Hunting', 'Slumdog Millionaire', 'The Social Network', 'Whiplash', 'The Departed'
    ],
    'Horror': [
        'The Exorcist', 'A Nightmare on Elm Street', 'Get Out', 'The Conjuring', 'Hereditary', 'It',
        'The Shining', 'Halloween', 'Psycho', 'The Ring', 'Scream', 'Paranormal Activity', 'The Babadook',
        'Us', 'Midsommar'
    ],
    'Sci-Fi': [
        'Inception', 'The Matrix', 'Interstellar', 'Blade Runner 2049', 'Star Wars: A New Hope', 'The Empire Strikes Back',
        'Jurassic Park', 'E.T.', 'Back to the Future', 'Avatar', 'The Fifth Element', 'District 9', 'Arrival', 'Dune', 'Ex Machina'
    ],
    'Romance': [
        'The Notebook', 'Titanic', 'La La Land', 'Pride and Prejudice', 'A Walk to Remember', 'The Fault in Our Stars',
        'Notting Hill', 'When Harry Met Sally', 'Pretty Woman', 'Silver Linings Playbook', 'Me Before You',
        'Love Actually', '500 Days of Summer', 'Crazy, Stupid, Love', 'The Proposal'
    ],
}

# Shuffle movies for each genre to randomize recommendations
for genre in movies_by_genre:
    random.shuffle(movies_by_genre[genre])

# To track the current movie index for each genre
current_movie_index = {genre: 0 for genre in movies_by_genre}

# Function to recommend a movie based on selected genre
def recommend_movie():
    selected_genre = genre_var.get()
    if selected_genre == "":
        messagebox.showwarning("No genre selected", "Please select a genre first.")
        return
    
    movie_list = movies_by_genre.get(selected_genre, [])
    if not movie_list:
        messagebox.showwarning("No recommendations", "No recommendations available for this genre.")
        return

    # Get the current index for the selected genre
    index = current_movie_index[selected_genre]
    recommended_movie = movie_list[index]

    # Update the index to the next movie, looping back to 0 if necessary
    current_movie_index[selected_genre] = (index + 1) % len(movie_list)

    messagebox.showinfo("Recommended Movie", f"We recommend you watch: {recommended_movie}")

# Setting up the Tkinter window
window = tk.Tk()
window.title("Movie Recommendation App")
window.geometry("600x600")
window.configure(bg="black")

# Adding a label
label = tk.Label(
    window,
    text="Select a Genre to Get a Movie Recommendation",
    font=("Helvetica", 16, "bold"),
    fg="white",
    bg="black"
)
label.pack(pady=20)

# Genre options
genre_var = tk.StringVar(value="")  # This will hold the selected genre

# Create radio buttons for each genre
radio_frame = tk.Frame(window, bg="black")
radio_frame.pack(pady=10)
for genre in movies_by_genre.keys():
    radio_button = tk.Radiobutton(
        radio_frame,
        text=genre,
        variable=genre_var,
        value=genre,
        font=("Helvetica", 14),
        fg="white",
        bg="black",
        selectcolor="grey"
    )
    radio_button.pack(anchor='w', padx=20)

# Recommend Button
recommend_button = tk.Button(
    window,
    text="Get Recommendation",
    command=recommend_movie,
    font=("Helvetica", 14, "bold"),
    bg="orange",
    fg="black",
    activebackground="yellow",
    activeforeground="black",
    relief="raised"
)
recommend_button.pack(pady=30)

# Footer label
footer_label = tk.Label(
    window,
    text="Enjoy Your Movie!",
    font=("Helvetica", 14, "italic"),
    fg="grey",
    bg="black"
)
footer_label.pack(side="bottom", pady=10)

# Run the main event loop
window.mainloop()
