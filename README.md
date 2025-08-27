# Ngoolgab Yarrenkoo Miriwoo-biny - Educational Website

A beautifully designed educational website with interactive learning units and games, featuring earth-tone styling perfect for educational contexts.

## 📁 Folder Structure

```
Games Websites/
├── index.html                 # Main landing page
├── Unit 1/                    # Unit 1 folder
│   ├── index.html            # Unit 1 landing page
│   └── game_1.html          # Unit 1 games
├── Unit 2/                    # Unit 2 folder
│   ├── index.html            # Unit 2 landing page
│   ├── game_1.html          # Unit 2 games
│   ├── game_2.html          # Unit 2 games
│   └── game_3.html          # Unit 2 games
├── Unit 3/                    # Unit 3 folder
│   ├── index.html            # Unit 3 landing page
│   └── game_1.html          # Unit 3 games
├── images/                    # Image assets (ready for future use)
├── js/                       # JavaScript files (ready for future use)
├── extract_excel_data.py     # Script to generate website from Excel
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🎨 Design Features

- **Earth-tone color scheme**: Professional brown gradients perfect for education
- **Responsive design**: Works on all devices and screen sizes
- **Interactive tiles**: Hover effects and smooth transitions
- **Clean navigation**: Easy-to-use breadcrumb navigation
- **Modern typography**: Segoe UI font family for readability

## 🚀 How to Use

1. **Open the website**: Double-click `index.html` or open it in your web browser
2. **Browse units**: Click on any unit tile (Unit 1, Unit 2, Unit 3)
3. **Play games**: Click on any game tile to access the interactive learning content
4. **Navigate**: Use back buttons to move between pages

## 🔧 Regenerating the Website

If you update the Excel file (`Ngoolgab yarrenkoo Miriwoo-biny.xlsx`), you can regenerate the website:

```bash
python3 extract_excel_data.py
```

This will:
- Read the Excel file and extract sheet names (units)
- Create unit folders with landing pages
- Generate individual game pages within each unit folder
- Maintain the organized folder structure

## 📊 Excel File Requirements

The Excel file should have:
- **Sheet names**: These become the unit names
- **Title column**: Game titles for the tiles
- **HTML column**: HTML code for the games

## 🌟 Benefits of the New Structure

- **Cleaner appearance**: Each unit has its own dedicated folder
- **Better organization**: Unit landing pages and games are grouped together
- **Easier maintenance**: All related content is in one place
- **Professional look**: Logical folder hierarchy
- **Scalable**: Easy to add new units or games to existing units

## 🎯 Educational Use

Perfect for:
- Language learning platforms
- Interactive educational content
- Student engagement activities
- Teacher resource organization
- Distance learning platforms

---

*Created with ❤️ for educational excellence*
