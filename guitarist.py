import random


class Guitarist: 
    def __init__(self, name, guitarist_class, guitar=None, crew=None, energy=50, rage=0):
        self.name = name
        self.guitarist_class = guitarist_class
        self.guitar = guitar
        self.crew = crew
        self.energy = energy
        self.rage = rage
        self.is_wasted = False

    def __repr__ (self):
        if self.name == 'Eddie Van Halen':
            return "Eddie Van Halen, the Shredder Virtuoso, a master of speed and technique, always ready to unleash mind-blowing solos. With his unparalleled skill, Eddie Van Halen unleashes devastating attacks like the electrifying Lightning Lick, the furious Tapping Fury, and the iconic Van Halen Dive Bomb."
        elif self.name == 'Slash':
            return "Slash, the Riff Master, oozes cool with his iconic top hat and legendary riffs that define rock 'n' roll. Slash commands the stage with his powerful Power Chord Slam, soulful Bluesy Bend, and the precise, cool Gunslinger Solo that leaves audiences in awe."
        elif self.name == 'Tony Iommi':
            return "Tony Iommi, the Doom Metal Master, brings the darkness with heavy, earth-shaking riffs that reverberate through the soul. Tony Iommi crafts dark and heavy sounds with his crushing Sabbath Chug, the thunderous Doom Drop, and the relentless Eternal Riff that echo through the ages."
        elif self.name == 'Kirk Hammett':
            return "Kirk Hammett, the Thrash Lord, wields his guitar like a weapon, delivering relentless and aggressive thrash metal assaults. Kirk Hammett dominates the thrash scene with his aggressive Whiplash Strike, the relentless Tremolo Assault, and the mighty Hammett Hammer that devastates all in its path."
        elif self.name == 'Dimebag Darell':
            return "Dimebag Darrell, the Groove King, lays down thunderous grooves with unmatched charisma and crushing power. Dimebag Darrell drives the groove with his ground-shaking Groove Bomb, the rhythmic Syncopated Strike, and the crushing Pantera Punch that floors the competition."
        
    
    def status(self):
        print(f"{self.name} stands at {self.energy * 2}% energy, with {self.rage * 2}% rage coursing through his veins. His guitar is {self.guitar.durability * 2 }% durable, and he is {'wasted' if self.is_wasted == True else 'not wasted'}! The crew's mood is at {self.crew.mood * 2}%")

    def gain_energy(self, amount):
        if self.energy < 50:
            self.energy += amount
            if self.energy > 50:
                self.energy = 50
        else :
            self.energy = 50

    def lose_energy(self, amount):
        if self.energy == 50:
            self.energy -= amount / 4
        elif 25 <= self.energy < 50:
            self.energy -= amount / 2    
        else:
            self.rage -= amount
            if self.energy <= 0:
                self.energy == 0

    def gain_rage(self, amount):
        if self.rage < 50:
            self.rage += amount
            if self.rage > 50:
                self.rage = 50
        else :
            self.rage = 50

    def lose_rage(self, amount):
        if self.rage == 50:
            self.rage -= amount / 4
        elif 20 <= self.rage < 50:
            self.rage -= amount / 2
        else:
            self.rage -= amount  
            if self.rage <= 0:
                self.rage == 0          


class Guitarist_class:
    def __init__(self, guitarist_class):
        self.guitarist_class = guitarist_class

    def attack_move(self, attacker, target):
        if self.guitarist_class == 'Shredder Virtuoso':    
            attack = random.randint(1, 3)
            if attack == 1:
                print(f"{attacker.name} unleashes a blistering Lightning Lick, electrifying the crowd and rattling his {target.name} nerves!")

                lose_energy_target = 10 if attacker.is_wasted else 15
                gain_rage_target = 8
                guitar_less_durability_attacker = 10 if attacker.is_wasted else 5
                gain_rage_attacker = 10 if attacker.is_wasted else 5

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 2:
                print(f"With fingers flying, {attacker.name} delivers a Tapping Fury that overwhelms {target.name}, cranking up the tension!")

                lose_energy_target = 15 if attacker.is_wasted else 20
                gain_rage_target = 10
                guitar_less_durability_attacker = 12 if attacker.is_wasted else 7
                gain_rage_attacker = 12 if attacker.is_wasted else 10

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 3:
                print(f"{attacker.name} goes all out with a Van Halen Dive Bomb, sending shockwaves through the arena and into {target.name}'s soul!")

                lose_energy_target = 18 if attacker.is_wasted else 25
                gain_rage_target = 15
                guitar_less_durability_attacker = 15 if attacker.is_wasted else 10
                gain_rage_attacker = 17 if attacker.is_wasted else 15

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

        elif self.guitarist_class == 'Riff Master':
            attack = random.randint(1, 3)
            if attack == 1:
                print(f"{attacker.name} delivers a devastating Power Chord Slam, shaking the stage and knocking the wind out of {target.name}!")
                
                lose_energy_target = 10 if attacker.is_wasted else 15
                lose_rage_target = 10
                guitar_less_durability_attacker = 10 if attacker.is_wasted else 5
                gain_rage_attacker = 10 if attacker.is_wasted else 8

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 2:
                print(f"{attacker.name} bends the blues into his strings, calming the storm as {target.name}'s rage begins to fade away.")    
                
                lose_energy_target = 12 if attacker.is_wasted else 18
                lose_rage_target = 12
                guitar_less_durability_attacker = 12 if attacker.is_wasted else 10
                gain_rage_attacker = 12 if attacker.is_wasted else 18

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()
                
            elif attack == 3:
                print(f"With unmatched precision, {attacker.name} fires off a Gunslinger Solo, subduing {target.name} with sheer coolness!")
                
                lose_energy_target = 18 if attacker.is_wasted else 25
                lose_rage_target = 15
                guitar_less_durability_attacker = 18 if attacker.is_wasted else 10
                gain_rage_attacker = 18 if attacker.is_wasted else 15

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

        elif self.guitarist_class == 'Doom Metal Master':
            attack = random.randint(1, 3)
            if attack == 1:
                print(f"{attacker.name} unleashes a heavy Sabbath Chug, drowning {target.name} in a sea of dark, slow riffs that sap their rage.")
                
                lose_energy_target = 13 if attacker.is_wasted else 15
                lose_rage_target = 8
                guitar_less_durability_attacker = 8 if attacker.is_wasted else 4
                gain_rage_attacker = 12 if attacker.is_wasted else 6

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 2:
                print(f"{attacker.name} drops the hammer with a Doom Drop, crushing {target.name}'s spirit under a wall of sound")    

                lose_energy_target = 18 if attacker.is_wasted else 20
                lose_rage_target = 14
                guitar_less_durability_attacker = 14 if attacker.is_wasted else 7
                gain_rage_attacker = 18 if attacker.is_wasted else 15

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 3:
                print(f"{attacker.name} plays an Eternal Riff that seems to last forever, draining the last drops of fight from {target.name}!")

                lose_energy_target = 23 if attacker.is_wasted else 25
                lose_rage_target = 16
                guitar_less_durability_attacker = 18 if attacker.is_wasted else 14
                gain_rage_attacker = 12 if attacker.is_wasted else 8

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()    

        elif self.guitarist_class == 'Groove King':
            attack = random.randint(1, 3)
            if attack == 1:
                print(f"{attacker.name} drops a Groove Bomb, shaking the ground and mellowing out {target.name}'s rage.")

                lose_energy_target = 10 if attacker.is_wasted else 12
                lose_rage_target = 9
                guitar_less_durability_attacker = 10 if attacker.is_wasted else 6
                gain_rage_attacker = 8 if attacker.is_wasted else 6

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 2:
                print(f"{attacker.name} syncs up with the rhythm, landing a Syncopated Strike that cools {target.name}'s fire.")

                lose_energy_target = 14 if attacker.is_wasted else 18
                lose_rage_target = 10
                guitar_less_durability_attacker = 15 if attacker.is_wasted else 12
                gain_rage_attacker = 15 if attacker.is_wasted else 12

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 3:
                print(f"{attacker.name} delivers a crushing Pantera Punch, knocking the fight right out of {target.name}!")

                lose_energy_target = 18 if attacker.is_wasted else 25
                lose_rage_target = 16
                guitar_less_durability_attacker = 16 if attacker.is_wasted else 14
                gain_rage_attacker = 18 if attacker.is_wasted else 22

                target.lose_energy(lose_energy_target)
                target.gain_rage(lose_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage -{lose_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()        

        elif self.guitarist_class == 'Thrash Lord':
            attack = random.randint(1, 3)
            if attack == 1:
                print(f"{attacker.name} slashes through the air with a Whiplash Strike, driving {target.name} into a frenzied rage!")

                lose_energy_target = 12 if attacker.is_wasted else 18
                gain_rage_target = 14
                guitar_less_durability_attacker = 9 if attacker.is_wasted else 7
                gain_rage_attacker = 11 if attacker.is_wasted else 9

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 2:
                print(f"{attacker.name} launches a relentless Tremolo Assault, pushing {target.name} to the edge with sheer speed!")

                lose_energy_target = 16 if attacker.is_wasted else 20
                gain_rage_target = 14
                guitar_less_durability_attacker = 12 if attacker.is_wasted else 14
                gain_rage_attacker = 18 if attacker.is_wasted else 15

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            elif attack == 3:
                print(f"With a mighty blow, {attacker.name} brings down the Hammett Hammer, leaving {target.name} in a fit of uncontrollable rage!")

                lose_energy_target = 20 if attacker.is_wasted else 26
                gain_rage_target = 18
                guitar_less_durability_attacker = 17 if attacker.is_wasted else 15
                gain_rage_attacker = 14 if attacker.is_wasted else 19

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()       

class Guitar:
    def __init__(self, model, durability=50,):
        self.model = model
        self.durability = durability

    def __repr__(self):
        if self.model == 'Fender Stratocaster':
            return "The Fender Stratocaster, known for its sharp, articulate tones, unleashes the piercing String Bend Scream and the ground-shaking Whammy Dive, leaving opponents reeling."
        elif self.model == 'Gibson Les Paul':
            return "The Gibson Les Paul, a powerhouse of rich, full-bodied sound, delivers the crushing Heavy Chord Crush and the relentless Sustain Monster that overwhelm opponents."
        elif self.model == 'Ibanez JEM':
            return "The Ibanez JEM, crafted for speed and precision, goes wild with the dazzling Fretboard Frenzy and the devastating Shred Storm, cutting through any defense with ease."

    def regain_durability(self, amount):
        self.durability += amount
        if self.durability > 50:
            self.durability = 50

    def less_durability(self, amount):
        self.durability -= amount
        if self.durability < 0:
            self.durability = 0
    
    def guitar_move(self, attacker, target):
        if self.model == 'Fender Stratocaster':
            trick = random.randint(1, 2)
            if trick == 1:
                print(f"The Stratocaster lets out a piercing String Bend Scream, sending shivers down {target.name}'s spine!")

                lose_energy_target = 15
                gain_rage_target = 12
                guitar_less_durability_attacker = 12
                gain_rage_attacker = 13

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status() 

            if trick == 2:
                print(f"The Stratocaster plunges with a Whammy Dive, shaking the arena and rattling {target.name}!")

                lose_energy_target = 18
                gain_rage_target = 14
                guitar_less_durability_attacker = 13
                gain_rage_attacker = 15

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

        elif self.model == 'Gibson Les Paul':
            trick = random.randint(1, 2)
            if trick == 1:
                print(f"The Les Paul delivers a Heavy Chord Crush, overwhelming {target.name} with sheer force!")

                lose_energy_target = 17
                gain_rage_target = 13
                guitar_less_durability_attacker = 13
                gain_rage_attacker = 14

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            if trick == 2:
                print(f"The Les Paul holds a note with its Sustain Monster, filling the air with unrelenting power!")

                lose_energy_target = 19
                gain_rage_target = 14
                guitar_less_durability_attacker = 14
                gain_rage_attacker = 16

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

        elif self.model == 'Ibanez JEM':
            trick = random.randint(1, 2)
            if trick == 1:
                print(f"The Ibanez JEM goes wild in a Fretboard Frenzy, dazzling and disorienting {target.name}!")

                lose_energy_target = 16
                gain_rage_target = 14
                guitar_less_durability_attacker = 13
                gain_rage_attacker = 15

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

            if trick == 2:
                print(f"The Ibanez JEM unleashes a Shred Storm, cutting through {target.name}'s defenses with sheer speed!")

                lose_energy_target = 10
                gain_rage_target = 16
                guitar_less_durability_attacker = 15
                gain_rage_attacker = 19

                target.lose_energy(lose_energy_target)
                target.gain_rage(gain_rage_target)
                attacker.guitar.less_durability(guitar_less_durability_attacker)
                attacker.gain_rage(gain_rage_attacker)

                print(f"{target.name}: energy -{lose_energy_target}, rage +{gain_rage_target}")
                print(f"{attacker.name}: guitar durability -{guitar_less_durability_attacker}, rage +{gain_rage_attacker}")
                attacker.status()
                target.status()

class Crew:
    def __init__(self, crew_class, guitarist=None, mood=50):
        self.crew_class = crew_class
        self.guitarist = guitarist
        self.mood = mood 

    def __repr__(self):
        if self.crew_class == 'Tech Crew':
            return "The Tech Crew, masters of the backstage, keep the show running smoothly with essential Gear Maintenance and swift Quick Fixes, ensuring guitars stay durable while keeping their crew in high spirits and slightly unsettling the opposition."
        elif self.crew_class == 'Manager':
            return "The Manager, the mastermind behind the scenes, boosts the crew's morale with a Strategic Boost and handles Conflict Resolution like a pro, increasing their guitarist’s rage and keeping the competition on edge, even nudging the opponent towards being wasted."
        elif self.crew_class == 'Fan Club':
            return "The Fan Club, ever-enthusiastic and devoted, raises the energy of the whole crew with a powerful Cheerleader Shot and incites a Fandom Frenzy, massively boosting mood and amping up their guitarist’s rage, while also making sure the opponent feels the heat"
        elif self.crew_class == 'Groupies':
            return "The Groupies, the heart of the band's entourage, provide emotional uplift through a Fan Boost and exclusive VIP Access, raising the crew's mood and adding a touch of wildness by slightly buzzing their guitarist or tipping the opponent into wasted territory."
        elif self.crew_class == 'Roadies':
            return "The Roadies, the backbone of the stage crew, ensure everything is set for the show with their precise Stage Setup and diligent Rig Repair, keeping guitar durability high and maintaining a positive vibe within the crew, while subtly disrupting the opponent’s team."

    def gain_mood(self, amount):
        self.mood += amount
        if self.mood > 50:
            self.mood = 50

    def lose_mood(self, amount):
        self.mood -= amount
        if self.mood < 0:
            self.mood = 0
        elif self.mood < 20:
            self.guitarist.loose_energy(2)
            print(f"The mood of {self.guitarist.name}'crew getting down, {self.guitarist.name} loses 2 energy points! ")
            
    def crew_move(self, attacker, target):
        if self.crew_class == 'Tech Crew':
            crew_action = random.randint(1, 2)
            if crew_action == 1:
                print(f"The Tech Crew performs essential Gear Maintenance, boosting guitar durability and lifting their own spirits while slightly unsettling {target.name}'s crew!")

                lose_mood_target = 13
                gain_mood_attacker = 16
                guitar_regain_durability_attacker = 15
                
                target.crew.lose_mood(lose_mood_target)
                attacker.guitar.regain_durability(guitar_regain_durability_attacker)
                attacker.crew.gain_mood(gain_mood_attacker)

                print(f"{target.name}: crew mood -{lose_mood_target}")
                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: guitar durability +{guitar_regain_durability_attacker}")
                attacker.status()
                target.status()

            elif crew_action == 2:
                print(f"With a Quick Fix, the Tech Crew maintains high spirits and slightly enhances guitar durability, while {target.name}'s crew feels the pinch!")

                lose_mood_target = 12
                gain_mood_attacker = 14
                guitar_regain_durability_attacker = 13
                
                target.crew.lose_mood(lose_mood_target)
                attacker.guitar.regain_durability(guitar_regain_durability_attacker)
                attacker.crew.gain_mood(gain_mood_attacker)

                print(f"{target.name}: crew mood -{lose_mood_target}")
                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: guitar durability +{guitar_regain_durability_attacker}")
                attacker.status()
                target.status()    
                
        elif self.crew_class == 'Manager':
            crew_action = random.randint(1, 2)
            if crew_action == 1:
                print(f"The Manager pulls a Strategic Boost, lifting {attacker.name} crew's mood and firing up their guitarist's rage while causing a noticeable drop in {target.name}'s crew morale!")

                lose_mood_target = 14
                gain_mood_attacker = 17
                gain_rage_attacker = 15
                
                target.crew.lose_mood(lose_mood_target)
                attacker.gain_rage(gain_rage_attacker)
                attacker.crew.gain_mood(gain_mood_attacker)

                print(f"{target.name}: crew mood -{lose_mood_target}")
                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: rage +{gain_rage_attacker}")
                attacker.status()
                target.status()    

            elif crew_action == 2:
                print(f"The Manager handles Conflict Resolution, keeping the team's spirits high and their guitarist's rage up, while making {target.name} a bit more wasted!")

                gain_mood_attacker = 12
                gain_rage_attacker = 15
                wasted_target = True
                
                target.crew.gain_mood(gain_mood_attacker)
                attacker.gain_rage(gain_rage_attacker)
                target.is_wasted = wasted_target

                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: rage +{gain_rage_attacker}")
                print(f"{target.name} is wasted !!")
                attacker.status()
                target.status()        

        elif self.crew_class == 'Groupies':
            crew_action = random.randint(1, 2)
            if crew_action == 1:
                print(f"The Groupies deliver a Fan Boost, lifting everyone's spirits and giving their guitarist a slight buzz!")

                gain_mood_attacker = 18
                gain_rage_attacker = 14
                wasted_target = True
                
                target.crew.gain_mood(gain_mood_attacker)
                attacker.gain_rage(gain_rage_attacker)
                target.is_wasted = wasted_target

                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: rage +{gain_rage_attacker}")
                print(f"{target.name} is wasted !!")
                attacker.status()
                target.status()     
            
            elif crew_action == 2:
                print(f"The Groupies offer VIP Access, enhancing their own mood and giving {attacker.name} a little more rage while making {target.name} more wasted!")

                gain_mood_attacker = 16
                gain_rage_attacker = 13
                wasted_target = True
                
                target.crew.gain_mood(gain_mood_attacker)
                attacker.gain_rage(gain_rage_attacker)
                target.is_wasted = wasted_target

                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: rage +{gain_rage_attacker}")
                print(f"{target.name} is wasted !!")
                attacker.status()
                target.status()     
        
        elif self.crew_class == "Fan Club":
            crew_action = random.randint(1, 2)
            if crew_action == 1:
                print(f"The Fan Club launches a Cheerleader Shot, raising the excitement and {attacker.name} rage while making {target.name} slightly wasted!")
        
                gain_mood_attacker = 18
                gain_rage_attacker = 15
                wasted_target = True
                
                target.crew.gain_mood(gain_mood_attacker)
                attacker.gain_rage(gain_rage_attacker)
                target.is_wasted = wasted_target

                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: rage +{gain_rage_attacker}")
                print(f"{target.name} is wasted !!")
                attacker.status()
                target.status()     

            elif crew_action == 2:
                print(f"The Fan Club ignites a Fandom Frenzy, lifting spirits and rage, and causing {target.name} to feel the effects of enthusiastic support!")

                gain_mood_attacker = 19
                gain_rage_attacker = 14
                wasted_target = True
                
                target.crew.gain_mood(gain_mood_attacker)
                attacker.gain_rage(gain_rage_attacker)
                target.is_wasted = wasted_target

                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: rage +{gain_rage_attacker}")
                print(f"{target.name} is wasted !!")
                attacker.status()
                target.status()         

        elif self.crew_class == "Roadies":
            crew_action = random.randint(1, 2)
            if crew_action == 1:
                print(f"The Roadies execute a flawless Stage Setup, improving guitar durability and boosting their own mood while causing a slight dip in {target.name}'s crew morale!")

                lose_mood_target = 13
                gain_mood_attacker = 16
                guitar_regain_durability_attacker = 14
                
                target.crew.lose_mood(lose_mood_target)
                attacker.guitar.regain_durability(guitar_regain_durability_attacker)
                attacker.crew.gain_mood(gain_mood_attacker)

                print(f"{target.name}: crew mood -{lose_mood_target}")
                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: guitar durability +{guitar_regain_durability_attacker}")
                attacker.status()
                target.status()

            elif crew_action == 2:
                print(f"With Rig Repair, the Roadies keep their spirits high and extend guitar life, while {target.name}'s crew feels the effect!") 

                lose_mood_target = 12
                gain_mood_attacker = 15
                guitar_regain_durability_attacker = 13
                
                target.crew.lose_mood(lose_mood_target)
                attacker.guitar.regain_durability(guitar_regain_durability_attacker)
                attacker.crew.gain_mood(gain_mood_attacker)

                print(f"{target.name}: crew mood -{lose_mood_target}")
                print(f"{attacker.name}: crew mood +{gain_mood_attacker}")
                print(f"{attacker.name}: guitar durability +{guitar_regain_durability_attacker}")
                attacker.status()
                target.status()


guitarist_info = {
        'Eddie Van Halen': 'Shredder Virtuoso',
        'Slash': 'Riff Master',
        'Tony Iommi': 'Doom Metal Master',
        'Kirk Hammett': 'Thrash Lord',
        'Dimebag Darell': 'Groove King'
    }

def choose_your_guitarist(player_num, already_choosen_guitarist=None):
    while True:
        input_guitarist = input(f'Player {player_num}, please enter the name of your guitarist: ')
        if input_guitarist == already_choosen_guitarist:
            print('This guitarist has been already choosen by player 1, please choose another guitarist !!')
        elif input_guitarist in guitarist_info:
            player_class = Guitarist_class(guitarist_class=guitarist_info[input_guitarist])
            player = Guitarist(name=input_guitarist, guitarist_class=player_class)
            print(f'Welcome in the contest,\n {player}')
            return player
        else:
            print('Not a valid name, please try agin !!')


guitar_list = ['Fender Stratocaster', 'Gibson Les Paul', 'Ibanez JEM']

def choose_your_guitar(player_num, player_obj):
    
    while True:
        input_guitar = input(f'Player {player_num}, please choose your guitar: ')      
        if input_guitar in guitar_list:
            guitar = Guitar(model=input_guitar)
            player_obj.guitar = guitar
            print(f'Awsome !!\n{player_obj.guitar}')
            break
        else:
            print('Not a valid guitar model, please try again !!')


crew_list = ['Tech Crew', 'Manager', 'Groupies', 'Fan Club', 'Roadies']

def choose_your_crew(player_num, player_obj):
    while True:
        input_crew = input(f'Player {player_num}, please choose your crew: ')
        if input_crew in crew_list:
            crew = Crew(crew_class=input_crew, guitarist=player_obj.name)
            player_obj.crew = crew
            print(f'Nice !!\n{player_obj.crew}')
            break
        else:
            print('Not a valid crew, please try again !!')


actions_list = ['attack', 'trick', 'crew', 'quit']
def input_move(player_obj):
    while True : 
        input_move = input(f'Please, {player_obj.name}, make a move (attack, trick or crew) or quit (quit): ')            
        if input_move in actions_list:
            return input_move
        else:
            print('Not a valide move, please try again !!')


def move(action, attacker, opponent):
    if action == 'attack':
        attacker.guitarist_class.attack_move(attacker, opponent)
    elif action == 'trick':
        attacker.guitar.guitar_move(attacker, opponent)
    elif action =='crew':
        attacker.crew.crew_move(attacker, opponent)  
    elif action == 'quit':
        print(f'What a shame, {attacker.name} gave up !! Too bas !!')
        exit()


def winner_looser(player_one_obj, player_two_obj):
    if player_one_obj.energy <= 0:
        print(f"The lights fade, the crowd goes silent...{player_one_obj.name} is completely drained of energy! They've given it their all, but tonight, the stage belongs to their opponent !")
    elif player_two_obj.energy <= 0:
        print(f"The lights fade, the crowd goes silent...{player_two_obj.name} is completely drained of energy! They've given it their all, but tonight, the stage belongs to their opponent !")
    elif player_one_obj.guitar.durability <= 0:
        print(f"The final string snaps, the amplifier fizzles out {player_one_obj.name}'s guitar has shattered beyond repair! Without their trusty axe, they can no longer fight on. The contest is over!")       
    elif player_two_obj.guitar.durability <= 0:
        print(f"The final string snaps, the amplifier fizzles out {player_two_obj.name}'s guitar has shattered beyond repair! Without their trusty axe, they can no longer fight on. The contest is over!")


def subit_death(player_1_obj, player_2_obj):
    def final_assault(winner, looser):
        winner.energy == 0
        winner.guitar.durability == 0
        print("!! MORT SUBITE !!")
        print(f"As the battle reaches its boiling point, with energy below critical levels, {winner.name} snaps. Rage surges to 100%, eyes burning with fury. In a moment of pure chaos, {winner.name} raises their guitar high and smashes it down with a bone-crushing blow, shattering both the guitar and their opponent's spirit. {looser.name} crumbles under the weight of the attack, completely overwhelmed.")
        print(f"The arena falls silent... {winner.name} has claimed absolute victory, by any means necessary. The contest is over.")
        exit()
    
    if player_1_obj.energy < 5 and player_1_obj.rage == 50 and player_1_obj.is_wasted == True:
        final_assault(player_1_obj, player_2_obj)
    elif player_2_obj.energy < 5 and player_1_obj.rage == 50 and player_1_obj.is_wasted == True:
        final_assault(player_2_obj, player_1_obj)
    else:
        return    
 
def contest(chosen_player_obj, other_player_obj):
    while chosen_player_obj.energy > 0 and chosen_player_obj.guitar.durability > 0 and other_player_obj.energy > 0 and other_player_obj.guitar.durability > 0:
        input_move_1 = input_move(chosen_player_obj)
        move(input_move_1, chosen_player_obj, other_player_obj)
        
        input_move_2 = input_move(other_player_obj)
        move(input_move_2, other_player_obj, chosen_player_obj)

        subit_death(chosen_player_obj, other_player_obj)
    else:
        winner_looser(chosen_player_obj, other_player_obj)   
        exit() 


def main():

    print("\n\nWelcome to the Ultimate Guitar Battle!\n\nIn this intense showdown, you'll lead your legendary guitarist to victory through electrifying attacks, strategic crew support, and tactical tricks. Your goal? Outlast and outplay your opponent by either draining their energy to zero or shattering their guitar into oblivion.\n\nChoose your guitarist, select the perfect guitar, and rally your crew. When the battle begins, you can opt to launch an attack, call on your crew for support, or pull off a crafty trick to gain the upper hand.\n\nRemember, the match ends when one guitarist is completely drained of energy or their guitar is no longer playable. Get ready to rock—because in this arena, it's all or nothing!\n\n")
    print("Game Commands: Each player takes turns to make their move. On your turn, you can choose from three commands: Attack to unleash a powerful move against your opponent, Crew to call on your team for support, or Tricks to perform a cunning strategy that can tilt the battle in your favor. Plan wisely, as each action can bring you closer to victory—or push you toward defeat!")
    print("Choose your guitarist between:\n1/ Eddie Van Halen\n2/ Slash\n3/ Tony Iommi\n4/ Kirk Hammett\n5/ Dimebag Darell")
    
    player_one = choose_your_guitarist(1)
    player_two = choose_your_guitarist(2, player_one.name)

    print('Please choose a guitar, Fender Stratocaster, Gibson Les Paul or Ibanez JEM')

    choose_your_guitar(1, player_one)
    choose_your_guitar(2, player_two)

    print('Please, finally choose a crew to follow you among the following one: Tech Crew, Manager, Groupies, Fan Club and Roadies. ')

    choose_your_crew(1, player_one)
    choose_your_crew(2, player_two)

    print('Sweet !! ready ? ') 
    start_first = random.randint(1,2)
    print(f'{player_one.name if start_first == 1 else player_two.name}, you have been chosen to start')
    contest(player_one, player_two) if start_first == 1 else contest(player_two, player_one)
    

if __name__ == '__main__':
    main()





    

