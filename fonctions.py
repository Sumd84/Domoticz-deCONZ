#!/usr/bin/env python3
# coding: utf-8 -*-

def rgb_to_xy(rgb):
	''' convert rgb tuple to xy tuple '''
	red, green, blue = rgb
	r = ((red + 0.055) / (1.0 + 0.055))**2.4 if (red > 0.04045) else (red / 12.92)
	g = ((green + 0.055) / (1.0 + 0.055))**2.4 if (green > 0.04045) else (green / 12.92)
	b = ((blue + 0.055) / (1.0 + 0.055))**2.4 if (blue > 0.04045) else (blue / 12.92)
	X = r * 0.664511 + g * 0.154324 + b * 0.162028
	Y = r * 0.283881 + g * 0.668433 + b * 0.047685
	Z = r * 0.000088 + g * 0.072310 + b * 0.986039
	cx = 0
	cy = 0
	if (X + Y + Z) != 0:
		cx = X / (X + Y + Z)
		cy = Y / (X + Y + Z)
	return (cx, cy)

def rgb_to_hsl(rgb):
	''' convert rgb tuple to hls tuple '''
	r, g, b = rgb
	r = float(r/255)
	g = float(g/255)
	b = float(b/255)
	high = max(r, g, b)
	low = min(r, g, b)
	h, s, l = ((high + low) / 2,)*3

	if high == low:
		h = 0.0
		s = 0.0
	else:
		d = high - low
		s = d / (2 - high - low) if l > 0.5 else d / (high + low)
		h = {
			r: (g - b) / d + (6 if g < b else 0),
			g: (b - r) / d + 2,
			b: (r - g) / d + 4,
		}[high]
		h /= 6

	return h, s, l
    
def xy_to_rgb(x, y, brightness = 1):
    
    x = float(x);
    y = float(y);
    z = 1.0 - x - y;
    
    Y = brightness; 
    X = (Y / y) * x;
    Z = (Y / y) * z;
    
    r =  X * 1.656492 - Y * 0.354851 - Z * 0.255038;
    g = -X * 0.707196 + Y * 1.655397 + Z * 0.036152;
    b =  X * 0.051713 - Y * 0.121364 + Z * 1.011530;
  
    r = 12.92 * r if r <= 0.0031308 else (1.0 + 0.055) * pow(r, (1.0 / 2.4)) - 0.055
    g = 12.92 * g if g <= 0.0031308 else (1.0 + 0.055) * pow(g, (1.0 / 2.4)) - 0.055
    b = 12.92 * b if b <= 0.0031308 else (1.0 + 0.055) * pow(b, (1.0 / 2.4)) - 0.055

    return {'r': round(r * 255, 0), 'g': round(g * 255, 0), 'b': round(b * 255, 0)}