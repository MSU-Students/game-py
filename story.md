# Sky Defenders: Terminal Command Protocol (CLI)

**Project Name**: Sky Defenders (Terminal)[cite: 1]
**Genre**: ASCII-Art Tactical Shooter[cite: 1]
**Development Level**: Entry-Level / Beginner[cite: 1]

---

## Project Directory Structure
Optimized for a terminal-based workflow focusing on ASCII rendering and command-line execution.

```text
Sky-Defenders-CLI/
├── src/                         # All Python source code
│   ├── components/              
│   │   ├── projectile.py        # Logic for '|', '*', and 'o' particles
│   │   ├── frame_buffer.py      # Manages the 2D grid matrix
│   ├── core/                    # Engine Core
│   │   ├── engine.py            # Main Loop (Input -> Update -> Render)
│   │   ├── renderer.py          # ANSI escape sequences and grid printing
│   │   └── terminal_setup.py    # Raw mode and non-blocking input setup
│   ├── modules/                 
│   │   ├── wave_manager.py      # Team 4: Difficulty and waves[cite: 1]
│   │   ├── input_handler.py     # Team 1: Movement and boundaries[cite: 1]
│   │   ├── data_persistence.py  # Team 5: User data and scores[cite: 1]
│   │   ├── game_animation.py    # Team 3: ASCII visual effects[cite: 1]
│   │   └── game_story.py        # Team 2: Text-based dialogues[cite: 1]
│   ├── entities/                
│   │   ├── pilot.py             # Player represented by '^A^'[cite: 1]
│   │   └── drone.py             # Enemy and Boss logic[cite: 1]
│   └── main.py                  # THE ENTRY POINT (Run this to play)
├── docs/                        
│   ├── features.md              # List of planned features
│   └── story.md                 # The Technical Specification[cite: 1]
├── .gitignore                   # Tells Git which files to ignore
└── README.md                    # Terminal setup and "Curses" library info
```

---

## Development Team Roles

| Team | Responsibility | Primary Objective |
| :--- | :--- | :--- |
| **Team 1** | **Navigation** | Implement movement mechanics and terminal boundaries[cite: 1]. |
| **Team 2** | **Story** | Manage text dialogue, mission briefings, and narrative flow[cite: 1]. |
| **Team 3** | **Animation/SFX** | Handle ASCII visual feedback and terminal beep triggers[cite: 1]. |
| **Team 4** | **Point System** | Calculate scoring, health depletion, and victory conditions[cite: 1]. |
| **Team 5** | **Profile Mgmt** | Develop user data entry and high-score persistence[cite: 1]. |

---

## 1. Narrative Overview
The peaceful skies are under attack by a rogue fleet[cite: 1]. As the premier pilot of the defense force, you must intercept the invasion, neutralize enemy squadrons, and eliminate the command "Boss" aircraft to restore security to the airspace[cite: 1].

---

## 2. Core Entities
* **Player**: The primary aircraft (`^A^`), positioned at the bottom-center[cite: 1].
* **Enemies**: Automated rogue drones (`<V>`) appearing from the top of the screen[cite: 1].
* **The Boss**: A heavily armored unit (`[== V ==]`) appearing at the conclusion of a stage[cite: 1].
* **Projectiles**: ASCII particles (`|`, `*`) fired by the Player or Enemies[cite: 1].
* **Shield**: A defensive layer absorbing damage before affecting Health[cite: 1].

---

## 3. Stage Specifications

### Easy Stage: "Low Orbit Patrol"
* **Player Configuration**: 10 HP, single-shot (`|`), infinite ammunition[cite: 1].
* **Defensive Layer**: Basic Shield (2 hits), slow regeneration (10s)[cite: 1].
* **Enemy Behavior**: 3 HP, slow speed, linear firing pattern[cite: 1].
* **Boss Encounter**: 15 HP, 5-bullet spread fire pattern[cite: 1].
* **Progression**:
    * **Wave 1**: 5 enemies; passive behavior[cite: 1].
    * **Wave 2**: 9 enemies; linear firing enabled[cite: 1].
    * **Wave 3**: 5 enemies + **Mini-Boss** (10 hits)[cite: 1].
    * **Wave 4**: 15 enemies; swarm formation[cite: 1].
    * **Wave 5**: 10 enemies + **Stage Boss** (15 hits)[cite: 1].

### Medium Stage: "Asteroid Ambush"
* **Player Configuration**: 15 HP, double-shot (`||`), 50-round capacity[cite: 1].
* **Defensive Layer**: Reinforced Shield (5 hits), standard regeneration (5s)[cite: 1].
* **Enemy Behavior**: 5 HP, includes "Kamikaze" drones (`>! <`) targeting player[cite: 1].
* **Boss Encounter**: 25 HP, teleportation mechanic every 5 seconds[cite: 1].
* **Progression**:
    * **Wave 1**: 10 enemies; standard formation[cite: 1].
    * **Wave 2**: 15 enemies; increased aggression[cite: 1].
    * **Wave 3**: 15 enemies + **Mini-Boss** (15 hits; Teleports)[cite: 1].
    * **Wave 4**: 18 enemies; complex movement[cite: 1].
    * **Wave 5**: 20 enemies + **Stage Boss** (25 hits; Orbital Beam)[cite: 1].

### Difficult Stage: "Deep Space Breach"
* **Player Configuration**: 20 HP, 3-way spread (`\ | /`), 30-round capacity[cite: 1].
* **Defensive Layer**: Multi-layer Shield (10 hits), high-speed regeneration[cite: 1].
* **Enemy Behavior**: 8 HP, 2-second "Ghost" (`? ?`) cloaking intervals[cite: 1].
* **Boss Encounter**: 50 HP, deploys "Logic Bomb" (`o`) for control inversion[cite: 1].
* **Progression**:
    * **Wave 1**: 20 enemies; 3-layer protective shielding[cite: 1].
    * **Wave 2**: 25 enemies; 100% speed increase[cite: 1].
    * **Wave 3**: 20 enemies + **Mini-Boss** (Heals nearby units)[cite: 1].
    * **Wave 4**: 30 enemies; fleet saturation[cite: 1].
    * **Wave 5**: 25 enemies + **Stage Boss** (50 hits; Shield recharges)[cite: 1].

---

## 4. Technical Logic for Developers

### **Movement Logic (Team 1)**
The Player moves across the terminal grid using both axes[cite: 1].
* **Input (W/A/S/D)**: Update grid coordinates[cite: 1].
* **Boundary Lock**: Prevent the Player from exceeding terminal width or height[cite: 1].

### **Collision & Health (Team 4)**
* **Damage Priority**: Decrease **Shield HP** first[cite: 1].
* **Health Depletion**: If Shield is `0`, decrease **Player Health** by 1[cite: 1].
* **Entity Removal**: At `0` Health, trigger ASCII "Explosion" (`#`) and remove[cite: 1].

### **Progression & Recovery (Team 4 & 5)**
* **Wave Recovery**: When `active_enemy_count` hits `0`, restore Health/Shield to Max[cite: 1].
* **Stage Transition**: Completing Wave 5 increases `base_health_max` and `shield_hp_max`[cite: 1].
* **Full Reset**: Set current Health/Shield to new maximums before next stage[cite: 1].

### **Wave Sequencing (Team 2 & 4)**
* **Monitoring**: Continuously track `active_enemy_count`[cite: 1].
* **Recovery Delay**: Initiate 2-second pause for recovery visuals before next spawn[cite: 1].
* **Mission Complete**: Trigger "Peace Restored" after final Boss falls[cite: 1].</V>
