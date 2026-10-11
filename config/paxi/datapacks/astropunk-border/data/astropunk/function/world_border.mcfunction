# Cap the vanilla border at Cosmonautics' recommended diameter.
# Preserve any smaller border and leave its center unchanged.
scoreboard objectives add ap_border_init dummy
execute in minecraft:overworld store result score #width ap_border_init run worldborder get
execute in minecraft:overworld if score #width ap_border_init matches 40001.. run worldborder set 40000
scoreboard objectives remove ap_border_init
