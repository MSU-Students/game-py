# USER STORY: Player and Enemy System

## Player Character: "CAPTAIN AIDEN"

As the main character, **Aiden**,  
I want to move, and fight enemies,  
so that I can survive and complete my journey.

### Abilities:
- Aiden can move left and right
- Aiden can attack using a basic strike
- Aiden can collect items (power-ups)
- Aiden has health points (HP)

### Stats:
- HP: 100
- Movement Speed: Normal

---

## Enemy Character: "Raven Stalker"

As an enemy unit, **Raven Stalker**,  
I want to detect and attack the player,  
so that I can challenge their progress.

### Behavior:
- Raven Stalker patrols a fixed area
- It will try to shot the player
- It attacks when in range
- It stops when defeated

### Stats:
- HP: 50
- Speed: Slightly faster than player

---

## Interaction System

- When Aiden touches Raven Stalker → Aiden loses HP
- When Aiden attacks Raven Stalker → enemy loses HP
- When enemy HP reaches 0 → Raven Stalker disappears
- When Aiden HP reaches 0 → Game Over screen appears

---

## Win Condition
- Defeat all enemies in the level
- Survive until the end of the stage