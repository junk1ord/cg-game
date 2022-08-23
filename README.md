# Computer Graphics
## Minor Project

---

The main highlight of this project is a 2D game visualization. There are many such 2D animation games present in the market at the moment, many of them quite widespread across the globe. My intent was to recreate a small simulation or snippets of one such game in my own version.

This game was programmed in Python environment. A dedicated library for creating such games in Python, called the ‘Pygame’ library was used here. Pygame is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language. Pygame is highly portable and runs on nearly every platform and operating system.

The game involves two characters, a player controlled by the user and an automated enemy character. There is a score counter which increments upon every hit taken by the enemy. This is a rather basic implementation of any 2D game like Mario or Flappy Bird, meaning some features taken from both games and merged into one small, compressed version.

---

### Brief Introduction 

Since the advent of the early consoles like the Mitashi consoles and the Nintendo consoles, 2D games saw a massive explosion in the popularity and demand. Many games on these two platforms were unofficially on the list of the Hall of Fame for many gaming communities. The current games like Mario series, the Contra series or Flappy Bird are the adaptations of their previous 2D versions, early introduced in the aforementioned consoles. This project was an attempt to study and recreate some of the features of these classic games. It implements scenarios like movement, automovements, shooting projectiles – or in simpler words, bullets, collision between character and objects, character and character and a live score counter. This games was developed in python. A dedicated library called the Pygame library was administered here. Pygame is fairly low-level when it comes to writing games. One will quickly find themselves needing to wrap common functions into their own game environment. The great thing about this is there is nothing inside pygame to get in their way. Their program is in full control of everything. Python uses the fundamentals of Object Oriented Programming. Python also retains the inheritance mechanism of Object Oriented Programming. Hence, every entity in this game is an object. The character we play and control is an object, so is the enemy, and the bullet projectiles that the character shoots. 

---

### Methodology

Three objects are needed here, the player, the enemy and the bullets. Hence, three objects were declared as such, along with respective attributes.

### Character Movement

The module to work with the keyboard is called the ‘key’ module. Within this module, there exists a function called ‘get_pressed’. As the name suggests, it updates a Boolean TRUE value for the key which is pressed in an array, while the rest get FALSE value in the same array. With this, an array, ‘keys’ was defined as: 

```python
keys = pygame.key.get_pressed()
```

The key binds are:

| Key | Function |
| ----------- | ----------- |
| W | Makes the Character jump |
| A | Makes the character move left |
| D | Makes the character move right |
| SPACE | Shoots bullets from the character |

---

The character has 9 sprites defined for both right movements as well as left side. Each sprite lasts 3 frames and hence the Frames Per Second number of the character is 27. For the enemy, there are 11 sprites defined for both right movements as well as left side. Each sprite lasts 3 frames and hence, the Frames Per Second or the FPS number of the enemy is 33. The player can move anywhere across the screen. It jumps in a parabolic fashion, that is, the player velocity decreases till it reaches its apex on top, velocity reaches zero, and starts increasing again, till the player reaches the ground level back. The player is also allowed to move within 5 pixel boundaries of the entire window, in the x direction. The enemy character moves within a fix set of coordinates, alternating its path of traversal once it reaches any boundaries specified. In gaming terminology, this path is called the enemy’s fixed ‘Patrol Route’.

---

### Bullets

The bullets eject out of the approximate centre of the player. They are under the constraint that at one time, only 5 bullets are allowed on the window to ensure that bullets aren’t spammed constantly.   

There are two ways in which the bullets disappear off the window:
1. If the bullet touches the window boundaries
2. If the bullet hits the enemy character. In this case, the score counter increases by one.

---

### Collisions

The condition of collision occurs only if the hitbox attributes of both the character and the enemy touch or intersect. 
```py
if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
  if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
    man.hit()
```

This results in the trigger of the ‘hit’ method described in the player’s object, resulting in a collision and a deduction in the total score by 5. The game freezes in the same condition and a message indicating the collision is displayed. The conditions reset themselves again back to the original setting.   

---

### Refreshing the Window

Every action in this game is executed frame by frame. Every action, interception, ejection or any other activity carried out here is per the frame in which the game currently is in. This means that, to update the results, the screen has to be refreshed with the new frame. That is, the game basically “runs” as the frames are updated after each action. 

In the main loop of the game, the run loop, the function `redrawGameWindow()` is called at the very end, to refresh and redraw the game window after all actions are performed.

This method involves:

```py
def redrawGameWindow():
  win.blit(bg, (0,0))
  text = font.render('SCORE: ' + str(score), 1, (0,0,0))
  win.blit(text, (310, 10))
  man.draw(win)
  goblin.draw(win)
  for bullet in bullets:
    bullet.draw(win)
  pygame.display.update()
```

The `win.blit` function restores the background. The text variable is a method which renders the correct score, and the `win.blit` function displays the text on the specified location. The `man.draw` method redraws the man again, so does the `goblin.draw`, the enemy. The `bullet.draw` function redraws the bullet. Finally, the `pygame.display.update()` method refreshes the entire window.
