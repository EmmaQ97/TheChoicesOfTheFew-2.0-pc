# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# ///Character names will be seperated. Having a 1 at the end of their variable, means that it is that character's full name.\\\
# Color of character names based off of eye color. Still need change Luiza's, and Urszula's HTML colors.

# ///CHARACTER'S SHORT-HAND NAME\\\

define r = Character("Rozalia", what_prefix='"', what_suffix='"', color="#47d147")

define l = Character("Luiza", what_prefix='"', what_suffix='"', color="#4d4dff")

define s = Character("Serafina", what_prefix='"', what_suffix='"', color="#cccccc")

define a = Character("Aldona", what_prefix='"', what_suffix='"', color="#d2a679")

define t = Character("Tamara", what_prefix='"', what_suffix='"', color="#ac7339")

define u = Character("Urszula", what_prefix='"', what_suffix='"', color="#bfbfbf")

# ///CHARACTER'S FULL NAME\\\

define r1 = Character("Rozalia Rowecki", color="#47d147")

define l1 = Character("Luiza Jaskólski", color="#4d4dff")

define s1 = Character("Serafina Kosmatka", color="#cccccc")

define a1 = Character("Aldona Andrysiak", color="#d2a679")

define t1 = Character("Tamara Szwedko", color="#ac7339")

define u1 = Character("Urszula Stasiuk", color="#bfbfbf")

# ///CHARACTER'S LAST NAME + MILITARY RANK\\\

define r11 = Character("LT Rowecki", color="#47d147")

define l11 = Character("SGT Jaskólski", color="#4d4dff")

define s11 = Character("CPL Kosmatka", color="#cccccc")

define a11 = Character("PFC Andrysiak", color="#d2a679")

define t11 = Character("PFC Szwedko", color="#ac7339")

define u11 = Character("PFC Stasiuk", color="#bfbfbf")

# ///MISCELLANEOUS CHARACTERS\\\

define em = Character("Emmanuel", what_prefix='"', what_suffix='"', color="#bfbfbf")

define unk = Character("Unknown", color="#bfbfbf")

define m = Character("Rozalia's Mother", what_prefix='"', what_suffix='"', color="#bfbfbf")

define c = Character("Child", color="#47d147")

define r0 = Character("Roza", what_prefix='"', what_suffix='"', color="#47d147")

define ss = Character("Kämpfer Soldier", what_prefix='"', what_suffix='"', color="#bfbfbf")

define dd = Character("Kämpfer Officer", what_prefix='"', what_suffix='"', color="#bfbfbf")

define graye = Character("Detached Smoker", color="#cccccc")

define frightened = Character("Cautious Female", color="#ac7339")

define braggart = Character("Confident Thief", color="#d2a679")

define scared = Character("Worried Bystander", color="#bfbfbf")

define nar = Character("Narrator (Rozalia)", color="#47d147")

define nar2 = Character("Narrator (Luiza)", color="#4d4dff")

define nar3 = Character("Narrator (Serafina)", color="#cccccc")

define nar4 = Character("Narrator 1 (Rozalia) & Narrator 2 (Luiza)", color="#00e6e6")

# ///INITIALIZATION FOR BACKGROUND IMAGES.

init:
    image bgoffice = "office.jpg"
    image bgmemory = "memories.jpg"
    image bgalley = "alleyway.jpg"
    image bgwarehouse = "warehouse.jpg"
    image bgoutside1 = "ruins1.jpg"
    image bgoutside2 = "ruins2.jpg"

# ///FLAGS TO TRIGGER WHEN PREQUISITES MET BASED ON PLAYER CHOICE.\\\

# Serafina's trigger has been set. All that needs to be done is pull when I feel the time is right, by writing in the
# code for the consequence of inaction/"wrong" choice.

# By the way, should probably clean up these comments at some point. Lastly, I need to trim the bits of narration that does
# more telling than showing...

default Remembering_the_Past = False

default Honoring_the_Present = False

default Uniting_the_Girls = False

# The game starts here.

label start:

    $ count = 0

    stop music fadeout 5.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room
    #REMOVE COMMENT HASHTAG FROM 62nd LINE AND THIS LINE. FOR NOW, IT'LL STAY COMMENTED OUT SO IT'S ONLY A PITCH BLACK SCREEN. 
    #AS I AM WORKING ON DIALOGUE FIRST.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy
    #REMOVE COMMENT HASHTAG FROM 70th LINE AND THIS LINE. FOR NOW, IT'LL STAY COMMENTED OUT SO NO CHARACTERS ARE ON SCREEN.
    #AS I AM WORKING ON DIALOGUE FIRST.

    scene black with dissolve

    show text "Author's Note" with Pause(2.5)

    scene black with dissolve

    # These display lines of dialogue.

    """
    This visual novel keeps track of the decisions you make throughout the story, and presents you with a different ending determined by your score. Which starts at 0.
    Your score will be shown towards one of the later chapters.

    """

    """
    GOOD MORNING CLASS. Shout outs to the folks that presented their pieces today. Great work as always. :)

    OH NO THE GAME IS BREAKING THE FOURTH WALL. Nah, I just decided this was the best way to say a few things before we start. I'll remove these messages from later versions of this project... ofc.

    This game is best played on your own so you can read at your own pace. For those of you that are familiar with visual novels, fellow GAMERS, you'll notice I reuse certain SFX and backgrounds. This is intentional because artists cost money.

    I AIN'T GOT MONEY. (... Not actually true, but hopefully you get my point.) 

    Characters also do not have their own art for the same reason. I don't want to pay someone and then trust them to get the art to me on time. So I've done everything as a one-man crew with the guidance of my committee's feedback. So not totally a one man crew. I lied again.

    The first three chapters are me setting things up. The story picks up towards the end. I promise.

    Choices matter. I suggest getting the endings in order with the 45 minutes that we have. Order is 'good', 'bad', and 'secret' endings. I'll point out the choices you need to make to reach each one.

    Oh, and as was mentioned in Will's email. This story is fictional. Inspired by the Warsaw Uprising during WW2.

    I think I covered mostly everything here.

    I'll take questions at the end, unless I don't, and instead answer them during the showcase. Whichever works best.

    May as well use this as a todo list: I NEED TO EDIT OUT CHAPTER NAMES WITH DATES INSTEAD.

    NOW that is officially all. THANK YOU, ENJOY. <3
    """

    scene black with dissolve

    show text "A Foreword" with Pause(2.5)

    scene black with dissolve

    # ///FOREWORD\\\
    # ///SETTING THE STORY UP\\\

    """
    Three sides: The Kämpfers from Deutschland, a dictatorship. The Republic of Polskiej. Finally, the people from Rossiya- the Russkaja.

    The three lived in harmony within a single large landmass, divided more or less evenly into three. The trio of continents ruled peacefully, for a time.

    Greedy to expand and seize the continent for themselves, the dictator of Deutschland broke a formal pact known as the 'Power of Three.'

    The pact had been established to quell distrust between the three powers. One country could not attack the other and if they did, the other would assist the defender.

    It was in each country's best interest to work together, so the surprise attack launched by Deutschland stunned Polskiej and Rossiya long enough for Deutschland to take much of Polskiej's land with ease.

    Warszawa, the capital of Polskiej, found itself under swift siege and it was not long before it was captured. Living under the rule of a country once considered an ally,

    the people of Warszawa took it upon themselves to plan a rebellion, with the help of the people of Rossiya. The Warszawan people knew that it wouldn't be long before Rossiya came to their aid. It was a part of the pact, after all.

    The story follows a group of six women who have taken up the call to arms in the service of their occupied country.

    Rozalia Rowecki, a resistance officer. Luiza Jaskólski, a caring friend. Serafina Kosmatka, the detached chain smoker. Aldona Andrysiak, the petty thief. Tamara Szwedko, the quick to anger city girl. Urszula Stasiuk, the quiet observer.

    These are but a few of the many resistance members to have banded together in opposition of those who have occupied Warszawa...

    """

    # ///BEGINNING OF THE VISUAL NOVEL\\\
    # ///INTRODUCTION\\\

    scene black with dissolve

    show text "Chapter 0\nA Story Retold" with Pause(2.5)

    scene black with dissolve

    nar """
    The crackling of flames filled my ears, the smell of blood and smoke making my stomach churn. The night was cool. Calm. Some might have found it beautiful, even as the intense red and orange colors engulfed the city. 

    Yet despite my fogged up mind and blurry vision, I found the strength with which to murmur the following words:
    """

    r """ This was not the way I had expected things would go.

    We were meant to have finished our story, hand in hand. Me and my girls. Why, am I the only one of them all that still breathes? 

    We made promises to friends and family that we would fight for our freedom. What we were actually fighting for, was time. Death had already staked its claim on us by wrapping its cold fingers around our throats.

    All that was left, was to live for as long as we could. While protecting those we loved with one hope in mind:

    Salvation.

    That our Russkajan allies would deliver to us the relief and freedom we so desperately desired. 

    And we- the people of Warszawa. We clung to that hope.

    We shouldn't have.
    """

    nar """
	The fires grew defeaning, and before I knew it my voice had been muffled by the hungry, roaring heat. 

	I had expected death to be so much colder. Chilly, even. Ah... I can't help but smile.
	"""

    # ///CHAPTER 1\\\
    # ///BESTFRIENDS 4 EVER\\\

    scene black with dissolve

    show text "Chapter 1\nWhere It All Began" with Pause(2.5)

    scene black with dissolve

    r "Zzz..."

    l "Lieu..."

    r "... zzz."

    l "... tenant."

    play sound "musicSFX/sfx/sfxdeskslam.wav"
    $ renpy.pause (1.0, hard=True)
    scene bgoffice with dissolve

    nar "My head jerked up from where it had been laying on my desk. For a second, I thought someone had fired an artillery shell right beside my ear. Until my eyes drifted around the room, and settled on the girl standing before me."

    r "H-huh?"

    l "Rozalia, how many times have I told you not to fall asleep at your desk? Let alone fall asleep at all?"

    nar "Pretty difficult question if you asked me. I raised my hand and started the tedious process of counting with my fingers."

    r "... Uh, Three, four, five..."

    nar "I brought up my other hand and continued my count."

    r "...Six-"

    l "S-stop that. What are you, a child?"

    r "Come on, that's no way to speak to your superior Luiza."

    l "Okay, Lieutenant Rozalia Rowecki. Could you please refer to me by my last name?"

    r "You know, just saying Liutenant Rowecki works-"

    l "Lieutenant Rowecki, could you PLEASE refer to me by my last name?"

    r "Heeeey, I'm only teasing you a little Luiz. Ease up for me and use my first name like you've always done."

    nar """I go ahead and point at the seat she was standing next to with a smile on my face. Luiza stared at me with her vibrant blue eyes for awhile longer.

    I'm sure I see a hint of concern along with disapproval in them, but I held my tongue for the time being as she goes to take a seat. I cleared my voice.

    """

    r "Ahem. Sergeant Luiza Jaskólski."

    l "Y-yes, Lieutenant?"

    r "I regret to inform you that you are hereby relieved of your position as a Sergeant of the Warszawan Home Army."

    nar "I could see the color draining from her face and it instantly made me feel like an ass, so I quickly added:"

    r "I'm only kidding."

    nar "Her shoulders rose and fell as she sighed in relief."

    l "Roza please don't do that ever again, or I'll always recognize you as the worst Lieutenant in Polskiej history."

    r "Sorry."

    nar"""I propped my feet up on my desk. A piece of caked together mud from the soles of my boot came loose, and Luiza was swift to acknowledge it with her eyes.

    Another sigh escaped her, but I could tell that this one wasn't due to relief.
    """

    l "Roza, I've been worried about the others. I'm aware that you have plans for us, and that we have the backing of the Warszawan people behind us. But I..."

    nar"""'So that's what this was about?' I thought to myself. I gazed out the window on my left, and past the beams of light that filtered in from outside.

    I knew there was construction work going on in the plot next to the building I was using as an office, but I heard nothing and saw little to no movement.
    """

    play sound "musicSFX/sfx/sfxdeskslam.wav"
    $ renpy.pause (1.0, hard=True)

    nar "My eyes flickered back to Luiza. She was standing again, body bent towards me with her hand firmly on the desk."

    r "So loud, Luiz... stop banging on my desk."

    l "Then pay attention Roza, please... and wipe the drool from your lips!"

    nar "'Alright, so maybe I had decided to take a nap. What of it?' I should've said to her then, with a big grin. Maybe that would've cheered her up. Make her smile at least a little."

    r "Staring at my lips are we? You know that's grounds for fraternization my dear Sergeant."

    l "Please take this a little more seriously!"

    nar """I tried Luiza. I tried. If I had taken things too seriously, the pressure to succeed would've brought me low faster than any bullet. 

    I cleared my throat and raised my voice to be as clear as possible, as I prepared to address her the way she wished for me to. She settled back into her seat.

    """
    l "Our girls aren't that experienced as soldiers, and you know that Roza. The only ones that know anything are us, and Serafina. So why-" 

    r "- Why do I trust them?"

    nar "I lowered my feet down to the ground, and brushed the dry piece of mud away with my arm."

    r """ Yes. It's true. Only three of us out of the six are experienced fighters, but those other three volunteered themselves for this. They know the risk that comes with an uprising, and still.

    Still, they asked to be a part of the movement. I wasn't about to turn them away. I couldn't...
    """

    nar "I should have."

    r "... They want to serve their country the same way we do. I'll let them have that honor, and I'll protect them with my life to see that their wish is fulfilled."

    nar """ I noticed Luiza's eyes drifting around the room and settling on different objects while she listened. First it was the potted plant I had off to the side, then the ceiling fan above.

    Then she started to focus on me. My hand. My arm. Then my face. I could hardly maintain eye contact with her, because she continued to break it. I was only wearing a plain old shirt and a pair of jeans.

    I know I didn't look all that impressive, but she could've at least been a little more polite. I'm only teasing of course. 

    I stared at her blue eyes all the while with my green ones, the cap I wore doing well to provide me with a little shade from the yellow-orange overhead lighting.
    """

    r "Luuuuuizaaa. Are you listening?"

    menu:

        "She kept on staring at me for some reason. So I let her.":
            jump dream_on

        "She snapped out of whatever trance she had been in. So I carried on.":
            jump wake_up

    label dream_on:

        $ Remembering_the_Past = True

        $ count += 1

        nar """ I watched her tired eyes travel down the contours of my body, until she came across my waist. I got worried here and started scratching the back of my head, because I was carrying a pistol beneath my shirt.

        I hadn't done anything to tip her off, or so I thought. Maybe I was worried for nothing, and she actually wasn't thinking of anything in particular. 

        Luiz was a funny one. Tells me to not fall asleep at my desk, but here she was daydreaming right in front of me. 

        'I may as well do the same.' I thought, so I did. In that silence, there was a temporary solace. We took that rare chance to stare at each other and dream, my mind choosing to travel to past memories.
        """

        scene bgmemory with dissolve

        r "Maaaa, I don't want to go back inside! I still want to play with Luiz!"

        m "I know you want to play with Luiza dear, but it's become cold and awfully late. What if you get sick? You know that pa will worry, don't you?"

        r "But if I leave now, I won't get to see Luiz again until tomorrow!"

        l "It's alright Roza! We can play in my yard next time!"

        r "But I don't want to waaaait!"

        nar "I rolled around in the dirt like a spoiled child. Luiza stood over me with a big smile on her face, while my mother looked on with worry. Everything was so much happier. Innocent."

        m "Roza, sweetie, you're going to ruin your dress rolling around like that!"

        r "Ma I don't want go! Pa's always busy and you're always busy too, so I want to be with Luiza all day instead!"

        nar """Thinking about our childhood reminded me of how much I had missed Luiza, after we seperated.

        It was only after the start of the war and in an urban setting, than suburban, that we'd find each other again. She had grown and so had I, but even after so long we still recognized one another.

        There was something important after this recollection of the past, that I wanted to tell Luiza. The thought of what I had wanted to say made my heart race in my chest, and filled me with an excitement unlike anything else.

        But when the opportunity to tell her what was on my mind presented itself.

        I hesitated.

        She looked so tired and unlike during our childhood, I was powerless to make her smile. Not at all like before.
        """

        if Remembering_the_Past:

            scene black with dissolve

            nar "We both blinked, and that was our sign that we'd arrived from our journey through our memories."

            jump present

        else:

            scene black with dissolve

            nar "I watched as Luiza came back to her senses with a start and a blink of the eyes."
       
            jump present

    label wake_up:

        $ count -= 1

        scene black with dissolve

        nar """Luiza blinked in surprise as she was suddenly reeled back into reality. Her tired gaze reclaimed its place on her visage.

        I needed her to be here in the present. Not wherever she had been.
        """

        jump present

    label present:

    scene bgoffice with dissolve

    l "I-I'm listening!"

    nar "I snickered, 'cause that was an outright lie and I knew it since I had been doing the same as her. Silly Luiz."

    r "Want to lay your head down on my desk?"

    l "N-no! I refuse to sleep when we have so much work to do, Roza."

    nar """A smile came over me. Always working so diligently. Worrying about others, when she should have been worrying about herself.

    Luiza...
    """

    r "It's okay. The general gist of what I said earlier was that you don't have to worry. I'll take care of the new girls."

    l "I'll help."

    r """Oh no you don't. You need your rest. Leave those three to me. I'll get them all caught up with what's going down, and we'll go from there.

    Also, I wanted to ask you. Do you remember how close we used to be during our childhood?
    """

    if Remembering_the_Past:
        nar """I recalled the look she gave me. Her lips curling up at the corners into her trademark smile.
        It made me feel elated. To know that she could still smile so brightly, followed by two simple words I won't forget:

        'I remember.'
        """
        jump what_once_was

    else:
        nar """Luiza remained silent like she hadn't heard me at all. That silence was so deafening. It felt as if I'd been shot through the heart.

        Maybe that's why I had forgotten to tell her that important thing that'd always been on my mind, ever since we reunited.
        """
        jump is_no_more

    label what_once_was:
        r """I knew you would,

        Luiza...
        """
        jump present1

    label is_no_more:
        r "..."
        jump present1

    label present1:

        r """... We stuck together through everything then, and in the end we came back together. That's why I'll make this promise to you now:

        No matter what we go through. We'll find each other again. I'll bring the gals along with me, too, and show you that I protected them like I promised I would.
        """

        nar """ What an asshole I was to her.

        Not to mention a fucking liar.

        And I'd do it all again.

        Just to see her smile.
        """

    # ///CHAPTER 2\\\
    # ///THE GREY-EYED SMOKER & THE CITY GIRLS\\\

    scene black with dissolve

    show text "Chapter 2\nThe Halfway Point" with Pause(2.5)

    scene black with dissolve

    nar """ It was a sunny day with clear skies and cool temperatures. It would have been considered a beautiful morning in almost any other country, 

    but here.

    I stepped out of the two story concrete building my office was located in, and stood at the top of the steps while Luiza brushed past me.
    """

    scene bgalley with dissolve

    s "Rozalia, Luiza..."

    nar """ Came an all too familiar mumble. My eyes fell upon the speaker: A woman with grey irises that reflected everything and everyone they looked at with perfect clarity.

    I feared those eyes of her's, because they saw things that I couldn't. Well, at least not until they had already happened to me, but by that point, it was already too late.

    If I had bothered to look closer into those clear pearly eyes and learned not to fear them, I would have realized that they were only a mirror. A mirror that if I stood in front of, showed despair.

    I can only wonder what Luiza saw in those eyes.

    """

    r "Serafina."

    s "Hey. Couldn't sleep at all last night."

    nar "Serafina flicked the cigarette from between her lips. It fell to the ground, and continued to burn before Serafina's boot snuffed it out completely."

    s "You're nervous too, aren't you?"

    r "I am, but there's no point dwelling on it."

    s "You should."

    nar "I never did learn why Serafina made me feel so unsettled. Her every word always nudging me closer to a precipice I refused to look into."

    r "Where are the new girls?"

    s "Where you told us to meet."

    l "Watch your step, Roza."

    r "Thanks."

    nar """I maneuvered my way down the short flight of steps, one foot after the other. The sound of Luiza's steps trailed after my own. 

    My eyes were drawn back to the sight of the empty construction area.
    """

    s "It's today, isn't it?"

    nar """An overwhelming sense of dread crept up on me after Serafina had spoken. Like a whisper into my ear, reminding me of my responsibilities. Of what was to come. 

    A shiver ran down my spine, but my attention returned to the smoker. Fortunately for me, it was not my voice that answered.
    """

    l "It is. The Russkajans will be coming to take Warszawa within a day or two, so we need to have a meeting before then."

    s "I was asking our lead."

    nar "Luiza winced as if she had been slapped across the face."

    r """It's as Luiza says. We're to have a meeting between the six of us, so we're all on the same page before the Russkajans invade.

    Now I'll pose the same question you asked me:

    Are you nervous?
    """

    nar "Serafina contemplated the question for a few seconds, a shaking hand reaching into her pocket to retrieve a pack of cigarettes along with a lighter."

    s "Yeah. I'm nervous."

    r "Then what are you going to do? Stand there and let everyone down?"

    s "No."

    r "Then-"

    s "But you will."

    nar """I wanted to do nothing more than to knock the girl's lights out, but for what?

    Speaking the truth?

    I turned away from her and hastened my way towards the large building next to the construction site."""

    menu:

        "Luiza followed, and together we let that bitch be.":
            jump put_aside

        "Luiza wasn't behind me from what I remember.":
            jump show_care

    label show_care:

        $ Honoring_the_Present = True

        $ count += 1

        if Honoring_the_Present:

            nar """I carried on, but when I looked over my shoulder Luiza wasn't there. Instead, I saw her exchanging some last words with Serafina.

            I don't know what Luiza said to her, but the smoker gave her a nod

            and smiled

            before taking her leave.

            """

        else:

            nar "So I moved on."
        jump present2

    label put_aside:

        $ count -= 1

        nar """Luiza followed after me quietly just like always. We didn't need Serafina anyway, and I was happy with that.

        The less people I had to protect that didn't need nor deserve protecting, the better.

        """
        
        jump present2

    label present2:

    scene bgwarehouse with dissolve

    nar """Luiza and I walked around the outskirts of the construction site, and before long we had arrived at the warehouse diagnoally across from my office.

    I stepped toward two large sliding doors and grabbed one by the handle. It took a great deal of strength, but I managed to slide the rusted warehouse door open just enough to let us through.

    Inside was a dimly lit interior, with particles of dust flying around from my disturbance. The place was reasonably large, with brown wooden crates stacked to one side of the room.

    Equipment took the other end, with shovels thrown haphazardly into a pile with several other pieces of machinery close by. Such as drills. There were workbenches with tools on them as well.

    Wrenches, screwdrivers, the works. Nothing that we would have to put to use, though.
    """

    a "Soooo. Wanna check out what I stole from one of the soldiers?"

    t "Stole? From the soldiers? What, are you trying to get us all killed?!"

    u "P-please settle down you two..."

    nar "As Luiza and I come closer the voices fell silent, and the smell of coffee grew stronger. Three heads turned our way."

    r "Sorry to interrupt you three."

    nar "The tension in the room had defused itself, for the most part, as sighs were let out."

    a "Hi Roza. You know, you're kinda late!"

    r "Sorry, I was taking care of some business. Where's the coffee at?"

    nar "The girl, Aldona, was seated on a crate. She motioned over to a table off to the side where several mugs of coffee were stating to go cold."

    r "Thank you Aldona."

    a "Anytime, Roza! If you had gotten here earlier you'd have had it warmer."

    r "I know, sorry, sorry."

    nar "I picked up a mug that hadn't been started, and had a sip while I watched the others interact."

    l "Did something happen Aldona? We heard you arguing."

    a "Kiiind oooof. Okay so like, I kinda pickpocketed something off of one of the soldiers and I don't mean to brag or anything but-"

    nar """I nearly snorted on my coffee when I witnessed Aldona be the recipient of a slap to the back of the skull, accompanied by a loud 'thump.'

    The shorter girl blinked her brown eyes a few times, clearly still in a daze. After she had gathered herself, she swiveled around to face the culprit.

    """

    a "Tamara you fucking bitch!"

    t "Maybe if you didn't brag all the time about doing dangerous stuff I wouldn't have to-"

    nar """Aldona grabbed Tamara by the collar of her shirt, and I was fully prepared to bear witness to an all out brawl like some jackass.

    So much for being a damn self-proclaimed protector when all I did was sit by and watch as things happened around me.

    Tamara squinted her dark brown eyes at the shorter girl expecting a blow to come, but it never did.
    """

    u "A-Aldona, Tamara, please. That's enough. Let's all j-just settle down and enjoy each other's company."

    nar """It took a few seconds, the two girls staring into each other's eyes with their fists prepared to do the talking.

    Urszula was the name of the girl that'd calmed them. The care she showed us was similar to Luiza's worry.

    I never really did appreciate her enough.
    """

    a "Look, we'll just settle this some other time. Okay?"

    r "Listen girls. We're supposed to be sticking together not falling apart at the seams. If you have a problem with each other, come to me. We'll sort it out."

    a "It's nothing Roza. We'll be fine."

    t "My ass we'll be fine! You STOLE from one of the soldiers! What if they come back to take back what's theirs?"

    a "The Kämpfer soldier was asleep, so how would he know?"

    t "It's not as simple as 'Oh he didn't see me, I must be safe.' Someone is going to start asking questions!"

    a "You're only upset because I got away with it."

    t "I'm upset because you put us all at risk!"

    nar "The pair's voices grew louder, and I was slowly starting to become irritated. Luiza looked to me, her blue eyes begging me to intervene."

    u "P-please don't start arguing again."

    r "Enough, girls! Enough. We can discuss things when we're all present. Since Serafina still isn't here."

    nar "I set my empty coffee mug down in time to spot a silhouette at the opening in the doors that I had made."

    s "Sorry I'm late."

    r "It's fine. This is all of us, so let's take things to the back."

    nar """I led the girls past a door out of the storage area, and into a dimly lit hallway that went deeper into the heart of the warehouse.

    I had a glance over my shoulder to check on what the others were up to.

    Luiza was staring straight ahead, while Aldona and Tamara chit-chatted away. For two girls that were quick to anger, they sure did get along. Sometimes. 

    Urszula was centered between the pair, helping to keep them in check no doubt. The last of us, was Serafina. She was hanging back from the group as usual, smoking away at a cigarette.

    I faced front and pushed a pushed door open.
    """ 

    scene bgoffice with dissolve

    nar """The room I took them to was our group meeting place. It was sparse in decorations, but large enough to accomodate us all.

    It contained a wooden desk that served as an island for the chairs that surrounded it. There were several books sitting atop wall hanging bookshelves, while filing cabinets hugged the walls.

    Everyone made themselves comfortable from the moment we stepped in.
    """

    a "I'll be taking the desk!"

    u "Aldona... why don't you have a seat in a chair next to me?"

    a "I want the desk, it's way cooler!"

    r "Aldona I can't see anything with you in my way."

    a "Come on Roza, let me have this honor like once!"

    r "If you're going to sit there then at least turn around and face me."

    a "Done!"

    t "I can't see!"

    a "Deal with it."

    r "ENOUGH! Everybody listen up."

    nar "Aldona's legs hung over the side of the table, while the other girls sat clockwise in front of me. All of them except Serafina, who stood by the door."

    r """The Russkajans are coming to take our capital of Polskiej from the Kämpfer soldiers. Within a few weeks, every resistance group in Polskiej will rise.

    You all would only know this if you had been listening to the radio broadcasts, but in the case that one of you hasn't, I decided to set this meeting up and inform you all. In private.

    That wasn't all though. I'm going to be dividing everyone into groups of two, so when the time comes we'll know who's with who.
    """

    nar "When I got to my last couple of words, the repeated noise of metal striking earth  reverberated down the hallway and into my ears."

    r "Construction workers must've finally arrived with their drills. Serafina, you're closest. Get the door."

    nar """Serafina gave her cigarette a single tap, and white ashes fell from the tip. All eyes were on her, but she took her time.

    Her hand gave the door a gentle push and with a click, it shut. Serafina turned to face us again.
    """

    r "Anyways, we're running out of time according to that clock on the wall. We have places we need to be, so I'll be assigning you to groups now."

    nar "There was another interruption before I could finish. A bang loud enough to pierce the air. The sound of the drills ceased."

    u "W-was that a gunshot?"

    r "No. It's got to be the drills. Probably a malfunction. Ignore it."

    t "Hey Aldona..."

    nar "Tamara was staring at Aldona, the latter looking down suspiciously into her lap with guilt in her eyes."

    t "... What did you still from that soldier?"

    # ///CHAPTER 3\\\
    # ///THE CHOICES WE MAKE\\\

    scene black with dissolve

    show text "Chapter 3\nThe Beginning of the End" with Pause(2.5)

    scene bgoffice with dissolve

    nar "Aldona refused to respond. It was only when Tamara stood up and started shaking her shoulders begging for her to answer, that she finally did."

    a "... It was a gun. I stole a gun from one of the soldiers."

    t "You've basically killed us all!"

    nar "Tamara reeled back a fist. I got to my feet, but I knew I wasn't going to make in time."

    if Honoring_the_Present:

        $ Uniting_the_Girls = True

        $ count += 1

        nar """Before any punches could be thrown, the person I last expected to step in did so. 

        This must've surprised the others, because they all stopped shuffling around to try and break the two girls up.
        """

        s "Settle down and maintain a clear mind, girls. Giving into chaos now will be our end before we've even had a chance to start the uprising."

        nar """Serafina glanced at Luiza, the two obviously partaking in a secret I didn't know about. I was furious. Jealous, even.

        My fingers held onto the sides of the table and gripped onto it tightly, and still I said nothing. I forced myself to sit back down.
        """

        l "It's as Serafina says. We should be watching out for each other now more than ever."

        nar """Serafina nodded

        and smiled again.
        """

        jump saving_them

    else:
        nar """Serafina, the useless bitch. All she did was stand by the door, when she was closer to Aldona and Tamara than I was.

        No. Instead all she did was flick the metallic cover of her lighter open, before shutting it again with an obnoxious 'click.'

        I should have got rid of her when I had the chance.
        """
        jump destroying_them

    label saving_them:

        nar "Tamara's tense arm relaxed and with a sigh, she swung around and went back to her seat."

        u "S-Serafina and Luiza are right. L-let's focus on helping one another."
        jump present3

    label destroying_them:

        $ count -= 1

        nar """Tamara managed to strike Aldona with a sucker punch to the side of the face. The two of them argued frequently, but they rarely ever hit each other.

        The rest of us were stunned, but Luiza. Poor Luiza. Tired as she was during those days, she still stepped forward to catch Aldona as she fell backwards, chair and all.

        Tamara had already returned to her seat by then, Aldona cupping her bruised cheek with one hand with eyes full of fire, as she shot a nasty look at Tamara.

        """
        jump present3

    label present3:

    r "I know tensions are pretty high right now, but I need you all to listen up one last time."

    nar "All eyes were on me once more."

    r "While it is true that Aldona has placed us all in jeopardy, we can't ignore that what's done is done. The only thing we can do now, is plan for the storm that we know is brewing."

    nar "I reached under my shirt, and brandished the pistol I had been carrying in my waistband, and stood before them."

    play sound "musicSFX/sfx/sfxwaltherppkcocked.wav"

    r "Your groups are as follows:"

    ss "Clear the building! I want that weapon found no matter what!"

    nar "The palm of my hand was starting to sweat, but my fingers remained wrapped around the grip of my pistol. A finger hung close to the trigger."

    r "Serafina and Urszula are with me, while Luiza is in charge of team two with Aldona and Tamara. We'll escape through the back, and split up from there."

    nar """I needed to keep a personal eye on Serafina, to make sure she didn't pull a fast one on us. Out of all the girls, she was the one I was always most suspicious of.

    Whether I thought that because of how jealous I was. Of how friendly she usually seemed to be with Luiza. Or because I genuinely felt something unnverving about her. Well.

    I couldn't say.

    I opened the door of the office and covered the hall leading back to the storage area, while the rest of the girls sprinted in the opposite direction to the back exit.
    """

    # ///CHAPTER 4\\\
    # ///Squadron 6 - TEAM 2\\\
    # ///Family\\\
    # ///Luiza, Tamara, Urszula\\\

#    scene black with dissolve
#    $ renpy.pause (1.0, hard=True)
#    show text "I don't want to remember anymore." with Pause(3.0) and pixellate
#    $ renpy.pause (4.0, hard=True)
#    scene black with pixellate
#    $ renpy.pause (1.0, hard=True)
#    show text "Are you afraid of the outcome?" with Pause(3.0) and pixellate
#    $ renpy.pause (4.0, hard=True)
#    scene black with pixellate
#    $ renpy.pause (1.0, hard=True)
#    show text "I am. It always ends the same way." with Pause(3.0) and pixellate
#    $ renpy.pause (4.0, hard=True)
#    scene black with pixellate
#    $ renpy.pause (1.0, hard=True)
#    show text "Things happened the way they did, because of the choices that you made." with Pause(3.0) and pixellate
#    $ renpy.pause (4.0, hard=True)
#    scene black with pixellate
#    $ renpy.pause (1.0, hard=True)
#    show text "Then I need to choose differently." with Pause(3.0) and pixellate
#    $ renpy.pause (4.0, hard=True)
#    scene black with pixellate
#    $ renpy.pause (3.5, hard=True)

    scene black with dissolve

    show text "Chapter 4\nThe Choices We Make" with Pause(2.5)

    scene black with dissolve

    nar3 "How much of the events were you able to remember? Let's find out."

    if (count == 3):

        nar3 """A perfect score of %(count)f? Not bad.

        But how much of your recounting was true, and what parts of it were fabrications...

        ... of the way you wanted to remember it all?
        """

        jump present4

    elif (count == -3):

        nar3 """A shitty score of %(count)f.

        You really did just want to fuck everything up, didn't you? Reliving events and making them out to be more terrible...

        ... than they actually were.
        """

        jump present4

    else:

        nar3 """... What?

        A score of %(count)f? No... That shouldn't be possible. I know how it all happened. Everything. So why can't I remember this retelling of the tale?
        """

        jump present4

    label present4:

    # PATH A [Unity]

    if (count == 3):

        scene black with dissolve

        show text "Good Path\nA Story Retold" with Pause(2.5)

        scene black with dissolve

        nar2 """A few weeks had passed since our big meeting in the warehouse, and I, Sergeant Luiza Jaskólski, was given the reigns of team two.

        I hadn't expected Roza to place me into a role of leadership, and to be honest, I was quivering in my boots at the time. Still, I didn't give in to my fears.

        No matter how exhausted I was.

        Roza told me to leave everything to her, so for her to go back on her promise meant that she needed me. 

        I wasn't about to let her down.

        Or so I thought.
        """

        scene bgoutside1 with dissolve

        $ renpy.pause (1.0, hard=True)
        play sound "musicSFX/sfx/sfxkar98kfiring.wav"
        $ renpy.pause (1.0, hard=True)

        a "This is almost too easy! They keep walking down the same street!"

        t "Here, have a few more rounds Ald."

        a "Thanks! Hey Tam, do you think they see all those bodies lining the street down there?"

        t "No. I don't think they do."

        a "Yeah that's what I thought too. Here, watch this."

        nar2 """Aldona was in a prone position, the barrel of her scoped rifle sticking out through a small corner of the sandbags we had set up.

        We were holding down in an abandoned building, the uprising in full swing all around us. For every bullet fired there was a bloodcurling scream to answer.

        For every life lost another family was shattered. This went both ways. For us, and for our enemies.
        """

        play sound "musicSFX/sfx/sfxkar98kfiring.wav"
        $ renpy.pause (1.0, hard=True)

        nar2 """I peeked around the corner of the window sill in time to see an enemy soldier's helmet go flying. His head was painted red, but he was still standing. Looking around.

        Poor soul didn't realize that he was already dead.
        """

        play sound "musicSFX/sfx/sfxkar98kfiring.wav"
        $ renpy.pause (1.0, hard=True)

        nar2 "This one went clean through the soldier's shin. That one seemed to do it, because the man toppled forward onto the body ridden street."

        a "Another bites the dust at the hands of the great Aldona Andrysiak!"

        t "Aldona quit your bragging and pull the spring back. We need to have you ready with another round before more show up."

        ss "They're upstairs! Go and put holes into them!"

        l "Aldona, Tamara. It's time."

        play music "musicSFX/music/good-path.mp3" fadein 1.0

        a "Damn it, already? I was just starting to have fun!"

        nar2 """'Having fun.' She says, with blood running down her forehead and her knee covered in bandages.

        Even Tamara smiled at the girl's exclamation, and she wasn't faring any better. Both of her eyes were no longer dark brown, but a milky white.

        But we still managed to survive this long without the Russkajan's help.
        """

        ss "They're down this hallway!"

        t "Luiza..."

        nar2 "Aldona passed her rifle to Tamara, who held it out for me to take. I placed my hand on her shoulder, and she turned to face me a little better."

        t "... It's been an honor."

        nar2 "I took hold of the rifle in both hands, and nodded to her."

        l "It's been an honor, Tamara Szwedko. Aldona Andrysiak."

        ss "Right behind this door! Get it open!"

        ss "I can't open it, sir! It's been blockaded!"

        a "Luiza, hurry."

        nar2 """I pressed the barrel of the rifle to Tamara's throat. She was staring at me, but I know that she couldn't see me. Knowing that made me feel a little better.

        Tamara grasped the gun with both hands, and tilted it upwards. Slowly. My finger crawled for the trigger.
        """

        ss "Get this fucking door open or we'll blow it to pieces!"

        nar2 "I pressed the trigger"

        play sound "musicSFX/sfx/sfxkar98kfiring.wav"
        $ renpy.pause (1.0, hard=True)

        nar2 """and it rained blood.

        Tamara's body fell lifelessly against my own before crumpling to the ground, like paper.
        """

        a "H-hurry up Luiza. I don't have all day you know."

        nar2 """Aldona sounded like her usual self, but by the heaving of her shoulders I could tell that she was crying.

        I was, too.

        I stepped around Tamara's corpse, and stood over Aldona from where she still lay. The barrel of the gun kissed the back of her head.
        """

        a "DO IT!"

        nar2 "She yelled, and I didn't hesitate."

        play sound "musicSFX/sfx/sfxkar98kfiring.wav"
        $ renpy.pause (1.0, hard=True)

        nar2 """Her head smacked into the ground as the round pierced through the back of her skull, spraying me with more blood and grey matter.

        The barricade we had set up beforehand, came crashing down. One wooden crate after another.
        """

        ss "There they are!"

        nar2 "I held the rifle underneath my chin, next. Prepared to make my own departure. I pulled the trigger."

        $ renpy.pause (1.0, hard=True)
        nar2 """Click.

        I should have saved a bullet for myself, but at least this gave me a few seconds longer to say:
        """

        l "Roza..."

        ss "Drop dead, bastard!"

        l "... I'm sorry."

        jump present5

    # PATH B [Destruction]

    elif (count == -3):

        scene black with dissolve

        show text "Bad Path\nBringing Everything to a Closure" with Pause(2.5)

        scene black with dissolve

        nar2 """A few weeks had passed since I was given charge of team two. I didn't think that Roza would assign me such a role.

        I should have told her no when I had the choice.

        Because everything went downhill from the moment we split up back then.

        I don't know whether to feel angry at Roza for doing this to me, when she promised me that she would take care of everything.

        Or should I feel sad, that I was dumped with another burden I had to carry? The weight of which heavy enough to break my back and force me to my knees.
        """

        scene bgoutside1 with dissolve

        t "Aldona, put your fucking gun down!"

        a "You first!"

        nar2 "Aldona and Tamara's relationship had deteriorated rapidly. From arguments, to throwing punches, to finally..."

        t "It's your fault that the uprising started sooner than it should've!"

        a "I didn't do anything! You just want someone to pin the blame on!"

        nar2 """... and there I was. Standing off to the side while the two girls I was tasked with protecting pointed guns at one another. In the dead center of a wartorn street.

        As if they had forgotten everything that happened back at the warehouse.
        """

        t "Accept your mistake and we can get over this!"

        a "I won't accept it because I've done nothing wrong!"

        t "You started everything! You ruined everything! Just like I said you would!"

        nar2 """I'm so tired of it all.

        The sleepless nights, the fearful days.

        The help from the Russkajans that never came.

        Friends becoming the enemy.

        Alongside broken promises.

        I'm just so 

        tired

        of it all."""

        play music "musicSFX/music/bad-path.mp3" fadein 1.0

        menu:

            "I pointed the barrel of my pistol at Tamara.":
                jump kill_tam

            "I pointed the barrel of my pistol at Aldona.":
                jump kill_ald

            "I did absolutely nothing.":
                jump do_nothing

        label kill_tam:

        t "Are you really going to side with her, Luiza!?"

        l "You're bringing us apart, Tamara."

        t "Roza should've never appointed you as leader of team two to begin with."

        l "It doesn't matter now. Because we're all going to die anyway."

        t "Then do it! Kill me! Pull the fucking trigger!"

        nar2 "I didn't get the chance to. Because a single shot from my right popped Tamara's head like a bubble. Her body collapsed backwards onto the paved road."

        a "I-I..."

        nar2 "Aldona dropped the rifle she had been carrying, the weapon clattering to the ground."

        a "I didn't mean to."

        nar2 "She fell to her knees."

        a "I didn't mean to kill her. I was just so angry because of the things she said..."

        l "Don't worry."

        a "Why did I have to..."

        l "We'll be following her soon."


        play sound "musicSFX/sfx/sfxtankturretrotating.wav"
        $ renpy.pause (3.0, hard=True)

        nar2 """A tank had been creeping along down the street, its engine roaring with the power it needed to drive the monster of a vehicle forwards.

        Soldiers flanked its sides. All of them came to a stop as the tank slowed to a halt, and meticulously swiveled its turret to face us.

        And for the first time in weeks.

        I was happy.
        """

        l "Goodbye."

        play sound "musicSFX/sfx/sfxtigertankfiring.wav"
        $ renpy.pause (2.0, hard=True)

        jump present5

        label kill_ald:

        a "So you're going to betray me too, Luiza?"

        l "You're bringing us down, Aldona."

        a "Meaning you're going to get rid of me?"

        l "We can't continue on like this. One of us has to go."

        a "Roza never should've made you the leader! She should've chosen me!"

        l "You lost your chance when you committed your fatal mistake."

        a "I'll fucking kill you!"

        nar2 """Aldona shifted her feet and the barrel of her rifle from Tamara, to me. Before I could fire, I saw a bright yellow flash and a puff of smoke.

        I collapsed backwards from the force of the impact. The bullet had pierced my stomach, and forced the air out of my lungs.

        I couldn't breath, and as I lay there staring at the light blue sea above. I realized that I was finally going to be at peace.
        """

        unk "Luiza."

        nar2 "I couldn't see. Everything was so foggy. Everything hurt."

        t """It's Tamara. 

        Aldona's dead.

        I killed her.
        """

        nar2 "This was it. Before blood could fill my throat, I murmured to her my last words:"

        l "Kill. Me."

        nar2 """We weren't going to survive. This was the end, and I knew it. There was a buzzing in my ears, and I recognized it as the noise of an engine.

        It had to have been a tank, but it was nothing I had to worry about anymore. 

        Because I...
        """

        play sound "musicSFX/sfx/sfxtankturretrotating.wav"
        $ renpy.pause (3.0, hard=True)

        t "Rest easy, Luiza."

        play sound "musicSFX/sfx/sfxtigertankfiring.wav"
        $ renpy.pause (2.0, hard=True)

        jump present5

        label do_nothing:

        a "You never really did understand me, Tam."

        t """I've always understood you. Understood that you're a selfish cunt that's always concerned with what her next achievement will be.

        So that you can brag about it all week, but not this time.

        Because this time,

        you earned your last accomplishment.
        """

        nar2 "Aldona lowered her rifle, and for a second I thought that everything would be alright."

        a """That's really how you saw me, Tamara?

        After all of those years we lived together in the capital, making do with what we had taken from others.

        Now is when you choose to show me what you really think?
        """

        t "That's right."

        a "We can still put our guns down."

        t "You and I both know that we're past the point of forgiveness."

        a "Want to steal then? One last time?"

        nar2 "Aldona raised her rifle, Tamara's already trained on her friend."

        t "Yeah. This will be the final time we take something."

        nar2 "The two girls nodded to each other, and Tamara held up three fingers. Then two."

        a "I'll miss you, Tam."

        nar2 "One."

        t "I'll miss you too, Ald."

        nar2 """They fired in unison, and fell back together. One died on one end of the street, while the other died on the other end.

        Now it was just me and my thoughts.

        Roza.

        I wish you had been here with me.
        """

        menu:

            "I pointed the barrel of my pistol to my head.":
                jump kill_yourself

        label kill_yourself:

        l """Forgive me, Roza.

        I wasn't able to protect them.
        """

        jump present5

    # PATH C [Broken Wing]

    else:

        scene black with dissolve

        show text "Secret Path\nCollection of the Archives" with Pause(1.5)

        scene black with dissolve

        l "This is Sergeant Luiza Jaskólski. Leader of Team 2."

        play music "musicSFX/music/secret-path.mp3" fadein 1.0

        scene bgoutside2 with dissolve

        l """Roza. I know you can't hear me. You're probably off fighting somewhere else in Warszawa, but I...

        ... I wanted to let you know that I let you down, and that I'm sorry.

        I failed to take care of the girls you placed under my care those weeks ago.

        I know how you had a lot of confidence in me. I only wish I could've been as confident as you believed me to be.

        There are so many blown out windows. Homes with missing doors. Walls painted dark red from dried blood. 

        The smell of death lingering so heavily in the air that it makes it hard for me to breathe.

        I can still hear the sound of gunfire in the distance.

        I know I should be hiding, but I want to see you.

        One last time.

        Please, Roza.

        Where are you?
        """
    
        jump present5

    label present5:

    # ///CHAPTER 5\\\
    # ///Squadron 6 - TEAM 1\\\
    # ///Squadron\\\
    # ///Rozalia, Serafina, Aldona\\\

    scene black with dissolve

    show text "Chapter 5\nThe Promises We Break" with Pause(2.5)

    scene black with dissolve

    # PATH A [Unity]

    if (count == 3):

        scene black with dissolve

        show text "Good Path\nA Story Retold" with Pause(2.5)

        scene black with dissolve

        nar """I am Lieutenant Rozalia Rowecki, leader of Team 1. Part of the Warszawan Home Army. 

        The crumbling, Warszawan Home Army.

        Yet even as it all fell to pieces. My girls and I still stand to represent the hope of the Warszawan people.

        And though our corpses may join those of our friends and family on the side of the road.

        Discarded.

        Abandoned.

        We stand, and continue to hang onto the hope that fueled us. A different hope. One that doesn't depend on the Russkajans to help us.
        """ 

        scene bgwarehouse with dissolve

        ss "Find the traitor among the two rats, and kill her!"

        nar """We were well hidden behind a corner. It'd be some time before the soldiers found us, so I decided to glance in Serafina's direction.

        To tell her what had been on my mind since the beginning.
        """

        r "They're talking about you, aren't they?"

        nar "I received a nod in return."

        r "But why?"

        s "Why what?"

        r "Why did you side with the Kämpfer soldiers?"

        s "Because it guaranteed me and my family's safety."

        r "Then why are you here with us?"

        nar "I could hear boots below, as men scrambled to pinpoint our position. Serafina shook her head, her hair brushing against her shoulders."

        s "Because of a silly promise I made to your friend."

        r "Luiza?"

        nar """I think I remembered. How Luiza had stayed back to say something to Serafina, before our meeting in the warehouse.

        I think I remembered too, how jealous I felt that I hadn't been made privy to their secret.
        """

        r "What exactly did she tell you?"

        ss "Send some men to check the catwalks on the second floor."

        nar """Urszula huddled close to my back. I could feel each of her breaths against my neck, but I didn't let it distract me.

        I looked away from Serafina and glared attentively at the door on the other end of the catwalk.
        """

        u "T-they're going to find us up here."

        r "We'll be alright."

        nar "I was a liar to the very end."

        r "Serafina, tell me. What did Luiza tell you?"

        s "She didn't tell me anything."

        r "Then what?"

        s "She asked for my help. In helping you protect the girls that you're so fond of."

        r "Luiza..."

        nar """I had been jealous of them for nothing.

        But this realization made me feel something powerful.

        Longing.

        I missed Luiza.
        """

        r "We'll protect them all, Serafina. I promi-"

        u "T-they're here!"

        nar "I saw the door at the far side open, and the moment I saw a helmet come into view I fired two rounds from my handgun."

        play sound "musicSFX/sfx/sfxwaltherppkdoubletap.wav"
        $ renpy.pause (1.0, hard=True)

        nar"One bullet missed and ricocheted off of the metal hinges on the door, but the second struck true right between the soldier's eyes."

        ss "Hear that?! Second floor of the warehouse!"

        r "We need to get out of here fast. Take the stairs behind us. Let's go."

        nar "I held onto Urszula's shoulder as I spun myself around and made for the staircase. Serafina and Urszula followed close behind."

        ss "We've taken the catwalks! Cut across and gun them down!"

        nar "I made it to the first base of the stairs, but when I turned the corner to continue onto the last flight of steps-"

        ss "You're surrounded."

        nar """Boots clanged against metal, and within seconds the soldiers cut off our exit from the top.

        Here we were, the three of us trapped like cornered rats. Up. Down. It didn't matter where we looked. Guns were trained on us.

        I bit my lip until it bled. Until I could taste the iron on my tongue.
        """

        r "Shit."

        nar "One of the men dressed in uniform and tie, stepped forth. He wasn't wearing a helmet like the others, but an officer's cap."

        dd """So much for the resistance, hm? If that gun hadn't been stolen those weeks ago, maybe you would've had better time to prepare.

        Not like it would have mattered, because I assure you the outcome would have been the same.
        """

        r "Cut the bullshit."

        nar "I held out my arm to shield the two girls behind me."

        dd "I wouldn't make anymore sudden movements if I were you."

        r "You're going to kill us anyway."

        nar "The officer tilted his chin in our direction."

        dd "The girl."

        r "Which one?"

        dd "The traitor."

        s "Traitor? I was only doing what I had to do."

        dd "What do you mean?"

        nar "Serafina slowly stepped forward. The soldiers backed up equally as slow, their weapons prepared to fire."

        s "I was the one that helped bring about the downfall of the Warszawan uprising."

        r "Serafina, you-"

        nar "I couldn't believe what I was listening to and apparently neither could the officer, who laughed from the base of the stairs."

        s "You laugh, but I set these rebels up for their demise. You can't deny me that."

        dd "Ah, but how right you are Serafina Kosmatka. Or should I say, Anna Engel."

        nar """I felt my fingers begin to go slack around the grip of my pistol.

        For how long had Serafina been lying to me? To us?
        """

        dd "This must come as a shock to your friends, but nothing to fear or regret over. They won't live long enough to feel either."

        s "I'll be taking my gun back now."

        nar """Serafina took the handgun from my hands, and pressed the barrel to Urszula's abdomen.

        This had to be some cruel circus act. A play gone wrong. It had to be.
        """

        u "S-Serafina..."

        s "Your executions start now. They'll be overseen by myself, and the officer here."

        dd "Go on."

        nar "I looked up the stairs. The soldiers were still there, watching. I glanced down the steps. More soldiers. There was nowhere to go. Nowhere, except-"

        play sound "musicSFX/sfx/sfxwaltherppkfire.wav"
        $ renpy.pause (1.0, hard=True)

        nar"""Urszula screamed as a bullet shot through her body, but Serafina wasn't done yet. While she was still screaming, the grey eyed smoker- traitor- shoved her out the window behind us.

        I could still hear her screams as she plummeted to the earth.

        Then silence.

        Serafina came over to me next, the barrel of her gun to my stomach.
        """

        r "You broke your promise to Luiza."

        s "You're one to talk about broken promises."

        nar "I grit my teeth as Serafina leaned in close to my ear, and whispered:"

        s "Forgive me."

        play sound "musicSFX/sfx/sfxwaltherppkfire.wav"
        $ renpy.pause (1.0, hard=True)

        nar "The hot piece of metal pierced my skin and flesh. I gasped from the shock."

        r "I-I won't... forget this... Sera...fina."

        nar "She stepped away from me, as I staggered backwards, holding my abdomen."

        s "You won't be alive to remember."

        nar """I watched as the men relaxed, guns lowering just as the back of my knees smacked against the window sill. I went right over.

        The ground became the sky, and as I fell out of the second story window I wondered if my death would come quick. If my head would crack against the pavement waiting below.

        The last I saw of Serafina, she was placing her hand on the Kämpfer officer's shoulder. All friendly-like. That, was when I heard-
        """

        play sound "musicSFX/sfx/sfxwaltherppkfire.wav"
        $ renpy.pause (1.0, hard=True)

        nar """- and I wondered, seconds before my body struck the ground 

        who that bullet had been for."""

        jump present6

    # PATH B [Destruction]

    elif (count == -3):

        scene black with dissolve

        show text "Bad Path\nBringing Everything to a Closure" with Pause(2.5)

        scene black with dissolve

        nar """I am Lieutenant Rozalia Rowecki. Leader of Team 1 partaking in the Warszawan uprising.

        The enemy had been hounding away at us at every corner. As if they knew everywhere we were going before we could get there.

        I had my suspicions that one of the two girls I was in charge of was a traitor. Maybe they both were.

        I raised my hand as a signal for us to stop at the base of the steps, halfway to the second floor of the warehouse.
        """

        scene bgwarehouse with dissolve

        u "I-Is something wrong, Roza?"

        nar """Yes. Something was wrong.

        And I was about to figure out why that was. Right here. Right now. Even as our enemy circled ever closer, like vultures or a pack of wolves.
        """

        menu:

            "I accused Urszula of being the mole among us.":
                jump accuse_urszula

            "I accused Serafina of being the mole among us.":
                jump accuse_serafina

        label accuse_urszula:

        nar "I turned to face Urszula, and looked her straight in the eyes."

        r "You're the traitor."

        u "I-I'm what?!"

        nar "She sounded genuinely surprised, but I expected nothing less of a woman who could pretend to care about others so much."

        r "You were always so quiet around us. Back when the six of us were all together. Even these last couple of weeks, you've been as silent as a mouse."

        u "B-but I've never done anything wrong to you or anyone else, Rozalia!"

        r "That's because you've been selling us out behind our fucking backs!"

        nar "I raised my voice at her, and that made everything clear in her head that I wasn't joking. A look of dread appeared on her face, as she frantically shook her head."

        u "I've only ever wanted what was best for all of us Rozalia. Please. L-listen to what I'm saying!"

        r "I don't listen to traitors."

        nar "I came closer to her, and jabbed my index finger against her stomach as I got close and personal with her."

        r """I knew something had been driving me up the wall. I just didn't expect it to be you. 

        Your reaction has confirmed it to me, though. 

        That you really are the traitor.
        """

        u "Rozalia you've got it all wrong!"

        nar "She pushed me away, so I tried to reach for her again."

        r "Shut-"

        play sound "musicSFX/sfx/sfxwaltherppkfire.wav"
        $ renpy.pause (1.0, hard=True)

        nar """I screamed, and held my wound. With blood quickly oozing between my fingers, I immediately knew

        I wasn't going to make it.
        """

        s "You disgust me, Lieutenant Rowecki."

        nar "I turned to face Serafina, who was holding a handgun with a smoking barrel."

        r "S-Serafina...?"

        nar "It was becoming difficult for me to breathe. I was barely standing on my own two feet."

        s """I made a promise to your friend Luiza to help keep your girls safe. 

        Yet here I am, witnessing our great leader accusing one of the same girls she tasked herself with protecting.
        """

        r "S-she's a fucking t-traitor, and you know it."

        s "You keep telling yourself that."

        nar "Serafina raised her gun to my head"

        s "Asshole."

        jump present6

        label accuse_serafina:

        nar "I turned to face Serafina, and looked her straight in the eyes."

        r "You're the traitor."

        nar "She said nothing at first, the two of us making eye contact. Staring at each other in silence."

        u "W-what?!"

        nar """Serafina cracked a smile, and started chuckling. Then chuckling turned into laughter. She laughed so much that she had to hold her stomach.

        I'm clueless as to what she had found so amusing.
        """

        s "You had me going there for a second, oh great leader."

        nar "Serafina wiped the tears from her eyes."

        s "That's the most I've laughed in awhile. Thank you."

        nar "I said nothing, and only stared. Urszula was hanging off to the side with a look of concern written on her face."

        s "Oh. Wait. You're actually serious, aren't you?"

        r "It's not a coincidence that the soldiers were able to track us down no matter where we went."

        s "And what does that have to do with me?"

        nar "I shoved Serafina against the wall, and pinned her there with my hands to either side of her head. Forcing her to look at me."

        r "You were almost always missing in the mornings. Were did you go, because I know for a damn fact that you didn't disappear for so long just to have a fucking smoke break."

        s """You're right. It wasn't a smoke break. 

        It was a piss break.
        """

        nar "I reeled back an arm and punched the wall inches away from Serafina's face. It hurt my knuckles, but I could care less."

        r "Why are you acting so full of yourself now? Because you've been caught? Because the jig is finally up?"

        u "R-Roza..."

        r "Don't fucking bother me right now, Urszula! I'm busy dealing with a damned rat!"

        nar "Serafina was smirking away at me. Saying absolutely nothing at all."

        u "... R-Roza, we're surrounded..."

        r "W-what did you say?!"

        nar """I looked away from Serafina for one second.

        That.

        Was my mistake.
        """

        play sound "musicSFX/sfx/sfxwaltherppkfire.wav"
        $ renpy.pause (1.0, hard=True)

        nar """I tried to scream, but all I did was gurgle blood. I collapsed to the floor on my back, and glared up at Serafina.

        There was nothing I could do, as I stared at my killer holding a pistol in her hand. She was saying something, but I could only make out bits and pieces.
        """

        s "... Soldiers... them know..."

        u "... They're... their way..."

        s "... Good..."

        nar """I tried again to make some kind of sound, but again. Blood was all that came out. A trembling seized my body, and colors started to fade.

        The look on Serafina's face was... sad. 

        Why?

        Urszula knelt down beside me.

        How long had they been working together?
        """

        u "... Almost... gone."

        s "... Should've... not pried... much. Roza..."

        nar """Ah...

        ... What did it matter.

        I think I'll... close my eyes... and... 

        ... rest for a little while.

        Good night, Luiza.

        I hope you don't get mad at me for... falling... asleep...

        ... a... gain...
        """

        jump present6

    # PATH C [Broken Wing]

    else:

        scene black with dissolve

        show text "Secret Path\nCollection of the Archives" with Pause(2.5)

        scene black with dissolve

        nar "I am Lieutenant Rozalia Rowecki. Leader of Team 1."

        scene bgoutside2 with dissolve

        nar """I lost Serafina and Urszula. We were supposed to have raided the warehouse that the soldiers had repurposed into an armory.

        But by the time morning came around, the two of them were still missing. I had searched everywhere for them last night, whispering their names in the dark.

        No one answered. So I assumed the worst.

        I thought I had done my best to protect them. Even Serafina, who I wanted to keep an eye on. Just in case. I still watched the both of their backs.
        """

        r "My best wasn't good enough. I, wasn't good enough."

        nar """I kicked a pebble down an empty street.

        I could hear the sound of gunfire nearby, but I didn't pay it any mind.

        I know I should be in hiding, but I honestly can't bring myself to take shelter. 

        Not when I know that my girls could still be out there.
        """

        r "Luiza. I miss you."

        nar """I wish I got the chance to see her.

        At the very least,

        one last time.
        """

        jump present6

    label present6:

    # ///CHAPTER 6\\\
    # ///THE END\\\

    scene black with dissolve

    show text "Chapter 6\nThe Lives That We Take" with Pause(2.5)

    scene black with dissolve

    # PATH A [Unity]

    if (count == 3):

        scene black with dissolve

        show text "Good Path\nA Story Retold" with Pause(2.5)

        scene black with dissolve

        nar """I opened my eyes and was greeted immediately by a cloudy sky.

        I leaned up to find a second pair of legs sticking out from underneath my own, the realization that I might have gone unconcious on top of someone hit me.

        So I turned around to see who it was.

        Urszula.
        """

        nar """I got off her and shook Urszula.

        She must have broken my fall.
        """

        r "Urszula. Urszula wake up."

        nar "She refused to stir. I flipped her over quietly, and realized why."

        r "Son of a bitch."

        nar """Urszula was bleeding profusely from the forehead... Poor girl. I hugged her limp body, and didn't let her go for a short while.

        A flurry of gunshots from the window I had fallen out of drew my eyes upwards- slowly. Something must've had happened, but I can't sit around and figure out what.

        I had to move.

        While I still could.

        The question was where?
        """

        scene bgoutside1 with dissolve

        nar """I wandered aimlessly with the tattered remains of a shirt wrapped around my wound, ducking into alleyways whenever I heard the distant sound of machinery or gunfire.

        I grew hungry quickly, and with the blood that I had lost I was woozy. Navigating my way around the city became too difficult for me. 

        My end was near.

        I picked a random house to hole up in, where I could I succumb to my injuries in peace. This was the only thing I still had control over. 

        Where I was to die.

        I navigated up the stairs of a quiet three-story house,

        and checked the final room on the third floor.

        To my disbelief I happened to come across,

        Aldona. Tamara.

        And to my horror...
        """

        r "... Luiza."

        nar """No. 

        No no no no.

        No no no no no no no no.
        """

        nar "I knelt down and wrapped my arms around Luiza. Her dimmed blue eyes stared up at me. I took her to a corner of the room, and hugged her lifeless body close to my own."

        nar """ This was not the way I had expected things would go.

        We were meant to have finished our story, hand in hand. Me and my girls. Why, am I the only one of them all that still breathes?

        Why.

        Oh why.

        Am I the only one,

        that is still breathing?
        """

        jump present8

    # PATH B [Destruction]

    elif (count == -3):

        scene black with dissolve

        show text "Bad Path\nBringing Everything to a Closure" with Pause(2.5)

        scene black with dissolve

        u "She's dead, Anna."

        scene bgwarehouse with dissolve

        nar3 "I holstered my gun."

        s "Any reports about Team 2?"

        u "They ran into mechanized infantry. All three were confirmed KIA by the tank's gunner."

        s "So."

        u "They're all dead."

        nar3 "I squatted next to the Lieutenant's corpse."

        s "You must've been tired of talking like that, Sonje."

        u "The stutter? I was starting to grow quite fond of it."

        nar3 "I cupped the Lieutenant's cheek with my hand. Still warm. She'll go cold soon."

        u "What now?"

        s "Nothing we can do except wait until the rest of the uprising is crushed."

        u "I'm still a little sour that things had to go this way."

        s "As am I. I kind of liked this group of girls. Too bad their leader wasn't too bright."

        u "She cared about them."

        s "... I know."

        nar3 "I stood up and wiped the blood from the palm of my hand against my pants."

        s "Their story had reached its end, but ours was still continuing."

        u "Aren't you the least bit excited, Anna?"

        s "That we're a little closer to achieving our freedom? I am."

        u "We need to make sure to stay ahead of everyone else."

        s "We have to. They'll shove us forward otherwise, and make us keep going regardless."

        u "And if we can't keep up, we're as good as dead."

        nar3 "I placed a fresh cigarette between my lips, and lit it."

        s "Such is the life of those condemned to the penal unit, Sonje."

        nar3 "I exhaled a thin stream of smoke from the corner of my lips."

        s "Let's go."

        jump present8

    else:

        scene black with dissolve

        show text "Secret Path\nCollection of the Archives" with Pause(2.5)

        scene black with dissolve

        scene bgoutside2 with dissolve

        nar "I see a figure in the distance."

        nar2 "I'm certain it's a soldier come to put me to rest."

        nar "I want to come closer, but I don't know if I should."

        nar2 "They should've shot me by now, but they haven't done so."

        nar "I decide to risk it and come closer, out of curiosity."

        nar2 "Wait, I think that's..."

        r "Luiza?"

        l "Rozalia?"

        nar "I can't believe she is still alive."

        nar2 "Is this a miracle?"

        nar "I jog halfway."

        nar2 "And meet her at the center of the crossroads."

        nar "I wrap my arms around her."

        nar2 "And hold her close."

        r "I missed you, Luiz."

        l "I missed you too, Roza."

        nar "Tears are welling up in my eyes."

        nar2 "I can't hold them back for long."

        nar "I wish this moment could last forever."

        nar2 "But war is cruel."

        nar "It takes everything important from us."

        nar2 "And gives nothing in return."

        nar4 "Only death."

        nar2 "And as the soldiers come marching down the streets from all sides."

        nar "I remember to ask a very important question."

        nar2 "That I'll provide the answer to."

        r "Luiza, do you love me?"

        l "I do, Rozalia. I love you."

        r "I love you too, Luiza."

        jump present7

    label present7:

    scene black with dissolve

    scene bgoffice with dissolve

    unk "Is that going to be your latest addition to your collection, Emmanuel?"

    em "Yes. Yes I believe it will be."

    unk "Why did you decide to write this all?"

    em """Because the women of Warsaw were strong and fierce. 

    Because no matter how many sons and daughters they had lost, they lived on with the pain of loss deeply entrenched within their hearts.

    Even as their home and those of others burned all around them.
    """

    unk "Well said, Emmanuel Ringelblum. I'll add this piece to the archives then."

    em "Very good."

    unk "Ah, there was one question I had."

    em "Go on."

    unk "Why didn't you decide to give them a happy ending?"

    em "Because to allow them a chance to escape their fate, was to disrespect the lives lost during the Warsaw uprising."

    jump present8

    label present8:

    scene black with dissolve

    show text "The Choices of the Few\nThe End." with Pause(2.5)
    $ renpy.pause (3.0, hard=True)

    stop music fadeout 1.0

    scene black with dissolve

    show text "Fin." with Pause(2.5)
    $ renpy.pause (3.0, hard=True)

    # This ends the game.

    return
