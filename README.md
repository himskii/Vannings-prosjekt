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

Det er lagt til pauser mellon relay aktivering og deaktivering når betingelsene er oppnåd. Det blir bare korte intervaller av vanning for å unngå og overvanne planten.

