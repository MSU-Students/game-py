# Sky Defenders: Technical Specification & Project Roadmap

**Project Name**: Sky Defenders  
**Genre**: Action / Arcade Shooter  
**Development Level**: Entry-Level / Beginner  

---

## Project Directory Structure
For a professional and organized workflow, the project should be structured as follows:
```text
Sky-Defenders/
├── assets/                  # Non-code files
│   ├── animations/          # Folders for frame-by-frame images
│   └── sounds/              # Audio files for shots and explosions
├── src/                     # All Python source code
│   ├── components/          # Small building blocks
│   │   ├── amo.py           # Projectile logic
│   │   ├── element.py       # Base class for all game objects
│   │   └── animation_frame.py
│   ├── core/                # The "Brain" of the game
│   │   ├── game.py          # Main game loop and state management
│   │   ├── screen.py        # Window and display settings
│   │   └── utils.py         # Helper functions
│   ├── modules/             # Team-specific logic files
│   │   ├── game_animation.py  # Team 3: Visual effects logic
│   │   ├── game_levels.py     # Team 4: Difficulty and waves
│   │   ├── game_navigation.py # Team 1: Movement and boundaries
│   │   ├── game_profile.py    # Team 5: User data and scores
│   │   └── game_story.py      # Team 2: Dialogues and cutscenes[cite: 1]
│   ├── entities/            # Game characters
│   │   ├── player.py        # Player-specific logic[cite: 1]
│   │   └── enemy.py         # Enemy and Boss logic[cite: 1]
│   └── main.py              # THE ENTRY POINT (Run this to play)
├── docs/                    # Documentation
│   ├── features.md          # List of planned features
│   └── story.md             # The Technical Specification[cite: 1]
├── .gitignore               # Tells Git which files to ignore
└── README.md                # Project overview and how-to-run
```

---

## Development Team Roles

| Team | Responsibility | Primary Objective |
| :--- | :--- | :--- |
| **Team 1** | **Navigation** | Implement movement mechanics and screen boundaries[cite: 1]. |
| **Team 2** | **Story** | Manage dialogue, mission briefings, and narrative flow[cite: 1]. |
| **Team 3** | **Animation/SFX** | Handle visual feedback and audio triggers for game events[cite: 1]. |
| **Team 4** | **Point System** | Calculate scoring, health depletion, and victory conditions[cite: 1]. |
| **Team 5** | **Profile Mgmt** | Develop user data entry and high-score persistence[cite: 1]. |

---

## 1. Narrative Overview
The peaceful skies are under attack by a rogue fleet[cite: 1]. As the premier pilot of the defense force, you must intercept the invasion, neutralize enemy squadrons, and eliminate the command "Boss" aircraft to restore security to the airspace[cite: 1].

---

## 2. Core Entities
*   **Player**: The primary aircraft controlled by the user, positioned at the bottom-center[cite: 1].
*   **Enemies**: Automated rogue aircraft appearing from the top of the screen[cite: 1].
*   **The Boss**: A heavily armored, high-health unit appearing at the conclusion of a stage[cite: 1].
*   **Projectiles**: Ammunition fired by the Player or Enemies[cite: 1].
*   **Shield**: A defensive layer that absorbs incoming damage before affecting health[cite: 1].

---

## 3. Stage Specifications

### Easy Stage
*   **Player Configuration**: 10 HP, single-shot weapon, infinite ammunition[cite: 1].
*   **Defensive Layer**: Basic Shield (2 hits), slow regeneration (10s)[cite: 1].
*   **Enemy Behavior**: 3 HP, slow movement speed, linear firing pattern[cite: 1].
*   **Boss Encounter**: 15 HP, 5-bullet spread fire pattern[cite: 1].
*   **Progression (Key Sequencing)**:
    *   **Wave 1 (Level Start)**: 5 enemies; passive behavior (cannot shoot projectiles)[cite: 1].
    *   **Wave 2**: 9 enemies; standard linear firing patterns enabled[cite: 1].
    *   **Wave 3**: 5 enemies accompanied by a **Mini-Boss** (10 hits)[cite: 1].
    *   **Wave 4**: 15 enemies; high-density swarm formation[cite: 1].
    *   **Wave 5 (Final)**: 10 enemies and the **Stage Boss** (15 hits)[cite: 1].

### Medium Stage
*   **Player Configuration**: 15 HP, double-shot weapon, 50-round capacity[cite: 1].
*   **Defensive Layer**: Reinforced Shield (5 hits), standard regeneration (5s)[cite: 1].
*   **Enemy Behavior**: 5 HP, includes "Kamikaze" units that target player position[cite: 1].
*   **Boss Encounter**: 25 HP, teleportation mechanic every 5 seconds[cite: 1].
*   **Progression (Key Sequencing)**:
    *   **Wave 1**: 10 enemies; standard formation patrol[cite: 1].
    *   **Wave 2**: 15 enemies; increased aggression and faster movement[cite: 1].
    *   **Wave 3**: 15 enemies accompanied by a **Mini-Boss** (15 hits; utilizes Teleportation)[cite: 1].
    *   **Wave 4**: 18 enemies; complex movement maneuvers[cite: 1].
    *   **Wave 5 (Final)**: 20 enemies and the **Stage Boss** (25 hits; utilizes Orbital Beam)[cite: 1].

### Difficult Stage
*   **Player Configuration**: 20 HP, 3-way spread shot, 30-round capacity[cite: 1].
*   **Defensive Layer**: Multi-layer Shield (10 hits), high-speed regeneration[cite: 1].
*   **Enemy Behavior**: 8 HP, incorporates 2-second "Ghost" cloaking intervals[cite: 1].
*   **Boss Encounter**: 50 HP, deploys "Logic Bomb" for control inversion[cite: 1].
*   **Progression (Key Sequencing)**:
    *   **Wave 1**: 20 enemies; units equipped with 3-layer protective shielding[cite: 1].
    *   **Wave 2**: 25 enemies; movement speed increased by 100%[cite: 1].
    *   **Wave 3**: 20 enemies accompanied by a **Mini-Boss** (Heals nearby Elite units)[cite: 1].
    *   **Wave 4**: 30 enemies; final fleet saturation invasion[cite: 1].
    *   **Wave 5 (Final)**: 25 enemies and the **Stage Boss** (50 hits; Shield recharges every 3s)[cite: 1].

---

## 4. Technical Logic for Developers

### **Movement Logic (Team 1)**
The Player now has full freedom of movement across the screen using both axes[cite: 1].
*   **Horizontal Axis (X)**:
    *   **Input Left**: Decrease X-coordinate to move toward the left boundary[cite: 1].
    *   **Input Right**: Increase X-coordinate to move toward the right boundary[cite: 1].
*   **Vertical Axis (Y)**:
    *   **Input Up**: Decrease Y-coordinate to move toward the top of the screen[cite: 1].
    *   **Input Down**: Increase Y-coordinate to move toward the bottom of the screen[cite: 1].
*   **Boundary Lock**: The system must prevent the Player from moving off-screen by checking that X is between `0` and `Screen_Width`, and Y is between `0` and `Screen_Height`[cite: 1].

---

### **Collision & Health (Team 4)**
Every entity must track integer variables for Health and Shield points to manage durability[cite: 1].
*   **Damage Priority**: Upon detection of a collision between a Projectile and the Player, the system must decrease **Shield HP** first[cite: 1].
*   **Health Depletion**: If the Shield HP is `0`, the system decreases **Player Health** by 1 per hit[cite: 1].
*   **Entity Removal**: When an entity's Health reaches `0`, the "Explosion" event is triggered, and the entity is removed from the game world[cite: 1].

---

### **Progression & Recovery (Team 4 & 5)**
The game rewards survival through a "Full Recovery" and "Attribute Growth" system to ensure the Player is prepared for escalating difficulty[cite: 1].
*   **Wave Completion Recovery**: When the `active_enemy_count` reaches `0` at the end of any wave, the Player’s current Health and Shield are immediately restored to their Maximum values[cite: 1].
*   **Stage Transition / Level Up**: When a player completes Wave 5 (Final) of a stage:
    *   **Max HP Increase**: The `base_health_max` variable is increased (e.g., Easy 25 HP → Medium 30 HP)[cite: 1].
    *   **Shield Upgrade**: The `shield_hp_max` is increased, and the `shield_regen_rate` is improved (e.g., 3s → 2s)[cite: 1].
    *   **Full Reset**: Current Health and Shield are set to these new higher maximums before the next stage starts[cite: 1].

---

### **Wave Sequencing (Team 2 & 4)**
The game flow is automated by monitoring the battlefield state[cite: 1].
*   **Active Monitoring**: The engine continuously tracks the `active_enemy_count`[cite: 1].
*   **Recovery Delay**: When the count reaches `0`, a 2-second "Recovery Delay" is initiated to allow for visual HP/Shield restoration before the next wave list spawns[cite: 1].
*   **Mission Complete**: If the `active_enemy_count` reaches `0` on Wave 5 of the Difficult stage, the system triggers the "Peace Restored" end-game sequence[cite: 1].
