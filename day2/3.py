# Q3 Write a Python program that reads a JSON file containing NASA APOD data and prints the keys: "explanation","Title"
# Use this link to copy your json data (do not use request module, just save the Json to a variable then do json operation)
# JSON Data url: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

json_data = {"copyright":"Gianni Tumino","date":"2024-07-05","explanation":"A glow from the summit of Mount Etna, famous active stratovolcano of planet Earth, stands out along the horizon in this mountain and night skyscape. Bands of diffuse light from congeries of innumerable stars along the Milky Way galaxy stretch across the sky above. In silhouette, the Milky Way's massive dust clouds are clumped along the galactic plane. But also familiar to northern skygazers are bright stars Deneb, Vega, and Altair, the Summer Triangle straddling dark nebulae and luminous star clouds poised over the volcanic peak. The deep combined exposures also reveal the light of active star forming regions along the Milky Way, echoing Etna's ruddy hue in the northern hemisphere summer's night.","hdurl":"https://apod.nasa.gov/apod/image/2407/GianniTumino_Etna&MW_14mm_JPG_LOGO__2048pix.jpg","media_type":"image","service_version":"v1","title":"Mount Etna Milky Way","url":"https://apod.nasa.gov/apod/image/2407/GianniTumino_Etna&MW_14mm_JPG_LOGO__1024pix.jpg"}

print("Explanation: ", json_data["explanation"])

print("Title: ", json_data["title"])