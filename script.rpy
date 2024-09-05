# Define characters
define p = Character("[name]", color="#c8ffc8")  # The protagonist's name will be chosen later.
define c = Character("[companion_name]", color="#ffc8c8")  # Companion name based on gender.
define n = Character(None)  # Invisible narrator

# Set up variables for player and companion gender
default name = "Player"
default companion_name = "Companion"
default hp = 30  # Player's initial HP is low due to injuries
default faction = "Neutral"  # To store player's alignment (Thugs, Empire, Liberation)

# Game Start
label start:
    scene black with fade
    n "..."
    n "Darkness surrounds you, the night heavy with rain, beating down on cobblestones."
    n "You feel pain—searing in your head, burning across your body. The sensation of blood mixing with rainwater on your skin."
    n "Your mind is blank... nothing comes to you. Who are you? Where are you? Only the pain remains."
    n "You struggle to open your eyes. A figure kneels beside you, their expression blank and stern, impossible to read."

    # Gender selection
    menu:
        "Am I a boy or a girl?":
            "A boy":
                $ name = "Boy"
            "A girl":
                $ name = "Girl"

    # Companion gender selection
    menu:
        "The person beside me... are they a boy or a girl?":
            "A boy":
                $ companion_name = "Boy Companion"
            "A girl":
                $ companion_name = "Girl Companion"

    scene alley with dissolve
    show c at left
    c "[name], you're awake."
    
    p "My head... everything hurts. I... I can't remember anything."

    c "You took a nasty hit to the head. And that fire magic... it nearly burned you alive."

    p "Who... who am I?"

    c "You don’t remember? Not even your name?"

    # Player enters their name
    $ name = renpy.input("What was my name?")
    $ name = name.strip() if name else "Unknown"
    
    p "My name... is [name]. But that's all I know."

    c "It’s understandable with what you’ve been through. Your memory might come back, but right now, we need to stay focused."

    n "You look at the companion, their stern, unreadable face offering no comfort."

    # Backstory discovery - setting the player's faction subtly
    menu:
        "What do you ask next?":
            "What happened to us?":
                c "We were ambushed. You were leading a mission. The fire magic hit you badly. We were trying to get into the Special Division."
                p "A mission? Special Division?"
                c "Yes. We were close to making it, but someone set us up. You were involved with the Empire’s plans, aiming to join their elite forces."
                $ faction = "Empire"
                p "The Empire... that makes sense. But why does it feel so strange?"

            "What are we doing here?":
                c "We were on a mission to contact a Liberation cell. You don’t remember, but you were trying to gather intel for them."
                p "Liberation cell? What does that mean?"
                c "The Liberation is fighting against the Empire. We were trying to get crucial information to them."
                $ faction = "Liberation"
                p "Liberation... It sounds important, but I can't grasp the details."

            "Who are the people after us?":
                c "There are local thugs after us. We’ve had conflicts with them over territory. You were trying to negotiate with them for survival."
                p "Thugs? So we were just trying to get by?"
                c "Yes. It was more about survival and avoiding conflict with the bigger factions."
                $ faction = "Thugs"
                p "Thugs... It seems like I should remember more."

    c "We need to move quickly. There's a dead body nearby. We can't stay here or we might get caught."

    n "You struggle to sit up, pain radiating through your body. The burns from the fire magic and the sharp throb in your head are unbearable."

    if hp <= 30:
        p "I can barely move... everything hurts."
        c "You’re in no shape to move fast. Lean on me, I’ll help you get out of here."
    else:
        p "I can manage, just give me a moment."
    
    # Discover the body
    show body at center
    n "A few feet away, you see the lifeless body of a man lying face down in the mud, blood staining the ground beneath him."

    p "Who... is that? Did I... do this?"

    c "No, you didn’t do this. But we need to be careful. If someone finds us, they might think otherwise."

    menu:
        "What do you want to do?":
            "Search the body":
                p "We should search him. Maybe there’s something useful."
                c "Alright, but make it quick."
            "Leave before anyone finds us":
                p "We should get out of here. If the Empire’s police come..."
                c "You’re right. We need to move before we’re spotted."

    # Continue the story based on the player’s choices
    return
