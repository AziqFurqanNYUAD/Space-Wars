# Space Wars

**Space Wars** is an arcade-style space game developed in Python using the Processing framework (Python Mode). The player controls a spaceship in a field of falling asteroids and collectibles. The project showcases basic game development concepts like animation, collision detection, user input, and simple power-up mechanics in the Processing environment. It serves as a demonstrative example of using Processing’s Python mode for interactive graphics and game development.

## Purpose

This project was created as an educational and demonstrative game. It illustrates how to build a simple 2D game using Processing’s Python Mode – combining Python programming with Processing’s visual capabilities. The code is organized to help developers (especially beginners) understand game loops, sprite handling, collision logic, and incorporating sound in a Processing.py sketch. **Space Wars** can be a learning tool for those who want to explore creative coding or start developing games in Python within the Processing IDE.

## Features

* **Classic Space Theme**: Top-down view of a spaceship with a continuously scrolling starfield background. The background alternates between two images (normal and inverted colors) to create a seamless looping effect.
* **Player Spacecraft**: A spaceship sprite (`trek.png`) that the player moves horizontally across the screen. It is rendered with a thruster (booster) graphic, giving the feel of a starship cruising through space.
* **Asteroid Obstacles**: Asteroids (`meteor.png` sprites) fall from the top of the screen. They appear one at a time and accelerate gradually as the player’s score increases (every 100 points, asteroids speed up). The player must dodge these; a collision is deadly (ends the game) unless a shield is active.
* **Collectible Items**:

  * *Coins* (`yellowcoin.png`): Appear periodically and fall downward. Each coin collected increases the score (5 points each) and contributes to the player’s point total.
  * *Infinity Stones* (`stone1.png` … `stone4.png`): Four types of gem-like items drop occasionally (one at a time, in random horizontal positions). Collecting each unique stone is key to activating a special power-up. Each stone collected grants 10 points. The game keeps track of which types you’ve collected in the current run (and even displays the collected stone icons on the HUD).
* **Sexa Shield (Power-Up)**: If the player collects all four different stones, the spaceship activates an **invincibility shield** called the “Sexa Shield.” A glowing ring (`ring.png` sprite) appears around the spaceship when this shield is active. While shielded, the spaceship can survive asteroid hits without game-over. The shield is temporary – it stays active for a limited time (tied to score gain). After activating the shield, if the player earns 15 more points, the shield deactivates. However, the player can collect another full set of 4 stones to re-activate the shield again. This mechanic adds a strategic element: survive long enough to gather power-ups and gain brief invincibility.
* **Scoring System**: The game keeps a running score (displayed on screen) that increases by collecting coins and stones. Surviving longer and grabbing items will yield a higher score. There is a simple on-screen counter (`Counter` class) that updates and shows the score continuously, and it also handles showing the final score on the end screen.
* **Sound and Music**: A background music track (`piano.mp3`) plays in a loop during gameplay to enhance the experience. (This is managed via the Minim audio library in Processing.) There may not be separate sound effects for collisions or item pickups, but the music adds atmosphere.
* **User Interface**:

  * *Start Menu*: When the game launches, it begins with a menu screen. This screen displays the game title and instructions for the player. The title “\~ Sexa Rush \~” is shown with a stylized font (from `Phosphate-Inline-16.vlw`), indicating the name of this space adventure. Below that, the instructions are listed, for example: “1. Use the left and right arrow keys to move your spaceship.” and information about collectibles and the shield. A “PLAY” button is drawn on this menu; the player can click it (or anywhere on the screen) to start the game.
  * *Gameplay Display*: During gameplay, besides the moving sprites, the current score is typically shown. Also, as mentioned, icons of collected infinity stones might be shown on the screen (e.g., in a corner) to indicate progress toward the shield. The shield’s presence (ring graphic around the ship) is a visual indicator of invincibility.
  * *End Screen*: When the game is over (the player’s ship was hit by an asteroid without a shield), an end screen or overlay shows the final score (using a `display_endscreen` method of the Counter). The game likely waits for a click, allowing the player to restart (which will reset the game state for a new run).

Overall, **Space Wars** provides a straightforward but engaging set of features that demonstrate how a small game can be structured in Processing.py. The focus is on dodging obstacles and collecting items rather than shooting, making it a simple avoid-and-collect style arcade game.

## Installation Instructions

To run the game on your local machine, follow these steps:

1. **Install Processing (3.x or 4.x)** – Download and install the Processing IDE from the official website (Processing.org) for your platform. Processing is required to run this project because the game is built as a Processing sketch.

2. **Add Python Mode in Processing** – By default, Processing uses Java. This game is written in Python Mode, so you need to enable that:

   * Launch the Processing IDE.
   * In the Processing editor, find the mode selector in the top-right corner of the window (it might say “Java” initially). Click it, and choose “Add Mode…” from the dropdown.
   * In the Modes listing, look for **“Python Mode for Processing”** and install it. (Processing will download the Python Mode plugin. Once installed, switch the mode to Python by selecting it in that same top-right menu. The editor UI usually changes color or icon to indicate Python Mode is active.)

3. **Download the Space Wars code** – You can clone this repository via Git or download it as a ZIP. Ensure that the folder structure is preserved. The main file is **`Sexarush.pyde`**, which should reside in a folder (sketch folder). If you cloned the repo, you will already have the correct structure.

4. **Open the project in Processing** – In the Processing IDE (with Python mode active), go to **File -> Open** and navigate to the `Sexarush.pyde` file inside the project’s folder (the `Space-Wars` folder you downloaded or cloned). Open this file. This will load the game’s source code into the Processing editor. *(If Processing prompts to rename the folder to match the sketch name, you can allow it or ignore if it’s already correct. The sketch name is “Sexarush”, so the folder name might be adjusted by Processing.)*

5. **Run the game** – Click the **Run** button (the triangular “Play” icon in the Processing IDE toolbar). The sketch will compile and start. A new window will pop up (sized 1000x1000 pixels) which is the game window. You should see the main menu with the title and a “PLAY” button. Click the play button (or anywhere on the window) to start the game.

**Troubleshooting**:

* Make sure you have Processing’s Python Mode properly installed; otherwise, the `.pyde` file won’t run. You can verify this by checking that the editor says “Python” in the mode selector.
* The game uses the Minim library for audio (to play the background music). In Processing (Java mode), Minim is an add-on, but in Python mode using `add_library("minim")` ensures it’s included. If you encounter any audio errors, you might need to install the Minim library via Processing’s Contribution Manager (Sketch -> Import Library -> Add Library, then search for “Minim”). Often, though, Processing comes with Minim by default, or the `add_library` call will handle it.
* All asset files (images and the audio file) should remain in the `data` and `images` subfolders as provided. Processing expects this standard structure (`data/` for media assets) and will load files from there. So if you get errors about files not found, ensure you didn’t rename or move the folders.

Once the game is running, you’re ready to play!

## How to Play

**Basic Controls**:

* **Move the Spaceship** – Use the **Left and Right arrow keys** to steer your spaceship horizontally across the screen. (There is no vertical movement for the player’s ship; the ship stays near the bottom of the screen and can only slide left or right.) Movement is constrained within the window (you can’t go off the edges — the code stops the ship at about 100 pixels from each edge to keep it fully in view).

**Gameplay Objective**:

* **Survive and Score Points** – The main goal is to avoid getting hit by asteroids for as long as possible while racking up points by collecting coins and “Infinity Stones.” There is no shooting mechanism; the challenge comes from dodging obstacles and utilizing the shield power-up effectively.

**Hazards to Avoid**:

* **Asteroids** – Rocks/meteors fall from the top. They have a fairly large size in the game (the meteor sprite is 100x200 pixels in dimension when drawn). Asteroids fall one at a time (as soon as one goes off screen or is dodged, the next one will spawn). As your score increases, asteroids will start falling faster (every 100 points the fall speed increases a bit). **If an asteroid hits your spaceship when you do not have an active shield, your ship is destroyed and the game ends**. You’ll then see your final score and can restart the game. So, dodging asteroids is critical at all times when unshielded.

**Items to Collect**:

* **Coins** – Small yellow coin icons will occasionally drop from the top, moving straight down. Each coin you catch is worth **5 points**. Collecting coins not only increases your score but can also indirectly help your survival by speeding up how quickly you reach the threshold for shield duration (see below). Coins appear one at a time and if missed (fall off the bottom) they will respawn later at a new random position. There’s no penalty for missing a coin, aside from the lost scoring opportunity.

* **Infinity Stones (Gems)** – These are special collectibles represented by four different colored gem icons (`stone1.png`, `stone2.png`, `stone3.png`, `stone4.png`). In the game’s story, you need to gather these “infinity stones” to activate a powerful shield. Stones drop from the top like coins (one at a time, at random positions) but less frequently. Each stone collected gives **+10 points** and is added to your collection if it’s a new type. The HUD displays which stones you’ve collected so far (by showing their icons, typically on the side of the screen). If you catch a duplicate stone (one you already collected in the current round), it still gives points but won’t count toward the set of four (the code checks and only adds to the collection if it’s not already collected). Try to collect all four unique stones!

* **Power-Up: Sexa Shield** – Once you have **all 4 different stones**, your ship’s **invincibility shield activates** automatically. You will see a bright ring graphic appear around your spaceship, indicating the **Sexa Shield** is on. While the shield is active, you can collide with asteroids safely – they will no longer end the game upon impact (essentially, you’re invulnerable to asteroids for a time). This gives you a breather to collect more points. Note: The shield does *not* make you invincible to everything; its main purpose is to protect against the asteroids. (Colliding with an asteroid while shielded might just let the asteroid pass through or reset it without harm to you – the specifics of the effect are simple: the game just doesn’t set Game over if shield is true.)

* **Shield Duration** – The Sexa Shield doesn’t last forever. The duration is tied to your score: specifically, once you’ve gained **15 points** *after* the shield was activated, the shield will turn off. In practice, this means you’ll remain invincible for a short while as you collect points (for example, you could collect a few coins or even another stone while shielded, but once 15 points have been accumulated beyond the activation point, the shield disappears). The game code uses this method to approximate a time limit for the shield. After the shield deactivates, you lose the ring graphic and are vulnerable to asteroids again. However, **you can re-activate the shield** by *collecting another full set of all 4 unique stones* again in that same run. The collection for shield resets once it activates (the game clears the collected list after giving you the shield, so you can start collecting afresh). This means the longer you survive, you could potentially get multiple shields. It becomes a cycle: survive -> collect gems -> gain shield -> use shield to survive longer -> shield expires -> collect gems again, etc. Using the shield wisely (for example, maybe taking advantage of the invincibility to grab hard-to-reach coins or to not worry about one asteroid) can improve your chances of a high score.

**Heads-Up Display (HUD)**:

* During gameplay, you’ll see your **Score** displayed (likely at the top of the screen in a clear font, provided by `PTMono-Regular-16.vlw`). The score updates in real-time as you collect items.
* The game may display small icons of the collected stones (often on a side of the screen, possibly the top-left). These serve to show which stones you’ve gotten so far towards the next shield. For example, if you have collected stone types 1 and 3, you might see those two icons lit up, and the slots for 2 and 4 empty. In the code, this is handled by drawing each collected stone’s image in a little list, and even drawing a rectangle border around them as a container. This helps you keep track of progress toward the power-up.
* When the shield is active, the **ring graphic** around the ship is the primary indicator. There isn’t a specific timer bar or count for the shield on the HUD, so you need to be mindful of roughly how many points you’ve scored since it turned on (or just be cautious once you’ve had it for a while). The shield ring disappears when it deactivates.

**Game Over and Restart**:

* If your ship gets hit by an asteroid while you have **no shield**, the game will set `Game = False` which triggers the end condition. Typically, the gameplay stops and an end screen or overlay will appear. The end screen (often just the same window displaying text) will show something like “Game Over” or “Your Score: \[score]”. In this project, the `Counter.display_endscreen(x, y)` method is likely used to display the final score at a certain position on the screen when the game ends.
* To play again, the game listens for a mouse click on the end screen. The code sets up that if the mouse is pressed after game over, it resets the game state: it puts you back to the start menu (by setting `Select = True` and `Game = True` again). In simpler terms, **click the mouse** to return to the main menu or restart. From the main menu, click “PLAY” to begin a new round. This allows continuous play-testing without restarting the program each time.

Enjoy playing **Space Wars (Sexa Rush)**, and see how high of a score you can achieve!

## Project Structure

The repository is organized as a typical Processing project. Notable files and directories:

```plaintext
Space-Wars/
├── Sexarush.pyde          # Main game code (Processing Python Mode sketch file)
├── data/                  # Data folder for media assets required by the game
│   ├── piano.mp3                  # Background music track (loaded via Minim)
│   ├── Phosphate-Inline-16.vlw    # Font file for the game title text (custom font)
│   └── PTMono-Regular-16.vlw      # Font file for in-game text (score, instructions)
├── images/                # Images folder for all sprite and background graphics
│   ├── bg.jpeg                 # Background image for the menu screen
│   ├── bg_space.jpg            # Main game background image (star field)
│   ├── bg_space_invert.jpg     # Inverted-color background image (used to alternate for scrolling)
│   ├── trek.png                # Spaceship sprite (the player’s ship)
│   ├── meteor.png              # Asteroid sprite (the obstacle to avoid)
│   ├── yellowcoin.png          # Coin sprite (collectible item for score)
│   ├── ring.png                # Shield effect sprite (drawn around the ship when shield is active)
│   ├── stone1.png              # Infinity Stone sprite 1 (collectible towards shield)
│   ├── stone2.png              # Infinity Stone sprite 2
│   ├── stone3.png              # Infinity Stone sprite 3
│   └── stone4.png              # Infinity Stone sprite 4
└── sketch.properties      # Processing sketch configuration file (specifies the use of Python Mode)
```

A brief overview of the key files:

* **Sexarush.pyde**: This is the main source code of the game. It contains all the classes and logic (within a single file, as is common for small Processing sketches). Key components defined in this file include:

  * *Background* class: Manages the scrolling background images (bg\_space.jpg and bg\_space\_invert.jpg), moving them and resetting positions to create an endless loop.
  * *SpaceShip* class: Represents the player’s ship. Handles drawing the ship sprite, movement input (left/right), and the collision logic with asteroids. It also checks the `Power_Up.turbo` flag to decide if the shield ring should be displayed and if collisions should end the game or be ignored.
  * *Obstacles* class: Controls the asteroid (meteor) generation and movement. It spawns a meteor at a random x position when no meteor is currently on screen, moves it downward each frame, and resets it when it leaves the screen or when conditions require. It also increases the fall speed based on score milestones.
  * *Coins* class: Spawns coins occasionally and moves them down. If collected by the ship, it increments the score and flags the coin to respawn later.
  * *Power\_Up* class: Manages the infinity stone drops and the shield activation. It keeps track of which stones have been collected in a list and sets the `turbo` (shield active) state when the collection is complete. It also handles dropping a new stone and resetting after one falls off screen or is collected.
  * *Counter* class: Manages the player’s score and handles displaying the score and the end-of-game score. It has methods to increment the score and to draw the score on the screen. It likely also zeroes the score on game reset.
  * Processing standard functions: `def setup():` to initialize game state (window size 1000x1000, load assets, create initial objects); `def draw():` which is the main loop executed every frame, handling game state logic (menu vs game vs end), calling all update and display methods each frame. Also, `def keyPressed()` and `def keyReleased()` to handle setting the movement flags when the user presses/releases the arrow keys. Mouse click handling for the menu “PLAY” button is implemented (detecting if the mouse click was on the button area to start the game), as well as using mouse press on game over to reset.
* **data/**: This folder is required by Processing to store media. The `.vlw` files are bitmap fonts generated by Processing (or pre-converted) – the code uses `loadFont()` to load these and then sets them for drawing text. The `piano.mp3` is loaded and played via the Minim audio library (the code calls `player = Minim(this)` and then uses `player.loadFile(...).loop()` to start the music.
* **images/**: Contains all the PNG/JPEG image assets:

  * **Backgrounds**: `bg.jpeg` is used on the menu (the code references `self.bg` for the menu background). `bg_space.jpg` and its inverted variant are used in-game for the scrolling starfield.
  * **Sprites**: `trek.png` is the spaceship image loaded for the player. `meteor.png` is the asteroid image loaded for obstacles. `yellowcoin.png` is the coin icon. The four `stone#.png` images represent the collectible gems; the code picks a random one when spawning a new gem. `ring.png` is the visual effect for the shield; drawn double-sized around the ship when shield is on.
  * **booster.png**: It appears in the repository but interestingly, the code references for “booster” actually relate to the gem images (perhaps a naming confusion). The `Power_Up` class uses `self.booster_img` to refer to the current stone image dropping. The file `booster.png` might not be explicitly used in the code (or it could have been intended as an alternate sprite for something like a thruster flame or a different power-up that wasn’t implemented). It’s listed in the repository but I did not see a direct reference in the code for `booster.png`. It’s possible it’s an unused asset or meant for a future feature.
* **sketch.properties**: This is a small config file automatically generated by Processing for the sketch. In this case, it simply notes that the sketch is using Python Mode (with the mode identifier for Processing.py). You typically won’t need to edit this; it’s mainly for Processing’s internal use. It’s checked into the repo likely just to ensure that if someone opens the sketch, it opens in the correct mode.

Developers looking at this structure can navigate the code in `Sexarush.pyde` to see how these components work together. It’s a single-file game for simplicity, but logically separated into classes and sections.

## Contributors

* **Aziq Furqan** – Creator and Developer of *Space Wars (Sexa Rush)*.
  *Credit:* This project was developed by Aziq as part of an academic or hobby endeavor at NYU Abu Dhabi (as indicated by the handle). All game design, coding, and assets assembly in the repository were done by them. If you use this code or build upon it, please attribute the original author.




