import pandas as pd
import os
from pathlib import Path

def extract_excel_data():
    """Extract data from the Excel file and return sheet names and game data"""
    try:
        # Read the Excel file
        excel_file = "Ngoolgab yarrenkoo Miriwoo-biny.xlsx"
        xl = pd.ExcelFile(excel_file)
        
        # Get sheet names (these will be our units)
        sheet_names = xl.sheet_names
        
        # Extract game data from each sheet
        all_games = {}
        for sheet_name in sheet_names:
            try:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                
                # Check if required columns exist
                if 'Title' in df.columns and 'HTML' in df.columns:
                    games = []
                    for _, row in df.iterrows():
                        if pd.notna(row['Title']) and pd.notna(row['HTML']):
                            games.append({
                                'title': str(row['Title']).strip(),
                                'html': str(row['HTML']).strip()
                            })
                    all_games[sheet_name] = games
                else:
                    print(f"Warning: Sheet '{sheet_name}' missing required columns 'Title' or 'HTML'")
                    all_games[sheet_name] = []
                    
            except Exception as e:
                print(f"Error reading sheet '{sheet_name}': {e}")
                all_games[sheet_name] = []
        
        return sheet_names, all_games
        
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return [], {}

def create_main_page(sheet_names):
    """Create the main page with unit tiles"""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>Ngoolgab Yarrenkoo Miriwoo-biny - Learning Units</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #8B7355 0%, #A0522D 50%, #8B4513 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }
        
        .header {
            margin-bottom: 40px;
            color: #F5F5DC;
        }
        
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .units-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }
        
        .unit-tile {
            background: linear-gradient(145deg, #D2B48C, #DEB887);
            border-radius: 15px;
            padding: 30px 20px;
            text-decoration: none;
            color: #654321;
            transition: all 0.3s ease;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            border: 2px solid #8B7355;
        }
        
        .unit-tile:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.25);
            background: linear-gradient(145deg, #E6D3B3, #F0E68C);
        }
        
        .unit-tile h2 {
            font-size: 1.8rem;
            margin-bottom: 10px;
            color: #8B4513;
        }
        
        .unit-tile p {
            font-size: 1rem;
            opacity: 0.8;
        }
        
        .footer {
            margin-top: 50px;
            color: #F5F5DC;
            opacity: 0.8;
        }
        
        @media (max-width: 768px) {
            .units-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
            
            .header h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Ngoolgab Yarrenkoo Miriwoo-biny</h1>
            <p>Interactive Learning Units</p>
        </div>
        
        <div class="units-grid">
"""
    
    for sheet_name in sheet_names:
        html_content += f"""            <a href="{sheet_name}/index.html" class="unit-tile">
                <h2>{sheet_name}</h2>
                <p>Click to explore learning activities</p>
            </a>
"""
    
    html_content += """        </div>
        
        <div class="footer">
            <p>&copy; 2024 Educational Learning Platform</p>
        </div>
    </div>
</body>
</html>"""
    
    return html_content

def create_unit_page(unit_name, games):
    """Create a unit page with game tiles"""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>{unit_name} - Learning Games</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #8B7355 0%, #A0522D 50%, #8B4513 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }}
        
        .header {{
            margin-bottom: 40px;
            color: #F5F5DC;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .back-button {{
            display: inline-block;
            background: linear-gradient(145deg, #D2B48C, #DEB887);
            color: #654321;
            text-decoration: none;
            padding: 12px 25px;
            border-radius: 25px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
            border: 2px solid #8B7355;
        }}
        
        .back-button:hover {{
            background: linear-gradient(145deg, #E6D3B3, #F0E68C);
            transform: translateY(-2px);
        }}
        
        .games-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }}
        
        .game-tile {{
            background: linear-gradient(145deg, #D2B48C, #DEB887);
            border-radius: 15px;
            padding: 30px 20px;
            text-decoration: none;
            color: #654321;
            transition: all 0.3s ease;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            border: 2px solid #8B7355;
        }}
        
        .game-tile:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.25);
            background: linear-gradient(145deg, #E6D3B3, #F0E68C);
        }}
        
        .game-tile h2 {{
            font-size: 1.5rem;
            margin-bottom: 10px;
            color: #8B4513;
        }}
        
        .game-tile p {{
            font-size: 1rem;
            opacity: 0.8;
        }}
        
        .footer {{
            margin-top: 50px;
            color: #F5F5DC;
            opacity: 0.8;
        }}
        
        @media (max-width: 768px) {{
            .games-grid {{
                grid-template-columns: 1fr;
                gap: 20px;
            }}
            
            .header h1 {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <a href="../index.html" class="back-button">← Back to Units</a>
            <h1>{unit_name}</h1>
            <p>Interactive Learning Games</p>
        </div>
        
        <div class="games-grid">
"""
    
    for i, game in enumerate(games):
        game_filename = f"game_{i+1}.html"
        html_content += f"""            <a href="{game_filename}" class="game-tile">
                <h2>{game['title']}</h2>
                <p>Click to play this learning game</p>
            </a>
"""
    
    html_content += """        </div>
        
        <div class="footer">
            <p>&copy; 2024 Educational Learning Platform</p>
        </div>
    </div>
</body>
</html>"""
    
    return html_content

def create_game_page(game_title, game_html, unit_name):
    """Create an individual game page with truly full-page layout"""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>{game_title}</title>
    <style>
        * {{
            margin: 0 !important;
            padding: 0 !important;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #ffffff;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }}
        
        .header {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(139, 115, 85, 0.95);
            backdrop-filter: blur(10px);
            padding: 10px 20px;
            text-align: center;
            box-shadow: 0 2px 20px rgba(0,0,0,0.3);
        }}
        
        .header h1 {{
            font-size: 1.5rem;
            margin-bottom: 5px;
            color: #F5F5DC;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .back-button {{
            display: inline-block;
            background: linear-gradient(145deg, #D2B48C, #DEB887);
            color: #654321;
            text-decoration: none;
            padding: 6px 16px;
            border-radius: 18px;
            margin-bottom: 8px;
            transition: all 0.3s ease;
            border: 2px solid #8B7355;
            font-size: 0.8rem;
        }}
        
        .back-button:hover {{
            background: linear-gradient(145deg, #E6D3B3, #F0E68C);
            transform: translateY(-2px);
        }}
        
        .game-container {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            padding: 0;
            margin: 0;
            border: none;
            box-shadow: none;
            background: transparent;
            overflow: hidden;
        }}
        
        .game-content {{
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(139, 115, 85, 0.95);
            backdrop-filter: blur(10px);
            color: #F5F5DC;
            text-align: center;
            padding: 8px;
            font-size: 0.7rem;
            opacity: 0.9;
        }}
        
        /* Make the game content fill the entire page */
        .game-container * {{
            max-width: 100vw !important;
            max-height: 100vh !important;
            width: auto !important;
            height: auto !important;
        }}
        
        /* Ensure embedded content takes full space */
        .game-container iframe {{
            width: 100vw !important;
            height: 100vh !important;
            border: none;
            margin: 0;
            padding: 0;
            position: absolute;
            top: 0;
            left: 0;
        }}
        
        .game-container embed,
        .game-container object,
        .game-container video {{
            width: 100vw !important;
            height: 100vh !important;
            border: none;
            margin: 0;
            padding: 0;
        }}
        
        /* Remove any default margins from game content */
        .game-container div,
        .game-container p,
        .game-container img {{
            margin: 0 !important;
            padding: 0 !important;
        }}
        
        /* Ensure images scale properly */
        .game-container img {{
            max-width: 100vw !important;
            max-height: 100vh !important;
            object-fit: contain;
        }}
    </style>
</head>
<body>
    <div class="header">
        <a href="index.html" class="back-button">← Back to {unit_name}</a>
        <h1>{game_title}</h1>
    </div>
    
    <div class="game-container">
        <div class="game-content">
            {game_html}
        </div>
    </div>
    
    <div class="footer">
        <p>&copy; 2024 Educational Learning Platform</p>
    </div>
</body>
</html>"""
    
    return html_content

def main():
    """Main function to generate all HTML files"""
    print("Extracting data from Excel file...")
    sheet_names, all_games = extract_excel_data()
    
    if not sheet_names:
        print("No data found. Please check the Excel file.")
        return
    
    print(f"Found {len(sheet_names)} units: {sheet_names}")
    
    # Create main index page
    print("Creating main index page...")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(create_main_page(sheet_names))
    
    # Create unit pages and game pages in their respective folders
    for unit_name in sheet_names:
        games = all_games.get(unit_name, [])
        print(f"Creating unit page for '{unit_name}' with {len(games)} games...")
        
        # Create unit landing page in the unit folder
        unit_index_filename = f"{unit_name}/index.html"
        with open(unit_index_filename, "w", encoding="utf-8") as f:
            f.write(create_unit_page(unit_name, games))
        
        # Create individual game pages in the same unit folder
        for i, game in enumerate(games):
            game_filename = f"{unit_name}/game_{i+1}.html"
            print(f"  Creating game page: {game_filename}")
            
            with open(game_filename, "w", encoding="utf-8") as f:
                f.write(create_game_page(game['title'], game['html'], unit_name))
    
    print(f"\nWebsite generation complete!")
    print(f"Created {len(sheet_names)} unit folders with landing pages and {sum(len(games) for games in all_games.values())} game pages")
    print("New folder structure:")
    for unit_name in sheet_names:
        print(f"  - {unit_name}/ (contains index.html and games)")
    print("Open 'index.html' in your web browser to view the website")

if __name__ == "__main__":
    main()