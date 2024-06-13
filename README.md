# minecraft-texturepack-creator
## where to find default minecraft texture pack (windows)
1. Press Win + R and search ```%appdata%```
2. Find ```.minecraft/versions/1.X.X.jar``` this will be your jar file of your desired minecraft version.
3. Copy your 1.X.X.jar file to your Desktop (duplicate copy to work on)
4. Extract your 1.X.X jar file using WinRar or any extractor.
5. Within your extracted 1.X.X folder, Find ```assets/minecraft/textures``` this is where you can find all minecraft textures to make your resource pack

## how to make your resource pack
1. Find any PNG editing software to edit your textures
2. Save your changes in 1.X.X/assets/minecraft/textures
3. In your 1.X.X folder, create a pack.mcmeta file (i used VSCode to add it in, making it a text document first might not work, it depends)
Add the following into your pack.mcmeta file:
bash```
{
  "pack": {
    "pack_format": 34, //texture pack version
    "description": "Average Colour Pack" //texture pack description
  }
}
```
4. Select assets folder and pack.mcmeta, right click and compress them.
5. Rename compressed Zip file into your preferred texture pack name
6. Add to resource pack folder in Minecraft. ESC > Options > Resource Pack

## How to use script to quickly edit packs
As there are over 2000 PNG files to edit, a simpler and faster way to edit all files at the same time is to use a script
1. Clone this repository
bash```git clone https://github.com/Nimastic/minecraft-texturepack-creator.git
cd minecraft-texturepack-creator
```
find your input source folder (original minecraft texture folder, aka ../1.X.X/assets/minecraft/textures
chooose an output folder (recommended to direct to a separate folder ../1.X.X/assets/minecraft/textures-edited will do)
edit the path in the scripts for both converter.py and replace_files.py before running code
bash``` 
python converter.py
replace_files.py
```

## textures directory
```bash
minecraft_textures/
├── block/
├── colormap/
├── effect/
├── entity/
├── environment/
├── font/
├── gui/
├── item/
├── map/
├── misc/
├── mob_effect/
├── models/
├── painting/
├── particle/
└── trims/
```


## Resource Pack Structure

```bash
YourResourcePack/
│
├── pack.mcmeta
├── assets/
│   └── minecraft/
│       ├── textures/
│       │   ├── block/
│       │   │   └── stone.png
│       │   └── item/
│       │       └── diamond_sword.png
│       ├── models/
│       │   ├── block/
│       │   │   └── stone.json
│       │   └── item/
│       │       └── diamond_sword.json
│       ├── blockstates/
│       │   └── stone.json
│       └── sounds/
│           └── custom_sound.ogg
└── README.txt (Optional)
```
