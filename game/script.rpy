define s = Character('Melvin', color="#c8ffc8")
define m = Character('C.A.F.A', color="#c8c8ff")

label start:

    "The world had succumbed to the relentless rise of the tides, leaving humanity clinging to life on scattered archipelagos that once were mountaintops."

    "Melvin, an old inventor with a heart full of regret, lay on his deathbed aboard his island-like ship, surrounded by the mechanical hums and the soft lapping of the water against the hull."

    "His companion, C.A.F.A, a robot built from scraps and hope, stood by him, its sensors dimly glowing in the twilight of humanity's dusk."
    
    "Melvin coughed, his voice barely above a whisper."

    s "It's a strange feeling, knowing the world's ending. I always thought we'd have more time to turn things around."

    m "The end of this world cycle is imminent. However, your efforts to reverse the course have been noted."

    s "I just wish my time machine had worked when we needed it most. Maybe then I could've made a real difference."

    m "The concept of your time machine was sound. Initiating repairs may offer a second chance."
    
    menu:

        "There's hope.":
            jump hope

        "It's pointless":
            jump pointless

    label hope:

        s "Do you really think there's hope? That we could go back and fix all this before it's too late?"

        jump sentiment

    label pointless:

        s "It's like an interactive book that you can read on a computer or a console."

        jump sentiment

    label sentiment:

        m "Hope is a human sentiment. As a machine, I calculate probabilities. The probability warrants action."

    s "Then there's no time to waste. If you can make that machine work, maybe all is not lost."

    m "Affirmative. Commencing repair operations on the temporal device. Your vision may yet alter our fate."

    s "I never thought I'd see the day when the fate of the world hung on an old man's dream and a robot's skill."

    m "It is an unprecedented scenario. Success would redefine our existence. Departing to commence repairs."

    s "Good luck, my friend. You carry the hopes of an old man and a world on your shoulders."

    m "Acknowledged. I will endeavor to uphold these hopes to the utmost of my operational capacity."

    "As Melvin took his final breaths, he watched C.A.F.A work tirelessly through the night."

    "The robot had become more than just circuits and code; it was a beacon of hope in this drowning world."