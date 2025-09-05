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
        
        # Extract game data from each sheet in original order
        all_games = {}
        for sheet_name in sheet_names:
            try:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                
                # Check if required columns exist
                if 'Title' in df.columns and 'HTML' in df.columns and 'Type' in df.columns:
                    games_list = []
                    for _, row in df.iterrows():
                        if pd.notna(row['Title']) and pd.notna(row['HTML']) and pd.notna(row['Type']):
                            games_list.append({
                                'title': str(row['Title']).strip(),
                                'html': str(row['HTML']).strip(),
                                'type': str(row['Type']).strip()
                            })
                    all_games[sheet_name] = games_list
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
    <link rel="stylesheet" href="styles.css">
</head>
<body class="games-page">
    <div class="games-container">
        <div class="games-header">
            <a href="index.html" class="back-button">← Back to Home</a>
            <h1>Ngoolgab Yarrenkoo Miriwoo-biny</h1>
            <p>Click on the boxes to play different games to help you keep Miriwoong strong.</p>
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
        
        <div class="games-footer">
            <p>&copy; 2024 Educational Learning Platform</p>
        </div>
    </div>
</body>
</html>"""
    
    return html_content

def create_unit_page(unit_name, games_list):
    """Create a unit page with game tiles organized by type in containers"""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>{unit_name} - Learning Games</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body class="unit-page">
    <div class="unit-container">
        <div class="unit-header">
            <a href="../games.html" class="back-button">← Back to Units</a>
            <h1>{unit_name}</h1>
            <p>Interactive Learning Games</p>
        </div>
"""
    
    # Group games by type while preserving original order
    games_by_type = {}
    type_order = []
    
    for i, game in enumerate(games_list, 1):
        game_type = game['type']
        if game_type not in games_by_type:
            games_by_type[game_type] = []
            type_order.append(game_type)
        games_by_type[game_type].append({
            'filename': f"game_{i}.html",
            'title': game['title'],
            'type': game['type']
        })
    
    # Create sections for each game type
    for game_type in type_order:
        games = games_by_type[game_type]
        html_content += f"""
        <div class="game-type-section">
            <div class="game-type-header">
                {game_type} ({len(games)} games)
            </div>
            <div class="games-grid">
"""
        
        for game in games:
            html_content += f"""                <a href="{game['filename']}" class="game-tile">
                    <div class="game-type-badge">{game['type']}</div>
                    <h3>{game['title']}</h3>
                    <p>Click to play this {game['type'].lower()} game</p>
                </a>
"""
        
        html_content += """            </div>
        </div>
"""
    
    html_content += """        
        <div class="games-footer">
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
    <link rel="stylesheet" href="../styles.css">
</head>
<body class="game-page">
    <div class="game-header">
        <a href="index.html" class="game-back-button">← Back to {unit_name}</a>
        <h1>{game_title}</h1>
    </div>
    
    <div class="game-container">
        <div class="game-content">
            {game_html}
        </div>
    </div>
    
    <div class="game-footer">
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
    
    # Create main games page
    print("Creating main games page...")
    with open("games.html", "w", encoding="utf-8") as f:
        f.write(create_main_page(sheet_names))
    
    # Create unit pages and game pages in their respective folders
    for unit_name in sheet_names:
        games_list = all_games.get(unit_name, [])
        total_games = len(games_list)
        print(f"Creating unit page for '{unit_name}' with {total_games} games in original Excel order...")
        
        # Create unit directory if it doesn't exist
        unit_dir = Path(unit_name)
        unit_dir.mkdir(exist_ok=True)
        
        # Create unit landing page in the unit folder
        unit_index_filename = f"{unit_name}/index.html"
        with open(unit_index_filename, "w", encoding="utf-8") as f:
            f.write(create_unit_page(unit_name, games_list))
        
        # Create individual game pages in the same unit folder
        # Use sequential numbering based on Excel order
        for i, game in enumerate(games_list, 1):
            game_filename = f"{unit_name}/game_{i}.html"
            print(f"  Creating game page: {game_filename} ({game['type']})")
            
            with open(game_filename, "w", encoding="utf-8") as f:
                f.write(create_game_page(game['title'], game['html'], unit_name))
    
    print(f"\nWebsite generation complete!")
    total_games = sum(len(games_list) for games_list in all_games.values())
    print(f"Created {len(sheet_names)} unit folders with landing pages and {total_games} game pages")
    print("New folder structure:")
    for unit_name in sheet_names:
        print(f"  - {unit_name}/ (contains index.html and games)")
    print("Open 'index.html' in your web browser to view the website")

if __name__ == "__main__":
    main()