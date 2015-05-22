import io
import csv
import json
import re

allNames = ['astro_Jfrancois', 'astro_timpeake', 'Thom_astro', 'Astro_Alex', 'AstroSamantha', 'astro_luca', 'astro_andre', 'astro_paolo', 'Astro_Andreas', 'CFuglesang', 'ESA_EAC', 'esa', 'esaoperations', 'Astro_Satoshi', 'Astro_Wakata', 'Astro_Soichi', 'Astro_Kimiya', 'JAXA_en', 'Aki_Hoshide', 'csa_asc', 'asc_csa', 'Astro_Jeremy', 'Astro_DavidS', 'AstroDaveMD', 'Cmdr_Hadfield', 'RobertaBondar', 'RobertThirsk', 'AstroGarneau', 'fka_roscosmos', 'spacetihon', 'OlegMKS', 'Msuraev', 'AntonAstrey', 'NASA', 'NASA_Astronauts', 'NASAPeople', 'AstroClass2013', 'SciAstro', 'Astro_Flow', 'Astro_Cady', 'Astro_Ferg', 'AstroCoastie', 'astro_Pettit', 'AstroDot', 'Astro_Wheels', 'Astro_Doug', 'Astro_Taz', 'Astro_Box', 'Astro2fish', 'Astro_Jeff', 'AstroAcaba', 'AstroKarenN', 'Astro_Kate7', 'astro_kjell', 'Astro_127', 'AstroIronMike', 'foreman_mike', 'astro_aggie', 'AstroIllini', 'Astro_Mike', 'Astro_Nicholas', 'Astro_Nicole', 'astro_reid', 'Astro_Rex', 'AstroRM', 'Astro_Ron', 'Astro_Sandy', 'AstroSerena', 'StationCDRKelly', 'Astro_Maker', 'Astro_Suni', 'AstroTerry', 'astro_tim', 'AstroMarshburn', 'Astro_TJ', 'Chief_Astronaut', 'Commercial_Crew', 'DESERT_RATS', 'HMP', 'ISS_Research', 'NASAMightyEagle', 'NASA_NEEMO', 'NASA_Orion', 'PavilionLake', 'MorpheusLander', 'AstroRobonaut', 'NASA_SLS', 'Astro_Clay']

allFollowers = []

for name in allNames:
    memFollows = []
    memFollows.extend(line.strip() for line in open("../"+name+'_followers.json'))
    allFollowers.append(len(memFollows))

print allFollowers
print max(allFollowers)
print min(allFollowers)
