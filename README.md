# Vannings-prosjekt
Kode og README for automatisert vannings pumpe. Raspberry PI prosjekt.

Når du kjører programmet, så får du bestemme mellom en automatisert aktivering eller manuell aktivering.

Sånn her funker de:

Automatisert: 
        En fuktighetssensor som aktiverer pumpen når vann IKKE blir funnet. 
        Sensoren får relay til å lukke kretsen mellom kraft kilden og pumpen, og aktiverer da pumpen.

Manuellt:
        En switch som skrur pumpen på mens den er holdt inne.
        Switchen får relay til å lukke kretsen mellom kraft kilden og pumpen, og aktiverer da pumpen.

Det er lagt til pauser mellon relay aktivering og deaktivering når betingelsene er oppnåd. Dette fører til korte intervaller av vanning for å unngå å overvanne planten.

Hvis du vil få bygd dette hjemme:
     Utstyr nødvendig:
             
             Raspberry PI (Model 4 blir brukt i min)
             Minst 20 jumper cables (Kan trenge flere dersom du vil ha mer rekkevidde)
             En fuktighetssensor (Finnes i Microbit:Tinker kit)
             Relay
             En vann pumpe
             (Plast rør dersom du trenger rekkevidde)
             En switch (Finnes i Microbit:Tinker kit)
             Breadboard (Ikke nødvendig)


Hvordan alt teknisk blir satt opp:  https://github.com/himskii/Vannings-prosjekt/assets/127395019/7f2cb3e2-2098-440f-9a40-8405b5cb84b5




