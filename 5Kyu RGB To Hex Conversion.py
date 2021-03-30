def rgb(r, g, b):
    r = str(hex(r if r <= 255 else 255 )[2:].zfill(2)).upper() if r > 0 else "00" 
    g = str(hex(g if g <= 255 else 255 )[2:].zfill(2)).upper() if g > 0 else "00" 
    b = str(hex(b if b <= 255 else 255 )[2:].zfill(2)).upper() if b > 0 else "00"     
    
    return(f"{r}{g}{b}")

print(rgb(0,0,0),"000000", "testing zero values")
print(rgb(1,2,3),"010203", "testing near zero values")
print(rgb(255,255,255), "FFFFFF", "testing max values")
print(rgb(254,253,252), "FEFDFC", "testing near max values")
print(rgb(-20,275,125), "00FF7D", "testing out of range values")