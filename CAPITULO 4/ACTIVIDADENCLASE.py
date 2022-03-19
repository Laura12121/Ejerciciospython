from difflib import Match

color= "#FF1234"
match color:
    case  "#FF1234" :
        print("🔴")
    case  "#56FF78" :
        print("🟢")
    case   "#1267FF" :
         print("🔵")
    case _: 
        print("Unknown color!")
        
