# Minecraft Texture Pack Creator

This repository contains tools and scripts to help you create and modify Minecraft texture packs quickly and efficiently.

## Where to Find the Default Minecraft Texture Pack (Windows)

1. Press `Win + R` and enter `%appdata%`.
2. Navigate to `.minecraft/versions/1.X.X.jar` (replace `1.X.X` with your desired Minecraft version).
3. Copy the `1.X.X.jar` file to your Desktop to work on a duplicate copy.
4. Extract the `1.X.X.jar` file using WinRAR or any other extraction tool.
5. Inside the extracted `1.X.X` folder, locate `assets/minecraft/textures`—this folder contains all the Minecraft textures needed to create your resource pack.

## How to Create Your Resource Pack

1. Use any PNG editing software to edit your textures.
2. Save your changes in `1.X.X/assets/minecraft/textures`.
3. In the `1.X.X` folder, create a `pack.mcmeta` file. You can use a text editor like VSCode to create it. Adding it as a text document first might not work depending on your system configuration. Add the following content to your `pack.mcmeta` file:

   ```json
   {
     "pack": {
       "pack_format": 34,
       "description": "Average Colour Pack"
     }
   }
4. Select the assets folder and the pack.mcmeta file, right-click, and compress them into a ZIP file.
5. Rename the compressed ZIP file to your preferred texture pack name.
6. Move the ZIP file to the Minecraft resource pack folder: ESC > Options > Resource Pack.

## How to Use the Script to Quickly Edit Packs
Given that there are over 2000 PNG files to edit, using a script is a faster and simpler way to edit all files simultaneously.
1. Clone this repository:
```
git clone https://github.com/Nimastic/minecraft-texturepack-creator.git
cd minecraft-texturepack-creator
pip install pillow
```
2. Locate your input source folder (the original Minecraft texture folder, e.g., ../1.X.X/assets/minecraft/textures).
3. Choose an output folder (it is recommended to direct it to a separate folder, e.g., ../1.X.X/assets/minecraft/textures-edited).
4. Edit the paths in the scripts converter.py and replace_files.py before running the code.
5. Run the scripts:
```
python converter.py
python replace_files.py
```
## Textures Directory Structure

```
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

## How your resource pack folder will look like
```
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
